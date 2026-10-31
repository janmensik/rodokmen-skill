#!/usr/bin/env python3
"""Klasický strom rodiny (všichni předci, manželé, děti i boční příbuzní) z data/osoby.py jako SVG.
Použití: tree_chart.py <out_dir>                         (plakát: SVG + HTML + PNG přes Chrome)
         tree_chart.py <out_file.svg> --web <hrefs.json> (klikací SVG pro web – volá ho export_web.py)"""
import base64, html, json, os, re, shutil, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)
import fakta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "vystupy")
WEB = "--web" in sys.argv
HREFS = {int(k): v for k, v in json.load(open(sys.argv[sys.argv.index("--web") + 1])).items()} if WEB else {}
CHROME = next((c for c in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                           "C:/Program Files/Google/Chrome/Application/chrome.exe",
                           "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
                           "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
                           "google-chrome", "chromium", "chromium-browser")
               if os.path.exists(c) or shutil.which(c)), None)

ns = {}
exec(open(os.path.join(ROOT, "data", "osoby.py"), encoding="utf-8").read(), ns)
P, LINES, SIDE = ns["P"], ns.get("LINES", {}), ns.get("SIDE", [])
WEBCFG = json.load(open(os.path.join(ROOT, "data", "web.json"), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, "data", "web.json")) else {}
DOCS = json.load(open(os.path.join(ROOT, "data", "dokumenty.json"), encoding="utf-8")) if os.path.exists(os.path.join(ROOT, "data", "dokumenty.json")) else []

BASE = {8: "#EFB45F", 9: "#F09A78", 10: "#E58AA6", 11: "#B99AE0",
        12: "#86B8E8", 13: "#6FCBB9", 14: "#9CD17A", 15: "#D3D46A"}
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"

# Portrait lookup: k -> first foto_* img key
PORTRAIT = {}
for d in DOCS:
    img = d.get("img", "")
    if img.startswith("foto_"):
        for k in d.get("osoby", []):
            PORTRAIT.setdefault(k, img)


def gen(k):
    return k.bit_length() - 1


def line_of(k):
    g = gen(k)
    return k >> (g - 3) if g >= 3 else None


def canonical_pos(k):
    g = gen(k)
    return (k - (1 << g) + 0.5) / (1 << g)


def short_subtitle(facts):
    """Extract clean place / occupation subtitle from person's facts."""
    parts = []
    for f in facts:
        if f.startswith("×"):
            continue
        if f.startswith("*"):
            # Extract place after date or year if any
            m = re.match(r"^\*\s*(?:\d+\.\s*\d+\.\s*)?\d{4}\s*(.*)$", f)
            if m and m.group(1).strip():
                parts.append(m.group(1).strip())
            continue
        if f.startswith("†"):
            continue
        parts.append(f)
    return " · ".join(parts[:2])


def card_subtitle(p, is_side=False):
    """Uniform card subtitle: Povolání · Místo (Job always first, Place always second)."""
    if isinstance(p, list):
        return short_subtitle(p)
    job = p.get("zam", "")
    place = p.get("bydl", "") or fakta.birth_place(p) or p.get("puvod", "")
    vztah = p.get("vztah", "")
    parts = []
    if job:
        parts.append(job)
    if is_side and vztah and not job:
        parts.append(vztah)
    if place:
        parts.append(place)
    if not parts:
        return short_subtitle(p.get("f", []))
    return " · ".join(parts[:2])


def color_for_k(k, is_side=False):
    if k == 1:
        return "#5B4A3A"
    g = gen(k)
    if g <= 2:
        side_bit = (k >> (g - 1)) & 1
        return "#C89B6E" if side_bit == 0 else "#6E9EC8"
    ln = line_of(k)
    c = BASE.get(ln, "#B5A898")
    return c


