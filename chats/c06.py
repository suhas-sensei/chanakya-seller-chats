"""Copies Muslim altaf Khan (src 333): 55 messages, 8 days, CSAT 5, agentic.

Shape being matched: the most verbose thread in the set. The real chat's agent replies run
265, 352, 469, 640, 589, 437, 450, 586 and 643 characters, it opens with three agent
messages back to back before the counterparty gets a word in, the counterparty sends an
image mid-thread, there is a three-message run into silence, and it ends on the rating
itself with no sign-off after it.
"""

CHAT = {
    "file": "c06", "id": 9006, "template": 55,
    "codes": "bcbbbcbcbcbcbcbcbccbcbcbcbccccbcbcbcbcbcbcbcbcbcbcbcbbc",
    "wa": "919924028887", "name": "Delicc Enterprises", "score": 5, "nps": 9,
    "sop": "scattered_reply",
    "sx": "SX322168 / SX328656 / SX328627 / SX328626 / SX329759",
    "seller_note": "13804 shipped, 99.14% fulfilment, 146 rejected, avg 30.9 days to ship",
    "order_note": "Five open: Myugen Iceman tee (guaranteed 23 Aug), Off Supply Core Black, "
                  "two Blacklist Bear waffle tees to Indore, Gilded Crane denim "
                  "(guaranteed 4 Sep)",
    "texts": [
        "Hi Delicc, Chanakya here. You've got five orders open with me and three are past "
        "their guaranteed dates, so rather than message you five times I'm putting them in "
        "one place. SX322168, SX328656, SX328627, SX328626 and SX329759. Tell me what you "
        "know about each and I'll work off that.",
        "Bhai teeno t-shirt wale ek hi lot me hain, wo lot supplier se kal aayega. Denim "
        "wala ready hai. Myugen wala stock me nahi hai, uska kya karein batao. Baaki do kal "
        "nikal jayenge pakka.",
        "Good, that answers most of it already.",
        "Taking them in order. SX328627 and SX328626, the Blacklist Bear waffle tees to "
        "Indore, and SX328656, the Off Supply Core Black, all come out of the lot landing "
        "tomorrow. I'll record the 18th against all three. If the lot is late, tell me "
        "tomorrow morning rather than tomorrow night. One message is enough, I'll apply it "
        "to all three.",
        "SX329759, the Gilded Crane denim, you say is ready. That one was guaranteed for "
        "the 4th and it's the 17th, so it's thirteen days over and the customer has asked "
        "twice. If it's genuinely ready it should go out today rather than tomorrow with "
        "the others. A ready piece sitting for one more pickup cycle on an order that's "
        "already two weeks late is the kind of thing that turns into a cancellation, and "
        "you'd be losing it after doing all the work.",
        "Haan denim wala aaj hi bhej dete hain, 2 baje ka pickup pakad lenge",
        "That's the right call. Now the one you asked me about, SX322168, the Myugen Iceman "
        "tee. It was guaranteed on 23 August and the customer required it by 10 September. "
        "Both dates are gone and you're telling me the stock isn't there. I'm not going to "
        "leave that sitting as a maybe for another month. Two options, and I'd like you to "
        "pick one today. Either you can source it within a week and I tell the customer "
        "that honestly, or you can't and I close it as a cancel today so they can buy "
        "elsewhere. If you pick the cancel it counts against your fulfilment, and I'd still "
        "tell you to pick it, because twenty five days of silence costs you more than one "
        "cancellation does.",
        "Cancel kar do bhai, wo piece dobara nahi aayega supplier ke paas",
        "Done, SX322168 cancelled and the stock released. I've logged it as supplier "
        "discontinued rather than a plain seller cancel, so anyone reading your account "
        "later sees what actually happened. The customer was told today, with the apology "
        "coming from us. You made the right call and you made it in one message, which is "
        "the whole reason this took four minutes instead of another month.",
        "Theek hai",
        "Four orders left, three on the 18th and one going out today. I'll come back to you "
        "tomorrow evening with what actually moved.",
        "Ek baat, ye guaranteed date kaun decide karta hai? Humse to koi poochta nahi hai "
        "isme",
        "It's set from the listing type, not by hand. In hand gets a short window, ETA a "
        "long one. You list bulk apparel as in hand, so you get three days to ship what "
        "takes you thirty.",
        "Achha, samajh gaya",
        "That's the whole problem, really.",
        # -- next morning
        "Denim kal nikal gaya. Lot bhi aaj subah aa gaya hai",
        "Confirmed, SX329759 is scanned and in transit on Delhivery. On the lot, good, that "
        "means the three tees can go today rather than tomorrow. Before you pack them, one "
        "thing worth doing while the lot is still open. Photograph the stack as it came in, "
        "with the packing slip visible. Your fulfilment is 99 percent, the best number I "
        "have on anyone at your volume, but when a lot arrives short you currently find out "
        "at packing time and then an order gets cancelled. A photo at intake means you know "
        "within the hour, and you can tell me before a customer is waiting.",
        "Lot ki photo, 40 piece aaye hain",
        "Slip bhi dikh rahi hai isme",
        "That's exactly it, and the slip says 40 against a lot you expected 42 in. So "
        "you're two short before you've packed anything. Which two are missing, and does "
        "either belong to SX328627 or SX328626? If they do, tell me now and I'll go to "
        "those two customers today rather than on the 19th when you find out at packing. "
        "This is the hour I was talking about.",
        "Dono waffle tee hi missing hain, Indore ke dono",
        "Then both Indore orders are the problem and neither can ship tomorrow. I'd rather "
        "act on that now. I'll tell both customers today that the piece didn't arrive in "
        "your lot and offer them the choice, wait for the next lot or cancel. That way the "
        "delay is a conversation instead of a broken promise, and your fulfilment only "
        "takes a hit if they actually cancel.",
        "Next lot 5 din me aayega, bata do",
        "Five days, I'll put that to them. SX328656, the Off Supply Core Black to "
        "Bangalore, is unaffected so that one still goes today. And to be clear about what "
        "just happened: you took a photo, we found a shortfall an hour later, and two "
        "customers are getting the truth instead of a missed date. That is worth doing on "
        "every single lot.",
        "Har lot ki photo bhejunga",
        "Send it here whenever a lot lands. I'll read it the same morning and flag anything "
        "short.",
        # -- into silence
        "Bhai sun lo",
        "Bangalore wala nikal gaya",
        "??",
        "??",
        "Sorry, that sat overnight. SX328656 is scanned and moving, I can see it. Both "
        "Indore customers came back yesterday, one is waiting for the next lot and one "
        "cancelled. So of the five you had open on Wednesday: two shipped, one cancelled by "
        "you, one cancelled by the customer, one waiting on a lot. Nothing is sitting in "
        "silence.",
        "Ek customer ne cancel kiya, wo mere count me jayega kya?",
        "No. A customer cancellation doesn't touch your fulfilment rate, only the ones you "
        "reject or let lapse do. So of the two cancels this week, the Myugen one counts "
        "against you and the Indore one doesn't. And the Myugen one only counts because the "
        "stock was gone, which is a listing problem we've already talked about rather than "
        "a service problem. Your 99 percent is intact, and at 13,000 shipped that number is "
        "the reason I give you the benefit of the doubt on a delay.",
        "Okk",
        "One order left open, waiting on your lot. I'll check back when that lot is due "
        "rather than before.",
        # -- lot day
        "Lot aa gaya",
        "Got a photo?",
        "Haan, upar bhej diya",
        "Counted it, 42 against 42, and both waffle tees are in. So the waiting Indore order "
        "can ship today and I've told the customer. That's the second lot in a row where the "
        "photo saved us a day, and on this one it saved the order outright, because that "
        "customer was one more miss from cancelling.",
        "Sab nikal gaya",
        "All clear at my end too. Nothing open.",
        "Aur koi order pending hai kya?",
        "Nothing pending, which is the first time your account has been fully clear since I "
        "picked it up. Worth saying what changed, because it wasn't effort. You answered "
        "five orders in one message instead of five, you photographed two lots at intake, "
        "and you cancelled one order you couldn't fill instead of letting it run. Your "
        "shipping speed didn't improve at all this week, your average is still 31 days. But "
        "nobody chased you, nothing lapsed, and two customers got a real choice instead of "
        "a missed date. That's the difference between 99 percent fulfilment and a store "
        "people complain about.",
        # -- five days on
        "Bhai ek naya lot aa raha hai",
        "Send the photo when it lands, same as before. And since a lot is coming, now is "
        "the right time to do the listing change we keep circling. Your bulk apparel is "
        "listed as in hand, which gives every order a three day window against your real "
        "thirty day cycle. That mismatch is why you were late on almost everything before "
        "this month and why you were getting chased daily. Move the bulk lines to ETA with "
        "a window that matches when your lots actually land. You'll see fewer orders on "
        "those listings and it will feel like a loss for about a week. What you get back is "
        "every order starting inside a promise you can keep. At 13,000 shipped you have "
        "nothing to prove on service, you're just being measured badly.",
        # -- two days on
        "60 listing change ki",
        "I can see them. Eleven orders have come in on those lines since the change and "
        "every one is inside its window. Before this week you'd have been late on most of "
        "them. Nothing about your shipping changed, only the promise attached to it.",
        "Achha!",
        "It's the least satisfying fix I give anyone, because it feels like paperwork "
        "rather than improvement. But you've gone from being chased every day to nobody "
        "messaging you at all, and you didn't ship a single parcel faster to get there.",
        "Pehle roz message aata tha, ab ek bhi nahi aaya is hafte",
        "That's the whole point. The chase was never about your speed, it was about the gap "
        "between your speed and what your listings promised. You closed the gap. One thing "
        "to watch: if a lot slips badly and the ETA window stops being true, change the "
        "window rather than hoping. The moment the promise goes stale you're back to being "
        "late.",
        "Haan wo dhyan me rakhunga bhai",
        "Good. Send the lot photos, keep the windows honest, and answer in one message like "
        "you did on Wednesday. That's the entire relationship from here, and it should mean "
        "you hear from me a good deal less.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        "5 - Excellent",
    ],
}
