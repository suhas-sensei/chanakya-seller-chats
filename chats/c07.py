"""TopGun. Talks in numbers. Quotes a payout, takes the order, moves on. No pleasantries.

Seller register: "5k daaldo" / "4000 possible ?" / "This week" / "Bhejdia aage" /
"Asking vendor". Almost never uses an address term, which is itself a register.

Episodes: mostly sourcing back and forth, which is what this relationship actually is, with
order chases threaded through it. One date negotiated down from next week, one mod build
that needed the listing type fixed rather than the seller pushed.
"""

from ._voice import intro, new_order, open_urgent, reminder

CHAT = {
    "file": "c07", "id": 9007,
    "wa": "917846907195", "name": "TopGun", "score": 5, "nps": 10,
    "sop": "promised_ship_date", "sx": "SX314239 / SX333644 / SX316819 / SX320617",
    "seller_note": "343 shipped, 99.45% fulfilment, 10 rejected, avg 15.7 days",
    "order_note": "Watches and Dior beauty. SX314239 Seiko Mod Daytona Black, Rs 16,996, "
                  "guaranteed 1 Sep",
    "flow": {
        "input": "high fulfilment seller but 15.7 days to ship, dates drifting",
        "action": "negotiated next week down to a date he picked, then fixed the listing "
                  "type so mod builds stopped starting late",
        "resolution": "dispatch average 15.7 to 6.2, fulfilment held at 99",
    },
    "turns": [
        ("2026-08-28 11:08", "cx", intro("TopGun")),
        ("2026-08-28 11:09", "cx",
         open_urgent("SX316819", "Seiko Mod GMT Gold", "17 September")),
        ("2026-08-28 11:26", "sl", "Wo kal nikal jayega"),
        ("2026-08-28 11:27", "cx", "noted"),
        ("2026-08-28 11:30", "cx", "Seiko Mod Daytona Rose Gold Rainbow - do you have this?"),
        ("2026-08-28 11:32", "sl", "Han 2 piece"),
        ("2026-08-28 11:33", "cx", "payout?"),
        ("2026-08-28 11:36", "sl", "15.5k"),
        ("2026-08-28 11:38", "cx", "15000 possible?"),
        ("2026-08-28 11:42", "sl", "15300 kar do"),
        ("2026-08-28 11:50", "cx", "dal diya"),
        ("2026-08-28 11:51", "tpl",
         new_order("Seiko Mod Daytona Rose Gold Rainbow", "OS", "15,298", "SX302230")),
        ("2026-08-28 12:15", "sl", "This week nikal jayega"),
        ("2026-09-02 10:05", "cx", "SX302230 - what is the status of this order?"),
        ("2026-09-02 13:20", "sl", "Bhejdia aage"),
        ("2026-09-02 13:22", "cx", "tracking panel me daal do phir"),
        ("2026-09-02 15:40", "sl", "Daal di"),
        ("2026-09-04 11:15", "cx", "Dior Ceramic Around the World Butterfly Travel - in hand?"),
        ("2026-09-04 11:44", "sl", "Han"),
        ("2026-09-04 11:45", "cx", "payout bta do"),
        ("2026-09-04 11:50", "sl", "4100"),
        ("2026-09-04 11:55", "cx", "dal diya order"),
        ("2026-09-04 11:56", "tpl",
         new_order("Dior Ceramic Around the World Butterfly Travel Tray", "OS", "4,101",
                   "SX320617")),
        ("2026-09-06 09:40", "cx", "SX320617 - status of this shipment?"),
        ("2026-09-06 12:10", "sl", "Kal"),
        ("2026-09-07 18:20", "sl", "Nikal gaya"),
        ("2026-09-07 18:24", "cx", "thik hai"),
        ("2026-09-11 11:15", "cx",
         "SX314239 seiko mod daytona black, 16,996. guaranteed 1 sep tha aur aaj 11 hai. "
         "kaha hai ye?"),
        ("2026-09-11 11:38", "sl", "Agle hafte"),
        ("2026-09-11 11:39", "cx",
         "agla hafta matlab 6 din aur, upar se 10 din already ja chuke hain. customer 2 baar "
         "pooch chuka hai, teesri baar me cancel karega"),
        ("2026-09-11 11:44", "sl", "Bezel ka kaam hai, 2 din"),
        ("2026-09-11 11:45", "cx",
         "2 din chalega. wo 13 hua, agla hafta nahi. main customer ko 13 bol du?"),
        ("2026-09-11 11:49", "sl", "Han 13 theek"),
        ("2026-09-11 11:50", "cx", "dal diya. aur ek suggestion hai agar sunna chaho"),
        ("2026-09-11 11:53", "sl", "Bolo"),
        ("2026-09-11 11:56", "cx",
         "aapke mod builds in hand pe listed hain. in hand ka window 48 ghante ka hai, aur "
         "aapko build karne me 10 din lagte hain. matlab har mod order shuru hi late se hota "
         "hai. ETA pe daalo to window sahi milega aur ye chase band ho jayegi"),
        ("2026-09-11 12:02", "sl", "Ye pata nahi tha"),
        ("2026-09-11 12:03", "cx", "sirf mod stock pe karna, baaki jaisa hai waisa rehne do"),
        ("2026-09-12 12:40", "cx", "kal SX314239 ka din hai, reminder"),
        ("2026-09-12 13:05", "sl", "Han"),
        ("2026-09-13 12:10", "sl", "Nikal gaya DTDC"),
        ("2026-09-13 12:12", "cx", "mil gaya"),
        ("2026-09-14 10:20", "cx", "YZY YS-01 Cream - y krva sakte?"),
        ("2026-09-14 10:45", "sl", "Kitne"),
        ("2026-09-14 10:46", "cx", "2, UK8 and UK9"),
        ("2026-09-14 10:52", "sl", "UK9 hai, UK8 nahi"),
        ("2026-09-14 10:53", "cx", "payout?"),
        ("2026-09-14 10:56", "sl", "2700"),
        ("2026-09-14 11:00", "cx", "dal diya UK9 wala"),
        ("2026-09-15 15:30", "cx", "Dior Solar Escape Pouch bhi chahiye, 2 piece"),
        ("2026-09-15 15:52", "sl", "3300 each"),
        ("2026-09-15 15:54", "cx", "3200 karlo, 2 le raha hu"),
        ("2026-09-15 15:58", "sl", "Chalo theek"),
        ("2026-09-15 16:05", "cx", "dono dal diye"),
        ("2026-09-16 09:30", "tpl",
         reminder("333644", "Dior Solar Escape Pouch", "OS")),
        ("2026-09-16 10:15", "sl", "Aaj wale orders kal nikal dunga"),
        ("2026-09-16 10:16", "cx", "kal matlab 17, confirm"),
        ("2026-09-16 10:20", "sl", "Han"),
        ("2026-09-17 11:40", "cx",
         "mod listings ETA pe daal di aapne? panel me abhi bhi in hand dikha raha hai kuch"),
        ("2026-09-17 12:05", "sl", "Aaj kar raha hu"),
        ("2026-09-17 12:07", "cx",
         "kar do. aapka fulfilment 99 percent hai jo mere paas sabse achha hai, sirf days to "
         "ship 15.7 pe atka hai. wahi ek cheez aapko peeche rakh rahi hai"),
        ("2026-09-17 12:12", "sl", "Samajh gaya"),
        ("2026-09-17 18:40", "sl", "Dono nikal gaye aur listings bhi change kar di"),
        ("2026-09-17 18:45", "cx", "dekh liya. dono ka tracking aa gaya"),
        ("2026-09-17 18:46", "cx",
         "aapka dispatch average 15.7 se 6.2 pe aa gaya is hafte. fulfilment 99 pe hi hai. "
         "kuch extra nahi kiya aapne, bas baithna band kiya"),
        ("2026-09-17 18:52", "sl", "Order badhenge isse?"),
        ("2026-09-17 18:54", "cx",
         "haan, aur isliye nahi ki koi switch dabata hai. buyer speed pe filter lagate hain, "
         "to wahi listings upar dikhne lagti hain"),
        ("2026-09-17 18:58", "sl", "Theek hai"),
    ],
}
