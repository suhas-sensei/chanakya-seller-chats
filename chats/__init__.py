"""The drafts, in the order the console lists them.

Each module copies one named real chat's skeleton from `templates.py` and supplies only
the words. `build.py` refuses to build if a draft's text count or author sequence
disagrees with its template.

Nine drafts, spanning 31 to 132 messages. The 225-message skeleton in `templates.py`
(Nikhil Manchewar, src 8371) is loaded and available but has no draft written against it
yet, so the spread here tops out above the source's p75 of 86 and below its p90 of 208.
"""

from . import c01, c02, c03, c04, c05, c06, c07, c08, c09

DRAFTS = [m.CHAT for m in (c01, c02, c03, c04, c05, c06, c07, c08, c09)]