# Build person nodes and horizontal units per generation
# Node: dict(id, name, years, sub, g, k_link, color, is_side, is_unk, photo)
# Unit: dict(id, g, nodes=[node1] or [node1, node2], sort_key, parent_unit_id, child_unit_ids, x=0.0, width=0.0)
nodes = {}
units = {}
units_by_g = {}
p_node_id = {}      # k -> node_id
p_unit_id = {}      # k -> unit_id containing k

BOX_W = 236
BOX_H = 88
COUPLE_GAP = 26
UNIT_GAP = 28
ROW_STEP = 196


def add_node(nid, name, yrs, sub, g, k_link, color, is_side=False, is_unk=False, photo=None, maiden=""):
    nodes[nid] = dict(id=nid, name=name, years=yrs, sub=sub, g=g, k_link=k_link,
                      color=color, is_side=is_side, is_unk=is_unk, photo=photo, maiden=maiden, x=0.0, y=0.0)
    return nid


def add_unit(uid, g, nids, sort_key, sibling_anchor_k=None, sib_dir=None):
    w = len(nids) * BOX_W + (len(nids) - 1) * COUPLE_GAP
    u = dict(id=uid, g=g, nodes=nids, sort_key=sort_key, width=w, x=0.0,
             children=[], parents_unit=None, sibling_of_k=None, sibling_anchor_k=sibling_anchor_k, sib_dir=sib_dir)
    units[uid] = u
    units_by_g.setdefault(g, []).append(u)
    return uid


# 1. Generation 0: check if P[1] has multiple children listed in deti or f
p1 = P[1]
deti = p1.get("deti", [])
child_matches = [re.match(r"^(.+?)\s*\((\*\s*\d{4})\)$", f.strip()) for f in p1.get("f", [])]
if deti:
    n_ch = len(deti)
    for idx, ch in enumerate(deti):
        cname = ch["n"]
        cyr = fakta.years(ch.get("y"))
        csub = card_subtitle(ch) or ("syn Jana a Julie" if ch.get("sex", "M") == "M" else "dcera Jana a Julie")
        nid = add_node(f"ch_{idx}", cname, cyr, csub, 0, 1, "#5B4A3A")
        uid = add_unit(f"u_ch_{idx}", 0, [nid], 0.5 + (idx - (n_ch - 1) / 2) * 0.001)
elif len(child_matches) >= 2 and all(child_matches):
    n_ch = len(child_matches)
    for idx, m in enumerate(child_matches):
        cname, cyr = m.group(1).strip(), m.group(2).strip()
        nid = add_node(f"ch_{idx}", cname, cyr, "dítě Jana a Julie", 0, 1, "#5B4A3A")
        uid = add_unit(f"u_ch_{idx}", 0, [nid], 0.5 + (idx - (n_ch - 1) / 2) * 0.001)
else:
    nid = add_node("p_1", p1["n"], fakta.years(p1.get("y")), card_subtitle(p1), 0, 1, "#5B4A3A")
    uid = add_unit("u_p_1", 0, [nid], 0.5)
    p_node_id[1] = nid
    p_unit_id[1] = uid

# 2. Ancestors in P (k >= 2), grouped into couple units (2m, 2m+1)
visited_couples = set()
for k in sorted(k for k in P if k >= 2):
    m = k // 2
    if m in visited_couples:
        continue
    visited_couples.add(m)
    kf, km = 2 * m, 2 * m + 1
    g = gen(kf)
    nids = []
    for kk in (kf, km):
        if kk in P:
            pk = P[kk]
            unk = pk.get("st") == "unk" or pk["n"].startswith("otec neuveden")
            maiden = pk.get("roz", "")
            nid = add_node(f"p_{kk}", pk["n"], fakta.years(pk.get("y") or fakta.birth_years(pk)), card_subtitle(pk),
                           g, kk if not unk else None, color_for_k(kk), is_unk=unk, photo=PORTRAIT.get(kk), maiden=maiden)
            p_node_id[kk] = nid
            nids.append(nid)
    skey = canonical_pos(m)
    uid = add_unit(f"u_couple_{m}", g, nids, skey)
    for kk in (kf, km):
        if kk in P:
            p_unit_id[kk] = uid

