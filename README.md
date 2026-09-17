# Chanakya seller chats — drafts in the csat-review console

Nine drafted Chanakya ↔ seller conversations. Each one **copies a named real chat** from
`~/culture-circle/local-reports/csat-review.html` — its message count, its author at every
index, its kinds and its timestamps — and supplies only the words. Rendered in that file's
own UI.

```bash
python3 build.py                 # rebuild both outputs, run every check
python3 build.py --scaffold 55   # per-index authoring scaffold for a template
python3 verify_ids.py            # check every SX id is real and owned by that seller
open chanakya-seller-chats.html  # file:// is fine, nothing is fetched
```

| file | what it is |
|---|---|
| `templates.py` | the ten skeletons lifted from real rated chats, and the date shift |
| `chats/cNN.py` | one draft each: which chat it copies, the seller, the words |
| `build.py` | clones the csat-review shell, marries words to skeletons, validates |
| `verify_ids.py` | proves every SX id exists and belongs to the seller it's used against |
| `chanakya-seller-chats.html` | the output console, self-contained, 0.60 MB |
| `chats.json` | the same payload for test use |

## Length and rhythm are copied, not invented

`build.py` fails the build if a draft's text count or author sequence disagrees with its
template. So this table is enforced, not claimed:

Ordered oldest first, the way the modal lists them:

| draft | seller | msgs | seller / Chanakya / staff | runs from | span | active | run | copied from |
|---|---|---|---|---|---|---|---|---|
| 006 | Delicc Enterprises | 55 | 28 / 27 / 0 | 18 Jul → 2 Aug | 16d | 8 | 4 | Muslim altaf Khan (5, agentic) |
| 009 | Mindyourkicks | 132 | 73 / 16 / 43 | 27 Jul → 1 Sep | 37d | 18 | 13 | Ananya Tambe (5, human) |
| 007 | ELITE FINDS | 67 | 33 / 29 / 5 | 5 Aug → 3 Sep | 30d | 15 | 4 | Vikas Garg (4, human) |
| 005 | Sneak Drip | 50 | 23 / 15 / 12 | 10 Aug → 27 Aug | 18d | 8 | 7 | Dhananjoy Das (5, human) |
| 004 | DJ1 | 42 | 25 / 15 / 2 | 15 Aug → 27 Aug | 13d | 6 | 7 | Uthpala H v (4, agentic) |
| 001 | TopGun | 31 | 12 / 13 / 6 | 17 Aug → 31 Aug | 15d | 5 | 6 | Achintya Singh (5, agentic) |
| 003 | Hypestreet India | 36 | 16 / 14 / 6 | 17 Aug → 17 Sep | 32d | 6 | 6 | Viraj . (5, agentic) |
| 008 | DS.WT | 84 | 50 / 8 / 26 | 17 Aug → 3 Sep | 18d | 10 | 10 | ANUJMAGO (4, agentic) |
| 002 | Elvara | 32 | 15 / 17 / 0 | 29 Aug → 7 Sep | 10d | 5 | 2 | Vivaan Agarwal (4, agentic) |

**Dates are staggered because the source's are.** One shift is applied to the whole set,
computed so the newest message across all templates lands on `templates.LATEST`
(2026-09-17). Everything else is the template's own calendar: each thread keeps its real
start date, its real end date and every gap in between. An earlier version anchored each
template's *first* day to a common date, which preserved each thread's internal span but
threw the stagger away, so all nine opened on the same morning and the sidebar read as one
batch. They now start six weeks apart, span 10 to 37 calendar days, and are active on 5 to
18 of them.

The nine templates were picked off a profile of all 500 source chats to spread the axes
that actually vary, so no two drafts read alike:

- **length** 31 → 132 messages
- **who talks** 13 Chanakya replies against 12 seller messages (001) → 8 against 50 (008)
- **verbosity** Chanakya's median reply 37 chars (003) → 291 chars (006)
- **burstiness** clean alternating turns (002, run of 2) → 13 unanswered in a row (009)
- **duration** a 10-day thread (002) → a 37-day one (009)
- **when** starts spread from 18 July to 29 August, ends from 2 August to 17 September
- **who carries it** bot alone (002, 006) → a teammate writing 43 of 132 messages (009)
- **how it ends** a warm sign-off, a rating with nothing after it (006), or the seller
  talking into silence three days later (003)

