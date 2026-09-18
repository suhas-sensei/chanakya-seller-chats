# Chanakya seller chats — order-chasing drafts

Eight drafted WhatsApp relationships between **Chanakya** and real SourceX sellers, rendered
in the csat-review ops console.

Each one runs **weeks**, not one sitting, and is built from short transactional episodes: a
reminder, a date, a follow-up, a payout, a sourcing question, an RTO. That is the shape of
the real thing.

```bash
python3 build.py                 # rebuild the page + JSON, run every check
python3 verify_ids.py            # every SX id real, and owned by the right seller
open chanakya-seller-chats.html
```

## Grounded in the real exports

Shape and voice both come from **`Seller WhatsApp Chat Export.zip`** — 34 real seller
threads, 17,276 lines. Measured from it:

| | real exports | these drafts |
|---|---|---|
| messages per thread | median **159**, range 11–842 | 50–88 |
| active days | median **19**, range 2–61 | 8–20 |
| episode length | 3–8 messages | 3–8 messages |

The drafts sit below the real median deliberately — long enough to be a relationship, short
enough to read. `chats/_voice.py` holds the full voice reference, quoted from the exports.

## Chanakya has two registers and switches between them

**Formal** opens *every* thread, and comes back whenever it turns serious — penalties, SLA
breaches, a lost parcel, anything a seller might later dispute. The opener is always the
same three beats, from `chats/_voice.py`: who he is, which order, what he needs.

> Hi TopGun, this is Chanakya from SourceX. I look after seller orders for Culture Circle.
>
> A gentle request about order SX316819 (Seiko Mod GMT Gold). The customer has an urgent
> requirement and has requested delivery by 17 September. Could you please help us fulfil
> this in time? When is the earliest you can ship this order? Thank you!

It drops to Hinglish on the second or third exchange and stays there:

> Can you please confirm the estimated shipping date for order SX333916.
>
> Please note the following. 9 of your 10 open orders are currently in SLA breach. Orders
> that cross the breach window are auto cancelled, and a 5% penalty is deducted.

Plus the fixed blocks, sent verbatim: the `REMINDER 🚨🚨🚨` template and the new-order block,
both marked in the UI as approved templates because that's what they are.

**Terse Hinglish** is the day to day, once there's rapport:

> SX184126 - what is the status of this order?  ·  any update?  ·  ye kab ship ho rha?
> ·  u there?  ·  ???  ·  are bhai  ·  confirm asap  ·  what is the reason of delay?

The status question is asked a dozen ways in the real data, so it's varied here too. When a
seller goes quiet, the same line is repeated verbatim — that's what actually happens.

## Negotiation levers, as actually used

- **SLA and penalty** — "90% of your orders are SLA breached", 5% on auto-cancel, and the
  distinction that a customer cancel carries none
- **TAT and ranking** — "isliye suggest kar raha hu, aapke TAT aur SLA best ho jayenge"
- **holding the date** — "bhai ye aapne bola tha sunday.. and today is tuesday"
- **asking for a real one** — "can you give me exact date? 1-2 din badha ke de do no issue"
- **the buyer** — "customer already is anxious", order count, lifetime value
- **removing the blocker** — a courier that's working today, a payout unblocked

## Eight sellers, eight registers

No two sound alike, and the address term is per seller — never one word for everyone.

| # | seller | msgs | days | register |
|---|---|---|---|---|
| c01 | ELITE FINDS | 52 | 8 | optimistic — "Checking" / "2 min" / "99%" / **boss** |
| c02 | Delicc Enterprises | 55 | 9 | polite — "Pls check" / "Kindly" / 🙏 / **sir, bro** |
| c03 | DS.WT | 69 | 13 | direct — "Any update **bhai**" as a suffix |
| c04 | Mindyourkicks | 75 | 11 | easy — "Hnji.." / "Acha.. koi na." / *no term* |
| c05 | Sneak Drip | 66 | 12 | argues — "Dekhona **bro**" / "where i come from **yaar**" |
| c06 | Dipanshu | 50 | 11 | two words — "yes wait" / "Aajaega" / **bro**, rarely |
| c07 | TopGun | 65 | 12 | numbers only — "15.5k" / "Bhejdia aage" / *no term* |
| c08 | DJ1 | 88 | 20 | wants to call — "Call kru?" / "Okok" |

## What the threads cover

Order-chasing is the spine; the payout threads all resolve into a shipment.

- **Payout, never marked complete** (c02, c04 — the main case). *"Don't worry, I will get it
  marked as complete from the backend and your payout will be processed."* Then Chanakya
  comes back **three days later** to confirm the money landed, and only then moves to the
  open order.
- **Payout, not delivered yet** (c05). The clock starts at delivery, not dispatch.
- **Bulk follow-up** — 5 and 6 orders clubbed into one message, only the exception split out
- **X−1 reminders** throughout, plus "tell me tonight, not tomorrow evening"
- **RTO reship** with a courier workaround (c06)
- **Reputation score and PDP views** dropping (c01), **high-value buyer** (c03)
- SLA breach and the penalty rule, auto-cancels traced to our own push-channel bug, address
  change caught before the label, stuck tracking, sourcing haggles

## Data

Every SX id, seller number, store name, product, price and stat is real, read GET-only from
Chanakya's Supabase. `verify_ids.py` proves each id exists **and belongs to the seller it's
used against** — it caught one order attributed to the wrong seller during this rewrite.

Chanakya's sender is **+91 92176 76103** (verified name Rajiv, GREEN). The words are
written. Nothing here was sent.

## The UI

Renderer, CSS and markup lifted verbatim from `csat-review.html`, vendored into
`shell/page.html` with all customer data stripped so the repo builds standalone. Changes:
labels, the SX id in the thread header, Human-attributed and NPS tiles removed, an opener
for the details modal, the **In → Chanakya → Out** strip, and a dashed treatment for
approved-template sends.

See `HANDOFF.md` for the full build, extend and verify guide.
