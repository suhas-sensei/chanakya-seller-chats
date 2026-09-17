#!/usr/bin/env python3
"""Vendor the csat-review page shell into shell/page.html.

    python3 extract_shell.py

`build.py` needs the source report for two different things: the skeletons (handled by
extract_skeletons.py) and the page shell itself, which is where the CSS, the bundled lucide
icons, the 160-line renderer and the DOM markup come from. This vendors that shell so the
repo builds standalone.

WHAT GETS VENDORED. The whole page with every data blob emptied: the three <style> blocks,
the lucide bundle, the renderer, the markup and the dialogs. About 1 MB of the original
62 MB.

WHAT DOES NOT. Three things are stripped, and all three are customer data:

    chat-data        500 real customer conversations           -> {"chats": [], "media": {}}
    row-badge-data   per-conversation dashboard state          -> {}
    customerAvatars  a map keyed by 500 real customer numbers  -> removed

The script refuses to write if any of those survive, so a stripping bug cannot quietly ship
customer data.

READ ONLY on the source report.
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "shell" / "page.html"
SOURCE = Path.home() / "culture-circle/local-reports/csat-review.html"

EMPTY_CHAT_DATA = {
    "generated_at": "", "chats": [], "media": {}, "quotas": {}, "window": "",
    "source": "", "selection": {}, "nps_scope": "",
}


def main():
    if not SOURCE.exists():
        raise SystemExit(f"source report not found at {SOURCE}")
    src = SOURCE.read_text(encoding="utf-8", errors="replace")
    before = len(src)

    out, n = re.subn(r'(<script id="chat-data" type="application/json">).*?(</script>)',
                     lambda m: m.group(1) + json.dumps(EMPTY_CHAT_DATA) + m.group(2),
                     src, flags=re.S)
    if n != 1:
        raise SystemExit(f"expected one chat-data block, found {n}")

    out, n = re.subn(r'(<script id="row-badge-data" type="application/json">).*?(</script>)',
                     lambda m: m.group(1) + "{}" + m.group(2), out, flags=re.S)
    if n != 1:
        raise SystemExit(f"expected one row-badge-data block, found {n}")

    out, n = re.subn(r"const customerAvatars=\{.*?\};\n?", "", out, flags=re.S)
    if n != 1:
        raise SystemExit(f"expected one customerAvatars map, found {n}")

    # refuse to ship if anything customer-shaped survived
    leaks = []
    if re.search(r'"customer_id"\s*:\s*"\d', out):
        leaks.append("a customer_id with a number in it")
    if re.search(r'"messages"\s*:\s*\[\s*\{', out):
        leaks.append("a populated messages array")
    if out.count("data:image/") > 0:
        leaks.append(f'{out.count("data:image/")} embedded data: images')
    if re.search(r'"customer_name"\s*:\s*"\w', out):
        leaks.append("a populated customer_name")
    if leaks:
        raise SystemExit("refusing to write, customer data survived stripping:\n  "
                         + "\n  ".join(leaks))

    # the pieces build.py needs must all still be there
    for needed in ('<script id="chat-data"', '<script id="row-badge-data"',
                   "renderThread", "lucide", 'id="method-modal"',
                   '<nav><button class="icon-button" id="jump-rating"'):
        if needed not in out:
            raise SystemExit(f"vendored shell lost something build.py needs: {needed}")
    if out.count("<style") != 3:
        raise SystemExit(f'expected 3 style blocks, found {out.count("<style")}')

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(out, encoding="utf-8")
    print(f"vendored the shell: {before / 1e6:.1f} MB source -> "
          f"{OUT.stat().st_size / 1e6:.2f} MB")
    print("stripped: chat-data (500 conversations), row-badge-data, "
          "customerAvatars (500 numbers)")
    print("kept: 3 style blocks, lucide, the renderer, the markup and dialogs")
    print("\nno customer data was written")


if __name__ == "__main__":
    main()
