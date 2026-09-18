#!/usr/bin/env python3
"""Render the drafts into the csat-review console, seller side.

    python3 build.py                 # rebuild, validate, report
    python3 build.py --scaffold 55   # print a template's per-index authoring scaffold

Writes, next to this script:
    chanakya-seller-chats.html   one self-contained file, opens over file://
    chats.json                   the same payload for test use

HOW THE UI IS THE OLD FILE, NOT A LOOKALIKE. This reads
`~/culture-circle/local-reports/csat-review.html`, lifts its three <style> blocks, its
bundled lucide icons and its 160-line renderer verbatim, and swaps only the data and the
strings that say "customer" where this console means "seller".

HOW THE LENGTH AND RHYTHM ARE THE OLD FILE'S TOO. Every draft names a real source chat in
`templates.py` and inherits its skeleton: message count, author per index, kind per index,
and timestamps (so day boundaries and week-long gaps survive). `chats/cNN.py` supplies only
the words. A draft whose text count or author sequence disagrees with its template fails
the build.

READ ONLY. The source report is read, never written. No Supabase, Meta, CC, Slack or
Temporal calls, and no credentials live here. The identifiers in `chats/` were read once
with GET and verified against the live id pools (see `verify_ids.py`).
"""

import base64
import hashlib
import json
import re
import sys
from pathlib import Path

import templates
from chats import DRAFTS

HERE = Path(__file__).resolve().parent

# The page shell (CSS, lucide, renderer, markup) comes from the csat-review report. A
# stripped copy carrying no customer data is checked in at shell/page.html so this builds
# standalone; the 62 MB original is used only when that copy is missing. Regenerate with
# extract_shell.py.
SHELL = HERE / "shell" / "page.html"
SOURCE = SHELL if SHELL.exists() else templates.SOURCE

CHANAKYA_WA = "+91 92176 76103"

# Read out of the source report's own chat-data payload. Quoted in the details modal so
# the page states what it matched rather than implying the numbers are its own.
SOURCE_SHAPE = {"chats": 500, "min_messages": 30, "p25": 38, "median": 51, "p75": 86,
                "p90": 208, "score5": 245, "score4": 155, "score3": 75, "score2": 7,
                "score1": 18}

ROLE = {"customer": "assistant", "bot": "assistant", "human": "assistant",
        "system": "assistant"}

CSAT_ROWS = [{"id": "CSAT_5", "title": "5 - Excellent", "description": "sorted it perfectly"},
             {"id": "CSAT_4", "title": "4 - Good", "description": "happy with the help"},
             {"id": "CSAT_3", "title": "3 - Okay", "description": "did the job"},
             {"id": "CSAT_2", "title": "2 - Poor", "description": "not really sorted"},
             {"id": "CSAT_1", "title": "1 - Bad", "description": "no help at all"}]

AVATAR_COLOURS = [("#b3261e", "#14161a"), ("#14161a", "#d4643c"), ("#1f4d3d", "#e0b85a"),
                  ("#31405c", "#c9a57e"), ("#5a3a2e", "#7fae97"), ("#3d3a52", "#d08d6e")]


