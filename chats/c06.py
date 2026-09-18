"""Dipanshu. Two and three word replies, almost never a full sentence. Says bro, rarely.

Seller register: "yes wait" / "Little bit" / "No bro" / "Aajaega" / "Eta all". Getting a
date out of him takes three messages, so Chanakya stops asking open questions and starts
offering dates to accept or reject.

Episodes: an RTO where the seller stalls to tomorrow and the courier is the excuse, a
tracking stall, and a run of On Running orders where the shipping date has to be pinned
each time.
"""

from ._voice import intro, new_order, open_rto, reminder

CHAT = {
    "file": "c06", "id": 9006,
    "wa": "919899230497", "name": "Dipanshu", "score": 5, "nps": None,
    "sop": "urgent_delivery", "sx": "SX315558 / SX339219 / SX339803 / SX338392",
    "seller_note": "1585 shipped, 90.82% fulfilment, 167 rejected, avg 10.1 days",
    "order_note": "SX315558 On Cloud 6 Geo Waterproof, Rs 23,297, RTO'd and back with the "
                  "seller. Three more On Running orders open",
    "flow": {
        "input": "SX315558 came back RTO, three more open behind it",
        "action": "refused the extra day, named a courier that was working, then switched "
                  "to offering dates instead of asking for them",
        "resolution": "reshipped same day, all four cleared inside the week",
    },
    "turns": [
        ("2026-09-01 19:15", "cx", intro("Dipanshu")),
        ("2026-09-01 19:16", "cx", open_rto("SX315558", "19041902816422")),
        ("2026-09-01 19:18", "sl", "Will check tom"),
        ("2026-09-01 19:22", "cx", "cool, waiting for your update tomorrow"),
        ("2026-09-02 11:00", "cx", "any update?"),
        ("2026-09-02 11:30", "sl", "i'll reship tomorrow"),
        ("2026-09-02 11:31", "cx",
         "why tomorrow, please do it today customer already is anxious"),
        ("2026-09-02 12:01", "sl", "tirupati shipment isnt working today"),
        ("2026-09-02 12:02", "cx",
         "10 other sellers used delhivery today because of the same issue, can you just try "
         "delhivery and see if works? but please reship today, it will help with your "
         "seller reputation score massively"),
        ("2026-09-02 16:02", "sl", "reshipped w delhivery, check your portal for tracking"),
        ("2026-09-02 16:03", "cx", "done thanks"),
        ("2026-09-02 16:04", "cx", "tracking live hai, main delivery tak dekh lunga"),
        ("2026-09-05 10:20", "cx", "SX339219 - status of this shipment?"),
        ("2026-09-05 12:40", "sl", "yes wait"),
        ("2026-09-05 15:10", "cx", "any update?"),
        ("2026-09-05 16:30", "sl", "Monday"),
        ("2026-09-05 16:31", "cx", "monday matlab 8 september?"),
        ("2026-09-05 16:35", "sl", "Han"),
        ("2026-09-07 11:00", "cx", "kal SX339219 ship ho raha hai, reminder"),
        ("2026-09-07 11:40", "sl", "Ok"),
        ("2026-09-08 17:30", "cx", "SX339219 - what is the update on this"),
        ("2026-09-08 19:15", "cx", "u there?"),
        ("2026-09-09 10:05", "sl", "Kal ho jayega"),
        ("2026-09-09 10:06", "cx",
         "bhai ye aapne bola tha monday, aur aaj tuesday hai. what is the reason of delay?"),
        ("2026-09-09 10:20", "sl", "Box damage tha"),
        ("2026-09-09 10:22", "cx",
         "achha, to wo batana chahiye tha monday ko. main customer ko galat date de chuka "
         "hu ab"),
        ("2026-09-09 10:26", "sl", "Sorry bro"),
        ("2026-09-09 10:28", "cx",
         "koi baat nahi. ab main date poochta nahi hu, main deta hu. 10 september sham tak "
         "nikal sakte ho? haan ya na"),
        ("2026-09-09 10:33", "sl", "Han"),
        ("2026-09-10 18:40", "sl", "Nikal gaya"),
        ("2026-09-10 18:45", "cx", "mil gaya, thanks"),
        ("2026-09-11 15:20", "cx", "On Running Cloudsurfer Next Lumos - in hand?"),
        ("2026-09-11 15:50", "sl", "Eta"),
        ("2026-09-11 15:51", "cx", "kitne din"),
        ("2026-09-11 15:55", "sl", "10 12"),
        ("2026-09-11 15:57", "cx", "payout?"),
        ("2026-09-11 16:02", "sl", "18500"),
        ("2026-09-11 16:10", "cx", "dal diya, 18599 pe"),
        ("2026-09-11 16:11", "tpl",
         new_order("On Running Cloudsurfer Next Lumos Black Dew", "UK9", "18,599",
                   "SX339803")),
        ("2026-09-11 16:30", "sl", "Ok"),
        ("2026-09-14 12:05", "cx",
         "SX315558 deliver ho gaya, signed. wo RTO wala case ab band hai"),
        ("2026-09-14 12:40", "sl", "Good"),
        ("2026-09-16 10:15", "cx",
         "ek baat. aapke 4 me se 3 orders pe date aage badhi hai is mahine. aapka dispatch "
         "average 10 din hai jo theek hai, par date miss hone se customer ko galat bolna "
         "padta hai"),
        ("2026-09-16 10:22", "sl", "Han"),
        ("2026-09-16 10:24", "cx",
         "isliye suggest kar raha hu, jo date de rahe ho usme 1-2 din ka buffer rakho. main "
         "wo date customer ko dunga aur wo hold hogi. aapke TAT aur SLA best ho jayenge"),
        ("2026-09-16 10:30", "sl", "Theek hai, aage se 2 din extra bolunga"),
        ("2026-09-16 10:31", "cx", "wahi chahiye tha"),
        ("2026-09-17 09:40", "tpl",
         reminder("338392", "On Running Cloudmonster 2 White Frost", "UK10")),
        ("2026-09-17 10:30", "sl", "19 ko"),
        ("2026-09-17 10:31", "cx", "19 noted, 18 ko reminder bhej dunga"),
        ("2026-09-17 10:33", "sl", "Ok bro"),
    ],
}
