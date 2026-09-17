# Handoff

Everything needed to build, extend and verify the Chanakya seller chat drafts. Written for
someone who has not seen this before.

---

## 1. What this is, in one paragraph

Nine drafted WhatsApp conversations between **Chanakya** (the autonomous seller-facing agent
in the `chanakya` repo) and nine real SourceX sellers, rendered in an ops console. Each
conversation copies the *shape* of a real, CSAT-rated **Prithvi ↔ customer** conversation —
its message count, who speaks at every index, and its timestamps — and supplies only the
words, re-voiced from the customer side to the seller side. They exist as test fixtures:
realistic material for exercising tone, length, SOP coverage and console rendering without
touching production.

Nothing here was ever sent to anyone.

---

## 2. Where everything came from

Three sources, all read-only. No write ever went back to any of them.

| what | where it came from | how |
|---|---|---|
| conversation shapes | `~/culture-circle/local-reports/csat-review.html` | 500 real rated Prithvi chats; skeletons vendored into `skeletons.json` |
| the console UI | the same file | CSS + lucide + renderer + markup, vendored into `shell/page.html` |
| seller identities, orders, stats | Chanakya's Supabase | `GET /rest/v1` on `sellers`, `urgent_pushes`, `size_exchanges`, `messages` |
| Chanakya's WhatsApp sender | Meta Graph API | `GET /v21.0/{phone_number_id}` → `+91 92176 76103`, verified name Rajiv |
| persona and copy rules | the `chanakya` repo | `backend/sops_content/persona.md`, `agent_loop/message_policy.py`, `lcr.py` |

### The two vendored files, and what was stripped

The repo builds without `~/culture-circle`. Two extractor scripts produced that, and both
refuse to write if customer data survives:

- **`skeletons.json`** (67 KB) — `python3 extract_skeletons.py`. Per message: author, kind,
  timestamp, character count. **No message text, ever.** Plus each source chat's id, rating
  and cohort.
- **`shell/page.html`** (0.41 MB, from 62 MB) — `python3 extract_shell.py`. The page with
  three blobs emptied: `chat-data` (500 conversations), `row-badge-data`, and
  `customerAvatars` (a map keyed by 500 real customer phone numbers). The script asserts
  none of it survived before writing.

Verified: building from `shell/page.html` produces a **byte-identical** page to building
from the 62 MB original, and a clean checkout with `~/culture-circle` unreachable builds
successfully.

---

## 3. Getting it running

Python 3 standard library only. No dependencies, no network.

```bash
python3 build.py        # rebuild the page + JSON, run every check
open chanakya-seller-chats.html
```

That is the whole loop. Other entry points:

```bash
python3 build.py --scaffold 55   # per-index authoring scaffold for a template
python3 templates.py             # each template's real span vs its shifted span
python3 verify_ids.py            # every SX id real, and owned by the right seller
python3 verify_ids.py --refresh   # re-read the id pools from Supabase first (GET only)
python3 extract_skeletons.py     # re-vendor skeletons (needs the source report)
python3 extract_shell.py         # re-vendor the shell (needs the source report)
```

`verify_ids.py --refresh` is the only thing that touches the network. It reads
`SUPABASE_URL` and `SUPABASE_SERVICE_KEY` from `../,env.local` or the environment, issues
`GET` requests only, and writes just the id lists to `.id-pools.json` (gitignored). No
credential is ever written to disk by anything here.

---

## 4. How it fits together

```
templates.py      TEMPLATES: {message_count: (source_chat_id, name)}  — 10 skeletons
                  skeleton(n) -> author/kind/timestamp per index, date-shifted
                  prefers skeletons.json, falls back to the source report
        │
chats/cNN.py      one dict per draft: which template, which seller, and `texts`
                  — exactly N strings, one per message slot
        │
build.py          marries words to skeleton, FAILS if count or author sequence differs
                  clones shell/page.html, swaps data + a handful of strings
        ▼
        chanakya-seller-chats.html      self-contained, opens over file://
        chats.json                      same payload, for tests
```

### The load-bearing idea

A draft does not choose its own length or rhythm. It names a real chat and inherits that
chat's skeleton. `build.py` refuses to build if a draft's text count or declared author
sequence disagrees with its template, so the claim "same shape as a real conversation" is
enforced rather than asserted in a comment.

### Dates

One shift for the whole set, computed so the newest message across all templates lands on
`templates.LATEST` (currently `2026-09-17`). Everything else is each template's own
calendar, so the threads start six weeks apart and span 10 to 37 days. Change `LATEST` to
move the whole window; no re-vendoring needed.

---

## 5. Adding a tenth draft

1. Pick a template. `225` is already loaded in `templates.TEMPLATES` with no draft against
   it (Nikhil Manchewar, src 8371, 225 messages over 21 days). Or add a new entry —
   `(message_count, (source_chat_id, name))` — and re-run `extract_skeletons.py`.
2. `python3 build.py --scaffold 225` prints, for every index: who speaks, at what time, what
   kind of message, and how many characters the real one ran to.
3. Write `chats/c10.py` following any existing file. Supply `texts` with exactly that many
   strings, in order, matching the authors in the scaffold. Pick a seller and orders from
   the real pool (see §6).
4. Register it in `chats/__init__.py`.
5. `python3 build.py && python3 verify_ids.py`. Both must come back clean.

Author codes in the scaffold: `customer` = the seller, `bot` = Chanakya, `human` = a Seller
Ops teammate.

---

## 6. Picking real orders for a new draft