# Connect P couples to their direct child in P
for m in visited_couples:
    parent_uid = f"u_couple_{m}"
    if m == 1:
        for u in units_by_g.get(0, []):
            if u["id"].startswith(("u_ch_", "u_p_1")):
                units[parent_uid]["children"].append((u["id"], u["nodes"][0]))
                u["parents_unit"] = parent_uid
    elif m in p_node_id:
        units[parent_uid]["children"].append((p_unit_id[m], p_node_id[m]))

# 3. Side branches (SIDE)
def build_side_branch(v, g, k_anchor, skey, parent_uid=None, sibling_k=None, is_top_sibling=False, sib_dir=None, idx_tag="0"):
    name = v["n"]
    yrs = fakta.years(v.get("y") or fakta.birth_years(v))
    sub = card_subtitle(v, is_side=True)
    col = color_for_k(k_anchor, is_side=True)
    nid = add_node(f"side_{idx_tag}", name, yrs, sub, g, k_anchor, col, is_side=True, maiden=v.get("roz", ""))
    nids = [nid]
    if v.get("manzel"):
        sp = v["manzel"]
        sp_yrs = fakta.years(sp.get("y") or fakta.birth_years(sp))
        sp_sub = card_subtitle(sp, is_side=True)
        sp_id = add_node(f"side_{idx_tag}_sp", sp["n"], sp_yrs, sp_sub, g, k_anchor, col, is_side=True, maiden=sp.get("roz", ""))
        nids.append(sp_id)
    uid = add_unit(f"u_side_{idx_tag}", g, nids, skey,
                   sibling_anchor_k=k_anchor if is_top_sibling else None,
                   sib_dir=sib_dir if is_top_sibling else None)
    if parent_uid:
        units[parent_uid]["children"].append((uid, nid))
        units[uid]["parents_unit"] = parent_uid
    elif sibling_k:
        units[uid]["sibling_of_k"] = (sibling_k, nid)
    deti = v.get("deti", [])
    for ci, ch in enumerate(deti):
        ch_offset = (ci - (len(deti) - 1) / 2) * 0.002
        build_side_branch(ch, g - 1, k_anchor, skey + ch_offset, parent_uid=uid, is_top_sibling=False, idx_tag=f"{idx_tag}_{ci}")


side_by_k = {}
for s in SIDE:
    side_by_k.setdefault(s["k"], []).append(s)

for k_anchor, slist in sorted(side_by_k.items()):
    if k_anchor not in P:
        continue
    g_anchor = gen(k_anchor)
    m_couple = k_anchor // 2
    base_key = canonical_pos(m_couple) if k_anchor >= 2 else 0.5
    has_desc = any((s.get("vetev") or {}).get("deti") for s in slist)
    # If a sibling branch has descendants in row g-1, place it on the outer side of m_couple in row g-1
    # (left if m_couple is even, right if m_couple is odd) so parent and child rows have identical order!
    if has_desc and m_couple >= 2:
        direction = -1 if (m_couple % 2 == 0) else 1
        dist_mult = 2 if (k_anchor % 2 != m_couple % 2) else 1
    else:
        direction = -1 if (k_anchor % 2 == 0) else 1
        dist_mult = 1
    step = 0.015 / (1 << max(0, g_anchor - 2))
    parent_m = k_anchor
    parent_couple_uid = f"u_couple_{parent_m}" if parent_m in visited_couples else None
    for si, s in enumerate(slist):
        v = s.get("vetev")
        if not v:
            m = re.match(r"^(.+?)\s*\(([^)]+)\)$", s["n"].strip())
            v = dict(n=m.group(1).strip() if m else s["n"], y=m.group(2).strip() if m else "", sub=s.get("t", "")[:38])
        skey = base_key + direction * (dist_mult + si * 0.4) * step
        build_side_branch(v, g_anchor, k_anchor, skey,
                          parent_uid=parent_couple_uid,
                          sibling_k=k_anchor if not parent_couple_uid else None,
                          is_top_sibling=True,
                          sib_dir=direction,
                          idx_tag=f"{k_anchor}_{si}")

