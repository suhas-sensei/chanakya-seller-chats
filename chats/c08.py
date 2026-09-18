"""DJ1. Wants to get on a call for everything. High volume, 920 rejections, slow dispatch.

Seller register: "Call kru?" / "Hanji bhai update aaya?" / "Okok" / "Free hokr krna" /
"Check krke batana". Answers questions with a question, prefers voice to text.

The longest thread here, and the messiest: a supplier who backs out twice, two cancels with
the penalty rule spelled out formally, an address change caught before the label, a stuck
tracking, and the listing fix that stops it recurring.
"""

from ._voice import new_order, reminder

CHAT = {
    "file": "c08", "id": 9008,
    "wa": "919716433953", "name": "DJ1", "score": 4, "nps": 8,
    "sop": "promised_ship_date",
    "sx": "SX318911 / SX315454 / SX314813 / SX318736 / SX313873",
    "seller_note": "4510 shipped, 83.13% fulfilment, 920 rejected, avg 19.6 days",
    "order_note": "Seiko mod builds listed as in hand; supplier withdrew on two of them",
    "flow": {
        "input": "mod builds listed in hand, supplier withdrew twice, dates drifting",
        "action": "held the dates, spelled out the penalty rule before it applied, and "
                  "moved the unreliable supplier's stock to ETA",
        "resolution": "two cancelled without penalty, dispatch and SLA recovering",
    },
    "turns": [
        ("2026-08-14 10:30", "cx",
         "Hello, Chanakya from SourceX. I will be looking after your order follow ups."),
        ("2026-08-14 10:31", "cx",
         "Can you please confirm the estimated shipping date for SX314813, Seiko Mod Santos "
         "Silver Fume."),
        ("2026-08-14 11:20", "sl", "Call kru?"),
        ("2026-08-14 11:22", "cx",
         "chat pe hi bata dijiye, mujhe record rakhna hota hai. bas date chahiye"),
        ("2026-08-14 11:30", "sl", "18 tak"),
        ("2026-08-14 11:31", "cx", "18 noted"),
        ("2026-08-17 10:00", "cx", "kal SX314813 ship hona hai, reminder"),
        ("2026-08-17 10:40", "sl", "Okok"),
        ("2026-08-18 18:20", "cx", "SX314813 - what is the status of this order?"),
        ("2026-08-18 20:10", "cx", "u there?"),
        ("2026-08-19 09:40", "sl", "Hanji bhai update aaya?"),
        ("2026-08-19 09:41", "cx", "main aapse pooch raha hu. SX314813 nikla ya nahi"),
        ("2026-08-19 09:50", "sl", "Check krke batana"),
        ("2026-08-19 09:52", "cx", "ye aapka order hai, aap check karke bataiye"),
        ("2026-08-19 10:30", "sl", "Nikal gaya kal shaam"),
        ("2026-08-19 10:32", "cx", "tracking panel me nahi hai. daal dijiye"),
        ("2026-08-19 12:15", "sl", "Daal di"),
        ("2026-08-21 11:05", "cx", "SX318909 - can you check status of this order?"),
        ("2026-08-21 13:40", "sl", "Nike Ja 3 wala?"),
        ("2026-08-21 13:41", "cx", "haan"),
        ("2026-08-21 13:50", "sl", "Kal nikal jayega"),
        ("2026-08-22 17:30", "sl", "Nikal gaya"),
        ("2026-08-22 17:33", "cx", "thik hai"),
        ("2026-08-25 10:15", "cx", "SX318911 - i want to know the status of this order"),
        ("2026-08-25 12:20", "sl", "Bhai isme thoda problem ho gaya"),
        ("2026-08-25 12:21", "cx", "kya hua"),
        ("2026-08-25 12:30", "sl", "Dial supplier ne mana kar diya"),
        ("2026-08-25 12:33", "cx",
         "matlab piece kabhi in hand tha hi nahi. ye delay nahi hai, ye sourcing ka issue "
         "hai. mil sakta hai ya customer ko cancel bolu?"),
        ("2026-08-25 12:40", "sl", "Mil jayega, 4-5 din"),
        ("2026-08-25 12:42", "cx",
         "to main 30 august bol deta hu customer ko, aur ye bhi bataunga ki sourcing wait "
         "hai. usse aage gaya to main cancel recommend karunga"),
        ("2026-08-25 12:48", "sl", "Okok 30 pakka"),
        ("2026-08-28 10:00", "cx", "SX315454 - lady datejust ka kya scene hai"),
        ("2026-08-28 14:20", "sl", "Wo bhi same supplier ka hai"),
        ("2026-08-28 14:22", "cx", "matlab wo bhi nahi aa raha"),
        ("2026-08-28 14:30", "sl", "Shayad"),
        ("2026-08-28 14:32", "cx", "shayad se kaam nahi chalega. aaj shaam tak confirm kar dijiye"),
        ("2026-08-28 18:40", "sl", "Nahi aa raha bhai dono"),
        ("2026-08-28 18:45", "cx",
         "Thank you for confirming. Please note how this works so there is no surprise. If "
         "an order is auto cancelled after crossing its window, a 5% penalty applies. If it "
         "is cancelled now on a confirmed sourcing failure, there is no penalty and I log "
         "the reason against the order."),
        ("2026-08-28 18:52", "sl", "Abhi hi kar do phir"),
        ("2026-08-28 18:58", "cx",
         "dono cancel kar diye, SX318911 aur SX315454. reason supplier withdrawal likha hai, "
         "plain seller cancel nahi. fulfilment pe asar padega par penalty nahi lagi"),
        ("2026-08-28 19:05", "sl", "Thank you bhai"),
        ("2026-08-29 11:10", "cx",
         "ab ek baat jo pehle honi chahiye thi. ye supplier 3 mahine se aapko maar raha hai "
         "aur uska stock aap in hand pe list kar rahe ho"),
        ("2026-08-29 11:14", "cx",
         "uske pieces ETA pe daal do real window ke saath. phir supplier ka miss aapke liye "
         "cancellation nahi banega, sirf ek late ETA banega"),
        ("2026-08-29 11:25", "sl", "Par ETA pe order kam aate hain"),
        ("2026-08-29 11:28", "cx",
         "kam order jo aap bhej sakte ho, wo zyada order se behtar hai jo aap nahi bhej "
         "sakte. aapka fulfilment 83 hai, wo in hand tag se zyada nuksan kar raha hai"),
        ("2026-08-29 11:35", "sl", "Samajh gaya, us supplier ka ETA kar dunga"),
        ("2026-09-01 10:20", "cx",
         "SX313873 - ASICS Superblast 3, 26,404 ka hai. ye aaj tak nahi nikla, kya scene hai"),
        ("2026-09-01 11:50", "sl", "Call kru iske liye?"),
        ("2026-09-01 11:52", "cx", "date bata dijiye, call ki zarurat nahi"),
        ("2026-09-01 12:10", "sl", "3 tarikh"),
        ("2026-09-02 10:00", "cx", "kal SX313873, reminder"),
        ("2026-09-02 10:35", "sl", "Han yaad hai"),
        ("2026-09-03 16:20", "sl", "Nikal gaya"),
        ("2026-09-03 16:25", "cx", "mil gaya, thanks"),
        ("2026-09-05 12:10", "cx",
         "SX318736 - address change hai. customer shift ho gaya hai. abhi tak nikla to nahi?"),
        ("2026-09-05 12:40", "sl", "Nahi, pack hai. kal jana tha"),
        ("2026-09-05 12:42", "cx",
         "achha hua pakad liya. naya address surat ka hi hai par sector alag. panel me update "
         "kar diya hai, aap kal label fresh nikalna, purana mat use karna"),
        ("2026-09-05 12:48", "sl", "Okok"),
        ("2026-09-06 11:30", "sl", "Nikal gaya, naya label se"),
        ("2026-09-06 11:33", "cx", "AWB me naya pincode dikh raha hai. sahi kiya"),
        ("2026-09-09 10:15", "cx", "SX309495 - tracking 5 din se ek jagah stuck hai"),
        ("2026-09-09 10:16", "cx", "https://www.aftership.com/track/delhivery/2827780209823"),
        ("2026-09-09 11:40", "sl", "Courier se pooch ke batata hu"),
        ("2026-09-09 15:20", "sl", "Wo bolte hain hub me hai, 2 din me move hoga"),
        ("2026-09-09 15:24", "cx",
         "theek hai. 2 din baad bhi nahi hila to reship karna padega, ek piece side me rakh "
         "lena"),
        ("2026-09-11 10:05", "cx", "SX309495 hila?"),
        ("2026-09-11 11:20", "sl", "Han kal se move ho raha"),
        ("2026-09-11 11:22", "cx", "good, phir reship nahi chahiye"),
        ("2026-09-12 12:30", "cx", "Seiko Mod Datejust Bordeaux Nebula - ye ho paayega?"),
        ("2026-09-12 14:10", "sl", "Han par ETA"),
        ("2026-09-12 14:11", "cx", "kitne din"),
        ("2026-09-12 14:20", "sl", "12"),
        ("2026-09-12 14:22", "cx", "payout?"),
        ("2026-09-12 14:30", "sl", "21500"),
        ("2026-09-12 14:40", "cx", "dal diya, ETA 12 days ke saath"),
        ("2026-09-12 14:41", "tpl",
         new_order("Seiko Mod Datejust 'Bordeaux Nebula'", "OS", "21,651", "SX318736")),
        ("2026-09-12 15:00", "sl", "Okok"),
        ("2026-09-15 10:40", "cx",
         "update - aapke SLA breach 7 se 2 pe aa gaye hain aur dispatch average 19.6 se 12 "
         "pe. ETA wala change kaam kar raha hai"),
        ("2026-09-15 11:30", "sl", "Achha hai bhai"),
        ("2026-09-15 11:32", "cx",
         "fulfilment 83 se hilne me ek mahina lagega kyunki wo rolling average hai. main "
         "aapko bata dunga jab 90 cross kare"),
        ("2026-09-15 11:40", "sl", "Free hokr krna"),
        ("2026-09-15 11:41", "cx", "kar dunga"),
        ("2026-09-16 09:50", "tpl",
         reminder("320882", "Seiko Mod Daytona Rose Gold Rainbow", "OS")),
        ("2026-09-16 10:40", "sl", "18 ko"),
        ("2026-09-16 10:41", "cx", "18 noted, 17 ko reminder aayega"),
        ("2026-09-17 10:00", "cx", "kal SX320882, reminder"),
        ("2026-09-17 10:35", "sl", "Han pakka"),
        ("2026-09-17 10:36", "cx", "thik hai"),
    ],
}
