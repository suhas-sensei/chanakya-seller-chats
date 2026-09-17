"""Skeletons lifted from real rated chats in csat-review.html.

A draft does not invent its own length or rhythm. It picks one real conversation and
copies that conversation's skeleton exactly: the message count, the author at every
index, the kind at every index, and the timestamps (so the session and day boundaries,
the overnight gaps and the week-long silences all survive).

`chats/cNN.py` then supplies only the words, one string per message. `build.py` refuses
to build if the count or the author sequence does not match the template, so "same length
and style as a real chat" is enforced rather than asserted in a comment.

Ten templates were chosen off a profile of all 500 source chats to spread the axes that
actually vary in the data:

  n    src   who                score cohort  days  longest-run  seller-ch  agent-ch
  31   6071  Achintya Singh     5     agentic  5     6            25         136
  32   7690  Vivaan Agarwal     4     agentic  5     2            30         212
  36   8725  Viraj .            5     agentic  6     6            16          43
  42   5235  Uthpala H v        4     agentic  6     7            34         105
  50   5008  Dhananjoy Das      5     human    8     7            34         141
  55    333  Muslim altaf Khan  5     agentic  8     4            24         338
  67   6675  Vikas Garg         4     human   15     4            39         141
  84   6838  ANUJMAGO           4     agentic 10    10            17         121
  132  6403  Ananya Tambe       5     human   18    13            38         152
  225  8371  Nikhil Manchewar   5     agentic 21    24            15         131

That is 31 to 225 messages; clean alternating turns through to bursts of 24 unanswered
seller messages; agent replies from a 43-character median to a 338-character median;
bot-run threads through to threads a human teammate carries.

READ ONLY. The source report is read and never written.
"""

import json
import re
from datetime import date
from functools import lru_cache
from pathlib import Path

SOURCE = Path.home() / "culture-circle/local-reports/csat-review.html"

# n -> (source chat id, the name it appears under). Both are checked on load, so a
# reshuffled or regenerated source report fails the build instead of silently shifting
# a draft onto a different conversation's skeleton.
TEMPLATES = {
    31: (6071, "Achintya Singh"),
    32: (7690, "Vivaan Agarwal"),
    36: (8725, "Viraj ."),
    42: (5235, "Uthpala H v"),
    50: (5008, "Dhananjoy Das"),
    55: (333, "Muslim altaf Khan"),
    67: (6675, "Vikas Garg"),
    84: (6838, "ANUJMAGO ANUJMAGO"),
    132: (6403, "Ananya Tambe"),
    225: (8371, "Nikhil Manchewar"),
}

# ONE shift for the whole set, not one per template.
#
# The source chats do not all begin together: they start anywhere from 8 July to 19 August
# and end anywhere from 23 July to 7 September. Anchoring each template's own first day to
# a common date (which is what this used to do) preserved each thread's internal span but
# threw away the stagger between them, so every chat opened on the same morning and the
# sidebar read as one batch.
#
# So: find the latest message across every template, map that single moment to LATEST, and
# shift every template by that same delta. Internal gaps survive, and so does the fact that
# one conversation started six weeks before another.
LATEST = "2026-09-17"


VENDORED = Path(__file__).resolve().parent / "skeletons.json"


