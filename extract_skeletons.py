#!/usr/bin/env python3
"""Vendor the template skeletons out of csat-review.html into skeletons.json.

    python3 extract_skeletons.py

Run this once on a machine that has the source report. After that the repo builds on its
own: `templates.py` prefers `skeletons.json` and only falls back to reading the 62 MB
report when the vendored file is missing.

WHAT GETS VENDORED. Structure only, per message: who spoke, what kind of message it was,
when, and how many characters it ran to. Plus each chat's source id, its rating, its cohort
and the name it appears under.

WHAT DOES NOT. No message text, ever. The whole point of the drafts is that the words are
written rather than copied, so the words on the other side have no reason to travel. The
report's embedded media (842 images, ~47 MB of base64) is not read at all.

READ ONLY on the source report.
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "skeletons.json"
SOURCE = Path.home() / "culture-circle/local-reports/csat-review.html"


def main():
    import templates

    if not SOURCE.exists():
        raise SystemExit(f"source report not found at {SOURCE}")

    src = SOURCE.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<script id="chat-data" type="application/json">', src)
    if not m:
        raise SystemExit(f"no chat-data payload in {SOURCE.name}")
    end = src.find("</script>", m.end())
    chats = {c["id"]: c for c in json.loads(src[m.end():end])["chats"]}

    out = {}
    for n, (src_id, name) in sorted(templates.TEMPLATES.items()):
        c = chats.get(src_id)
        if c is None:
            raise SystemExit(f"template chat {src_id} is not in {SOURCE.name}")
        got = (c.get("customer_name") or c.get("label") or "").strip()
        if got != name:
            raise SystemExit(f"chat {src_id} is '{got}', expected '{name}'")
        if len(c["messages"]) != n:
            raise SystemExit(f"chat {src_id} is {len(c['messages'])} messages, want {n}")
        out[str(n)] = {
            "src_id": src_id, "src_name": name, "src_label": c.get("label"),
            "src_score": c["score"], "src_cohort": c["cohort"], "n": n,
            # a=author, k=kind, t=original timestamp to the minute, c=character count.
            # Original timestamps, not shifted: templates.py computes the shift so LATEST
            # stays adjustable without re-vendoring.
            "seq": [{"a": x["author"], "k": x["kind"], "t": x["created_at"][:16],
                     "c": len(x["text"] or "")} for x in c["messages"]],
        }

    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    total = sum(t["n"] for t in out.values())
    print(f"vendored {len(out)} skeletons, {total} message slots, "
          f"{OUT.stat().st_size / 1024:.0f} KB")
    for k, t in sorted(out.items(), key=lambda kv: int(kv[0])):
        print(f'  n={k:>4}  src {t["src_id"]:<5} {t["src_name"]:<18} '
              f'{t["src_label"]:<10} score {t["src_score"]} {t["src_cohort"]}')
    print("\nno message text was written; only structure")


if __name__ == "__main__":
    main()