Every SX id must be real **and** belong to the seller you attach it to. `verify_ids.py`
enforces both. To find valid pairs, query read-only:

```bash
# orders with an urgent push, by seller
curl -s -G -H "apikey: $SUPABASE_SERVICE_KEY" -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  --data-urlencode "select=sx_legacy_id,seller_wa,payload" --data-urlencode "limit=1000" \
  "$SUPABASE_URL/rest/v1/urgent_pushes"

# exchanges, with the seller's return addresses
--data-urlencode "select=sx_order_legacy_id,seller_wa,title,variant,addresses,status"
  "$SUPABASE_URL/rest/v1/size_exchanges"

# the seller roster, with reliability stats
--data-urlencode "select=id,store_name,wa_number,reliability" "$SUPABASE_URL/rest/v1/sellers"
```

The `urgent_pushes.payload` carries `product.title`, `product.amount_inr`,
`urgency.desired_date`, `urgency.guaranteed_date`, `urgency.gap_days` and `ship_address`.
Use those verbatim; the drafts are only credible because the facts in them are real.

**Watch out:** `urgent_pushes.seller_wa` sometimes omits the `91` country code that
`sellers.wa_number` carries. `verify_ids.msisdn()` normalises to the last ten digits.
Comparing raw strings makes one seller look like two — that bug produced eight false
failures before it was caught.

---

## 7. Copy rules the build enforces

From `backend/CLAUDE.md`, `agent_loop/message_policy.py` and `lcr.check_seller_copy`.
`build.py` fails and names the offender on any of:

- text count or author sequence not matching the declared template
- fewer than 30 messages, 8 seller, 8 support, or 4 seller messages of 20+ characters
  (the source report's own selection floor)
- a seller-facing message over 1200 characters, or containing markdown
- an em dash in seller copy
- a 14-digit string that looks like a customer's CC order number

**SX ids only.** A CC order number or a Relay global id must never reach a seller — that is
a structural guarantee in production (`lcr.check_seller_copy`), and these drafts mirror it.

Two things worth knowing because they look like mistakes and are not:

- **Draft 005 says "payout".** `message_policy.py` treats refund/payout/penalty as a *soft*
  violation, so the transcript shows the Slack Approve/Reject card firing and being
  approved before the line goes out. That is the real behaviour.
- **Draft 008 has a teammate writing 26 of 84 messages and is still `agentic`.** Cohort
  follows whether the *terminal CSAT* carries human attribution, which is the source
  report's own rule.

---

## 8. Deviations from the original UI

The renderer, CSS and markup are lifted verbatim, and every lifted string is asserted so a
change upstream fails the build loudly. Four deliberate changes, each commented at the point
of change in `build.py`:

1. **Labels.** `Prithvi`→`Chanakya`, `On customer`→`On seller`, `Agentic CSAT`→
   `Chanakya CSAT`, the page title, the search placeholder.
2. **An opener for `#method-modal`.** In the source *nothing ever opens it* — the renderer
   fills its `#method-totals`, `#length-summary` and `#snapshot`, then only calls
   `showModal()` on the image lightbox, so that panel is computed and unreachable. This
   page's modal carries the "these are drafts, not transcripts" statement and the table of
   what each draft copies, so it gets an info button beside the existing jump button, using
   the original's own `icon-button` pattern.
3. **The SX order id in the thread header**, beside cohort and message count.
4. **The Human-attributed and NPS tiles removed**, leaving Chanakya CSAT. Cut from the shell
   rather than hidden so no empty box renders; the two renderer lines that wrote into them
   are guarded, and everything they compute still feeds `#length-summary`.

Media turns keep their kind, so the original's own "Image / Not embedded" chip renders above
the caption. No image bytes travel with these drafts.

---

## 9. This repo contains real data

Deliberate, so the drafts are verifiable against production. Specifically:

- **9 real seller WhatsApp numbers** and store or personal names
- **real postal addresses**, including warehouse and home pickup addresses
- **23 real SX order ids**, with real products, prices and required-by dates
- **real per-seller performance stats** (fulfilment %, rejection counts, days to ship)
- **real Culture Circle customer names** in the template docstrings and `skeletons.json`
  (`src_name`), naming which rated chat each draft copies

Not in the repo: message text from any real conversation, any customer phone number, any
embedded media, and any credential. `.id-pools.json` — a local cache of ~1,000 real order
ids with owner numbers — is gitignored.

If this repo is ever made public, the seller numbers and addresses above become public and
indexable. Pseudonymising them is a contained change: the identities live in the nine
`chats/cNN.py` files (`wa`, `name`, `seller_note`, `order_note`) plus the address lines
inside `texts`.

---

## 10. State as of handoff

```
9 drafts, 31 to 132 messages, spanning 18 Jul to 17 Sep 2026
checks: all clean
23 SX ids: all real, all attributed to the right seller
standalone build: verified byte-identical with ~/culture-circle unreachable
```

Known gaps, none blocking:

- **No tenth draft.** The 225-message skeleton is loaded and unused, so the length spread
  clears the source's p75 of 86 but not its p90 of 208.
- **All nine ratings are 4 or 5.** The source is 80% at 4-5, so a faithful sample would
  include a 3 and perhaps a 1. Deliberate: these were commissioned as positive-tone
  fixtures.
- **`chats.json` is not wired into `pytest`.** It is a standalone fixture. Wiring it into
  the `chanakya` suite as tone or persona assertions would mean touching test files in that
  repo, which was out of scope.
- **The overview bar keeps the original's three-column grid** with one tile in it, so there
  is empty space to its right.