# 4. Sort each generation row by sort_key and compute non-overlapping horizontal positions
max_g = max(units_by_g)
for g in range(max_g + 1):
    units_by_g.setdefault(g, [])
    units_by_g[g].sort(key=lambda u: u["sort_key"])

# Initial layout: space each row centered around 0
for g, ulist in units_by_g.items():
    total_w = sum(u["width"] for u in ulist) + max(0, len(ulist) - 1) * UNIT_GAP
    cur = -total_w / 2
    for u in ulist:
        u["x"] = cur + u["width"] / 2
        cur += u["width"] + UNIT_GAP


def resolve_overlaps(ulist):
    """Symmetric 1D block-merge (VPSC) overlap resolution: preserves the center of mass of every colliding group."""
    if len(ulist) <= 1:
        return
    blocks = []
    for i, u in enumerate(ulist):
        blocks.append([i, i, [0.0], u["x"], 1])
        while len(blocks) >= 2:
            b1, b2 = blocks[-2], blocks[-1]
            x1_base = b1[3] / b1[4]
            x2_base = b2[3] / b2[4]
            u_last = ulist[b1[1]]
            u_first = ulist[b2[0]]
            min_d = (u_last["width"] + u_first["width"]) / 2 + UNIT_GAP
            actual_d = x2_base - (x1_base + b1[2][-1])
            if actual_d >= min_d:
                break
            blocks.pop()
            base_off = b1[2][-1] + min_d
            for off in b2[2]:
                b1[2].append(base_off + off)
            for j in range(b2[0], b2[1] + 1):
                b1[3] += ulist[j]["x"] - b1[2][j - b1[0]]
            b1[1] = b2[1]
            b1[4] += b2[4]
    for start_i, end_i, offsets, sum_d, cnt in blocks:
        base_x = sum_d / cnt
        for idx, off in enumerate(offsets):
            ulist[start_i + idx]["x"] = base_x + off


def place_siblings(ulist):
    by_couple_dir = {}
    for u in ulist:
        if u["sibling_anchor_k"]:
            anc_uid = p_unit_id.get(u["sibling_anchor_k"])
            if anc_uid:
                d = u["sib_dir"] or (-1 if (u["sibling_anchor_k"] % 2 == 0) else 1)
                by_couple_dir.setdefault((anc_uid, d), []).append(u)
    for (anc_uid, dir_sign), sib_units in by_couple_dir.items():
        anc_u = units[anc_uid]
        if dir_sign > 0:
            cur_edge = anc_u["x"] + anc_u["width"] / 2 + UNIT_GAP
            for su in sib_units:
                su["x"] = cur_edge + su["width"] / 2
                cur_edge += su["width"] + UNIT_GAP
        else:
            cur_edge = anc_u["x"] - anc_u["width"] / 2 - UNIT_GAP
            for su in reversed(sib_units):
                su["x"] = cur_edge - su["width"] / 2
                cur_edge -= su["width"] + UNIT_GAP


def sync_node_positions():
    for g, ulist in units_by_g.items():
        y = (max_g - g) * ROW_STEP + 240
        for u in ulist:
            nids = u["nodes"]
            if len(nids) == 1:
                nodes[nids[0]]["x"] = u["x"]
                nodes[nids[0]]["y"] = y
            else:
                nodes[nids[0]]["x"] = u["x"] - (BOX_W + COUPLE_GAP) / 2
                nodes[nids[0]]["y"] = y
                nodes[nids[1]]["x"] = u["x"] + (BOX_W + COUPLE_GAP) / 2
                nodes[nids[1]]["y"] = y


