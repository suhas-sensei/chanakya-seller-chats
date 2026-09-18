# Chanakya seller chats — order-chasing drafts

Ten drafted WhatsApp threads between **Chanakya** and real SourceX sellers, rendered in the
csat-review ops console.

These are jobs, not conversations. An order is late, or a payout is blocking one. Chanakya
chases, negotiates, and it resolves. They run **10 to 16 messages** because that is how long
the real thing takes.

```bash
python3 build.py                 # rebuild the page + JSON, run every check
python3 verify_ids.py            # every SX id real, and owned by the right seller
open chanakya-seller-chats.html
```

## What each thread does

Every thread carries an **In → Chanakya → Out** strip under the header, so the shape reads
without scrolling the transcript.

| # | seller | msgs | what it is |
|---|---|---|---|
| c01 | Dipanshu | 11 | RTO reship. Seller stalls to tomorrow, Chanakya gives him a courier that's working today plus the reputation cost of waiting |
| c02 | ELITE FINDS | 12 | Reputation score 94 → 87 and PDP views down 31%. The seller's own numbers are the lever |
| c03 | Elvara | 14 | ₹28k Prada, buyer has ordered 9 times. Payout cleared first, then traded on lifetime value |
| c04 | Mindyourkicks | 16 | **Payout: order never marked complete.** Fixed from the backend, confirmed 3 days later, then moved to the open order |
| c05 | Manan | 14 | **Payout: customer hasn't received delivery yet.** The clock starts at delivery, not dispatch |
| c06 | Delicc Enterprises | 11 | **Bulk follow-up.** Five orders due the same day, clubbed into one message |
| c07 | DJ1 | 10 | **X−1 reminder.** Seller commits to the 24th, Chanakya lands on the 23rd |
| c08 | TopGun | 11 | "Next week" negotiated down to a date the seller picks himself |
| c09 | Sneak Drip | 15 | Payout used as the reason not to ship. Money cleared, then the order argued out of the queue anyway |
| c10 | DS.WT | 13 | Bulk follow-up with a ₹23k exception chased to a 9pm answer |

Nine of ten are order-first. The three payout threads all resolve into a shipment, because
that is the point of fixing the payout.

## How Chanakya sounds

Lifted from the production screenshots: lowercase, short, "brother", no throat-clearing,
and a counter-offer rather than a request.

> why tomorrow, please do it today customer already is anxious

> 10 other sellers used delhivery today because of the same issue, can you just try
> delhivery and see if works? but please reship today, it will help with your seller
> reputation score massively

> brother if you hold it till monday its 12 days and it becomes a cancel. then you lose the
> sale and the payout on it. ship tomorrow and ill make sure monday lands

The negotiation levers, in order of how often they land: **reputation score and PDP views**,
**what the buyer is worth**, **what the delay actually costs the seller**, and **a courier
that is working right now**. Chanakya never just repeats the ask.

Sellers answer the way they actually do: `agle hafte bhejenge`, `payout atka hua hai`,
`i'll reship tomorrow`, `tirupati shipment isnt working today`.

## Payout handling

Two cases, in the proportion they actually occur:

1. **Not marked complete** (c03, c04, c09 — the majority). The seller never closed the
   delivered order, so the payout never released. Chanakya says the line and fixes it:
   *"dont worry, ill get it marked complete from the backend and your payout will be
   processed"*.
2. **Customer hasn't received it yet** (c05). Nothing is broken; the seller just thinks the
   clock starts at dispatch.

c04 is the full arc the flow is meant to have: problem → backend fix → **Chanakya comes back
three days later** to confirm the money landed → then the open shipment. One continued
relationship, not three tickets.

## Follow-up behaviour

- Seller commits to date X → Chanakya lands on **X−1**, and asks to hear about a slip *the
  night before*, not on the evening of.
- Several orders due the same day → **one message listing 2 to 6 of them**, then only the
  exception gets split out. Five separate chases get one reply and four ignored messages.

## Data

Every SX id, seller number, store name, product, price, date and reliability stat is real,
read GET-only from Chanakya's Supabase. `verify_ids.py` proves each id exists **and belongs
to the seller it's used against**:

```
23 id/draft pairs across 10 drafts
all ids real and attributed to the right seller
```

Chanakya's sender is **+91 92176 76103** (verified name Rajiv, GREEN). The words are
written. Nothing here was sent.

## The UI

The renderer, CSS and markup are lifted verbatim from `csat-review.html`, vendored into
`shell/page.html` with all customer data stripped, so the repo builds standalone. Changes:
labels (`Prithvi`→`Chanakya`, `On customer`→`On seller`), the SX id in the thread header,
the Human-attributed and NPS tiles removed, an opener for the details modal (unreachable in
the original), and the **In → Chanakya → Out** strip.

## Checks the build enforces

- a seller-facing message over 1200 chars, or containing markdown
- an em dash in seller copy
- a bare 14-digit number that reads as a customer's CC order id — AWBs are allowed, because
  they're the same shape and are fine to send
- SX ids only, mirroring `lcr.check_seller_copy`

`build.py` also still supports the older skeleton format (`template` + `texts`), where a
draft copies a real csat-review chat message-for-message. The 30-message selection floor
only binds those drafts; the order-chasing threads set their own length.

See `HANDOFF.md` for the full build, extend and verify guide.