Source shape for comparison: floor 30 messages with 8 each side, p25 38, median 51, p75 86,
p90 208. This set clears p75 and stops short of the p90 tail — the 225-message skeleton
(Nikhil Manchewar, src 8371) is loaded in `templates.py` but has no draft written against
it.

Ratings: 5 fives and 4 fours. The source is 80% at 4 or 5, which is where "the tone is
positive" comes from.

## The UI is the old file, not a lookalike

`build.py` reads `csat-review.html` and lifts its three `<style>` blocks, its bundled
lucide icons and its 160-line renderer **verbatim**. Swapped: the two JSON payloads, the
avatar map (regenerated for these sellers, same SVG shape), and `Prithvi`→`Chanakya`,
`On customer`→`On seller`, `Agentic CSAT`→`Chanakya CSAT`, the title, the search
placeholder. Every lifted string is asserted, so if the source report changes the build
fails loudly instead of half-patching.

Deliberate deviations, each documented at the point of change:

- **The SX order id sits in the thread header**, beside the cohort and message count. On
  this lane it's the only id anyone can act on, and it's what the search box asks for. The
  multi-order threads list all of them (draft 006 carries five) and still fit without
  overflow at 1440px and at 390px.
- **The Human-attributed and NPS tiles are removed**, leaving Chanakya CSAT. They're cut
  from the shell rather than hidden so nothing renders an empty box, and the two renderer
  lines that wrote into them are guarded — everything they compute still feeds
  `#length-summary` in the details modal.

- **An opener for `#method-modal`.** In the source nothing ever opens it: the renderer
  fills its `#method-totals`, `#length-summary` and `#snapshot` and only calls
  `showModal()` on the image lightbox, so that copy is computed and unreachable. This
  page's modal carries the "these are drafts, not transcripts" statement and the table of
  what each draft copies, so it gets an info button beside the existing jump button using
  the original's own `icon-button` pattern.
- **An empty cohort reads "Not recorded"** rather than `--/ 5`.

Media turns keep their kind, so the original's own "Image / Not embedded" chip appears
above the caption — no bytes travel with these drafts.

## Identifiers are real; the words are written

`verify_ids.py` scrapes every `SX\d{6}` out of the drafts and checks it against the ids
that exist in Chanakya's own data, then checks ownership:

```
23 id/draft pairs across 9 drafts
all ids real and attributed to the right seller
```

Pools are `urgent_pushes.sx_legacy_id` (777), `size_exchanges.sx_order_legacy_id` (193)
and ids already named to a seller in `messages.body` (378) — union 1,007, with the owning
seller known for 970. Comparison normalises to the last ten digits, because
`urgent_pushes.seller_wa` sometimes drops the country code that `sellers.wa_number` keeps.

Store names, reliability stats, products, prices, required-by dates and return addresses
come from the same read-only pull. Chanakya's sender is **+91 92176 76103** (verified name
Rajiv, quality GREEN) from the Meta Graph API. The message text is drafted. Nothing here
was sent to anyone and no credential is stored in this directory.

## Checks the build enforces

Build fails and names the offender on any of:

- text count or author sequence not matching the declared template
- fewer than 30 messages, 8 seller, 8 support, or 4 seller messages of 20+ chars
- a seller-facing message over 1200 chars, or containing markdown
  (`agent_loop/message_policy.py`)
- an em dash in seller copy, or a 14-digit string that looks like a CC order number
  (`lcr.check_seller_copy` is what this mirrors — SX ids only)

Draft 005 mentions a payout, which `message_policy.py` treats as a **soft** violation, so
the transcript shows the Slack Approve/Reject card firing and being approved before the
line goes out. Drafts 005, 007 and 009 copy human-cohort templates and are marked human;
008 has a teammate writing 26 of its 84 messages and stays agentic, because its terminal
rating carries no human attribution — the source's own rule.
