"""Payout pending because the customer has not received the delivery yet. The second case.

Nothing is broken here, the seller just does not know the payout clock starts at delivery
rather than dispatch. Chanakya says so, waits, confirms, and rolls straight into the next
open order.
"""

CHAT = {
    "file": "c05", "id": 9005,
    "wa": "919810273087", "name": "Manan", "score": 5, "nps": None,
    "sop": "payout_pending", "sx": "SX333662 / SX304406",
    "seller_note": "1166 shipped, 92.82% fulfilment, avg 3.9 days",
    "order_note": "SX333662 ON Cloud 6 Triple White (UK8) in transit to Noida; SX304406 "
                  "ON Cloud 5 Waterproof (UK11.5) still open",
    "flow": {
        "input": "seller chasing payout on an order that has not delivered yet",
        "action": "explained the payout clock starts at delivery, not dispatch, and held "
                  "the date",
        "resolution": "delivered, payout ran on the 22nd, next order dated",
    },
    "turns": [
        ("2026-09-18 15:20", "sl", "SX333662 ka payout kab aayega"),
        ("2026-09-18 15:22", "cx",
         "that one hasnt delivered yet brother. AWB shows in transit, out for delivery "
         "tomorrow in noida"),
        ("2026-09-18 15:25", "sl", "maine to 4 din pehle bhej diya tha"),
        ("2026-09-18 15:26", "cx",
         "you did, and that was on time. the payout clock starts when the customer "
         "actually receives it, not when you dispatch"),
        ("2026-09-18 15:29", "sl", "achha, to delivery ke baad"),
        ("2026-09-18 15:30", "cx",
         "yes. delivery is tomorrow so it should move on the 22nd run"),
        ("2026-09-18 15:32", "sl", "theek hai"),
        ("2026-09-20 10:15", "cx",
         "delivered yesterday, signed for. payout is queued for the 22nd"),
        ("2026-09-20 10:26", "sl", "ok bhai"),
        ("2026-09-22 12:05", "cx", "brother payout aa gaya?"),
        ("2026-09-22 12:31", "sl", "haan aa gaya"),
        ("2026-09-22 12:32", "cx",
         "good. SX304406 is your only open one now, on cloud 5 waterproof UK11.5. when "
         "does that ship?"),
        ("2026-09-22 12:36", "sl", "kal bhej denge"),
        ("2026-09-22 12:36", "cx", "tomorrow noted, ill remind you in the morning"),
    ],
}
