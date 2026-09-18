"""Mindyourkicks. "Hnji", trailing dots, easy going. Fastest dispatch on the roster.

Seller register: "Hnji.. koi urgent ho to bta dena" / "Han wo to kr hi rha" / "Acha.. koi
na." / "Aap btao". Rarely uses an address term at all.

Episodes: sourcing back and forth on perfume, a payout blocked because nothing was marked
complete, the three day follow up to confirm the money landed, then the open order. A
tracking feed lag that was our problem, not his.
"""

from ._voice import intro, new_order, open_confirm, reminder

CHAT = {
    "file": "c04", "id": 9004,
    "wa": "919821187865", "name": "Mindyourkicks", "score": 5, "nps": 10,
    "sop": "payout_pending", "sx": "SX337953 / SX337952 / SX339047",
    "seller_note": "1004 shipped, 94.57% fulfilment, 63 rejected, avg 2.2 days",
    "order_note": "Two delivered orders unmarked, blocking payout. SX339047 Rasasi Hawas "
                  "Ice open, customer needed it by 17 Sep",
    "flow": {
        "input": "payout not moving, seller does not know why",
        "action": "closed the unmarked orders from the backend, confirmed in three days, "
                  "then moved to the open order and the courier feed lag",
        "resolution": "payout received, order shipped same evening, feed lag fixed our side",
    },
    "turns": [
        ("2026-08-26 12:08", "cx", intro("Mindyourkicks")),
        ("2026-08-26 12:09", "cx",
         open_confirm("SX335948", "Ajmal Aristocrat EDP for Men")),
        ("2026-08-26 12:22", "sl", "Wo kal nikal gaya tha.. tracking daal di thi"),
        ("2026-08-26 12:24", "cx", "mil gaya, thanks"),
        ("2026-08-26 12:30", "cx", "Ahmed Al Maghribi Kaaf EDP - do you have this?"),
        ("2026-08-26 12:34", "sl", "Hnji.. 2 piece hai"),
        ("2026-08-26 12:35", "cx", "payout?"),
        ("2026-08-26 12:40", "sl", "3800"),
        ("2026-08-26 12:42", "cx", "in hand?"),
        ("2026-08-26 12:43", "sl", "Han in hand"),
        ("2026-08-26 12:50", "cx", "dal diya order"),
        ("2026-08-26 12:51", "tpl",
         new_order("Ahmed Al Maghribi Kaaf EDP", "100ml", "3,808", "SX337892")),
        ("2026-08-26 13:05", "sl", "Kal nikal dunga"),
        ("2026-08-27 17:20", "sl", "Nikal gaya.. tracking daal di"),
        ("2026-08-27 17:25", "cx", "thik hai"),
        ("2026-09-01 11:15", "cx", "Fragrance World Liquid Brun - ye ho paayega?"),
        ("2026-09-01 11:38", "sl", "Han.. kitne chahiye"),
        ("2026-09-01 11:39", "cx", "2"),
        ("2026-09-01 11:44", "sl", "Ho jayega"),
        ("2026-09-01 11:50", "cx", "dal diya"),
        ("2026-09-03 10:05", "sl", "Bhai payout nahi aaya 2 order ka"),
        ("2026-09-03 10:06", "sl", "SX337952 aur SX337953"),
        ("2026-09-03 10:20", "cx", "Getting it checked"),
        ("2026-09-03 10:44", "cx",
         "dono delivered hain par aapki side se complete mark nahi hue. payout usi ke baad "
         "release hota hai, isliye atka hua hai"),
        ("2026-09-03 10:47", "sl", "Acha.. mujhe pata hi nahi tha"),
        ("2026-09-03 10:49", "cx",
         "chinta mat karo, main backend se complete mark karwa deta hu aur aapka payout "
         "process ho jayega. aapko kuch nahi karna"),
        ("2026-09-03 10:52", "sl", "Thank you bhai"),
        ("2026-09-03 10:53", "cx", "monday run hai, tab tak aa jana chahiye"),
        ("2026-09-06 11:30", "cx", "payout aa gaya? mujhe released dikh raha hai"),
        ("2026-09-06 12:05", "sl", "Han aa gaya.. abhi dekha"),
        ("2026-09-06 12:07", "cx",
         "aage se delivered hote hi app me complete kar dena, phir mujhpe wait nahi karna "
         "padega"),
        ("2026-09-06 12:09", "sl", "Han ab pata chal gaya"),
        ("2026-09-06 12:12", "cx",
         "ek aur cheez, SX339047 rasasi hawas ice abhi open hai. customer ko 17 tak chahiye "
         "tha. kab bhej rahe ho?"),
        ("2026-09-06 12:20", "sl", "Aaj sham tak nikal jayega"),
        ("2026-09-06 12:21", "cx", "noted, raat ko dekh lunga"),
        ("2026-09-06 19:30", "cx", "AWB aa gaya, xpressbees. thanks"),
        ("2026-09-06 19:41", "sl", "Ho gaya"),
        ("2026-09-09 14:20", "sl", "Bhai SX337953 ka reminder kyu aa raha hai"),
        ("2026-09-09 14:20", "sl", "Wo to parso bhej diya tha"),
        ("2026-09-09 14:35", "cx", "ek min dekhta hu"),
        ("2026-09-09 14:48", "cx",
         "aap sahi ho. xpressbees ne pickup 7 tarikh ko 6 baje kiya tha, par unka feed "
         "humein 41 ghante baad mila. isliye humari side pe unshipped dikh raha tha aur "
         "reminder chala gaya"),
        ("2026-09-09 14:52", "sl", "Har baar yahi hota hai xpressbees me"),
        ("2026-09-09 14:54", "cx",
         "sabse slow feed wahi hai. urgent walo pe delhivery ya bluedart use karo to ye "
         "baat hi nahi hogi"),
        ("2026-09-09 14:58", "sl", "Cost zyada hai unka"),
        ("2026-09-09 15:00", "cx",
         "to sirf urgent flag walo pe. wo 6 me se 1 order hota hai, itna extra kuch nahi "
         "hai aur reminder loop se bach jaoge"),
        ("2026-09-09 15:04", "sl", "Acha.. theek hai"),
        ("2026-09-09 15:05", "cx", "reminder maine off kar diya, tracking bhi push kar di"),
        ("2026-09-11 10:40", "cx", "Azzaro The Most Wanted Parfum - in hand?"),
        ("2026-09-11 11:02", "sl", "Nahi.. 4 din lagenge"),
        ("2026-09-11 11:03", "cx", "ETA pe daal deta hu phir"),
        ("2026-09-11 11:05", "sl", "Han.. par date sahi likhna"),
        ("2026-09-11 11:06", "cx", "18 days window jayega, aap 4 me de doge to aur achha"),
        ("2026-09-11 11:09", "sl", "Ho jayega"),
        ("2026-09-12 16:10", "cx", "Lattafa Asad Bourbon EDP - y krva sakte?"),
        ("2026-09-12 16:40", "sl", "Han"),
        ("2026-09-12 16:41", "cx", "payout bta do"),
        ("2026-09-12 16:45", "sl", "2500"),
        ("2026-09-12 16:52", "cx", "2511 pe dal raha hu"),
        ("2026-09-12 16:54", "sl", "Han chalega"),
        ("2026-09-14 12:05", "tpl",
         reminder("334342", "Lattafa Eclaire EDP for Women", "100ml")),
        ("2026-09-14 12:30", "sl", "Hnji.. aaj hi nikal jayega"),
        ("2026-09-14 18:50", "sl", "Nikal gaya"),
        ("2026-09-14 18:55", "cx", "dekh liya"),
        ("2026-09-15 10:15", "sl", "Bhai ek baat puchni thi"),
        ("2026-09-15 10:16", "cx", "haan boliye"),
        ("2026-09-15 10:18", "sl", "Order kam aa rahe hain.. pehle roz 8-10 aate the ab 2-3"),
        ("2026-09-15 10:40", "cx",
         "dekha maine. aapke numbers bilkul theek hain, 2.2 din dispatch aur 94 percent "
         "fulfilment. problem category me hai"),
        ("2026-09-15 10:41", "cx",
         "fragrance listings 6 hafte me 400 se 1900 ho gayi hain. wahi listing ab 5 guna "
         "zyada competition ke peeche hai"),
        ("2026-09-15 10:46", "sl", "Acha.. to price kam karun?"),
        ("2026-09-15 10:48", "cx",
         "nahi. aapka 200-300 upar hai lekin maal original hai. price kaat ke aap unki "
         "ladai me chale jaoge aur apni strength kho doge"),
        ("2026-09-15 10:52", "sl", "Phir kya karun.. aap btao"),
        ("2026-09-15 10:55", "cx",
         "in hand share badhao. aapki 38 listings me se sirf 29 percent in hand hain. buyer "
         "sabse pehle usi pe filter lagata hai, aur aap 2 din me bhejte ho to wahi aapka "
         "asli fayda hai"),
        ("2026-09-15 11:00", "sl", "Han ye kar sakta hu"),
        ("2026-09-15 11:01", "cx", "is hafte karke agle friday mujhe batao, main numbers dekhunga"),
        ("2026-09-15 11:03", "sl", "Pakka"),
        ("2026-09-17 09:30", "cx", "SX339008 - status of this shipment?"),
        ("2026-09-17 10:10", "sl", "Aaj ja raha hai.. koi urgent ho iske alawa to bta dena"),
        ("2026-09-17 10:12", "cx", "abhi ke liye ye hi tha"),
    ],
}
