"""The drafts, in the order the console lists them.

Eight seller relationships, each running weeks and built from short transactional
episodes: a reminder, a date, a follow up, a payout, a sourcing question, an RTO. Shape
and voice both come from `Seller WhatsApp Chat Export.zip` (34 real seller threads, 17,276
lines) rather than from the customer-side report. See `_voice.py` before writing a new one.

    c01  ELITE FINDS         optimistic, "checking", "99%", says boss
    c02  Delicc Enterprises  polite, "Pls", "Kindly", 🙏, says sir and bro
    c03  DS.WT               bhai as a suffix, big operator, direct
    c04  Mindyourkicks       "Hnji", trailing dots, no address term
    c05  Sneak Drip          argues his corner, mixes bhai, bro and yaar
    c06  Dipanshu            two and three word replies, rarely says bro
    c07  TopGun              talks in numbers, no pleasantries, no address term
    c08  DJ1                 wants to call for everything, "Okok"

Drafts carry explicit `turns`. The older skeleton-copying format (`template` + `texts`,
matching a csat-review chat message for message) is still supported by `build.py`.
"""

from . import c01, c02, c03, c04, c05, c06, c07, c08

DRAFTS = [m.CHAT for m in (c01, c02, c03, c04, c05, c06, c07, c08)]
