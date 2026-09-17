"""Copies Uthpala H v (src 5235): 42 messages, 6 days, CSAT 4, agentic.

Shape being matched: the thread that goes unanswered. The real chat has a run of seven
consecutive customer messages across two parts of one day, a one-line staff interjection,
four more unanswered customer messages, then a 361-character staff reply three days later
before it finally resolves. This is what the console's Awaiting state actually looks like,
and it still rated 4 once someone answered properly.
"""

CHAT = {
    "file": "c04", "id": 9004, "template": 42,
    "codes": "cbcbcbcbcbcbcbccccccchcccchcbcbcbcbcbcbbcb",
    "wa": "919716433953", "name": "DJ1", "score": 4, "nps": 7,
    "sop": "promised_ship_date", "sx": "SX318911 / SX315454",
    "seller_note": "4510 shipped, 83.13% fulfilment, 920 rejected, avg 19.6 days",
    "order_note": "SX318911 Seiko Mod Nautilus Denim, Rs 21,651, guaranteed 8 Sep, Purulia; "
                  "SX315454 Seiko Mod Lady Datejust, Rs 21,452, Ambala",
    "texts": [
        "Hello SX318911",
        "Hey DJ1. What's happening with that one?",
        "Kal tak bhej denge, pakka wala",
        "I'll take the 18th on SX318911, the Denim Nautilus. It's three days past guarantee "
        "already so I'd rather that date held than moved again.",
        "Ok ji",
        "Noted, thanks DJ1.",
        # -- four days later
        "Bhai isme thoda problem ho gaya hai",
        "Tell me what it is. SX318911 still hasn't moved and we're a week past the date you "
        "gave me.",
        "Dial supplier ne dhoka diya",
        "So the piece was never in hand. That changes this from a delay into a sourcing "
        "problem, and the customer is owed a straight answer. Can you get the dial at all, "
        "or should I put a cancel to them?",
        "Mil jayega bhai, 4-5 din lagenge",
        "Then I'll tell them the 26th and be honest that it's a sourcing wait, not a courier "
        "one. If it slips past that I'm going to recommend they cancel rather than keep them "
        "holding, and I'd rather warn you now than surprise you.",
        "Theek hai bhai, 26 tak pakka ho jayega",
        "Recorded the 26th. Tell me on the 24th if it looks shaky, not on the 26th itself.",
        # -- the seller talks into silence, twice over
        "Bhai sun rahe ho",
        "Ek aur order ka bhi problem hai SX315454",
        "Hello??",
        "Koi hai yahan pe",
        "Lady Datejust ka bhi dial nahi mila",
        "Dono cancel kar do, to better rahega",
        "Customer ko galat date batane se achha hai cancel ho jaye",
        "DJ1, this is Nikhil from Seller Ops.",
        "Haan ji boliye",
        "Do order ka dial nahi mil raha, cancel karna chahta hu, penalty lagegi kya",
        "??",
        "Reply kar dijiye please, customer roz message kar raha hai",
        # -- three days later, a real answer
        "Sorry for the gap, that's on us. Straight answers. Cancelling two orders you "
        "genuinely cannot source counts as seller cancellations, so yes it affects your "
        "fulfilment rate. It carries no cash penalty and no risk to your account at your "
        "volume. The alternative is two customers waiting weeks for dials that aren't "
        "coming, so cancelling is the right call.",
        "Theek hai samajh gaya",
        "Back with you on this, DJ1.",
        "Dono cancel kar do phir, aur kya karein",
        "Both cancelled, SX318911 and SX315454, and the stock released. I've logged the "
        "reason as supplier sourcing failure rather than a plain seller cancel, which "
        "doesn't undo the fulfilment hit but it does mean anyone reading your account later "
        "sees what actually happened. The customers were told today, with the apology coming "
        "from us and not from you.",
        "Thanks bhai. Ye Seiko mod wale supplier se bahut problem ho rahi hai, teen mahine "
        "se same dikkat hai",
        "Then the listings are the problem, not the supplier. If one supplier is unreliable "
        "and you list their pieces as in hand, every failure becomes your fulfilment number. "
        "List those as ETA with a real window and a supplier miss stops being a cancellation.",
        "Par ETA pe order kam aate hain, in hand wale me zyada aate hain",
        "Fewer orders you can honour beats more you can't. Your fulfilment is 83, which is "
        "already costing you more visibility than the in hand label buys you.",
        "Haan ye sahi hai, Seiko wale ETA pe daal dunga",
        "Start with that supplier's pieces only. Leave the rest.",
        "Kar dunga",
        "Good. Thanks DJ1.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        "4 - Good",
        "noted, appreciate you taking the time",
    ],
}
