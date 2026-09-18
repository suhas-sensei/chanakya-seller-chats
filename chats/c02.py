"""Delicc Enterprises. Polite, writes "Pls" and "Kindly", confirms by EOD, thanks with 🙏.

Seller register: "Pls check" / "Kindly" / "Today Eod confirmed" / "Tomorrow for sure" /
"Hanji thank you so much bhai". Uses sir and bro, never boss.

Episodes: payout chased because nothing was marked complete, fixed from the backend,
confirmed three days later, then straight into the open orders. Bulk list of five. A lot
lands short and two customers get a choice.
"""

from ._voice import intro, new_order, open_update, reminder

CHAT = {
    "file": "c02", "id": 9002,
    "wa": "919924028887", "name": "Delicc Enterprises", "score": 5, "nps": 10,
    "sop": "payout_pending",
    "sx": "SX328656 / SX328627 / SX328626 / SX329759 / SX323268",
    "seller_note": "13804 shipped, 99.14% fulfilment, 146 rejected, avg 30.9 days to ship",
    "order_note": "Three delivered orders never marked complete, blocking payout. Five "
                  "more due to ship the same week",
    "flow": {
        "input": "seller chasing payout, refusing to ship until it lands",
        "action": "found nothing was marked complete, closed it from the backend, came "
                  "back in three days to confirm, then clubbed the five open orders",
        "resolution": "payout ran, four shipped, one cancelled clean",
    },
    "turns": [
        ("2026-08-18 16:20", "cx", intro("Delicc Enterprises")),
        ("2026-08-18 16:21", "cx",
         open_update("SX330749", "Off supply Always In Motion Blue T-shirt")),
        ("2026-08-18 17:05", "sl", "Noted sir, will check and revert"),
        ("2026-08-19 10:02", "sl", "Hi sir, pls process payout of 3 delivered orders"),
        ("2026-08-19 10:02", "sl", "SX310920 SX310921 SX313055"),
        ("2026-08-19 10:02", "sl", "It is pending from 2 weeks 🙏"),
        ("2026-08-19 10:20", "cx", "Getting it checked"),
        ("2026-08-19 10:41", "cx",
         "Checked. All three are delivered but not marked complete from your side, that is "
         "why the payout has not released. Nothing is stuck at our end."),
        ("2026-08-19 10:44", "sl", "Maine kuch kiya hi nahi sir"),
        ("2026-08-19 10:44", "sl", "Kaise mark karte hain?"),
        ("2026-08-19 10:46", "cx",
         "Don't worry, I will get it marked as complete from the backend and your payout "
         "will be processed. You don't have to do anything."),
        ("2026-08-19 10:48", "sl", "Hanji thank you so much bhai 🙏"),
        ("2026-08-19 10:49", "cx", "next settlement run is monday. it should land then"),
        ("2026-08-22 11:15", "cx", "payout aa gaya? mujhe apni side pe released dikh raha hai"),
        ("2026-08-22 11:48", "sl", "Yes sir received, all 3 🙏"),
        ("2026-08-22 11:49", "cx",
         "good. ek cheez, aage se delivered hote hi app me complete mark kar dena. phir "
         "mujhpe wait nahi karna padega"),
        ("2026-08-22 11:52", "sl", "Noted sir, will do"),
        ("2026-08-22 11:54", "cx",
         "ab orders. ye 5 is hafte due hain, ek hi message me daal raha hu\n\n"
         "SX328656 off supply core black\nSX328627 blacklist bear waffle\n"
         "SX328626 blacklist bear waffle\nSX329759 gilded crane denim\n"
         "SX323268 gymbrat acid edge tank\n\nsab ready?"),
        ("2026-08-22 12:30", "sl", "Pls give me 1 hour, checking stock"),
        ("2026-08-22 13:35", "sl", "4 ready hain sir. Waffle me se ek nahi mila"),
        ("2026-08-22 13:36", "cx", "kaunsa, SX328627 ya SX328626?"),
        ("2026-08-22 13:38", "sl", "SX328626"),
        ("2026-08-22 13:40", "cx",
         "theek hai. 4 aaj nikal do, SX328626 main customer ke saath dekh leta hu. wo size "
         "kab tak aayega?"),
        ("2026-08-22 13:44", "sl", "Next lot 5 days"),
        ("2026-08-22 13:46", "cx",
         "5 din is order pe zyada hai, ye already 9 din late hai. main unhe cancel offer "
         "karta hu apology ke saath, warna aapke board pe padha rahega"),
        ("2026-08-22 13:50", "sl", "Ok sir pls do"),
        ("2026-08-22 18:05", "sl", "Today Eod confirmed, 4 shipped"),
        ("2026-08-22 18:20", "cx", "dekh liya, 4 ka tracking aa gaya"),
        ("2026-08-22 18:21", "cx", "SX328626 customer ne cancel le liya, aap clear ho"),
        ("2026-08-22 18:26", "sl", "Thank you 🙏"),
        ("2026-08-27 09:40", "tpl",
         reminder("330749", "Off supply Always In Motion Blue T-shirt", "L")),
        ("2026-08-27 10:12", "sl", "Tomorrow for sure sir"),
        ("2026-08-27 10:13", "cx", "noted"),
        ("2026-08-28 09:30", "cx", "SX330749 - status of this shipment?"),
        ("2026-08-28 12:44", "sl", "Pls check, shipped in morning"),
        ("2026-08-28 12:51", "cx", "mil gaya, thanks"),
        ("2026-09-01 15:10", "cx",
         "bhai ek problem hai. SX323800 ka tracking 4 din se ek hi jagah stuck hai"),
        ("2026-09-01 15:11", "cx", "https://www.aftership.com/track/delhivery/2827780209823"),
        ("2026-09-01 15:40", "sl", "Pls give me some time, will check with courier"),
        ("2026-09-01 17:22", "sl", "Courier says misroute, they are pulling it back"),
        ("2026-09-01 17:25", "cx",
         "okay. customer ko main bata deta hu. agar 3 din me move nahi hua to reship karna "
         "padega, aap ek pair reserve rakhna"),
        ("2026-09-01 17:30", "sl", "Reserved sir"),
        ("2026-09-04 11:05", "cx", "SX323800 - koi movement?"),
        ("2026-09-04 11:31", "sl", "Still same"),
        ("2026-09-04 11:33", "cx",
         "then reship kar do aaj, aur AWB mujhe bhej dena. lost wale ka claim main file kar "
         "deta hu, aapko double loss nahi hoga"),
        ("2026-09-04 11:36", "sl", "Kindly file it sir, doing reship now"),
        ("2026-09-04 16:50", "sl", "Reshipped, AWB portal me daal di"),
        ("2026-09-04 16:55", "cx", "dekh liya. claim bhi laga diya hai"),
        ("2026-09-08 10:15", "cx",
         "bhai ek honest baat. aapka fulfilment 99 percent hai jo 13,000 orders pe kaafi "
         "achha hai. lekin days to ship 31 hai, wo sabse kharab number hai mere paas"),
        ("2026-09-08 10:18", "sl", "Bulk se aata hai stock sir, time lagta hai"),
        ("2026-09-08 10:20", "cx",
         "to bulk wali lines ETA pe daal do, in hand sirf wahi jo shelf pe hai. shipping "
         "speed wahi rahegi, par clock sahi ho jayega aur main aapko roz chase nahi karunga"),
        ("2026-09-08 10:26", "sl", "Samajh gaya, will change this week"),
        ("2026-09-12 12:00", "sl", "60 listings changed to ETA sir"),
        ("2026-09-12 12:14", "cx",
         "dekh liya. us ke baad 11 orders aaye hain aur sab window ke andar hain. is hafte "
         "ek bhi reminder nahi bheja maine"),
        ("2026-09-12 12:20", "sl", "Yes noticed 🙏 thank you bhai"),
        ("2026-09-15 11:02", "tpl",
         new_order("Off Supply Gilded Crane Embroidered Denim", "L", "3,999", "SX329759")),
        ("2026-09-15 11:30", "sl", "In hand, will ship today"),
        ("2026-09-15 11:31", "cx", "thik hai"),
    ],
}
