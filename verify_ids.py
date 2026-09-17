#!/usr/bin/env python3
"""Check that every SX order id in the drafts is a real one.

    python3 verify_ids.py            # verify against the cached pools
    python3 verify_ids.py --refresh  # re-read the pools from Supabase first (GET only)

Scrapes every `SX\\d{6}` out of the draft text and metadata and checks it against the set
of ids that actually exist in Chanakya's own data. Three pools, because a real order can be
known to us through any of them:

    urgent_pushes.sx_legacy_id          orders Prithvi pushed as urgent
    size_exchanges.sx_order_legacy_id   orders with an exchange raised
    messages.body                       ids Chanakya has already named to a seller

Exits non-zero and names the offenders if anything is invented, so a made-up order id
cannot reach the page unnoticed.

READ ONLY. With --refresh this issues GET requests and nothing else. It stores only the id
lists in `.id-pools.json`; no credential is written to disk. Without --refresh it does not
touch the network at all.
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / ".id-pools.json"
ENV = HERE.parent / ",env.local"

# table -> (id column, seller column). The seller column lets us check the stronger claim:
# not just that an order id exists, but that it is the order of the seller the draft puts
# it against. `messages` keys by conversation rather than a number, so it proves existence
# only and is not used for ownership.
POOLS = [("urgent_pushes", "sx_legacy_id", "seller_wa"),
         ("size_exchanges", "sx_order_legacy_id", "seller_wa"),
         ("messages", "body", None)]

SX = re.compile(r"\bSX\d{6}\b")


def msisdn(n):
    """Last ten digits. `sellers.wa_number` and `size_exchanges.seller_wa` carry the
    country code, `urgent_pushes.seller_wa` sometimes doesn't, and the console's
    customer_id field wants the full number. Comparing raw strings makes the same seller
    look like two."""
    digits = re.sub(r"\D", "", str(n or ""))
    return digits[-10:]


def env():
    """Read SUPABASE_URL / SUPABASE_SERVICE_KEY out of the repo env file, or the process
    environment. Never echoed, never written anywhere."""
    out = dict(os.environ)
    if ENV.exists():
        for line in ENV.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            out.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    missing = [k for k in ("SUPABASE_URL", "SUPABASE_SERVICE_KEY") if not out.get(k)]
    if missing:
        sys.exit(f"missing {', '.join(missing)}; cannot refresh")
    return out


def refresh():
    e = env()
    base, key = e["SUPABASE_URL"].rstrip("/"), e["SUPABASE_SERVICE_KEY"]
    pools, owners = {}, {}
    for table, column, seller_col in POOLS:
        cols = column if not seller_col else f"{column},{seller_col}"
        url = (f"{base}/rest/v1/{table}?"
               + urllib.parse.urlencode({"select": cols, "limit": 5000}))
        req = urllib.request.Request(url, headers={"apikey": key,
                                                   "Authorization": f"Bearer {key}"})
        rows = json.load(urllib.request.urlopen(req, timeout=60))
        found = set()
        for r in rows:
            v = r.get(column)
            if not v:
                continue
            ids = SX.findall(v) if column == "body" else ([v] if SX.fullmatch(v) else [])
            found.update(ids)
            if seller_col and r.get(seller_col):
                wa = msisdn(r[seller_col])
                for i in ids:
                    owners.setdefault(i, set()).add(wa)
        pools[table] = sorted(found)
        print(f"  {table:<16} {len(rows):>5} rows, {len(pools[table]):>4} distinct ids")
    CACHE.write_text(json.dumps({"pools": pools,
                                 "owners": {k: sorted(v) for k, v in owners.items()}},
                                indent=1), encoding="utf-8")
    return pools, owners


def load():
    if not CACHE.exists():
        sys.exit(f"no cached pools at {CACHE.name}; run with --refresh once")
    d = json.loads(CACHE.read_text())
    # normalise on the way in as well as on the way out, so a cache written before the
    # msisdn rule cannot produce a false ownership failure
    return ({k: set(v) for k, v in d["pools"].items()},
            {k: {msisdn(x) for x in v} for k, v in d["owners"].items()})


def main():
    if "--refresh" in sys.argv:
        print("refreshing id pools (GET only):")
        pools, owners = (lambda p, o: ({k: set(v) for k, v in p.items()}, o))(*refresh())
    else:
        pools, owners = load()

    every = set().union(*pools.values())
    print("\npools: " + ", ".join(f"{k} {len(v)}" for k, v in pools.items())
          + f"  (union {len(every)}; ownership known for {len(owners)})")

    sys.path.insert(0, str(HERE))
    from chats import DRAFTS

    bad, rows = [], []
    for d in DRAFTS:
        wa = msisdn(d["wa"])
        blob = "\n".join(list(d["texts"]) + [d["sx"], d["order_note"]])
        for i in sorted(set(SX.findall(blob))):
            where = [t for t, s in pools.items() if i in s]
            own = owners.get(i, set())
            if not where:
                verdict = "*** NOT FOUND ***"
                bad.append(f'{d["file"]} ({d["name"]}): {i} is in no pool')
            elif not own:
                verdict = "exists (owner not recorded)"
            elif wa in own:
                verdict = "exists, owned by this seller"
            else:
                verdict = f'*** OWNED BY {",".join(sorted(own))} ***'
                bad.append(f'{d["file"]} ({d["name"]}, {wa}): {i} belongs to '
                           f'{",".join(sorted(own))}')
            rows.append((i, d["file"], "+".join(t.replace("_", " ") for t in where),
                         verdict))

    print(f"\n{len(rows)} id/draft pairs across {len(DRAFTS)} drafts")
    for i, f, where, verdict in rows:
        print(f"  {i}  {f:<5} {where:<32} {verdict}")

    print("\n" + ("all ids real and attributed to the right seller" if not bad
                  else "FAILED"))
    for b in bad:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