# Iterative relaxation (bottom-up + top-down, anchored on starting point in the center)
for it in range(120):
    sync_node_positions()
    # 1. Bottom-up: align ancestor couples above their children (with gentle pull toward their own parents),
    #    then place top-level siblings right next to their anchor couple BEFORE resolving overlaps
    for g in range(1, max_g + 1):
        ulist = units_by_g[g]
        for u in ulist:
            if u["id"].startswith("u_couple_"):
                m = int(u["id"].split("_")[-1])
                if m == 1:
                    cxs = [nodes[cid]["x"] for _, cid in u["children"]]
                elif m in p_node_id:
                    cxs = [nodes[p_node_id[m]]["x"]]
                else:
                    cxs = [nodes[cid]["x"] for _, cid in u["children"]]
                pxs = [units[f"u_couple_{kk}"]["x"] for kk in (2 * m, 2 * m + 1) if f"u_couple_{kk}" in units]
                if cxs and pxs:
                    u["x"] = 0.65 * (sum(cxs) / len(cxs)) + 0.35 * (sum(pxs) / len(pxs))
                elif cxs:
                    u["x"] = sum(cxs) / len(cxs)
        place_siblings(ulist)
        resolve_overlaps(ulist)
        sync_node_positions()

    # 2. Top-down: align couples between their parents and children, and place descendant units under their parents
    for g in range(max_g - 1, -1, -1):
        ulist = units_by_g[g]
        for u in ulist:
            if u["id"].startswith("u_couple_"):
                m = int(u["id"].split("_")[-1])
                if m == 1:
                    cxs = [nodes[cid]["x"] for _, cid in u["children"]]
                elif m in p_node_id:
                    cxs = [nodes[p_node_id[m]]["x"]]
                else:
                    cxs = [nodes[cid]["x"] for _, cid in u["children"]]
                pxs = [units[f"u_couple_{kk}"]["x"] for kk in (2 * m, 2 * m + 1) if f"u_couple_{kk}" in units]
                if pxs and cxs:
                    u["x"] = 0.55 * (sum(cxs) / len(cxs)) + 0.45 * (sum(pxs) / len(pxs))
        by_parent = {}
        for u in ulist:
            if u["parents_unit"] and not u["id"].startswith("u_couple_") and not u["sibling_anchor_k"]:
                by_parent.setdefault(u["parents_unit"], []).append(u)
        for puid, ch_units in by_parent.items():
            px = units[puid]["x"]
            tot_w = sum(cu["width"] for cu in ch_units) + max(0, len(ch_units) - 1) * UNIT_GAP
            cur = px - tot_w / 2
            for cu in ch_units:
                cu["x"] = cur + cu["width"] / 2
                cur += cu["width"] + UNIT_GAP
        place_siblings(ulist)
        resolve_overlaps(ulist)
        sync_node_positions()

    # Keep starting point (Kryštof, Tea, Hynek a Jonáš Menšíkovi) anchored at x = 0
    anchor_x = units["u_p_1"]["x"] if "u_p_1" in units else units["u_couple_1"]["x"]
    for u in units.values():
        u["x"] -= anchor_x
    sync_node_positions()

sync_node_positions()

# Compute canvas bounds with dedicated left margin for generation labels
all_left = min(n["x"] - BOX_W / 2 for n in nodes.values())
all_right = max(n["x"] + BOX_W / 2 for n in nodes.values())
PAD_LEFT = 370
PAD_RIGHT = 120
SHIFT_X = PAD_LEFT - all_left
for u in units.values():
    u["x"] += SHIFT_X
sync_node_positions()

W = int(all_right - all_left + PAD_LEFT + PAD_RIGHT)
H = (max_g + 1) * ROW_STEP + 380

# Helper for embedding portrait image
def portrait_href(img_key):
    if WEB:
        base = os.environ.get("BASE_URL", "/rodokmen").rstrip("/")
        prefix = f"{base}/" if base else "/"
        return f"{prefix}img/{img_key}.jpg"
    p = os.path.join(ROOT, "vyrezy", img_key + ".jpg")
    if os.path.exists(p):
        b64 = base64.b64encode(open(p, "rb").read()).decode("ascii")
        return f"data:image/jpeg;base64,{b64}"
    return ""


