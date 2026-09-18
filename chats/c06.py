"""Bulk follow-up. Five orders due the same day, clubbed into one message.

The point of the bulk flow: one ping listing everything due, the seller answers once, and
Chanakya only splits out the exception. Five separate chases would get one reply and four
ignored messages.
"""

CHAT = {
    "file": "c06", "id": 9006,
    "wa": "919924028887", "name": "Delicc Enterprises", "score": 5, "nps": 9,
    "sop": "scattered_reply",
    "sx": "SX328656 / SX328627 / SX328626 / SX329759 / SX323268",
    "seller_note": "13804 shipped, 99.14% fulfilment, avg 30.9 days to ship",
    "order_note": "Five orders due to ship the same day; SX328626 short in the lot",
    "flow": {
        "input": "five orders due to ship today on one seller",
        "action": "clubbed all five into a single reminder, split out only the one that "
                  "was short",
        "resolution": "four shipped that evening, the fifth cancelled clean with the buyer",
    },
    "turns": [
        ("2026-09-18 09:10", "cx",
         "morning brother. 5 orders are due to ship today, putting them in one message so "
         "you dont get 5 pings\n\nSX328656 off supply core black\n"
         "SX328627 blacklist bear waffle\nSX328626 blacklist bear waffle\n"
         "SX329759 gilded crane denim\nSX323268 gymbrat acid edge tank\n\nall ready?"),
        ("2026-09-18 09:40", "sl", "4 ready hain. waffle me se ek size nahi mila"),
        ("2026-09-18 09:41", "cx", "which one, SX328627 or SX328626?"),
        ("2026-09-18 09:43", "sl", "SX328626"),
        ("2026-09-18 09:44", "cx",
         "ok. ship the 4 today and ill handle SX328626 with the customer. when does that "
         "size come in?"),
        ("2026-09-18 09:47", "sl", "5 din me next lot"),
        ("2026-09-18 09:48", "cx",
         "5 days is too long for this one, its already 9 days late. ill offer them a "
         "cancel with an apology from us rather than make them wait. that way it doesnt "
         "sit on your board"),
        ("2026-09-18 09:50", "sl", "theek hai kar do"),
        ("2026-09-18 17:20", "cx",
         "4 out of 4 scanned, delhivery. SX328626 the customer took the cancel, so youre "
         "clear for today"),
        ("2026-09-18 17:31", "sl", "badhiya"),
        ("2026-09-18 17:32", "cx",
         "youve got 3 more due thursday, ill club those the same way"),
    ],
}
