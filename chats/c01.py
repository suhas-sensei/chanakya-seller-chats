"""RTO reship. Courier workaround plus the reputation angle to get it out the same day.

Closest to the reference screenshots: seller stalls to "tomorrow", Chanakya refuses the
extra day, seller gives a courier excuse, Chanakya answers it with what other sellers did
today and closes on reputation score.
"""

CHAT = {
    "file": "c01", "id": 9001,
    "wa": "919899230497", "name": "Dipanshu", "score": 5, "nps": None,
    "sop": "urgent_delivery", "sx": "SX315558",
    "seller_note": "1585 shipped, 90.82% fulfilment, avg 10.1 days",
    "order_note": "SX315558 On Running Cloud 6 Geo Waterproof Dew Gobi (W), Rs 23,297, "
                  "RTO'd and back with the seller",
    "flow": {
        "input": "SX315558 came back RTO, sitting with the seller",
        "action": "refused the extra day, gave him a courier that was working and the "
                  "reputation cost of waiting",
        "resolution": "reshipped same day on Delhivery, tracking live",
    },
    "turns": [
        ("2026-09-17 19:16", "cx",
         "hey Dipanshu, chanakya from sourcex. order SX315558 got RTO'd, AWB "
         "19041902816422. did you receive it back? will you reship or whats the plan?"),
        ("2026-09-17 19:18", "sl", "Will check tom"),
        ("2026-09-17 19:22", "cx", "cool, waiting for your update tomorrow"),
        ("2026-09-18 11:00", "cx", "brother any update?"),
        ("2026-09-18 11:30", "sl", "i'll reship tomorrow"),
        ("2026-09-18 11:31", "cx",
         "why tomorrow, please do it today customer already is anxious"),
        ("2026-09-18 12:01", "sl", "tirupati shipment isnt working today"),
        ("2026-09-18 12:02", "cx",
         "10 other sellers used delhivery today because of the same issue, can you just "
         "try delhivery and see if works? but please reship today, it will help with your "
         "seller reputation score massively"),
        ("2026-09-18 16:02", "sl", "reshipped w delhivery, check your portal for tracking"),
        ("2026-09-18 16:03", "cx", "done thanks brother"),
        ("2026-09-18 16:04", "cx",
         "tracking is live, ill keep an eye on it till it delivers"),
    ],
}
