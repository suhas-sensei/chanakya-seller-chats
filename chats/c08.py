"""Copies ANUJMAGO (src 6838): 84 messages, 10 days, CSAT 4, agentic.

Shape being matched: the thread a human ends up carrying. 50 counterparty messages against
8 agent replies and 26 from staff, with long unanswered bursts, two images, a 663-character
staff message on day seven and a 35-message final session that includes replies of 421,
502 and 552 characters. It stays agentic because the terminal rating carries no human
attribution, which is the source's own rule.

Built on DS.WT's real record: 8,520 shipped, 86.72% fulfilment, and 3,221 rejected orders,
the largest rejection count in the pool.
"""

CHAT = {
    "file": "c08", "id": 9008, "template": 84,
    "codes": "ccbcbcbcccchcccccchchchccbcbcbchcchcccccccccchcchccccchhhhhcchhhhchchccchhhhchchhbcb",
    "wa": "918860608766", "name": "DS.WT", "score": 4, "nps": 7,
    "sop": "order_modify",
    "sx": "SX324592 / SX320011 / SX322955 / SX322647 / SX323083",
    "seller_note": "8520 shipped, 86.72% fulfilment, 3221 rejected, avg 9.1 days",
    "order_note": "SX324592 Coach Nolita 19 auto-cancelled unaccepted; SX320011 and "
                  "SX322955 Louis Vuitton Icon, Rs 23,057 each, supplier withdrew",
    "texts": [
        "Hi",
        "Screenshot dekho",
        "I can see it. What am I looking at?",
        "Mera order reject ho raha hai",
        "That screenshot is the listing being pulled, not an order being rejected. Those "
        "are different things and the difference matters here. Which SX id are you talking "
        "about? Give me the id and I'll read the actual record.",
        "SX324592, COACH bag wala hai",
        "Read it. SX324592, the Coach Nolita 19 at 20,496 rupees to Vizianagaram. It wasn't "
        "rejected by us. It was auto-cancelled after you didn't accept it inside the "
        "window, which on a 20,000 rupee piece is 24 hours. So the order came in, sat "
        "unaccepted for a day and a half, and the system released it back. That's the third "
        "time this month on your account and it's the most expensive habit you have, "
        "because you lose the order and take the fulfilment hit for something that needed "
        "one tap.",
        "Mujhe notification nahi aaya",
        "Phir kya karun",
        "Din me 40-50 order aate hain, sab manually accept karna mushkil hota hai bhai, "
        "staff nahi hai",
        "Aur notification bhi late aata hai app me",
        "DS.WT, Nikhil from Seller Ops. I'm going to look at the notification issue "
        "properly rather than guess at it.",
        "Haan sir dekh lijiye, bahut nuksan ho raha",
        # -- four days later, into silence
        "Hi",
        "Aaj bhi do order cancel ho gaye hain",
        "Dono ka screenshot",
        "Dekh lijiye",
        "?",
        # -- next day
        "Looking at it today. Apologies for the wait over the weekend.",
        "Ok ji",
        "Can you tell me which phone you use for the seller app, and whether "
        "notifications are on?",
        "Android phone",
        "And are notifications enabled for the app in your phone settings, not just inside "
        "it?",
        "Haan sab on hai",
        # -- next day
        "Pata chala?",
        "Nikhil's still on the notification side. Separately, SX322647 and SX323083 both "
        "need accepting today, they're the two Polo Ralph Lauren shirts.",
        "Accept kiya",
        "Thanks.",
        # -- four days on
        "SX320011 aur SX322955 ka kya hua",
        "Both Louis Vuitton Icon, 23,057 each. Both accepted, both unshipped, both nine "
        "days over. What's holding them?",
        "Stock",
        "DS.WT, update on the notifications. We found the cause and it isn't your phone.",
        "??",
        "Sir wo LV wale do order me stock ka issue hai, supplier ne mana kar diya. Aur "
        "notification ka bataiye kya hua, roz order cancel ho rahe hain isse mera",
        "Both answers are coming, give me till this evening.",
        "Ji ji",
        "Wait kar raha hu",
        # -- and then nobody answers, for two days
        "Sir?",
        "Aaj teen order cancel ho gaye, teeno accept karne se pehle hi",
        "Ye mahine me 40 order cancel ho chuke hain sirf accept na hone se. Mera fulfilment "
        "86 se neeche jaa raha hai",
        "?",
        "Koi reply dijiye sir",
        "??",
        "Do din se koi reply nahi hai",
        "Sir please dekh lijiye, aise business band ho jayega mera",
        "DS.WT, sorry for the silence, that was two days too long and it's on me. Here's "
        "the whole answer, including the part that doesn't reflect well on us. The "
        "notifications weren't reaching you because your account sits on an older push "
        "channel we deprecated in July. Around two hundred stores were never migrated off "
        "it, so you've had order alerts arriving hours late or not at all since then. "
        "That's our bug, not your phone and not your staff. You've lost roughly forty "
        "orders this month to a window you couldn't see. What happens now: your account "
        "moves to the current channel tonight, and the auto-cancels from the last sixty "
        "days are being reviewed so they stop counting against your fulfilment.",
        "Ok",
        "Notification aane laga hai ab sir",
        "Good. The fulfilment correction takes a few more days because each reversal needs "
        "signing off. I'll confirm when it lands rather than leave you checking.",
        # -- the long final session
        "Hi",
        "Sir fulfilment ka kya",
        "Dashboard pe abhi bhi 86 dikha raha hai, correction hua kya",
        "?",
        "Aur ek LV order ka customer ne cancel kar diya, wo bhi dekho",
        "I'm here, and the correction landed this morning, your dashboard just hadn't "
        "refreshed. You're at 91.4 percent, up from 86.7. Thirty one auto-cancels were "
        "reversed out of the calculation. The other nine weren't eligible because they "
        "predate the channel change.",
        "On the Louis Vuitton orders, both of them. SX320011 and SX322955 were the same "
        "piece from the same supplier who backed out, so one customer cancelling was always "
        "going to happen and the second one will too. I'd rather you cancelled the "
        "remaining one today than let it run. A customer cancellation doesn't touch your "
        "rate; a lapse does. That's the only reason I'm pushing you to act on it rather "
        "than wait it out.",
        "Now the bigger thing, because the notification bug was hiding it. Your rejection "
        "count is 3,221 against 8,520 shipped. Even with the auto-cancels stripped out, "
        "that's a very large number and it isn't a notification problem. It's a listing "
        "problem, and it's the one thing left that's actually yours.",
        "You have around 900 listings live. From the sample we pulled, roughly a third of "
        "them are stock you've already sold elsewhere. Every order that lands on one of "
        "those is a rejection you can't avoid, because the item isn't there.",
        "That part is yours to fix, and it's the last thing.",
        "Sir 900 listing manually check karna bahut mushkil hai",
        "Koi tool hai iske liye",
        "There's a bulk export. Download your live listings as a sheet, mark what's gone, "
        "upload it back. It's one afternoon, not nine hundred clicks.",
        "Chanakya can send you the export link and walk you through the format. Do it once "
        "properly and then make it a monthly habit, because a catalogue drifts out of date "
        "whether you look at it or not, and yours has had a year to drift.",
        "One last thing and then I'll get out of your way. I've been blunt about the 3,221 "
        "because it's the number that decides your flow, but it's worth saying what sits "
        "underneath it. You've shipped 8,520 orders. Your average dispatch is nine days on "
        "a catalogue of nine hundred lines with no staff. That's a real operation, and the "
        "reason this month hurt so much is that you're running it at a scale where small "
        "leaks cost real money. Fix the catalogue and you're one of the strongest stores we "
        "have.",
        "Chanakya takes it from here. Good luck.",
        "Thank you sir",
        "Anytime, DS.WT.",
        "Chanakya bhai, export link bhej do. Aur ye batao LV wala cancel kar dena hai kya "
        "aaj hi? Aur fulfilment 91 pe aa gaya hai, dekh liya",
        "Export link is on its way, and yes, cancel the remaining Louis Vuitton today. I'll "
        "do it for you now if you'd rather, just say the word. On the export, three things "
        "to watch when you open the sheet. Mark only what you're certain is gone, because a "
        "wrongly removed listing costs you an order you could have filled. Leave the price "
        "column alone, it overwrites live prices if you touch it. And upload in one go "
        "rather than in batches, because a partial upload leaves your catalogue in a "
        "half-updated state that's worse than either end of it.",
        "Kar do",
        "LV wala aap hi cancel kar dijiye please",
        "Export kal kar lunga, aaj time nahi",
        "Nikhil again, briefly. I've cancelled SX322955 myself so it's off your list "
        "tonight, logged as supplier withdrawal rather than a seller cancel.",
        "And your fulfilment reads 91.4 now, so you saw it right. One more reversal batch "
        "is pending, which should put you just over 92. That's the last of the correction, "
        "nothing else is coming after it, so don't wait on a further jump.",
        "If the catalogue clean up drops you below 92 for a few weeks, ignore it. Removing "
        "dead listings looks like a decline before it looks like a recovery.",
        "Right, now I'm actually done. Over to Chanakya.",
        "Thanks sir",
        "Good luck with the export tomorrow, DS.WT.",
        "Sir COD ka bhi issue",
        "COD refusals I can look at, but not this week, and I'd rather finish one thing "
        "than start two. Get the catalogue done, let the fulfilment correction settle, and "
        "message Chanakya in a fortnight. I'll pull your COD numbers then and we'll do it "
        "properly rather than badly.",
        "Two things at a time is how stores end up doing neither. You've had a bad month "
        "caused mostly by our bug. Fix the catalogue, then we'll talk about COD.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        "4 - Good",
        "noted, appreciate you taking the time",
    ],
}
