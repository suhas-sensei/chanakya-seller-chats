# Handoff

Everything needed to build, extend and verify the Chanakya seller chat drafts. Written for
someone who has not seen this before.

---

## 1. What this is, in one paragraph

Eight drafted WhatsApp relationships between **Chanakya** (the autonomous seller-facing
agent in the `chanakya` repo) and eight real SourceX sellers, rendered in an ops console.
Each runs weeks and is built from short transactional episodes: a reminder, a date, a
follow-up, a payout, a sourcing question, an RTO. They exist as test fixtures — realistic
material for exercising tone, negotiation, SOP coverage and console rendering without
touching production.

Nothing here was ever sent to anyone.

**Shape and voice come from the real seller exports**, not from the customer-side report.
`Seller WhatsApp Chat Export.zip` holds 34 real seller threads, 17,276 lines, running a
median 159 messages over 19 active days. `chats/_voice.py` is the voice reference distilled
from it — read that before writing a draft. An earlier version copied customer chats
message-for-message and read like coaching sessions; that machinery still works (§5) but is
not what the current set uses.

---

## 2. Where everything came from

Three sources, all read-only. No write ever went back to any of them.

| what | where it came from | how |
|---|---|---|
| voice and shape | `Seller WhatsApp Chat Export.zip` | 34 real seller threads, 17,276 lines; distilled into `chats/_voice.py` |
| legacy chat skeletons | `~/culture-circle/local-reports/csat-review.html` | 500 real rated Prithvi chats; vendored into `skeletons.json` |
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
chats/cNN.py      one dict per draft: seller, order, `flow`, and `turns`
                  turns = [(timestamp, who, text), ...]   who: cx | tpl | sl | ops
        │
build.py          build_turns()  -> free-form drafts (all eight current ones)
                  build_chat()   -> skeleton-bound drafts (legacy, still supported)
                  finish_chat()  -> shared tail, derives the console's counters
                  clones shell/page.html, swaps data + a handful of strings
        ▼
        chanakya-seller-chats.html      self-contained, opens over file://
        chats.json                      same payload, for tests
```

### The flow strip

Each draft carries `flow: {input, action, resolution}`, rendered as an **In → Chanakya →
Out** bar under the thread header (`FLOW_JS` / `FLOW_CSS` in `build.py`). It exists so a
reader sees what the thread was for without reading it. If you add a draft, write the flow
first — if you can't state the resolution in a line, the thread doesn't have one.

### Dates

Free-form drafts carry their own timestamps, written into each turn. Nothing is shifted.

### The legacy skeleton path

`templates.py` still holds ten skeletons lifted from real csat-review chats, and
`build_chat()` still enforces them: a draft declaring `template` + `texts` must match its
source chat's message count and author sequence exactly, or the build fails. Those drafts
also get the source report's 30-message selection floor. Free-form drafts skip both.

---

## 5. Adding a draft

1. Pick a seller and real orders from the pool (§6). The ids must be that seller's.
2. Write the `flow` first: what came in, what Chanakya does about it, how it ends.
3. Copy any existing `chats/cNN.py`. Fill `turns` with `(timestamp, who, text)` —
   `cx` = Chanakya, `sl` = the seller, `ops` = a Seller Ops teammate.
4. Register it in `chats/__init__.py`.
5. `python3 build.py && python3 verify_ids.py`. Both must come back clean.

**Read `chats/_voice.py` first.** It is the voice reference, quoted from the real exports.
The short version:

- **Two registers.** Open formal, and go formal again whenever it turns serious — penalties,
  SLA, a lost parcel. Everything else is terse Hinglish.
- **Vary the ask.** "what is the status of this order?" / "status of this shipment?" /
  "any update?" / "ye kab ship ho rha?" / "what is the update on this". Repeat one verbatim
  when the seller goes quiet, which is what actually happens.
- **Never repeat the ask without a lever.** SLA and the 5% penalty, TAT and ranking, holding
  the date he gave you, what the buyer is worth, or removing the blocker outright.
- **Address terms are per seller.** bhai, bro, boss, ji, sir, yaar, Hnji, or nothing at all.
  Do not give every seller the same word, and do not default to one for Chanakya either.

**Writing the seller.** Give each one a register and stay in it. The eight in use are listed
in `chats/__init__.py`; the observed set is in `_voice.py`. Hinglish, terse, typos fine.

To use the legacy skeleton path instead: `python3 build.py --scaffold 225` prints, for every
index, who speaks, when, what kind and how long the real message was. The 225 skeleton
(Nikhil Manchewar, src 8371, 21 days) is loaded with no draft against it.

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
10 drafts, 10 to 16 messages, spanning 11 Sep to 24 Sep 2026
checks: all clean
23 SX ids: all real, all attributed to the right seller
standalone build: verified with ~/culture-circle unreachable
```

Coverage: 3 payout threads (2 unmarked-complete, 1 undelivered), 2 bulk follow-ups, 1 X−1
reminder, 1 RTO reship, 1 reputation/PDP negotiation, 1 high-value-buyer negotiation, 1
date negotiation. Nine of ten are order-first; all three payout threads resolve into a
shipment.

Known gaps, none blocking:

- **Ratings are 9 fives and 1 four.** Deliberate: commissioned as positive-tone fixtures.
  A faithful sample of the source would include a 3 and a 1.
- **No em dashes**, even though the production screenshots use them. `backend/CLAUDE.md`
  lists no-em-dash as a seller-copy invariant and the build enforces it. Relaxing it is one
  line in `build.py` if the invariant is stale.
- **The word "payout" is a soft violation** in `agent_loop/message_policy.py`, so in
  production those lines would queue a Slack Approve/Reject card before sending. The drafts
  show the messages as sent; they do not show the card.
- **`chats.json` is not wired into `pytest`.** Standalone fixture. Wiring it into the
  `chanakya` suite would mean touching test files in that repo, which was out of scope.
- **The overview bar keeps the original's three-column grid** with one tile in it, so there
  is empty space to its right.
- **The 225-message skeleton is loaded and unused** in `templates.py`.