# Render SVG elements
defs, bg_bands, conn_lines, card_groups = [], [], [], []

GEN_LABELS = {
    0: "0. generace – děti a vnoučata",
    1: "1. generace – rodiče, sourozenci a bratranci",
    2: "2. generace – prarodiče a tety",
    3: "3. generace – praprarodiče",
    4: "4. generace – prapraprarodiče",
    5: "5. generace – 4× prarodiče",
    6: "6. generace – 5× prarodiče",
    7: "7. generace – 6× prarodiče",
    8: "8. generace – 7× prarodiče",
}

for g in range(max_g + 1):
    y_center = (max_g - g) * ROW_STEP + 240
    band_y = y_center - BOX_H / 2 - 18
    band_h = BOX_H + 36
    bg = "#F5F0E6" if g % 2 == 0 else "#EFE9DC"
    bg_bands.append(f'<rect x="40" y="{band_y:.1f}" width="{W - 80}" height="{band_h:.1f}" rx="14" fill="{bg}" opacity="0.65"/>')
    lbl = GEN_LABELS.get(g, f"{g}. generace")
    bg_bands.append(f'<text x="68" y="{band_y + 26:.1f}" font-size="15" font-weight="600" fill="#8C7B68" letter-spacing="1">{html.escape(lbl.upper())}</text>')