@lru_cache(maxsize=1)
def _vendored():
    """The checked-in skeletons, if present. Structure only: author, kind, timestamp and
    character count per message, no text. Lets the repo build without the 62 MB source
    report. Regenerate with `extract_skeletons.py`."""
    if not VENDORED.exists():
        return None
    return json.loads(VENDORED.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _raw_chats():
    """Fallback for when the vendored file is absent: read the source report itself."""
    if not SOURCE.exists():
        raise SystemExit(
            f"neither {VENDORED.name} nor the source report at {SOURCE} is available.\n"
            "Run extract_skeletons.py on a machine that has the report, or restore it.")
    src = SOURCE.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<script id="chat-data" type="application/json">', src)
    if not m:
        raise SystemExit(f"no chat-data payload in {SOURCE}")
    end = src.find("</script>", m.end())
    return {c["id"]: c for c in json.loads(src[m.end():end])["chats"]}


def _messages(n):
    """(src_id, name, score, cohort, [(author, kind, 'YYYY-MM-DD HH:MM', chars), ...]) for
    one template, from the vendored file if we have it and the report otherwise. Both paths
    verify the chat is still the one the draft was written against."""
    src_id, name = TEMPLATES[n]
    v = _vendored()
    if v is not None and str(n) in v:
        t = v[str(n)]
        if t["src_id"] != src_id or t["src_name"] != name or t["n"] != n:
            raise SystemExit(f"{VENDORED.name} disagrees with TEMPLATES for n={n}")
        return (src_id, name, t["src_score"], t["src_cohort"],
                [(x["a"], x["k"], x["t"], x["c"]) for x in t["seq"]])

    chats = _raw_chats()
    if src_id not in chats:
        raise SystemExit(f"source chat {src_id} is gone from {SOURCE.name}")
    c = chats[src_id]
    got = (c.get("customer_name") or c.get("label") or "").strip()
    if got != name:
        raise SystemExit(f"source chat {src_id} is now '{got}', expected '{name}'")
    if len(c["messages"]) != n:
        raise SystemExit(f"source chat {src_id} is now {len(c['messages'])} messages, "
                         f"expected {n}")
    return (src_id, name, c["score"], c["cohort"],
            [(x["author"], x["kind"], x["created_at"][:16], len(x["text"] or ""))
             for x in c["messages"]])


@lru_cache(maxsize=1)
def _shift():
    """The single delta applied to every template. Computed from the latest message in the
    whole set, so it does not depend on which template you ask for first."""
    ends = [date.fromisoformat(_messages(n)[4][-1][2][:10]) for n in TEMPLATES]
    return date.fromisoformat(LATEST) - max(ends)


@lru_cache(maxsize=None)
def skeleton(n):
    """The template for a given length: author/kind/timestamp per index, plus the shape
    numbers the draft is claiming to match."""
    src_id, name, score, cohort, msgs = _messages(n)

    shift = _shift()
    seq = []
    for author, kind, at, chars in msgs:
        d = date.fromisoformat(at[:10]) + shift
        seq.append({
            "author": author,                 # customer | bot | human | system
            "kind": kind,                     # text | interactive | image | ...
            "at": f"{d.isoformat()} {at[11:16]}",
            "src_chars": chars,
        })
    return {
        "n": n, "src_id": src_id, "src_name": name,
        "src_score": score, "src_cohort": cohort,
        "seq": seq,
        "codes": "".join(s["author"][0] for s in seq),
        "days": len({s["at"][:10] for s in seq}),
        "interactive": [i for i, s in enumerate(seq) if s["kind"] == "interactive"],
        "starts": seq[0]["at"][:10], "ends": seq[-1]["at"][:10],
        "span_days": (date.fromisoformat(seq[-1]["at"][:10])
                      - date.fromisoformat(seq[0]["at"][:10])).days + 1,
        "src_starts": msgs[0][2][:10], "src_ends": msgs[-1][2][:10],
    }


def summary():
    rows = [f"global shift {_shift().days:+d} days, so the newest message in the set "
            f"lands on {LATEST}", "",
            f'{"n":>4}  {"src":<5} {"who":<18} {"src span":<24} '
            f'{"draft span":<24} days  active']
    for n in sorted(TEMPLATES, key=lambda k: skeleton(k)["starts"]):
        t = skeleton(n)
        rows.append(f'{n:>4}  {t["src_id"]:<5} {t["src_name"]:<18} '
                    f'{t["src_starts"]} to {t["src_ends"]}      '
                    f'{t["starts"]} to {t["ends"]}      '
                    f'{t["span_days"]:>3}  {t["days"]:>2}')
    return "\n".join(rows)


if __name__ == "__main__":
    print(summary())
    for n in sorted(TEMPLATES):
        t = skeleton(n)
        print(f"\n--- n={n} ({t['src_name']})")
        print("   ", t["codes"])
