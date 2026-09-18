"""Voice reference and the fixed template blocks, taken from the real seller exports.

Read this before writing a draft. Everything here was lifted from
`Seller WhatsApp Chat Export.zip` (34 real seller threads, 17,276 lines), not invented.

MEASURED SHAPE
    median thread      159 messages over 19 active days
    range              11 to 842 messages, 2 to 61 active days
    episode length     3 to 8 messages: a reminder, a date, a follow-up, done
A thread is long because it covers many orders over weeks. It is not one conversation.

CHANAKYA HAS TWO REGISTERS AND SWITCHES BETWEEN THEM

Formal. Opens a relationship, and comes back whenever it turns serious: penalties, SLA
breaches, a lost parcel, anything a seller might later dispute.
    "Can you please confirm the estimated shipping date for this order."
    "Concerned person will share shortly."
    "Noted, will be done in 48 hours.."
    "Getting it checked"
    "Kindly take care while shipping"

Terse Hinglish. The day to day, once there is rapport.
    "SX184126 - what is the status of this order?"   (verbatim repeat if ignored)
    "any update?"   "ye kab ship ho rha?"   "ye ho paayega?"   "u there?"   "???"
    "are bhai"   "hello bhai"   "okay bhai"   "confirm asap"   "check and let me know"
    "what is the reason of delay?"   "dal diya"   "thik hai"

The status question is asked a dozen different ways in the real data. Vary it:
    what is the status of this order? / status of this shipment? / can you check status of
    this order? / i want to know the status of this order / what is the update on this

NEGOTIATION LEVERS, as actually used
    SLA and penalty      "90% of your orders are SLA breached"
                         "cancelling this & refunding 5% penalty will be deducted"
    TAT and ranking      "isliye suggest kar raha hu, aapke TAT aur SLA best ho jayenge
                          timely shipping se"
    holding the date     "bhai ye aapne bola tha saturday this will be shipped.. and today
                          is tuesday can you confirm me the status?"
    asking for a real date  "Can you give me exact dates? 1-2 din badha ke de do no issue"
    the buyer            "customer already is anxious"
    removing the blocker "10 other sellers used delhivery today because of the same issue"

ADDRESS TERMS ARE PER SELLER, NOT UNIVERSAL
Real threads use bhai, bro, boss, ji, sir, yaar, Hnji, and often nothing at all. Pick one
or two per seller and stay with them. Do not give every seller the same word.

SELLER REGISTERS observed, one per draft
    price-first, clipped     "5k daaldo"  "Aaj wale orders kal nikal dunga"  "This week"
    polite, formal-ish       "Pls check"  "Kindly"  "Today Eod confirmed"  "Tomorrow for sure"
    bhai-suffix habit        "Any update bhai"  "Sorted bhai aagaya"
    Hnji, trailing dots      "Hnji.. koi urgent ho to bta dena"  "Acha.. koi na."
    complains, yaar          "Bhai you see where i come from also yaar"  "Dekhona bro"
    very terse               "yes wait"  "Little bit"  "No bro"  "Aajaega"
    wants to call            "Call kru?"  "Hanji bhai update aaya?"  "Okok"
    boss, optimistic         "Wait"  "Checking"  "2 min"  "Ho jayega"  "99%"  "bosss"
"""

# Verbatim from the exports. Sent as a block, which is why drafts send it as `tpl`.
REMINDER = ("REMINDER 🚨🚨🚨\n"
            "Your order is pending to be shipped\n"
            "{id} - {product} - {size}.\n"
            "It is now mandatory to ship all in hand orders within 48H and all ETA orders "
            "within 18 days for faster payouts\n"
            "PLEASE SEND THE EXACT SHIPPING DATE HERE. Thank you.")

NEW_ORDER = ("Product name - {product}\n"
             "Size - {size}\n"
             "Payout - {payout}\n"
             "SOLD AT: culturecircle\n"
             "SourceX ID: {sx}")

ORDER_BRIEF = (
    "Hey\n"
    "Got an order for Culture Circle on Source X\n"
    "{product}\n"
    "SKU ID: {sku}\n"
    "Size: {size}\n"
    "Payout : {payout}\n\n"
    "*Important points to note*\n\n"
    "1. It's now *mandatory* to verify the pair on the SourceX App via CheckCheck. It is "
    "free for you and paid via SourceX.\n\n"
    "2. Kindly process it within the next working *48 hours or else the order will be "
    "cancelled*. We will not be able to provide a resolution in case customer cancels due "
    "to delay.\n\n"
    "3. Please share images and update tracking after you ship the pair in the app.\n\n"
    "4. *DO NOT* directly contact the buyer in any way. For any query regarding buyer "
    "details, address and others connect with us. If any violation is found, it will lead "
    "to *instant lifetime ban* from SourceX.")


# HOW CHANAKYA OPENS
#
# Always formal, always the same three beats: who he is, which order, what he needs. Taken
# from the live templates in `backend/src/rubberstate/agent/templates.py` and from how the
# formal ops register reads in the exports.
#
# Only the opening. Once the seller replies the register drops to terse Hinglish and stays
# there, and comes back to formal only when something becomes disputable: a penalty, an SLA
# breach, a lost parcel.

INTRO = ("Hi {name}, this is Chanakya from SourceX. I look after seller orders for "
         "Culture Circle.")

OPEN_UPDATE = ("About order {sx}, {product}. When are you shipping it? The customer is "
               "waiting, so please share an update.")

OPEN_URGENT = ("A gentle request about order {sx} ({product}). The customer has an urgent "
               "requirement and has requested delivery by {by}. Could you please help us "
               "fulfil this in time? When is the earliest you can ship this order? "
               "Thank you!")

OPEN_CONFIRM = "Could you please confirm the estimated shipping date for order {sx}, {product}."

OPEN_RTO = ("Order {sx} has been returned to origin. AWB {awb}. Could you please confirm "
            "whether you have received it back, and whether you intend to reship?")


def intro(name):
    return INTRO.format(name=name)


def open_update(sx, product):
    return OPEN_UPDATE.format(sx=sx, product=product)


def open_urgent(sx, product, by):
    return OPEN_URGENT.format(sx=sx, product=product, by=by)


def open_confirm(sx, product):
    return OPEN_CONFIRM.format(sx=sx, product=product)


def open_rto(sx, awb):
    return OPEN_RTO.format(sx=sx, awb=awb)


def reminder(id_, product, size):
    return REMINDER.format(id=id_, product=product, size=size)


def new_order(product, size, payout, sx):
    return NEW_ORDER.format(product=product, size=size, payout=payout, sx=sx)
