"""Negotiating "next week" down to a date. The commonest trade on this lane.

Seller opens with a week, Chanakya prices what that week actually costs, and lands on the
real dependency instead. The date comes from the seller, which is why it holds.
"""

CHAT = {
    "file": "c08", "id": 9008,
    "wa": "917846907195", "name": "TopGun", "score": 5, "nps": 10,
    "sop": "promised_ship_date", "sx": "SX314239",
    "seller_note": "343 shipped, 99.45% fulfilment, 10 rejected, avg 15.7 days",
    "order_note": "SX314239 Seiko Mod Daytona Black, Rs 16,996, guaranteed 1 Sep, Mumbai",
    "flow": {
        "input": "SX314239 ten days past guarantee, seller offering next week",
        "action": "priced the wait against a cancel, found the real dependency and took a "
                  "date off the seller",
        "resolution": "shipped on the 13th, six days earlier than offered",
    },
    "turns": [
        ("2026-09-11 11:15", "cx",
         "TopGun, chanakya. SX314239 seiko mod daytona black, 16,996. guaranteed 1 sep and "
         "its the 11th. where is it brother?"),
        ("2026-09-11 11:38", "sl", "agle hafte"),
        ("2026-09-11 11:39", "cx",
         "next week is 6 more days on top of the 10 already gone. this customer has asked "
         "twice, one more and they cancel"),
        ("2026-09-11 11:44", "sl", "bezel ka kaam chal raha hai, 2 din lagenge"),
        ("2026-09-11 11:45", "cx",
         "2 days i can work with. thats the 13th, not next week. can i give the customer "
         "the 13th?"),
        ("2026-09-11 11:49", "sl", "haan 13 theek hai"),
        ("2026-09-11 11:50", "cx",
         "done. and list the mod builds as ETA next time, then you get a real window "
         "instead of starting every one already late"),
        ("2026-09-11 11:55", "sl", "haan wo karna padega"),
        ("2026-09-13 09:40", "cx", "brother, today is the 13th. SX314239 going out?"),
        ("2026-09-13 12:10", "sl", "haan nikal gaya, DTDC"),
        ("2026-09-13 12:12", "cx", "got it, thanks brother"),
    ],
}
