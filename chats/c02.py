"""Reputation score and PDP views. The negotiation lever is the seller's own numbers.

Seller opens with "next week". Chanakya does not argue about the date, he shows the score
drop and the view drop it already caused, which reframes shipping today as the seller's
problem rather than ours.
"""

CHAT = {
    "file": "c02", "id": 9002,
    "wa": "918766709652", "name": "ELITE FINDS", "score": 5, "nps": 9,
    "sop": "promised_ship_date", "sx": "SX333916",
    "seller_note": "2904 shipped, 92.96% fulfilment, 391 rejected, avg 8.6 days",
    "order_note": "SX333916 Nike Gamma Force (W) White and Pink, Rs 3,178, guaranteed "
                  "9 Sep, Bangalore",
    "flow": {
        "input": "SX333916 four days past guarantee, seller offering next week",
        "action": "showed the reputation score drop and the 31% PDP view fall it caused, "
                  "traded next week for tonight's pickup",
        "resolution": "three overdue orders out the same evening",
    },
    "turns": [
        ("2026-09-17 10:02", "cx",
         "hey ELITE FINDS, chanakya from sourcex. SX333916 nike gamma force W white pink, "
         "guaranteed was 9 sep. where is it brother?"),
        ("2026-09-17 10:26", "sl", "agle hafte bhejenge"),
        ("2026-09-17 10:27", "cx",
         "next week is 7 days away and this one is already 4 days late. thats 11 days for "
         "a pair you have in hand"),
        ("2026-09-17 10:31", "sl", "abhi bulk aaya nahi hai"),
        ("2026-09-17 10:33", "cx",
         "brother your reputation score went 94 to 87 this week and your PDP views are "
         "down 31 percent because of it. thats not a warning, its already happening to "
         "your listings"),
        ("2026-09-17 10:38", "sl",
         "views kam ho rahe the, samajh nahi aa raha tha kyu"),
        ("2026-09-17 10:39", "cx",
         "now you know. the score recovers as soon as the late ones clear. ship this plus "
         "the 2 other overdue today and youll see views back inside a week"),
        ("2026-09-17 10:44", "sl", "aaj ka pickup to nikal gaya"),
        ("2026-09-17 10:45", "cx",
         "delhivery runs an evening pickup till 7. can you push these 3 into that? one day "
         "matters a lot on this score"),
        ("2026-09-17 10:52", "sl", "theek hai try karta hu"),
        ("2026-09-17 18:40", "sl", "3 nikal gaye, SX333916 bhi usme hai"),
        ("2026-09-17 18:42", "cx",
         "perfect, thats the fastest way back up. ill check your score friday and tell you "
         "where it lands"),
    ],
}
