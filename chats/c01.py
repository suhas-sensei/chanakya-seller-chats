"""ELITE FINDS. Optimistic, always "checking", always 99 percent. Calls Chanakya boss.

Seller register: "Wait" / "Checking" / "2 min" / "Ho jayega" / "99%" / "bosss". Never
commits to a number without being pushed, then over-promises slightly.

Episodes: formal open + REMINDER, a date that slips, the reputation and PDP negotiation,
a bulk list of four, an SLA warning in the formal register, resolution.
"""

from ._voice import new_order, reminder

GF = "Nike Gamma Force (W) 'White & Pink'"

CHAT = {
    "file": "c01", "id": 9001,
    "wa": "918766709652", "name": "ELITE FINDS", "score": 5, "nps": 9,
    "sop": "promised_ship_date", "sx": "SX333916 / SX332884 / SX331593 / SX315597",
    "seller_note": "2904 shipped, 92.96% fulfilment, 391 rejected, avg 8.6 days",
    "order_note": "Nine open orders, all Nike Gamma Force (W) White and Pink. Oldest "
                  "SX296908 guaranteed 15 Jul",
    "flow": {
        "input": "nine open orders on one SKU, four past SLA",
        "action": "opened formal, chased on the seller's own TAT and PDP numbers, "
                  "clubbed the rest into one list",
        "resolution": "four out that week, SLA breach down from 9 to 2",
    },
    "turns": [
        ("2026-08-24 11:40", "cx",
         "Hello, this is Chanakya from SourceX. I handle seller orders for Culture Circle."),
        ("2026-08-24 11:41", "cx",
         "Can you please confirm the estimated shipping date for order SX333916."),
        ("2026-08-24 11:41", "tpl", reminder("333916", GF, "UK5")),
        ("2026-08-24 12:15", "sl", "Checking"),
        ("2026-08-24 12:15", "sl", "2 min"),
        ("2026-08-24 12:31", "sl", "Will ship today boss"),
        ("2026-08-24 12:32", "cx", "Okay"),
        ("2026-08-26 10:05", "cx", "SX333916 - what is the status of this order?"),
        ("2026-08-26 15:22", "cx", "SX333916 - what is the status of this order?"),
        ("2026-08-26 15:40", "sl", "Checking"),
        ("2026-08-26 15:52", "sl", "Ho jayega"),
        ("2026-08-26 15:52", "sl", "99%"),
        ("2026-08-26 15:53", "cx",
         "bhai ye aapne bola tha sunday will ship.. and today is tuesday. can you confirm "
         "me the status?"),
        ("2026-08-26 16:10", "sl", "Bulk aane wala hai"),
        ("2026-08-26 16:10", "sl", "Iss week"),
        ("2026-08-26 16:12", "cx", "can you give me exact date? 1-2 din badha ke de do no issue"),
        ("2026-08-26 16:20", "sl", "28 pakka"),
        ("2026-08-26 16:21", "cx", "28 noted"),
        ("2026-08-27 11:00", "cx", "SX333916 kal ship ho raha hai na, reminder"),
        ("2026-08-27 11:26", "sl", "Haan boss"),
        ("2026-08-28 17:30", "cx", "any update?"),
        ("2026-08-28 19:02", "cx", "u there?"),
        ("2026-08-29 10:14", "sl", "Bulk late ho gaya"),
        ("2026-08-29 10:15", "cx", "what is the reason of delay?"),
        ("2026-08-29 10:22", "sl", "Supplier ne 3 din aur maang liye"),
        ("2026-08-29 10:30", "cx",
         "bhai ek baat batata hu. aapke 9 orders open hain aur 4 SLA breach me hain. iska "
         "asar seedha listing pe pad raha hai"),
        ("2026-08-29 10:31", "cx",
         "aapka seller score 94 se 87 aa gaya hai is hafte, aur PDP views 31 percent neeche "
         "hain. ye warning nahi hai, ye already ho raha hai"),
        ("2026-08-29 10:38", "sl", "Views to kam the.. samajh nahi aa raha tha kyu"),
        ("2026-08-29 10:39", "cx",
         "ab pata hai. score wapas aata hai jaise hi late orders clear hote hain. isliye "
         "suggest kar raha hu, aapke TAT aur SLA best ho jayenge timely shipping se"),
        ("2026-08-29 10:45", "sl", "Samajh gaya boss"),
        ("2026-09-02 12:05", "sl", "Bulk aa gaya"),
        ("2026-09-02 12:06", "cx",
         "good. ye 4 aaj nikal jayenge?\n\nSX333916 UK5\nSX332884 UK6\nSX331593 UK4.5\n"
         "SX331712 UK7"),
        ("2026-09-02 12:20", "sl", "3 ho jayenge. UK4.5 nahi aaya"),
        ("2026-09-02 12:21", "cx", "SX331593 me kitna time?"),
        ("2026-09-02 12:26", "sl", "Next bulk"),
        ("2026-09-02 12:28", "cx",
         "wo 10 din ho jayega aur ye order already 20 din late hai. main customer ko cancel "
         "offer kar deta hu, warna aapke SLA pe aur load aayega"),
        ("2026-09-02 12:33", "sl", "Theek hai kar do"),
        ("2026-09-02 18:40", "sl", "3 nikal gaye, tracking daal di"),
        ("2026-09-02 18:42", "cx", "dekh liya, thanks"),
        ("2026-09-05 11:10", "cx",
         "Please note, SX296908 has now crossed 50 days and will be auto cancelled on "
         "Monday with a 5% penalty against the order value. Kindly confirm today if it can "
         "be shipped."),
        ("2026-09-05 11:34", "sl", "Wait"),
        ("2026-09-05 11:52", "sl", "Wo size to discontinue ho gaya bosss"),
        ("2026-09-05 11:54", "cx",
         "then let me close it from our side as unavailable rather than let it auto cancel. "
         "no penalty that way. confirm?"),
        ("2026-09-05 11:58", "sl", "Haan please"),
        ("2026-09-05 12:01", "cx", "done"),
        ("2026-09-17 10:20", "cx",
         "bhai update - aapke SLA breach 9 se 2 pe aa gaye hain aur PDP views 18 percent "
         "recover ho chuke hain"),
        ("2026-09-17 10:41", "sl", "Achha laga sunke boss"),
        ("2026-09-17 10:42", "cx", "same day dispatch continue rakho, wahi kaam kar raha hai"),
        ("2026-09-17 10:44", "sl", "Haan"),
        ("2026-09-17 14:05", "tpl",
         new_order(GF, "UK6.5", "3,477", "SX336018")),
        ("2026-09-17 14:30", "sl", "In hand hai, kal nikal dunga"),
        ("2026-09-17 14:31", "cx", "thik hai"),
    ],
}
