"""High value customer. Seller is blocked on payout, Chanakya clears it then trades on
who the buyer is.

Two levers in one thread: unblock the money so the excuse is gone, then use the customer's
lifetime value to buy a same-day dispatch on a 28k piece.
"""

CHAT = {
    "file": "c03", "id": 9003,
    "wa": "918575633111", "name": "Elvara", "score": 5, "nps": 10,
    "sop": "urgent_delivery", "sx": "SX321255",
    "seller_note": "7938 shipped, 86.22% fulfilment, 1371 rejected, avg 10.1 days",
    "order_note": "SX321255 Prada Square Sunglasses Black, Rs 28,078, guaranteed 11 Sep, "
                  "buyer has ordered 9 times",
    "flow": {
        "input": "SX321255 held back, seller refusing to ship until payout clears",
        "action": "cleared the payout block from the backend, then traded on the buyer's "
                  "9 orders and 4.2L lifetime",
        "resolution": "shipped same day, packed to the buyer's known complaint",
    },
    "turns": [
        ("2026-09-17 12:05", "cx",
         "Elvara, chanakya here. SX321255 prada square sunglasses, 28,078. guaranteed "
         "11 sep, still not shipped. whats holding it brother?"),
        ("2026-09-17 12:20", "sl",
         "payout atka hua hai, 6 order ka paisa nahi aaya. jab tak clear nahi hoga nahi "
         "bhejenge"),
        ("2026-09-17 12:21", "cx", "let me look at that before i ask you for anything else"),
        ("2026-09-17 12:26", "cx",
         "found it. 5 of those 6 are delivered but not marked complete from your side, "
         "thats the only thing holding them. dont worry, ill get it marked complete from "
         "the backend and your payout will be processed"),
        ("2026-09-17 12:29", "sl", "sach me? mujhe laga aapke side ka issue hai"),
        ("2026-09-17 12:30", "cx",
         "no, its a two tap thing nobody walked you through. done from my end now, it goes "
         "in the next run"),
        ("2026-09-17 12:33", "sl", "thank you bhai"),
        ("2026-09-17 12:35", "cx",
         "now SX321255. this buyer has ordered 9 times from us, 4.2 lakh lifetime. they "
         "asked about this pair twice this week"),
        ("2026-09-17 12:38", "sl", "achha wo regular hai"),
        ("2026-09-17 12:39", "cx",
         "and they buy at this price point every month. one bad delivery on a 28k piece "
         "and we lose the next 10 orders, and those orders come to sellers like you"),
        ("2026-09-17 12:44", "sl", "samajh gaya, aaj hi nikal jayega"),
        ("2026-09-17 12:45", "cx",
         "appreciate it brother. one thing, pack the hard case with fill around it. this "
         "buyer has flagged loose packaging before"),
        ("2026-09-17 17:50", "sl", "haan dhyan rakha. nikal gaya, AWB portal pe hai"),
        ("2026-09-17 17:52", "cx", "got it, thanks brother"),
    ],
}
