"""Payout pending because the seller never marked the orders complete. The main case.

The full arc the flow is meant to have: payout problem, fix it from the backend, come back
three days later to confirm the money actually landed, and only then move to the order
that is still sitting. One continued relationship, not three separate tickets.
"""

CHAT = {
    "file": "c04", "id": 9004,
    "wa": "919821187865", "name": "Mindyourkicks", "score": 5, "nps": 10,
    "sop": "payout_pending", "sx": "SX337953 / SX339047",
    "seller_note": "1004 shipped, 94.57% fulfilment, avg 2.2 days, fastest dispatch here",
    "order_note": "Three delivered orders unmarked, blocking payout. SX339047 Rasasi "
                  "Hawas Ice still open, customer needed it by 17 Sep",
    "flow": {
        "input": "seller chasing payout on three delivered orders",
        "action": "found them unmarked, closed them from the backend, confirmed the money "
                  "landed three days later, then moved to the open order",
        "resolution": "payout received, SX339047 shipped the same evening",
    },
    "turns": [
        ("2026-09-17 10:12", "sl", "bhai payout nahi aaya 3 order ka"),
        ("2026-09-17 10:14", "cx", "checking"),
        ("2026-09-17 10:16", "cx",
         "SX337952, SX337953 and SX335948 are all delivered but not marked complete from "
         "your side. payout only releases after that, thats why its sitting"),
        ("2026-09-17 10:18", "sl", "maine to kuch kiya hi nahi, complete kaise karte hain"),
        ("2026-09-17 10:19", "cx",
         "dont worry, ill get it marked complete from the backend and your payout will be "
         "processed. you dont have to do anything"),
        ("2026-09-17 10:21", "sl", "ok bhai thank you"),
        ("2026-09-17 10:22", "cx", "done. next run is monday, it should land then"),
        ("2026-09-20 11:05", "cx",
         "brother, payout aa gaya? i can see it went through from my side"),
        ("2026-09-20 11:40", "sl", "haan aa gaya, abhi check kiya. teeno ka pura"),
        ("2026-09-20 11:41", "cx",
         "good. going forward mark it complete as soon as the customer receives it, then "
         "you never have to wait on me for this"),
        ("2026-09-20 11:43", "sl", "haan ab pata chal gaya"),
        ("2026-09-20 11:44", "cx",
         "one more thing while youre here. SX339047 rasasi hawas ice is still open, "
         "customer needed it by the 17th. when are you shipping?"),
        ("2026-09-20 11:47", "sl", "aaj sham tak nikal jayega"),
        ("2026-09-20 11:47", "cx", "today evening, noted. ill check tonight"),
        ("2026-09-20 19:30", "cx", "AWB is up, xpressbees. thanks brother"),
        ("2026-09-20 19:41", "sl", "ho gaya"),
    ],
}
