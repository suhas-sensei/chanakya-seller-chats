"""The drafts, in the order the console lists them.

Ten order-chasing threads. Each one is a job rather than a conversation: an order is late
or a payout is blocking one, Chanakya negotiates, it resolves. They are short on purpose,
10 to 16 messages, because that is how long the real thing takes.

Coverage:

    c01  RTO reship, courier workaround, reputation lever
    c02  reputation score and PDP views dropping
    c03  high value buyer, payout cleared first
    c04  payout: order never marked complete  (the main case, with the 3-day follow-up)
    c05  payout: customer has not received delivery yet
    c06  bulk follow-up, five orders clubbed
    c07  the X minus 1 reminder
    c08  negotiating "next week" down to a date
    c09  payout used as the reason not to ship
    c10  bulk follow-up with a high value exception

Drafts carry explicit `turns` and set their own length. The older skeleton-copying format
(`template` + `texts`, matching a real chat's shape message for message) is still supported
by `build.py` if a draft declares it.
"""

from . import c01, c02, c03, c04, c05, c06, c07, c08, c09, c10

DRAFTS = [m.CHAT for m in (c01, c02, c03, c04, c05, c06, c07, c08, c09, c10)]
