"""Copies Viraj . (src 8725): 36 messages, 6 days, CSAT 5, agentic.

Shape being matched: the terse end of the agent register. The real chat's bot replies have
a 43-character median, it carries two tool steps that render as their own bubbles, a
teammate posts alone across two days with one 443-character message, and it ends with five
consecutive seller messages that nobody answers. The rating was recorded before that tail,
which is why a 5 sits on a thread trailing off into silence.
"""

CHAT = {
    "file": "c03", "id": 9003, "template": 36,
    "codes": "cbcbcbcbcbcbbcbbhhhhhhcbcbcbcbbccccc",
    "wa": "917275493283", "name": "Hypestreet India", "score": 5, "nps": None,
    "sop": "size_exchange", "sx": "SX334538",
    "seller_note": "1747 shipped, 89.62% fulfilment, 217 rejected, avg 4.8 days",
    "order_note": "SX334538 Kenzo Classic T-Shirt Black (S), pickup to Home, Kanpur 208026",
    "texts": [
        "Hi",
        "Hey Hypestreet. Go ahead.",
        "SX334538 ka exchange aaya hai, customer ko M chahiye. Mere paas M hai but return "
        "address confirm karna hai",
        "Right. The Kenzo Classic T-Shirt in S comes back to you and the M goes out. Your "
        "Home address on file is J104 Ratan Orbit, Indira Nagar, Kanpur 208026. Same one?",
        "Haan ji",
        "Scheduled. Nothing else.",
        "Theek hai thanks",
        "Pickup scan lands tomorrow, I'll say.",
        # -- five days later
        "Bhai pickup abhi tak nahi aaya hai",
        "That's four days, too long. Let me look at it rather than guess.",
        "Haan dekh lo please",
        "used verify_tracking",
        "Found it. The pickup was attempted on the 19th and marked customer not available, "
        "which is wrong, the pickup is from you and not the customer. The courier logged it "
        "against the wrong leg. I've raised it and asked for a fresh attempt tomorrow. "
        "Nothing for you to do.",
        "Achha ji",
        "used schedule_recheck",
        "Re-check set for tomorrow evening. If the courier misses it again I'll stop asking "
        "them and route it through the other partner instead, which costs us a day but ends "
        "the loop. Either way you'll hear from me tomorrow rather than having to chase it "
        "next week.",
        # -- a teammate, alone, across two days
        "Hi Hypestreet, Nikhil from Seller Ops, picking up the pickup failures.",
        "We've looked at the last thirty reverse pickups booked to your Kanpur address.",
        "Eleven of them failed on the first attempt, all with the same wrong reason code. "
        "That isn't your address and it isn't the courier's driver, it's how the booking is "
        "being generated at our end for Kanpur pincodes.",
        "So this was ours. You've been chasing a problem we created, eleven separate times, "
        "and nobody on our side told you what it actually was.",
        "Two things are changing. The booking template for your pincode is being corrected "
        "this week, which should take the first attempt failure rate to near zero. And for "
        "the eleven that failed, we're crediting the extra handling back to your account "
        "rather than making you claim it, because you shouldn't have to file for our bug. "
        "You don't need to do anything for either. Chanakya will confirm when the template "
        "fix is live.",
        "One ask in return. If a pickup fails after this week, tell Chanakya the same day "
        "rather than waiting to see whether it retries. A same day report gives us the "
        "courier log while it's still useful. After 48 hours it's gone.",
        # -- a fortnight on
        "Bhai pickup theek chal raha",
        "Good to hear. I checked before replying: eighteen reverse pickups since the fix, "
        "seventeen collected on the first attempt. That's the number that was eleven out of "
        "thirty. You should stop seeing this entirely. Thanks for flagging it.",
        "Badhiya",
        "Anything else open on your side?",
        "Nahi, sab clear hai",
        "Then I'll leave you to it. Have a good week.",
        "Aap bhi bhai, thanks",
        "Anytime, take care.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        # -- three days later the seller comes back and nobody picks it up
        "Bhai ek naya exchange aaya hai",
        "?",
        "SX320771?",
        ".",
        "Kal bata dena",
    ],
}
