"""DS.WT. Big operator, no staff, ends half his messages with bhai. Direct, not polite.

Seller register: "Any update bhai" / "Sorted bhai aagaya" / "Bhai did you book a pickup?"
/ "yes please". Short, uses bhai as a suffix rather than an opener.

Episodes: an RTO with a courier workaround, a bulk list of six with a 23k exception chased
into the night, orders auto cancelling because app alerts were not arriving, and the
listing clean up that follows from it.
"""

from ._voice import intro, new_order, reminder

CHAT = {
    "file": "c03", "id": 9003,
    "wa": "918860608766", "name": "DS.WT", "score": 4, "nps": 7,
    "sop": "order_modify",
    "sx": "SX324592 / SX320011 / SX322955 / SX322647 / SX323083 / SX320118",
    "seller_note": "8520 shipped, 86.72% fulfilment, 3221 rejected, avg 9.1 days",
    "order_note": "Six due the same day including a Rs 23,057 Louis Vuitton Icon; orders "
                  "auto cancelling unaccepted",
    "flow": {
        "input": "orders auto cancelling unaccepted, six more due the same day",
        "action": "traced the missed alerts to a deprecated push channel on our side, "
                  "clubbed the six, chased the 23k piece to a same-night answer",
        "resolution": "auto cancels reversed out of his rate, all six shipped",
    },
    "turns": [
        ("2026-08-20 11:05", "cx", intro("DS.WT")),
        ("2026-08-20 11:06", "cx",
         "Kindly note SX324592 was auto cancelled this morning as it was not accepted "
         "within 24 hours. Could you tell me if there was an issue at your end?"),
        ("2026-08-20 11:40", "sl", "Notification hi nahi aaya bhai"),
        ("2026-08-20 11:41", "cx", "ye pehli baar hua ya pehle bhi?"),
        ("2026-08-20 11:44", "sl", "3rd time this month"),
        ("2026-08-20 11:45", "cx",
         "okay, ye main apni side pe check karwata hu. aap tab tak panel manually dekh lena "
         "din me do baar"),
        ("2026-08-20 11:47", "sl", "yes please"),
        ("2026-08-21 16:20", "cx", "SX320118 - what is the update on this"),
        ("2026-08-21 17:35", "sl", "Kal nikal jayega bhai"),
        ("2026-08-21 17:36", "cx", "thik hai"),
        ("2026-08-22 10:10", "cx", "SX320118 aaj ja raha hai na, reminder"),
        ("2026-08-22 10:52", "sl", "Haan"),
        ("2026-08-22 19:40", "sl", "Sorted bhai aagaya tracking"),
        ("2026-08-22 19:44", "cx", "dekh liya"),
        ("2026-08-25 09:05", "cx",
         "bhai aaj aapke 6 orders due hain. 6 alag message bhejne se achha ek me daal raha "
         "hu\n\nSX322647 polo RL white graphic\nSX323083 polo RL white graphic\n"
         "SX320118 polo RL navy\nSX312849 prada paradoxe\nSX324592 coach nolita 19\n"
         "SX320011 LV icon\n\ninme se koi nahi ja raha?"),
        ("2026-08-25 09:34", "sl", "5 ja rahe hain. LV wala supplier se nahi aaya"),
        ("2026-08-25 09:35", "cx",
         "wahi ek tension ka hai. SX320011 23,057 ka hai aur us buyer ne is saal 6 baar "
         "order kiya hai"),
        ("2026-08-25 09:39", "sl", "Pata hai bhai par piece hi nahi hai"),
        ("2026-08-25 09:40", "cx", "supplier kab confirm karega?"),
        ("2026-08-25 09:43", "sl", "Shaam tak"),
        ("2026-08-25 09:45", "cx",
         "theek hai. 5 abhi nikal do aur jaise hi wo confirm kare mujhe bata dena, raat 10 "
         "baje bhi chalega. itne bade piece pe main buyer ko aaj hi real date dena chahta "
         "hu, kal nahi"),
        ("2026-08-25 09:48", "sl", "Ok bhai"),
        ("2026-08-25 21:10", "sl", "LV mil gaya, kal subah nikal jayega"),
        ("2026-08-25 21:12", "cx", "yahi sunna tha. itni raat message karne ke liye thanks"),
        ("2026-08-25 21:13", "cx", "buyer ko main subah dispatch bata deta hu"),
        ("2026-08-26 10:30", "sl", "Nikal gaya"),
        ("2026-08-26 10:33", "cx", "sab 6 clear. achha hafta gaya aapka"),
        ("2026-08-28 12:05", "sl", "Bhai 2 aur order cancel ho gaye aaj"),
        ("2026-08-28 12:06", "sl", "Accept karne se pehle hi"),
        ("2026-08-28 12:20", "cx", "SX id bhej do dono ke"),
        ("2026-08-28 12:24", "sl", "SX322955 aur SX311180"),
        ("2026-08-28 12:55", "cx",
         "mil gaya. ye aapka phone nahi hai. aapka account ek purane push channel pe hai "
         "jo humne july me band kar diya tha, isliye alerts late aa rahe the ya aa hi nahi "
         "rahe the"),
        ("2026-08-28 12:56", "cx",
         "ye humari galti hai, aapki nahi. aaj raat aapka account current channel pe shift "
         "ho jayega"),
        ("2026-08-28 13:02", "sl", "Itne order chale gaye is chakkar me bhai"),
        ("2026-08-28 13:04", "cx",
         "pata hai. pichhle 60 din ke auto cancels review me daal diye hain taaki wo aapke "
         "fulfilment rate se hat jayein. jo orders gaye wo wapas nahi aayenge, us pe main "
         "jhooth nahi bolunga"),
        ("2026-08-28 13:09", "sl", "Theek hai bhai"),
        ("2026-08-30 10:20", "sl", "Notification aane lag gaya"),
        ("2026-08-30 10:22", "cx", "good. correction bhi is hafte lag jayega"),
        ("2026-09-02 11:15", "cx",
         "31 auto cancels reverse ho gaye hain. aapka fulfilment 86.7 se 91.4 pe aa gaya"),
        ("2026-09-02 11:40", "sl", "Dikh raha hai bhai, thanks"),
        ("2026-09-02 11:44", "cx",
         "ab jo bacha hai wo aapka hai. 3,221 rejections hain 8,520 orders pe. auto cancel "
         "hata bhi dein to ye bahut zyada hai"),
        ("2026-09-02 11:47", "sl", "Wo stock ka issue hai"),
        ("2026-09-02 11:49", "cx",
         "haan, aapki 900 listings me se ek tihai wo stock hai jo aap already bech chuke ho "
         "kahin aur. har order jo us pe girta hai wo guaranteed rejection hai"),
        ("2026-09-02 11:53", "sl", "900 manually check karna mushkil hai bhai"),
        ("2026-09-02 11:55", "cx",
         "bulk export hai. sheet download karo, jo gaya hua hai mark karo, wapas upload. ek "
         "dopahar ka kaam hai, 900 click nahi"),
        ("2026-09-02 11:58", "sl", "Link bhej do"),
        ("2026-09-02 12:00", "cx", "bhej diya. ek baat dhyan rakhna"),
        ("2026-09-02 12:01", "cx",
         "price column ko haath mat lagana, wo live prices overwrite kar deta hai. aur "
         "upload ek hi baar me karna, aadha upload sabse bura hota hai"),
        ("2026-09-02 12:05", "sl", "Noted"),
        ("2026-09-05 17:30", "sl", "310 listing hata di bhai"),
        ("2026-09-05 17:40", "cx",
         "itna bada clean up 10 din tak views pe dikhega. ghabrana mat, wo listings order "
         "de rahi thi jo aap pura kar hi nahi sakte the"),
        ("2026-09-05 17:44", "sl", "Views already gir gaye"),
        ("2026-09-05 17:46", "cx", "10 din. usse zyada laga to mujhe bolna, main pricing dekhunga"),
        ("2026-09-09 10:05", "cx", "SX327252 - can you check status of this order?"),
        ("2026-09-09 11:20", "sl", "Any update bhai mujhe hi nahi mila ye order"),
        ("2026-09-09 11:24", "cx", "panel me accepted dikha raha hai 6 tarikh ko"),
        ("2026-09-09 11:30", "sl", "Achha wo mil gaya. Kal nikal dunga"),
        ("2026-09-09 11:31", "cx", "confirm asap kal"),
        ("2026-09-10 18:10", "sl", "Bhai did you book a pickup? Courier aaya nahi"),
        ("2026-09-10 18:12", "cx",
         "pickup aap book karte ho apni side se, hum nahi. reverse pickup alag hota hai, wo "
         "hum karte hain"),
        ("2026-09-10 18:16", "sl", "Achha samjha"),
        ("2026-09-10 19:40", "sl", "Book kar diya, kal ja raha"),
        ("2026-09-15 11:00", "cx",
         "update - rejections 3,221 se 640 pe hain 30 din me, aur order count clean up se "
         "pehle wale level se upar hai"),
        ("2026-09-15 11:22", "sl", "Badhiya bhai"),
        ("2026-09-15 11:24", "cx", "sunday wala clean up habit bana lo, bas itna"),
        ("2026-09-15 11:26", "sl", "Haan wo ab fix hai"),
        ("2026-09-16 15:40", "tpl",
         new_order("Louis Vuitton Icon Personalisable & refillable", "OS", "23,057",
                   "SX322955")),
        ("2026-09-16 16:02", "sl", "48h me nikal jayega"),
        ("2026-09-16 16:03", "cx", "noted bhai"),
    ],
}
