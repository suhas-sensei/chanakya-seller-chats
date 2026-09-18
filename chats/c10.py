"""Bulk follow-up with a high value exception. Six orders clubbed, one worth chasing late.

Same bulk shape as c06, but the exception is a 23k piece for a repeat buyer, so Chanakya
asks to be messaged at 10pm rather than waiting for the morning.
"""

CHAT = {
    "file": "c10", "id": 9010,
    "wa": "918860608766", "name": "DS.WT", "score": 5, "nps": 9,
    "sop": "scattered_reply",
    "sx": "SX322647 / SX323083 / SX320118 / SX312849 / SX324592 / SX320011",
    "seller_note": "8520 shipped, 86.72% fulfilment, 3221 rejected, avg 9.1 days",
    "order_note": "Six due the same day; SX320011 Louis Vuitton Icon, Rs 23,057, buyer has "
                  "ordered 6 times this year",
    "flow": {
        "input": "six orders due the same day, one a 23k piece for a repeat buyer",
        "action": "clubbed the reminder, released the five and chased the LV late into the "
                  "evening for a same-night answer",
        "resolution": "five out that day, LV sourced by 9pm and shipped next morning",
    },
    "turns": [
        ("2026-09-19 09:05", "cx",
         "brother, 6 of yours are due to ship today. one message instead of six\n\n"
         "SX322647 polo RL white graphic\nSX323083 polo RL white graphic\n"
         "SX320118 polo RL navy\nSX312849 prada paradoxe\nSX324592 coach nolita 19\n"
         "SX320011 LV icon\n\nany of these not going out?"),
        ("2026-09-19 09:34", "sl", "5 ja rahe hain. LV wala supplier se nahi aaya"),
        ("2026-09-19 09:35", "cx",
         "thats the one i care about. SX320011 is 23,057 and that buyer has bought from us "
         "6 times this year"),
        ("2026-09-19 09:39", "sl", "pata hai, par piece hi nahi hai abhi"),
        ("2026-09-19 09:40", "cx", "when does your supplier confirm?"),
        ("2026-09-19 09:43", "sl", "shaam tak bata dega"),
        ("2026-09-19 09:44", "cx",
         "ok. push the 5 out now and message me the moment he confirms, even if its 10pm. "
         "on a piece this size i want to give the buyer a real date today, not tomorrow"),
        ("2026-09-19 09:47", "sl", "theek hai"),
        ("2026-09-19 21:10", "sl", "LV mil gaya, kal subah nikal jayega"),
        ("2026-09-19 21:12", "cx",
         "thats the one i was worried about. thanks for messaging this late brother"),
        ("2026-09-19 21:13", "cx",
         "ill tell the buyer tomorrow morning dispatch, they wont have to ask"),
        ("2026-09-20 10:05", "sl", "nikal gaya"),
        ("2026-09-20 10:07", "cx", "all 6 done. clean week on your board"),
    ],
}
