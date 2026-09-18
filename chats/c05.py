"""Sneak Drip. Argues, explains his position, says yaar. Lowest fulfilment on the roster.

Seller register: "Can you please help bhai" / "Dekhona bro" / "Bhai you see where i come
from also yaar" / "That's the issue". Mixes bhai, bro and yaar in the same thread.

Episodes: payout chased on an order that had not delivered yet, the SLA breach warning in
the formal register with a real penalty attached, COD refusals taken to the team, and a
cap that costs him volume.
"""

from ._voice import intro, open_update, reminder

CHAT = {
    "file": "c05", "id": 9005,
    "wa": "917774922888", "name": "Sneak Drip", "score": 4, "nps": 7,
    "sop": "payout_pending", "sx": "SX327430 / SX333867 / SX316135",
    "seller_note": "316 shipped, 79.95% fulfilment, 82 rejected, avg 4.1 days",
    "order_note": "Payout chased before delivery; 90% of open orders in SLA breach; 14 of "
                  "38 COD orders refused at the door",
    "flow": {
        "input": "payout chased on an undelivered order, SLA breach across the account",
        "action": "explained the payout clock, issued the penalty warning formally, took "
                  "his COD refusal numbers to the team",
        "resolution": "COD capped at 6k on trial, refusals 22 to 2, breach cleared",
    },
    "turns": [
        ("2026-08-18 11:30", "cx", intro("Sneak Drip")),
        ("2026-08-18 11:31", "cx",
         open_update("SX325430", "ALL SAINTS Xander Flocked Logo Oversized")),
        ("2026-08-18 15:20", "sl", "Bhai SX327430 ka payout kab aayega"),
        ("2026-08-18 15:35", "cx",
         "wo abhi deliver nahi hua hai. AWB in transit dikha raha hai, kal out for delivery "
         "hai jalgaon me"),
        ("2026-08-18 15:38", "sl", "Maine to 4 din pehle bhej diya tha yaar"),
        ("2026-08-18 15:40", "cx",
         "bheja tha aur time pe bheja tha. par payout ka clock delivery se chalta hai, "
         "dispatch se nahi"),
        ("2026-08-18 15:44", "sl", "Acha.. to delivery ke baad"),
        ("2026-08-18 15:45", "cx", "haan. kal delivery hai to 20 ke run me chala jayega"),
        ("2026-08-18 15:47", "sl", "Theek hai"),
        ("2026-08-20 10:15", "cx", "kal deliver ho gaya tha, signed. payout 20 ke run me hai"),
        ("2026-08-20 10:31", "sl", "Ok bro"),
        ("2026-08-21 12:05", "sl", "Aa gaya bhai"),
        ("2026-08-21 12:07", "cx", "good"),
        ("2026-08-25 11:00", "cx",
         "Please note the following. 9 of your 10 open orders are currently in SLA breach. "
         "Orders that cross the breach window are auto cancelled, and a 5% penalty is "
         "deducted against the order value at that point."),
        ("2026-08-25 11:01", "cx",
         "I would rather you cleared them than take the penalty. Can you tell me which of "
         "these can ship this week?"),
        ("2026-08-25 11:30", "sl", "Bhai 5 percent to bahut hai"),
        ("2026-08-25 11:32", "cx",
         "isliye pehle bata raha hu. abhi tak ek bhi penalty nahi laga hai aapke account pe"),
        ("2026-08-25 11:36", "sl", "Can you please help bhai, kaunse pehle karu"),
        ("2026-08-25 11:40", "cx",
         "ye 4 sabse purane hain, inhe pehle karo\n\nSX315848 all saints xander\n"
         "SX325831 all saints petals\nSX320932 polo RL white graphic\n"
         "SX316135 breaker white\n\nbaaki 5 agle hafte"),
        ("2026-08-25 11:46", "sl", "Ok 3 to kal ho jayenge"),
        ("2026-08-25 11:47", "cx", "aur chautha?"),
        ("2026-08-25 11:52", "sl", "SX316135 XL nahi hai stock me"),
        ("2026-08-25 11:54", "cx", "kab tak aayega"),
        ("2026-08-25 11:58", "sl", "Pata nahi bro, vendor reply nahi kar raha"),
        ("2026-08-25 12:00", "cx",
         "to us pe intezar mat karo. main aaj hi customer ko cancel offer karta hu. customer "
         "cancel karta hai to penalty nahi lagti, auto cancel me lagti hai"),
        ("2026-08-25 12:04", "sl", "Acha aisa hai? Pata nahi tha"),
        ("2026-08-25 12:05", "cx", "haan. isliye jo nahi ho sakta wo mujhe jaldi batao, chhupao mat"),
        ("2026-08-26 18:20", "sl", "3 nikal gaye bhai"),
        ("2026-08-26 18:26", "cx", "dekh liya. SX316135 customer ne cancel le liya, penalty nahi"),
        ("2026-08-26 18:30", "sl", "Thank you yaar"),
        ("2026-08-29 10:10", "cx", "baaki 5 ka kya plan hai"),
        ("2026-08-29 11:40", "sl", "Dekhona bro, COD orders hain wo"),
        ("2026-08-29 11:41", "cx", "COD hone se kya dikkat aa rahi hai"),
        ("2026-08-29 11:48", "sl",
         "Bhai you see where i come from also yaar. COD bhejta hu, customer leta hi nahi. "
         "packing gaya, shipping gaya, wapas aata hai, mera paisa doob gaya"),
        ("2026-08-29 11:52", "cx", "aapke kitne COD wapas aaye is mahine"),
        ("2026-08-29 11:55", "sl", "Bahut.. 14 15 to honge"),
        ("2026-08-29 12:20", "cx",
         "maine nikale. 38 COD me se 14 refuse hue hain, aur 12 unme se 8,000 se upar ke "
         "hain. ye aapka pura fulfilment gap hai, shipping nahi"),
        ("2026-08-29 12:24", "sl", "Wahi to keh raha hu bhai"),
        ("2026-08-29 12:26", "cx",
         "main aapke numbers team ke paas le jata hu. promise nahi kar raha ki wo maanenge, "
         "par sirf complaint nahi, data ke saath jaunga"),
        ("2026-08-29 12:30", "sl", "Itna hi kaafi hai bro"),
        ("2026-09-01 10:05", "cx", "SX325430 - i want to know the status of this order"),
        ("2026-09-01 12:15", "sl", "Kal"),
        ("2026-09-01 12:16", "cx", "kal matlab 2 september, confirm?"),
        ("2026-09-01 12:20", "sl", "Han"),
        ("2026-09-02 10:00", "cx", "aaj wala reminder, SX325430"),
        ("2026-09-02 17:45", "sl", "Nikal gaya"),
        ("2026-09-04 14:10", "ops",
         "Hello Sneak Drip, this is Nikhil from Seller Ops. Chanakya has shared your COD "
         "refusal numbers with us."),
        ("2026-09-04 14:12", "ops",
         "We are placing your store on a COD cap of Rs 6,000 for a one month trial, "
         "effective today. Orders above that value will be prepaid only."),
        ("2026-09-04 14:18", "sl", "Sach me sir? Bahut badhiya"),
        ("2026-09-04 14:20", "ops",
         "One month, then we review it with you. Please keep an eye on your order volume "
         "as well, since a cap does reduce it."),
        ("2026-09-04 14:24", "sl", "Han dekh lenge, thank you"),
        ("2026-09-04 14:30", "cx",
         "wapas aa gaya. ye numbers ki wajah se hua hai, complaint ki wajah se nahi. agli "
         "baar bhi jab kuch paisa kha raha ho to mujhe numbers do"),
        ("2026-09-04 14:34", "sl", "Bhai aapne uthaya isliye hua"),
        ("2026-09-04 14:35", "cx", "maine sirf le jaya. argue aapke refusal rate ne kiya"),
        ("2026-09-08 11:20", "sl", "Bhai COD cap ke baad refusal band"),
        ("2026-09-08 11:21", "sl", "Par order bhi kam ho gaye"),
        ("2026-09-08 11:30", "cx",
         "dono sach hain. refusals 22 se 2 pe hain, orders 15 percent neeche. sawal ye hai "
         "ki aap fayde me ho ya nahi"),
        ("2026-09-08 11:32", "cx",
         "ho. jo 15 percent gaya wo wahi tha jo waise bhi aapke kharche pe wapas aa raha tha"),
        ("2026-09-08 11:38", "sl", "Hisab se to faida hi hai"),
        ("2026-09-08 11:40", "cx", "month review main khud lekar aaunga, aapko poochna nahi padega"),
        ("2026-09-10 09:40", "tpl",
         reminder("305429", "ALL SAINTS Laser SS Crew Sunburn Orange", "XL")),
        ("2026-09-10 10:20", "sl", "Aaj kar dunga bhai"),
        ("2026-09-10 18:30", "sl", "Ho gaya"),
        ("2026-09-10 18:33", "cx", "thik hai"),
        ("2026-09-15 10:05", "cx",
         "aapke SLA breach 9 se 0 pe aa gaye hain. ek bhi penalty nahi lagi"),
        ("2026-09-15 10:22", "sl", "Achha laga sunke"),
        ("2026-09-15 10:24", "cx",
         "fulfilment 80 se 88 pe hai. 90 cross karte hi main aapko bata dunga, aapko roz "
         "check nahi karna padega"),
        ("2026-09-15 10:28", "sl", "Thanks bro, ab thoda aasan lag raha hai"),
    ],
}