# Draw marriage connectors and parent-child orthogonal lines
for g in range(max_g + 1):
    ulist = units_by_g[g]
    # Marriage symbols inside 2-node units
    for u in ulist:
        if len(u["nodes"]) == 2:
            n0, n1 = nodes[u["nodes"][0]], nodes[u["nodes"][1]]
            mx = (n0["x"] + BOX_W / 2 + n1["x"] - BOX_W / 2) / 2
            my = n0["y"]
            conn_lines.append(f'<line x1="{n0["x"] + BOX_W / 2:.1f}" y1="{my:.1f}" x2="{n1["x"] - BOX_W / 2:.1f}" y2="{my:.1f}" stroke="#8C7A66" stroke-width="2.5"/>')
            conn_lines.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="11" fill="#FBF8F2" stroke="#8C7A66" stroke-width="1.8"/>')
            conn_lines.append(f'<text x="{mx:.1f}" y="{my + 4.5:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="#6E5D4B">∞</text>')

    # Parent -> children busbars between row g and row g-1
    fams = [u for u in ulist if u["children"]]
    # Assign non-overlapping busbar levels for overlapping horizontal spans
    spans = []
    for u in fams:
        px = u["x"]
        cxs = [nodes[cid]["x"] for _, cid in u["children"]]
        xmin, xmax = min([px] + cxs), max([px] + cxs)
        level = 0
        while any(l == level and not (xmax < a - 15 or xmin > b + 15) for a, b, l in spans):
            level += 1
        spans.append((xmin, xmax, level))
        y_parent = nodes[u["nodes"][0]]["y"]
        y_start = y_parent if len(u["nodes"]) == 2 else y_parent + BOX_H / 2
        y_child_top = nodes[u["children"][0][1]]["y"] - BOX_H / 2
        y_bus = y_parent + BOX_H / 2 + 28 + level * 12
        y_bus = min(y_bus, y_child_top - 14)
        stroke = "#7A6A58" if u["id"].startswith("u_couple_") else "#9A8B7A"
        sw = "2.4" if u["id"].startswith("u_couple_") else "2.0"
        conn_lines.append(f'<line x1="{px:.1f}" y1="{y_start:.1f}" x2="{px:.1f}" y2="{y_bus:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        if xmax - xmin > 1:
            conn_lines.append(f'<line x1="{xmin:.1f}" y1="{y_bus:.1f}" x2="{xmax:.1f}" y2="{y_bus:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        for _, cid in u["children"]:
            cx = nodes[cid]["x"]
            conn_lines.append(f'<line x1="{cx:.1f}" y1="{y_bus:.1f}" x2="{cx:.1f}" y2="{y_child_top:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')

    # Sibling bridges where parents are not in P (e.g. Eva Čákiová & Iva Gajdošová)
    for u in ulist:
        if u["sibling_of_k"]:
            sk, s_nid = u["sibling_of_k"]
            if sk in p_node_id:
                n_a = nodes[p_node_id[sk]]
                n_b = nodes[s_nid]
                y_top = n_a["y"] - BOX_H / 2
                y_br = y_top - 18
                conn_lines.append(f'<path d="M{n_a["x"]:.1f},{y_top:.1f} L{n_a["x"]:.1f},{y_br:.1f} L{n_b["x"]:.1f},{y_br:.1f} L{n_b["x"]:.1f},{y_top:.1f}" '
                                  f'fill="none" stroke="#9A8B7A" stroke-width="2" stroke-dasharray="5,4"/>')

# Draw person cards
for nid, n in nodes.items():
    x0 = n["x"] - BOX_W / 2
    y0 = n["y"] - BOX_H / 2
    col = n["color"]
    bg_card = "#5B4A3A" if n["g"] == 0 and not n["is_side"] else ("#F4F1EA" if n["is_unk"] else ("#FCF9F4" if n["is_side"] else "#FFFFFF"))
    fg_name = "#FFF8EE" if n["g"] == 0 and not n["is_side"] else ("#8A8278" if n["is_unk"] else "#1F1A15")
    fg_yr = "#F1E3CF" if n["g"] == 0 and not n["is_side"] else "#5C5146"
    fg_sub = "#E2D3BE" if n["g"] == 0 and not n["is_side"] else "#7A6E62"
    stroke_card = "#433528" if n["g"] == 0 and not n["is_side"] else ("#C8C0B4" if n["is_side"] else "#D6CEC2")
    dash = ' stroke-dasharray="5,3"' if n["is_side"] else ""

    photo_svg = ""
    tx = x0 + 18
    avail_w = BOX_W - 28
    if n["photo"]:
        ph_url = portrait_href(n["photo"])
        if ph_url:
            clip_id = f"clip_{nid}"
            defs.append(f'<clipPath id="{clip_id}"><rect x="{x0 + 14:.1f}" y="{y0 + 12:.1f}" width="52" height="64" rx="8"/></clipPath>')
            photo_svg = (f'<image href="{ph_url}" x="{x0 + 14:.1f}" y="{y0 + 12:.1f}" width="52" height="64" '
                         f'preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip_id})"/>'
                         f'<rect x="{x0 + 14:.1f}" y="{y0 + 12:.1f}" width="52" height="64" rx="8" fill="none" stroke="#D6CEC2" stroke-width="1"/>')
            tx = x0 + 76
            avail_w = BOX_W - 86

    name = n["name"]
    yrs = n["years"]
    sub = n["sub"]
    maiden = n.get("maiden", "")
    yrs_disp = f"{yrs} · roz. {maiden}" if maiden and yrs else (f"roz. {maiden}" if maiden else yrs)
    if len(sub) > 34:
        sub = sub[:32] + "…"
    fs_name = min(16.5, max(12.5, avail_w / (0.58 * max(len(name), 1))))
    italic = ' font-style="italic"' if n["is_unk"] else ""

    inner = [
        f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{BOX_W}" height="{BOX_H}" rx="10" fill="{bg_card}" stroke="{stroke_card}" stroke-width="1.6"{dash}/>',
        f'<rect x="{x0:.1f}" y="{y0:.1f}" width="7" height="{BOX_H}" rx="3.5" fill="{col}"/>',
        photo_svg,
        f'<text x="{tx:.1f}" y="{y0 + 30:.1f}" font-size="{fs_name:.1f}" font-weight="700" fill="{fg_name}"{italic}>{html.escape(name)}</text>',
    ]
    if yrs_disp:
        fs_yr = 12 if len(yrs_disp) > 18 else 13.5
        inner.append(f'<text x="{tx:.1f}" y="{y0 + 51:.1f}" font-size="{fs_yr}" font-weight="500" fill="{fg_yr}">{html.escape(yrs_disp)}</text>')
    if sub:
        inner.append(f'<text x="{tx:.1f}" y="{y0 + 70:.1f}" font-size="12" fill="{fg_sub}">{html.escape(sub)}</text>')

    href_url = HREFS.get(n["k_link"]) if WEB and n["k_link"] else None
    title_name = f'{name}{f" (roz. {maiden})" if maiden else ""}'
    title_txt = f'{title_name} {yrs} {sub}'.strip()
    if href_url:
        card_groups.append(f'<a href="{href_url}" class="tree-card"><title>{html.escape(title_txt)}</title>{"".join(inner)}</a>')
    else:
        card_groups.append(f'<g class="tree-card"><title>{html.escape(title_txt)}</title>{"".join(inner)}</g>')

total_people = sum(1 for n in nodes.values() if not n["is_unk"])
title_svg = (
    f'<text x="{W / 2:.1f}" y="95" text-anchor="middle" font-family="Georgia, \'Times New Roman\', serif" font-size="64" fill="#3B2E22">'
    f'{html.escape(WEBCFG.get("nazev", "Rodokmen"))} – kompletní strom rodiny</text>'
    f'<text x="{W / 2:.1f}" y="145" text-anchor="middle" font-size="24" fill="#6B5A48">'
    f'{total_people} členů rodiny v {max_g + 1} generacích (přímí předci, manželé, děti, sourozenci, tety, strýcové a bratranci)</text>'
)
footer_svg = (
    f'<text x="{W / 2:.1f}" y="{H - 40}" text-anchor="middle" font-size="20" fill="#7A6B5B">'
    f'Plný rámeček = přímá linie a děti · Přerušovaný rámeček = boční příbuzní a jejich rodiny · ∞ = manželství / partnerství</text>'
)

if WEB:
    web_svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 160 {W} {H - 160}" font-family="{FONT}" class="fan tree-svg">'
        f'<defs>{"".join(defs)}</defs>'
        f'{"".join(bg_bands)}{"".join(conn_lines)}<g class="fan-links">{"".join(card_groups)}</g>{footer_svg}</svg>'
    )
    open(OUT, "w", encoding="utf-8").write(web_svg)
    print(OUT, len(card_groups), "osob ve stromu")
    sys.exit(0)

full_svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">'
    f'<rect width="{W}" height="{H}" fill="#FBF8F2"/><defs>{"".join(defs)}</defs>'
    f'{title_svg}{"".join(bg_bands)}{"".join(conn_lines)}{"".join(card_groups)}{footer_svg}</svg>'
)
os.makedirs(OUT, exist_ok=True)
svg_path = os.path.join(OUT, "rodokmen_strom.svg")
html_path = os.path.join(OUT, "rodokmen_strom.html")
png_path = os.path.join(OUT, "rodokmen_strom.png")
open(svg_path, "w", encoding="utf-8").write(full_svg)
open(html_path, "w", encoding="utf-8").write(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#FBF8F2}}</style>{full_svg}')
if CHROME:
    prof = tempfile.mkdtemp(prefix="treechart-")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={prof}",
                    "--force-device-scale-factor=1", f"--window-size={W},{H}", f"--screenshot={png_path}",
                    __import__("pathlib").Path(html_path).as_uri()], check=True, capture_output=True, timeout=120)
    shutil.rmtree(prof, ignore_errors=True)
    print(png_path, total_people, "osob v", max_g + 1, "generacích")
else:
    print(svg_path, total_people, "osob")
