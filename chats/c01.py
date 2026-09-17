"""Copies Achintya Singh (src 6071): 31 messages, 5 days, CSAT 5, agentic.

Shape being matched: a dense same-day opening (14 messages, clean alternating turns), then
nothing for eleven days, then a Seller Ops teammate posting alone across three days with
one very long explanation, then a final session where the seller comes back with a long
grievance and it lands well.
"""

CHAT = {
    "file": "c01", "id": 9001, "template": 31,
    "codes": "cbcbcbcbcbcbcbhhhhhhcbcbcbcbbcb",
    "wa": "917846907195", "name": "TopGun", "score": 5, "nps": 10,
    "sop": "urgent_delivery", "sx": "SX333644",
    "seller_note": "343 shipped, 99.45% fulfilment, 10 rejected, avg 15.7 days to ship",
    "order_note": "SX333644 Dior Solar Escape Pouch, Rs 3,297, guaranteed 3 Sep, Meerut",
    "texts": [
        # -- day 1, dense and alternating
        "Hlo",
        "Hey TopGun. What can I help you with?",
        "SX333644 ka status batao",
        "That's the Dior Solar Escape Pouch going to Meerut. Still showing unshipped and "
        "it's 7 days past its guaranteed date. What's holding it?",
        "Courier ne pickup miss kiya",
        "That happens, and it isn't on you if they didn't turn up. Can you rebook for "
        "today's slot? If it goes out today I can tell the customer it's moving and "
        "nobody escalates it.",
        "Aaj ka slot full hai, kal subah pickup hai. 11 baje tak nikal jayega",
        "Tomorrow morning works. I'll record the 18th against SX333644 and put a check on "
        "it, so if there's no AWB by midday I'll ping you here.",
        "Theek hai. Ek baat, ye Dior wale orders me packing ka standard kya hai exactly?",
        "Original dust bag and box, and the pouch inside its sleeve. Beauty items get "
        "opened at authentication, so anything loose in transit comes back as a damage "
        "claim.",
        "Bubble wrap chalega?",
        "Bubble wrap around the box is fine and I'd encourage it. What I'd avoid is "
        "wrapping the pouch itself, the print marks under pressure. Box it, then wrap the "
        "box, then the outer polybag.",
        "Samajh gaya, thanks",
        "Good. Rebook the pickup tonight and I'll watch SX333644 tomorrow.",
        # -- eleven days later, a teammate, alone
        "Hi TopGun, Nikhil from Seller Ops. Your store is up for the quarterly rating "
        "review.",
        "Here's what that means in practice, so nothing comes as a surprise. We look at "
        "three things over 90 days: days to ship, fulfilment rate, and exchange rate. "
        "Yours read 15.7, 99.45 and 4 percent. The fulfilment number is the best in your "
        "tier and the exchange rate is low, so neither is a concern. Days to ship is the "
        "one that matters, because from October the ranking weight on it goes up and "
        "anything above 10 days starts losing position on shared listings. You are not "
        "being penalised for anything today. I'm telling you now because you have six "
        "weeks to move the number before it counts, and at your volume that is very "
        "achievable.",
        "One more thing.",
        "The review itself isn't a meeting, it's automatic. You'll see a rating band on "
        "your dashboard on 1 October and again on 1 January. If the band drops we reach "
        "out before anything changes on your listings, so you'll never find out by losing "
        "traffic first.",
        "Chanakya handles your day to day and has the same numbers I do, so ask him "
        "anything between now and October.",
        "Last thing. If you want the days to ship number down fast, the lever is "
        "dispatching in hand stock the same day rather than batching it for the next "
        "pickup. That's most of your 15.7 and it costs you nothing to change. Chanakya "
        "can show you which orders are sitting.",
        # -- final session
        "Hi",
        "Morning TopGun. Your rating band went up today, you're in the second tier from "
        "the top. Days to ship is the only thing between you and the first.",
        "Bhai ek problem hai. Same day dispatch karna hai to courier pickup 2 baje tak hi "
        "aata hai. Order 3 baje aaye to agle din hi jayega, isme meri kya galti hai. Aur "
        "bulk pickup me per parcel rate kam padta hai, roz roz single parcel bhejne me "
        "cost double ho jati hai. Aap log number dekhte ho par ground reality yeh hai ki "
        "chhote seller ke liye daily pickup afford karna mushkil hai. Iska koi solution "
        "hai ya bas number hi dekhoge?",
        "Fair point and a real cost, not an excuse. There's a way to get both, and it "
        "isn't daily single pickups.",
        "Batao phir",
        "Two pickups a week, but on fixed days rather than whenever you're full.",
        "Isse number kaise girega",
        "Because a fixed slot caps the wait at three days, not nine.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        "5 - Excellent",
        "noted, appreciate you taking the time",
    ],
}
