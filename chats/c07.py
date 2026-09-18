"""The X minus 1 reminder. Seller commits to a date, Chanakya lands the day before.

Short by design. The whole value is the message on the 23rd, plus asking to be told the
night before if the dependency slips rather than on the evening of the date itself.
"""

CHAT = {
    "file": "c07", "id": 9007,
    "wa": "919716433953", "name": "DJ1", "score": 5, "nps": None,
    "sop": "promised_ship_date", "sx": "SX318911",
    "seller_note": "4510 shipped, 83.13% fulfilment, 920 rejected, avg 19.6 days",
    "order_note": "SX318911 Seiko Mod Nautilus Denim, Rs 21,651, guaranteed 8 Sep, Purulia",
    "flow": {
        "input": "SX318911 well past guarantee, seller commits to the 24th",
        "action": "reminded on the 23rd and asked to hear about a slip the night before, "
                  "not the evening of",
        "resolution": "shipped on the 24th as committed",
    },
    "turns": [
        ("2026-09-21 10:40", "cx",
         "DJ1, chanakya. SX318911 seiko mod nautilus denim. guaranteed was the 8th. when "
         "can you ship brother?"),
        ("2026-09-21 11:02", "sl", "24 ko pakka"),
        ("2026-09-21 11:03", "cx", "24th noted, thats 3 days out. ill hold you to it"),
        ("2026-09-23 10:15", "cx",
         "brother, SX318911 is scheduled for tomorrow. heads up so it doesnt slip"),
        ("2026-09-23 10:41", "sl", "haan yaad hai, dial aaj aa raha hai"),
        ("2026-09-23 10:42", "cx",
         "good. if the dial doesnt land today tell me tonight, not tomorrow evening. i can "
         "do something with a day, i cant do anything with an hour"),
        ("2026-09-23 10:46", "sl", "haan bata dunga"),
        ("2026-09-24 09:20", "sl", "nikal gaya subah"),
        ("2026-09-24 09:22", "cx",
         "AWB showing, bluedart. you said the 24th and you did the 24th, thats on your "
         "record now"),
        ("2026-09-24 09:30", "sl", "thanks bhai"),
    ],
}
