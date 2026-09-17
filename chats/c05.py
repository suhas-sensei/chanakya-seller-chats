"""Copies Dhananjoy Das (src 5008): 50 messages, 8 days, CSAT 5, human cohort.

Shape being matched: opens on an approved template rather than a seller message, carries a
CSAT prompt at index 11 and another at the end, goes seven messages unanswered across four
days in the middle, then a teammate takes the thread over for the whole final session and
the rating lands on their work, which is why the source counts this one as human.
"""

CHAT = {
    "file": "c05", "id": 9005, "template": 50, "cohort": "human",
    "codes": "bcbcbcbcbcbbcbcbcbcbcbcccccccbchchhhhhchhchhchhbcb",
    "wa": "917774922888", "name": "Sneak Drip", "score": 5, "nps": 9,
    "sop": "payout_pending", "sx": "SX327430 / SX333867",
    "seller_note": "316 shipped, 79.95% fulfilment, 82 rejected, avg 4.1 days",
    "order_note": "SX327430 Polo Ralph Lauren Tipped Polo (XL) return to Jalgaon; six "
                  "delivered orders unsettled, oldest SX333867",
    "texts": [
        "Hi Sneak Drip, this is Chanakya from SourceX. About order SX327430, Polo Ralph "
        "Lauren Men's Custom Slim Fit Tipped Polo in XL. A return has been initiated, "
        "reason size issue. Which address should the return go to? Reply here and I'll set "
        "up the reverse pickup.",
        "Address wahi jalgaon ka hai. Par pehle ye batao mera paisa kab aayega, 2 hafte ho "
        "gaye hain bhai",
        "Jalgaon address noted, I'll schedule the pickup. On the money, let me pull your "
        "settlement position before I say anything.",
        "Haan dekho, 6 order deliver ho chuke hain aur ek ka bhi paisa nahi aaya abhi tak, "
        "problem ho rahi hai",
        "Six delivered and unsettled, oldest is SX333867. They're held on a verification "
        "flag at our end, not on anything you did. Bank details on file didn't match the "
        "name when finance ran it, and that one mismatch holds everything behind it.",
        # -- four days later
        "Account to wahi hai jo shuru se hai. Bank me Haresh N Patil likha hai, aapke paas "
        "kya likha hai bhai",
        "We have it as Haresh Patil, without the N. That's the whole hold. I've sent the "
        "corrected name to finance with your statement reference. Being straight with you "
        "about what happens next: the correction is quick, the settlement run is weekly, "
        "and yours is the Monday one. So realistically you're looking at Monday rather than "
        "today, and I'd rather tell you that than say soon.",
        "Monday tak wait ka",
        "Yes. I'll message you on Monday whether it lands or it doesn't.",
        "Order bhejte rahein tab tak ya rok du?",
        "Keep shipping. The hold is on the rail, not you.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        "5 - Excellent",
        "noted, appreciate you taking the time",
        # -- next day
        "Bhai return pickup ke liye label mujhe banana hai kya, courier wale label pooch "
        "rahe the",
        "No, on a return the customer prints it. If a courier asks you for a label, that's "
        "the wrong courier at your door.",
        # -- two days on
        "Ok ji",
        "Money's in. The name matched, the verification hold came off this morning and "
        "finance put all six into today's run rather than making you wait for Monday. "
        "That's a week earlier than I told you, which is the direction I'd rather be wrong "
        "in. Check your account and tell me if any of the six is missing, because a partial "
        "release is the one thing I'd want to catch today rather than next week.",
        "Check kiya, sab aa gaya bhai",
        "Good. That's the full backlog cleared, not a partial. You were owed that money for "
        "two weeks over a missing initial, which shouldn't have taken a chase to find. I've "
        "noted the reporting gap separately.",
        "Ab COD ka bhi dekh lo bhai, please",
        "Pulling it now. 38 COD orders in 30 days, 14 refused at the door, almost all above "
        "8,000 rupees. That's your whole fulfilment gap, and it isn't your shipping.",
        # -- and then nobody answers, for four days
        "To phir iska solution kya hai bhai",
        "COD band karwa sakte ho mere store ke liye?",
        "Hello",
        "Koi reply nahi aaya abhi tak",
        "Bhai dekho, paise ka issue aapne solve kar diya wo achha tha. Par COD ka pooch "
        "raha hu 5 din se, koi jawab nahi. 14 order refuse hue hain, mera packing aur "
        "shipping ka paisa gaya, aur fulfilment bhi kharab hua. Kuch to rasta hoga na.",
        "?????",
        # -- the final session
        "Hello",
        "I'm here, and the five day gap isn't acceptable, so no excuse for it. The COD "
        "question went to the team on the 24th and then I stopped chasing it, which is the "
        "part that's on me. Here's where it actually is: they've agreed to trial a COD cap "
        "by order value for your store, and Nikhil from Seller Ops is picking it up with "
        "you directly because the cap is his call and not mine. He's on this thread now.",
        "Theek hai, sun raha hu",
        "Sneak Drip, Nikhil here. I've read the whole thread, so you don't need to repeat "
        "it.",
        "Nikhil ji, mujhe bas itna chahiye ki 8000 se upar ke order COD me na aaye. Baaki "
        "sab theek hai. 14 order refuse hone se mera 20 hazaar ka nuksan hua hai is mahine "
        "me. Aur fulfilment 80 pe aa gaya hai.",
        "That's a reasonable ask and the data backs it.",
        "Here's what I can do right now.",
        "A COD cap of 6,000 rupees on your store, starting today, trial for one month. "
        "Anything above that goes prepaid only, no exceptions.",
        "On the 20,000 you're out, I can't return handling on refused COD because there's "
        "no mechanism for it, and I'd rather tell you that than promise something that "
        "won't arrive. What the cap does is stop it happening again from today, which is "
        "the part I can actually control.",
        "Your fulfilment will take about a month to reflect it because it's a rolling 90 "
        "day average. Nothing you can do to speed that up, it just has to roll.",
        "Cap chalega, wahi chahiye tha. Wapas nahi mila to koi baat nahi, aage se na ho "
        "wahi kaafi hai. Ek baat poochni thi, cap ke baad order kam aayenge kya? Kyunki "
        "mere jyada order COD wale hi aate hain, prepaid kam aate hain.",
        "Honestly, yes, your order count will drop. Best guess is 15 percent. The orders "
        "you lose are mostly the ones that were coming back at your cost anyway, so you "
        "should end up better off on money even with fewer orders.",
        "I'd rather you heard that from me now than found it on your dashboard next week "
        "and thought we'd hidden it. If the drop is worse than that, message Chanakya and "
        "we'll revisit the cap before the month is up rather than making you wait it out.",
        "Theek hai sir, ek month try karte hain. Thank you dono ko",
        "Sounds fair to me.",
        "Cap is live from now. Chanakya has the details.",
        "Ok sir",
        "One last thing. The settlement reporting gap Chanakya flagged is being fixed too, "
        "so a held settlement reaches you as a message instead of you chasing us.",
        "That's everything from my side. Take care.",
        "quick one before you go, how was the help you got from us today? one tap, and it "
        "genuinely helps us improve your seller experience massively",
        "5 - Excellent",
        "noted, appreciate you taking the time",
    ],
}