def avatar(wa):
    """A seller avatar in the source's exact SVG shape, deterministic from the number so
    a rebuild never reshuffles the sidebar."""
    h = int(hashlib.sha1(wa.encode()).hexdigest(), 16)
    bg, fg = AVATAR_COLOURS[h % len(AVATAR_COLOURS)]
    mid, dx, dy = f"m{h % 10**10}", h % 9, (h // 9) % 9
    rot = (h // 81) % 360
    el, er = 12 + (h // 7) % 3, 20 + (h // 11) % 3
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36" fill="none" '
           'role="img" width="48" height="48"><title>Seller avatar, mood: happy</title>'
           f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="36" '
           'height="36"><rect width="36" height="36" rx="72" fill="#fff"></rect></mask>'
           f'<g mask="url(#{mid})"><rect width="36" height="36" fill="{bg}"></rect>'
           f'<rect x="0" y="0" width="36" height="36" rx="36" fill="{fg}" '
           f'transform="translate({dx} {dy}) rotate({rot} 18 18) scale(1.1)"></rect>'
           '<g transform="translate(0 3)">'
           '<path d="M13,20 a1,0.75 0 0,0 10,0" fill="#f4f2ed"></path>'
           f'<rect x="{el}" y="14" width="1.5" height="2" rx="1" fill="#f4f2ed"></rect>'
           f'<rect x="{er}" y="14" width="1.5" height="2" rx="1" fill="#f4f2ed"></rect>'
           '</g></g></svg>')
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


WHO = {"cx": "bot", "sl": "customer", "ops": "human"}


def build_turns(d, index):
    """A free-form draft: explicit (timestamp, who, text) turns, no skeleton.

    These are the order-chasing threads. They are short and transactional on purpose,
    because the job is input -> negotiation -> resolution rather than a conversation.
    A skeleton copied off a 132-message customer chat is the wrong shape for that, so
    these drafts set their own length.
    """
    msgs = []
    for i, (at, who, text) in enumerate(d["turns"]):
        if who not in WHO:
            raise SystemExit(f'{d["file"]} turn {i}: unknown speaker {who!r}')
        author = WHO[who]
        msgs.append({
            "id": d["id"] * 1000 + i, "author": author, "kind": "text",
            "role": "assistant", "text": text,
            "created_at": f"{at}:00+05:30", "media_id": None,
            "operator_name": d.get("operator", "Seller Ops") if author == "human" else None,
            "interactive": None,
        })
    return finish_chat(d, index, msgs, template=None)


def build_chat(d, index):
    """Marry one draft's words to its template's skeleton. Raises on any mismatch."""
    t = templates.skeleton(d["template"])
    texts = d["texts"]
    if len(texts) != t["n"]:
        raise SystemExit(f'{d["file"]}: {len(texts)} texts but template {d["template"]} '
                         f'({t["src_name"]}) has {t["n"]} messages')
    if "codes" in d and d["codes"] != t["codes"]:
        raise SystemExit(f'{d["file"]}: declared author sequence does not match template '
                         f'{d["template"]}\n  declared {d["codes"]}\n  template {t["codes"]}')

    msgs = []
    for i, (slot, text) in enumerate(zip(t["seq"], texts)):
        author, kind = slot["author"], slot["kind"]
        # Media kinds are kept. No bytes travel with these drafts, and the original
        # renderer already handles exactly that case: it prints its own
        # "Image / Not embedded" chip above whatever was said, so an image turn stays an
        # image turn with the caption beneath it. Kinds it does not treat as media
        # (web_search and friends) fall through and render as plain text, which is how a
        # tool step reads in Chanakya's own console.
        m = {"id": d["id"] * 1000 + i, "author": author, "kind": kind,
             "role": "user" if text.strip().startswith(("5 -", "4 -", "3 -", "2 -", "1 -"))
                     else ROLE[author],
             "text": text, "created_at": f'{slot["at"]}:00+05:30', "media_id": None,
             "operator_name": d.get("operator", "Nikhil (Seller Ops)")
                              if author == "human" else None,
             "interactive": None}
        if kind == "interactive":
            # Three things arrive as interactive sends on this lane: the CSAT list, the
            # exchange Confirm button, and an approved Meta template (which carries no
            # rows at all). Pick by what the body says rather than making every one a
            # Confirm card.
            m["text"] = None
            if "how was the help" in text:
                shape, rows = "list", CSAT_ROWS
            elif "Tap Confirm" in text:
                shape, rows = "button", [{"title": "Confirm"}]
            else:
                shape, rows = "template", []
            m["interactive"] = {"type": shape, "body": {"text": text}, "rows": rows}
        msgs.append(m)

    return finish_chat(d, index, msgs, t)


def finish_chat(d, index, msgs, template):
    """Shared tail: derive the console's counters from the built messages."""
    seller = [m for m in msgs if m["author"] == "customer"]
    support = [m for m in msgs if m["author"] in ("bot", "human")]
    human = [m for m in msgs if m["author"] == "human"]
    subst = [m for m in seller if len(m["text"] or "") >= 20]
    csat_at = next((m["created_at"] for m in reversed(msgs) if m["role"] == "user"),
                   msgs[-1]["created_at"])
    nps = None
    if d.get("nps") is not None:
        nps = {"id": d["id"], "score": d["nps"], "asked_at": csat_at,
               "answered_at": csat_at, "trigger": "feedback"}
    t = template
    days = sorted({m["created_at"][:10] for m in msgs})
    from datetime import date as _date
    span = (_date.fromisoformat(days[-1]) - _date.fromisoformat(days[0])).days + 1

    return {
        "id": d["id"], "customer_id": d["wa"], "score": d["score"],
        "asked_at": csat_at, "answered_at": csat_at, "trigger": "session_close",
        "cohort": "human" if d.get("cohort") == "human" else "agentic",
        "customer_name": d["name"], "agent_name": None,
        "message_count": len(msgs), "customer_count": len(seller),
        "support_count": len(support), "human_count": len(human),
        "substantive_customer": len(subst),
        "characters": sum(len(m["text"] or "") for m in msgs),
        "first_message_at": msgs[0]["created_at"],
        "nps_n": 1 if nps else 0, "label": f"Chat {index + 1:03d}",
        "quality": "exceptional" if d["score"] >= 4 else "average",
        "messages": msgs, "nps_history": [nps] if nps else [], "nps": nps,
        "ticket": {"status": "closed", "assigned_to_me": True, "days_pending": 0,
                   "unread_count": 0},
        # seller-console extras, surfaced in the details modal
        "sop": d["sop"], "sx": d["sx"], "seller_note": d["seller_note"],
        "order_note": d["order_note"],
        # what came in, what Chanakya did about it, how it ended. Rendered as a strip
        # under the thread header so a reader sees the shape without reading the thread.
        "flow": d.get("flow"),
        "template": ({"n": t["n"], "src_id": t["src_id"], "src_name": t["src_name"],
                      "src_score": t["src_score"], "src_cohort": t["src_cohort"],
                      "days": t["days"], "starts": t["starts"], "ends": t["ends"],
                      "span_days": t["span_days"],
                      "src_starts": t["src_starts"], "src_ends": t["src_ends"]}
                     if t else
                     {"n": len(msgs), "src_id": None, "src_name": "written to the flow",
                      "src_score": None, "src_cohort": "agentic",
                      "days": len(days), "starts": days[0], "ends": days[-1],
                      "span_days": span, "src_starts": None, "src_ends": None}),
    }


def row_badges(chats):
    tag_defs = {
        "urgent_delivery": {"label": "Urgent delivery", "color": "red"},
        "promised_ship_date": {"label": "Promised ship date", "color": "orange"},
        "scattered_reply": {"label": "Scattered reply", "color": "violet"},
        "tracking_not_yet_visible": {"label": "Tracking lag", "color": "blue"},
        "payout_pending": {"label": "Payout pending", "color": "orange"},
        "size_exchange": {"label": "Size exchange", "color": "blue"},
        "order_modify": {"label": "Order modify", "color": "green"},
        "cancellation_request": {"label": "Cancellation", "color": "gray"},
        "commitment": {"label": "Commitment held", "color": "green"},
    }
    # Only where the ticket chip adds something the SOP tag doesn't. The renderer maps an
    # unknown category to "Other" and 'order' to "Price-match", neither of which means
    # anything seller-side, so those lanes get no ticket chip.
    ticket_category = {"urgent_delivery": "urgent_update",
                       "promised_ship_date": "urgent_update",
                       "scattered_reply": "urgent_update"}
    out = {}
    for c in chats:
        last = c["messages"][-1]
        out[c["customer_id"]] = {
            "control": "human" if c["human_count"] else "bot",
            "last_author": last["author"], "last_at": last["created_at"],
            "queued": False, "queuedAt": None, "waitingSince": None, "escalated": False,
            "tagKeys": [c["sop"], "commitment"],
            "ticketCategories": ([ticket_category[c["sop"]]]
                                 if c["sop"] in ticket_category else []),
        }
    return {"captured_at": max(c["messages"][-1]["created_at"] for c in chats),
            "chats": out, "tagDefs": tag_defs}


RENDER_SUBS = [
    ("m.author==='bot'?'Prithvi'", "m.author==='bot'?'Chanakya'"),
    ("title:'Prithvi replying'", "title:'Chanakya replying'"),
    # The Human-attributed and NPS tiles are dropped from the shell below, so the two
    # lines that write into them have to tolerate a missing node. Everything they compute
    # is still used by #length-summary in the details modal, so only the write is guarded.
    ("$(g+'-avg').innerHTML=mean(chats)+'<small>/ 5</small>';",
     "const avgEl=$(g+'-avg');"
     "if(avgEl)avgEl.innerHTML=chats.length?mean(chats)+'<small>/ 5</small>':"
     "'<span style=\"font-size:15px;font-weight:400;color:var(--muted)\">"
     "Not recorded</span>';"),
    ("$('nps-avg').textContent=aggregateNps===null?'Not recorded'",
     "const npsEl=$('nps-avg');if(npsEl)npsEl.textContent=aggregateNps===null?'Not recorded'"),
    ("Recorded NPS is available for ${recordedNps.length} of ${data.chats.length} customers",
     "Recorded NPS is available for ${recordedNps.length} of ${data.chats.length} sellers"),
    # The seller's SX order id belongs in the thread header. On this lane it's the only id
    # anyone can act on, and it's what the search box asks you for. The flow strip goes
    # here too: these threads are a job, not a conversation, so what came in, what Chanakya
    # did and how it ended should be readable without scrolling the transcript.
    ("<p>${groupName(c.cohort)} &middot; ${c.messages.length.toLocaleString('en-IN')} "
     "messages</p>",
     "<p><b style=\"color:var(--ink);font-weight:600\">${escapeHTML(c.sx)}</b>"
     " &middot; ${c.messages.length.toLocaleString('en-IN')} messages</p>"),
    ("</div>`;\n $('back').onclick=",
     "</div>${flowStrip(c)}`;\n $('back').onclick="),
]

# Injected ahead of the renderer. Uses the page's own variables so it themes with
# everything else.
FLOW_JS = """
function flowStrip(c){
 if(!c.flow) return '';
 const cell=(k,v)=>`<div class="flow-cell"><div class="flow-k">${k}</div>`
   +`<div class="flow-v">${escapeHTML(v)}</div></div>`;
 return `<div class="flow">${cell('In',c.flow.input)}${cell('Chanakya',c.flow.action)}`
   +`${cell('Out',c.flow.resolution)}</div>`;
}
"""

FLOW_CSS = """
.thread-head{flex-wrap:wrap}
.flow{flex-basis:100%;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));
 gap:1px;margin:12px 0 0;background:var(--line);border:1px solid var(--line);
 border-radius:8px;overflow:hidden}
.flow-cell{background:var(--bg);padding:8px 11px;min-width:0}
.flow-k{font-size:9.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);
 margin-bottom:3px}
.flow-v{font-size:12px;line-height:1.45;color:var(--ink)}
.flow-cell:nth-child(3) .flow-v{color:var(--accent,#1f6f4f)}
@media(max-width:640px){.flow{grid-template-columns:1fr}}
"""

# The two tiles the seller console has no use for. Removed from the shell rather than
# hidden, so nothing renders an empty box.
DROP_TILES = [
    '<div class="metric"><div class="metric-label"><span class="dot human"></span>'
    'Human CSAT</div><div class="metric-value" id="human-avg"></div></div>',
    '<div class="metric"><div class="metric-label">NPS</div>'
    '<div class="metric-value" id="nps-avg"></div></div>',
]

MODAL = """<h2>Sample details</h2>
<p><b>These are drafted conversations, not recorded ones.</b> Nine Chanakya seller threads,
each one copying a named real chat from <code>csat-review.html</code>: its message count,
its author at every index, and its timestamps, so the sessions, overnight gaps and
week-long silences are that conversation's, not invented. Only the words are written.
Every SX order id, seller phone number, store name, product, price, required-by date,
reliability stat and return address is real and was read GET-only from Chanakya's own
Supabase and the Meta Graph API, then checked against the live id pools. Nothing here was
sent to anyone.</p>
<table><thead><tr><th>Cohort</th><th>Chats</th><th>Rating sum</th><th>Mean</th></tr></thead>
<tbody id="method-totals"></tbody></table>
<p id="length-summary"></p>
<p><b>Which chat each draft copies, oldest first.</b> The whole set is shifted by one
delta so the newest message lands on {latest}. Each thread keeps its own start date, its
own end date and every gap in between, which is why these begin weeks apart rather than
all on the same morning.</p>
<table><thead><tr><th>Draft</th><th>Seller</th><th>Msgs</th><th>Runs</th><th>Span</th>
<th>Copied from</th></tr></thead><tbody>{template_rows}</tbody></table>
<p><b>Why these ten.</b> They were picked off a profile of all {chats} source chats to
spread the axes that actually vary: length, burstiness, how verbose the agent is, how many
days it runs over, and whether a bot carries it alone or a human teammate takes it over.
The source's own floor is {min_messages} messages with 8 each side; its lengths run {p25}
at p25, {median} at the median, {p75} at p75 and {p90} at p90. This set spans 31 to 132
messages, so it clears p75 and stops short of the p90 tail.</p>
<p><b>Ratings.</b> The source is {score5} fives and {score4} fours against {score3} threes,
{score2} twos and {score1} ones, which is where "the tone is positive" comes from. These
drafts keep to 4 and 5 deliberately.</p>
<p><b>Quality definition:</b> Exceptional = CSAT 4 or 5; average = 3; bad = 1 or 2. Rating
buckets, not independent transcript evaluations.</p>
<p><b>Attribution:</b> Agentic means the terminal CSAT carries no human agent attribution.
Drafts that copy a human-cohort template are marked human; drafts where a teammate appears
mid-thread but the rating is not theirs stay agentic, the same definition the source
uses.</p>
<p><b>Copy rules enforced.</b> Seller-facing text carries SX ids only, never a CC order
number or Relay global id (<code>lcr.check_seller_copy</code>). Plain WhatsApp text, no
markdown, under 1200 characters (<code>agent_loop/message_policy.py</code>). No em dashes
in free text. The draft that mentions a payout shows the Slack Approve/Reject card firing
first, because that word is a soft violation.</p>
<p><b>Sender.</b> Chanakya writes from {wa}, verified name Rajiv, quality GREEN.</p>
<p id="snapshot"></p>
<div class="close-row"><button class="command" data-close="method-modal">Close</button></div>"""


def scaffold(n):
    """Per-index authoring scaffold for a template: who speaks, what kind, how long the
    real message was. Used while writing chats/cNN.py."""
    t = templates.skeleton(n)
    print(f'template n={n}  src {t["src_id"]} "{t["src_name"]}"  '
          f'score {t["src_score"]} {t["src_cohort"]}  {t["days"]} days')
    print(f'codes: {t["codes"]}\n')
    day = None
    for i, s in enumerate(t["seq"]):
        if s["at"][:10] != day:
            day = s["at"][:10]
            print(f'  -- {day}')
        tag = "INTERACTIVE" if s["kind"] == "interactive" else s["kind"].upper() \
            if s["kind"] != "text" else ""
        print(f'  {i:>3}  {s["author"]:<8} {s["at"][11:]}  ~{s["src_chars"]:<4} {tag}')


def main():
    src = SOURCE.read_text(encoding="utf-8", errors="replace")

    blocks = []
    for m in re.finditer(r"<(script|style)([^>]*)>", src):
        tag, attrs = m.group(1), m.group(2)
        end = src.find(f"</{tag}>", m.end())
        blocks.append({"tag": tag, "attrs": attrs.strip(), "body": src[m.end():end]})
    styles = [b for b in blocks if b["tag"] == "style"]
    assert len(styles) == 3, f"expected 3 style blocks, found {len(styles)}"
    old_render = next(b["body"] for b in blocks if b["tag"] == "script"
                      and not b["attrs"] and "renderThread" in b["body"])

    render = re.sub(r"const customerAvatars=\{.*?\};\n?", "", old_render, flags=re.S)
    for old, new in RENDER_SUBS:
        assert old in render, f"renderer string not found, source changed: {old[:60]}"
        render = render.replace(old, new)

    chats = [(build_turns(d, i) if "turns" in d else build_chat(d, i))
             for i, d in enumerate(DRAFTS)]
    payload = {
        "generated_at": max(c["messages"][-1]["created_at"] for c in chats),
        "chats": chats, "media": {},
        "quotas": {"agentic": {}, "human": {}},
        "window": "All drafted seller-facing history through the terminal CSAT answer.",
        "source": ("Drafted words over real Chanakya identifiers (urgent_pushes, sellers, "
                   "size_exchanges, messages; read-only, ids verified). Length, author "
                   "sequence and timestamps copied per chat from csat-review.html."),
        "selection": {"minimum_messages": SOURCE_SHAPE["min_messages"],
                      "minimum_customer_messages": 8, "minimum_support_messages": 8,
                      "minimum_substantive_customer_messages": 4,
                      "sort": "Good-ending conversations first, longest first."},
        "nps_scope": "Drafted NPS, written alongside the terminal CSAT answer.",
    }
    avatars = {c["customer_id"]: avatar(c["customer_id"]) for c in chats}

    rows = "".join(
        f'<tr><td>{c["label"]}</td><td>{c["customer_name"]}</td>'
        f'<td>{c["message_count"]}</td>'
        f'<td>{c["template"]["starts"]} to {c["template"]["ends"]}</td>'
        f'<td>{c["template"]["span_days"]} days, {c["template"]["days"]} active</td>'
        f'<td>{c["template"]["src_name"]} (id {c["template"]["src_id"]}, '
        f'{c["template"]["src_cohort"]}, CSAT {c["template"]["src_score"]})</td></tr>'
        for c in sorted(chats, key=lambda x: x["template"]["starts"]))
    modal = MODAL.format(wa=CHANAKYA_WA, template_rows=rows,
                         latest=templates.LATEST, **SOURCE_SHAPE)

    html = src
    html = re.sub(r'(<script id="chat-data" type="application/json">).*?(</script>)',
                  lambda m: m.group(1) + json.dumps(payload) + m.group(2), html, flags=re.S)
    html = re.sub(r'(<script id="row-badge-data" type="application/json">).*?(</script>)',
                  lambda m: m.group(1) + json.dumps(row_badges(chats)) + m.group(2),
                  html, flags=re.S)
    html = html.replace(old_render,
                        "\nconst customerAvatars=" + json.dumps(avatars) + ";\n"
                        + FLOW_JS + render)
    html = html.replace("</head>", f"<style>{FLOW_CSS}</style></head>")
    html = html.replace("<title>prvithi transcripts</title>",
                        "<title>Chanakya seller transcripts</title>")
    html = html.replace("On customer <span", "On seller <span")
    html = html.replace('placeholder="Search by order id" aria-label="Search by order ID, '
                        'name, or message"',
                        'placeholder="Search by SX order id" aria-label="Search by SX '
                        'order id, store name, or message"')
    for tile in DROP_TILES:
        assert tile in html, f"tile markup not found, source changed: {tile[:60]}"
        html = html.replace(tile, "")
    html = html.replace("Agentic CSAT", "Chanakya CSAT")
    html = html.replace('title="Ticket allocations and unread states are demo data"',
                        'title="Ticket state is drafted alongside each conversation"')
    html = re.sub(r'(<dialog id="method-modal" class="modal">).*?(</dialog>)',
                  lambda m: m.group(1) + modal + m.group(2), html, flags=re.S)

    # In the source export nothing ever opens #method-modal: the renderer fills its
    # #method-totals / #length-summary / #snapshot and only calls showModal() on the image
    # lightbox, so the sample-details copy is computed and unreachable. This page's modal
    # carries the "these are drafts" statement and the table of what each draft copies, so
    # it needs an opener. Added with the original's own icon-button pattern.
    opener = ('<button class="icon-button" id="open-method" title="Sample details" '
              'aria-label="Sample details"><i data-lucide="info"></i></button>')
    assert '<nav><button class="icon-button" id="jump-rating"' in html
    html = html.replace('<nav><button class="icon-button" id="jump-rating"',
                        f'<nav>{opener}<button class="icon-button" id="jump-rating"')
    html = html.replace("updateList();renderThread();",
                        "$('open-method').onclick=()=>$('method-modal').showModal();\n"
                        "updateList();renderThread();")

    (HERE / "chanakya-seller-chats.html").write_text(html, encoding="utf-8")
    (HERE / "chats.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False),
                                     encoding="utf-8")

    # ---- report, and assert the drafts really are what the modal claims --------------
    print(f"{len(chats)} chats, html {len(html) / 1e6:.2f} MB\n")
    hdr = (f'{"":4} {"store":20} {"msgs":>4} {"sl":>3} {"cx":>3} {"hu":>3} '
           f'{"run":>3} {"slch":>4} {"cxch":>4} {"csat":>4}  '
           f'{"runs from":<24} span  active')
    print(hdr)
    bad = []
    for c in sorted(chats, key=lambda x: x["template"]["starts"]):
        ms = c["messages"]
        run = best = 1
        for a, b in zip(ms, ms[1:]):
            run = run + 1 if a["author"] == b["author"] else 1
            best = max(best, run)
        sl = [len(m["text"] or "") for m in ms if m["author"] == "customer"]
        cx = [len(m["text"] or "") for m in ms if m["author"] == "bot"]
        med = lambda xs: sorted(xs)[len(xs) // 2] if xs else 0
        t = c["template"]
        print(f'{c["label"][-3:]:4} {c["customer_name"]:20} '
              f'{c["message_count"]:>4} {c["customer_count"]:>3} '
              f'{len([m for m in ms if m["author"] == "bot"]):>3} {c["human_count"]:>3} '
              f'{best:>3} {med(sl):>4} {med(cx):>4} {c["score"]:>4}  '
              f'{t["starts"]} to {t["ends"]}  {t["span_days"]:>4}  {t["days"]:>4}')

        # The 30-message floor is the csat-review report's own selection rule, so it only
        # binds drafts that copy one of its chats. The order-chasing threads are short
        # deliberately: the job is input, negotiation, resolution, and padding that out to
        # 30 messages would make them worse, not more faithful.
        if c["template"]["src_id"] is not None:
            if c["message_count"] < SOURCE_SHAPE["min_messages"]:
                bad.append(f'{c["label"]} {c["message_count"]} messages, floor 30')
            if c["customer_count"] < 8:
                bad.append(f'{c["label"]} {c["customer_count"]} seller messages, floor 8')
            if c["support_count"] < 8:
                bad.append(f'{c["label"]} {c["support_count"]} support messages, floor 8')
            if c["substantive_customer"] < 4:
                bad.append(f'{c["label"]} {c["substantive_customer"]} substantive, floor 4')
        elif c["message_count"] < 6:
            bad.append(f'{c["label"]} only {c["message_count"]} messages, too thin to read')
        for m in ms:
            if m["author"] not in ("bot", "human") or not m["text"]:
                continue
            t = m["text"]
            if len(t) > 1200:
                bad.append(f'{c["label"]} {m["created_at"][:16]} over 1200 chars')
            if "—" in t:
                bad.append(f'{c["label"]} {m["created_at"][:16]} em dash in seller copy')
            if re.search(r"\*\*|__|```|^#{1,6} ", t, re.M):
                bad.append(f'{c["label"]} {m["created_at"][:16]} markdown in seller copy')
            # A bare 14-digit run is what a customer's CC order number looks like, and that
            # must never reach a seller. A courier AWB is the same shape and is perfectly
            # fine to send, so only flag digits that are NOT introduced as an AWB.
            for hit in re.finditer(r"\b\d{14}\b", t):
                lead = t[max(0, hit.start() - 24):hit.start()].lower()
                if "awb" not in lead and "tracking" not in lead:
                    bad.append(f'{c["label"]} {m["created_at"][:16]} bare 14-digit number, '
                               f"reads as a CC order id: {hit.group()}")

    lens = sorted(c["message_count"] for c in chats)
    print(f'\nlength spread: {lens}')
    print(f'source shape:  floor {SOURCE_SHAPE["min_messages"]}, p25 {SOURCE_SHAPE["p25"]}, '
          f'median {SOURCE_SHAPE["median"]}, p75 {SOURCE_SHAPE["p75"]}, '
          f'p90 {SOURCE_SHAPE["p90"]}')
    print(f'csat: {sum(1 for c in chats if c["score"] == 5)} fives, '
          f'{sum(1 for c in chats if c["score"] == 4)} fours')
    print("checks: " + ("all clean" if not bad else "FAILED"))
    for b in bad:
        print("  " + b)
    print(f'\nwrote {HERE / "chanakya-seller-chats.html"}')
    print(f'wrote {HERE / "chats.json"}')
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--scaffold":
        scaffold(int(sys.argv[2]))
    else:
        sys.exit(main())
