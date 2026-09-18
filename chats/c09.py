"""Payout used as the reason not to ship. Chanakya clears the money, then refuses to let
the order wait for it anyway.

The second half is the real negotiation: the payout is fixed but will not land until
Monday, and holding the order till then turns a sale into a cancellation.
"""

CHAT = {
    "file": "c09", "id": 9009,
    "wa": "917774922888", "name": "Sneak Drip", "score": 4, "nps": 8,
    "sop": "payout_pending", "sx": "SX327430",
    "seller_note": "316 shipped, 79.95% fulfilment, 82 rejected, avg 4.1 days",
    "order_note": "Four delivered orders unmarked, blocking payout. SX327430 Polo Ralph "
                  "Lauren Tipped Polo (XL) held back behind it",
    "flow": {
        "input": "seller refusing to ship SX327430 until four stuck payouts clear",
        "action": "closed the four from the backend, then argued the order out of the "
                  "queue rather than letting it wait for Monday",
        "resolution": "order shipped next day and delivered Saturday, payout ran Monday",
    },
    "turns": [
        ("2026-09-17 14:05", "cx",
         "Sneak Drip, chanakya. SX327430 polo ralph lauren tipped polo XL, still sitting "
         "with you. whats the plan brother?"),
        ("2026-09-17 14:22", "sl",
         "pehle payout clear karo. 4 order ka paisa atka hai. uske baad hi bhejenge"),
        ("2026-09-17 14:23", "cx", "fair. let me check that before i ask you for anything"),
        ("2026-09-17 14:29", "cx",
         "all 4 are delivered but not marked complete from your side. SX315848, SX325831, "
         "SX320932 and SX295538. thats the whole blocker"),
        ("2026-09-17 14:32", "sl", "matlab galti meri hai?"),
        ("2026-09-17 14:33", "cx",
         "no, its a step nobody walked you through. dont worry, ill get it marked complete "
         "from the backend and your payout will be processed"),
        ("2026-09-17 14:36", "sl", "kab tak aayega"),
        ("2026-09-17 14:37", "cx",
         "monday run. im not going to tell you friday because it wont be friday"),
        ("2026-09-17 14:40", "sl", "theek hai"),
        ("2026-09-17 14:41", "cx",
         "now SX327430. can that go out tomorrow? the customer has waited 8 days and that "
         "order isnt tied to the payout at all"),
        ("2026-09-17 14:45", "sl", "payout aane ke baad"),
        ("2026-09-17 14:46", "cx",
         "brother if you hold it till monday its 12 days and it becomes a cancel. then you "
         "lose the sale and the payout on it. ship tomorrow and ill make sure monday lands"),
        ("2026-09-17 14:52", "sl", "chalo kal bhej dete hain"),
        ("2026-09-22 09:30", "cx",
         "payout ran this morning, all 4. and SX327430 delivered saturday. both sides done"),
        ("2026-09-22 09:48", "sl", "aa gaya bhai, dekh liya. thanks"),
    ],
}
