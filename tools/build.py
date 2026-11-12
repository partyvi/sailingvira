"""Build the static site from content/ into site/.

Usage: python3 tools/build.py [repo_dir]

Pages:
  /                 English home        /ua/              Ukrainian home
  /<project>/       English project     /ua/<project>/    Ukrainian project
plus sitemap.xml, robots.txt, 404.html and assets/.

All links between pages are relative, so the site works both at
https://sailingvira.com/ and at a GitHub Pages sub-path.

Story body format: see CLAUDE.md.
"""
import hashlib, html, json, os, re, shutil, sys
import yaml, markdown

B = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = f"{B}/site"
LANGS = ["en", "ua"]
HTML_LANG = {"en": "en", "ua": "uk"}  # ISO code for Ukrainian is "uk"; folders and URLs use "ua"

UI = {
    "en": {"all": "All projects", "prev": "Previous", "next": "Next", "photos": "photos", "posts": "diary posts",
           "days": "work days", "years": "Texas", "projects": "projects", "day": "Day", "diary": "Diary",
           "page": "Story page", "story_page": "Story page", "open": "Open photo", "close": "Close",
           "blog": "Diary on Blogger", "missing": "", "notfound": "Page not found",
           "notfound_text": "This page does not exist. Go to all projects.",
           "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]},
    "ua": {"all": "Усі проєкти", "prev": "Попередній", "next": "Наступний", "photos": "фото", "posts": "записів у щоденнику",
           "days": "робочих днів", "years": "Техас", "projects": "проєкти", "day": "День", "diary": "Щоденник",
           "page": "Сторінка", "story_page": "Сторінка історії", "open": "Відкрити фото", "close": "Закрити",
           "blog": "Щоденник на Blogger",
           "missing": "Український переклад цієї історії ще готується. Поки що текст англійською.",
           "notfound": "Сторінку не знайдено", "notfound_text": "Такої сторінки немає. Перейдіть до всіх проєктів.",
           "months": ["січ", "лют", "бер", "кві", "тра", "чер", "лип", "сер", "вер", "жов", "лис", "гру"]},
}

# ---------------------------------------------------------------- data
site = yaml.safe_load(open(f"{B}/content/site.yml", encoding="utf-8"))
BASE = site["base_url"].rstrip("/")
sec = json.load(open(f"{B}/data/sections.json"))
POSTS = {}  # diary url -> (date, title, is_page)
for v in sec.values():
    POSTS.setdefault(v["url"], (v["date"], v["ptitle"].strip(), v["kind"] == "page"))

IMG = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)\)\s*$")
SRC = re.compile(r"^(Diary|Story page):\s*(.*)$")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
esc = html.escape


def size(url, s):
    """Blogger photo URL at another size (s1600 = big, w600 = grid)."""
    url = re.sub(r"/[swh]\d+[^/]*/([^/]+)$", rf"/{s}/\1", url)
    return re.sub(r"=[swh]\d+[^/]*$", f"={s}", url)


def daynums(t):
    out = []
    for m in re.finditer(r"Days?\s*#?\s*(\d{1,3})(?![\d/])((?:\s*[-,]\s*\d{1,3}(?![\d/]))*)", t):
        out.append(int(m.group(1)))
        out += [int(x) for x in re.findall(r"\d{1,3}", m.group(2))]
    return out


def inline(text):
    def short(m):  # bare URL -> short link text
        u = m.group(1); t = re.sub(r"^https?://(www\.)?", "", u)
        return f"[{t[:48] + '…' if len(t) > 52 else t}]({u})"
    text = re.sub(r"(?<![(<\"\]])(https?://[^\s<)]+[^\s<).,;])", short, text)
    h = markdown.markdown(text)
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)
    return re.sub(r"^<p>(.*)</p>$", r"\1", h, flags=re.S)


def read_md(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, txt)


def parse_body(body):
    """Body -> (intro blocks, chapters). Blocks: {"p"}, {"ul"}, {"g": [urls], "src": [links]}."""
    intro, chapters, cur, para = [], [], None, []

    def target():
        return cur["blocks"] if cur else intro

    def flush():
        if para:
            target().append({"p": inline(" ".join(para))}); para.clear()

    for raw in body.split("\n"):
        ln = raw.strip()
        if not ln:
            flush(); continue
        if ln.startswith("## "):
            flush(); cur = {"h": ln[3:].strip(), "blocks": [], "links": []}; chapters.append(cur); continue
        m = IMG.match(ln)
        if m:
            flush(); t = target()
            if not (t and "g" in t[-1] and not t[-1]["src"]):
                t.append({"g": [], "src": []})
            t[-1]["g"].append((m.group(2), m.group(1).strip())); continue
        m = SRC.match(ln)
        if m:
            flush()
            links = [{"label": a, "url": u, "page": m.group(1) == "Story page"} for a, u in LINK.findall(m.group(2))]
            t = target()
            if t and "g" in t[-1] and not t[-1]["src"]:
                t[-1]["src"] = links
            else:
                t.append({"g": [], "src": links})
            if cur:
                cur["links"] += [l["url"] for l in links]
            continue
        if ln.startswith("- "):
            flush(); t = target()
            if not (t and "ul" in t[-1]):
                t.append({"ul": []})
            t[-1]["ul"].append(inline(ln[2:])); continue
        para.append(ln)
    flush()
    return intro, chapters


def load_projects(lang):
    d = f"{B}/content/{lang}/projects"
    out = {}
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            meta, body = read_md(f"{d}/{fn}")
            intro, chapters = parse_body(body)
            out[fn[:-3]] = {"meta": meta, "intro": intro, "chapters": chapters}
    return out


sections = sorted(yaml.safe_load(open(f"{B}/content/sections.yml", encoding="utf-8")), key=lambda s: s["order"])
P = {lang: load_projects(lang) for lang in LANGS}
EN = P["en"]
order = []  # project ids in site order
for s in sections:
    order += [pid for pid, p in sorted(EN.items(), key=lambda x: x[1]["meta"].get("order", 99))
              if p["meta"].get("section") == s["id"]]


# ---------------------------------------------------------------- helpers
def fmt(d, lang):
    return f"{int(d[8:])} {UI[lang]['months'][int(d[5:7]) - 1]} {d[:4]}"


def span(a, b, lang):
    if not a:
        return ""
    if a == b:
        return fmt(a, lang)
    if a[:7] == b[:7]:
        return f"{int(a[8:])}–{fmt(b, lang)}"
    if a[:4] == b[:4]:
        return f"{fmt(a, lang)[:-5]} – {fmt(b, lang)}"
    return f"{fmt(a, lang)} – {fmt(b, lang)}"


def month_span(a, b, lang):
    f = lambda d: f"{UI[lang]['months'][int(d[5:7]) - 1]} {d[:4]}"
    return f(a) if f(a) == f(b) else f"{f(a)} – {f(b)}"


def url_of(lang, pid=None):
    """Site-relative path, e.g. 'uk/fuel/'."""
    return ("ua/" if lang == "ua" else "") + (f"{pid}/" if pid else "")


def text(v, lang):
    if isinstance(v, dict):
        return v.get(lang) or v.get("en") or ""
    return v or ""


def project(pid, lang):
    """Project in this language, falling back to English. Returns (data, translated?)."""
    p = P[lang].get(pid)
    if p and p["chapters"]:
        en_meta = EN[pid]["meta"]
        meta = {**en_meta, **{k: v for k, v in p["meta"].items() if v}}
        return {**p, "meta": meta}, True
    return EN[pid], lang == "en"


def photos_of(p):
    return [u for c in p["chapters"] for b in c["blocks"] if "g" in b for u, _ in b["g"]]


def chapter_info(c):
    info = [POSTS[u] for u in c["links"] if u in POSTS]
    dates = sorted(d for d, _, _ in info)
    days = sorted({n for _, t, page in info if not page for n in daynums(t)})
    return (dates[0], dates[-1]) if dates else (None, None), days


def src_html(links, lang):
    out = []
    for l in links:
        known = POSTS.get(l["url"])
        if l["page"]:
            label = f"{UI[lang]['story_page']} · {esc(l['label'])}"
        else:
            label = f"{UI[lang]['diary']} · {fmt(known[0], lang) if known else esc(l['label'])}"
        out.append(f'<a href="{esc(l["url"])}" target="_blank" rel="noopener">{label} ↗</a>')
    return '<div class="src mono">' + "".join(out) + "</div>"


def blocks_html(blocks, lang, alt):
    h = []
    for b in blocks:
        if "p" in b:
            h.append(f"<p>{b['p']}</p>")
        elif "ul" in b:
            h.append("<ul>" + "".join(f"<li>{x}</li>" for x in b["ul"]) + "</ul>")
        else:
            n = len(b["g"])
            if n:
                cls = " n1" if n == 1 else " n2" if n == 2 else ""
                h.append(f'<div class="gal{cls}">' + "".join(
                    f'<button data-big="{esc(size(u, "s1600"))}" aria-label="{UI[lang]["open"]}">'
                    f'<img src="{esc(size(u, "w600"))}" loading="lazy" alt="{esc(a or alt)}"></button>' for u, a in b["g"]) + "</div>")
            if b["src"]:
                h.append(src_html(b["src"], lang))
    return "\n".join(h)


ASSET_V = hashlib.md5((open(f"{B}/tools/assets/style.css", "rb").read() +
                       open(f"{B}/tools/assets/app.js", "rb").read())).hexdigest()[:8]
FONTS = ("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Source+Serif+4:ital,"
         "opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap")


def page(path, lang, pid, title, desc, body, image="", lightbox=False):
    depth = path.count("/")
    rel = "../" * depth
    alts = "".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{BASE}/{url_of(l, pid)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{BASE}/{url_of("en", pid)}">'
    robots = '<meta name="robots" content="noindex, nofollow">' if site.get("noindex") else ""
    lang_links = "".join(
        f'<a href="{rel}{url_of(l, pid)}" hreflang="{HTML_LANG[l]}"{" aria-current=page" if l == lang else ""}>{ {"en": "EN", "ua": "УКР"}[l]}</a>'
        for l in LANGS)
    og_img = f'<meta property="og:image" content="{esc(size(image, "w1200"))}">' if image else ""
    lb = ""
    if lightbox:
        lb = (f'<div class="lb" id="lb" hidden><img id="lbimg" alt=""><div class="bar"><span id="lbcap"></span>'
              f'<span class="ctl"><button id="lbprev" aria-label="{UI[lang]["prev"]}">←</button>'
              f'<button id="lbnext" aria-label="{UI[lang]["next"]}">→</button>'
              f'<button id="lbclose">{UI[lang]["close"]}</button></span></div></div>'
              f'<script src="{rel}assets/app.js?v={ASSET_V}"></script>')
    doc = f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{BASE}/{url_of(lang, pid)}">{alts}
<meta property="og:type" content="article"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{BASE}/{url_of(lang, pid)}">{og_img}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{rel}assets/style.css?v={ASSET_V}">
</head>
<body>
<div class="wrap">
<header class="sitebar"><a class="brand" href="{rel}{url_of(lang)}">{esc(site["name"])}</a>
<nav><a href="{rel}{url_of(lang)}">{UI[lang]["all"]}</a><span class="lang">{lang_links}</span></nav></header>
{body}
<footer class="foot mono"><a href="{esc(site["blog_url"])}" target="_blank" rel="noopener">{UI[lang]["blog"]} ↗</a>
<span>© {esc(site["name"])}</span></footer>
</div>
{lb}
</body>
</html>
"""
    os.makedirs(os.path.dirname(f"{OUT}/{path}") or OUT, exist_ok=True)
    open(f"{OUT}/{path}", "w", encoding="utf-8").write(doc)


# ---------------------------------------------------------------- build
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f"{OUT}/assets")
for f in os.listdir(f"{B}/tools/assets"):
    shutil.copy(f"{B}/tools/assets/{f}", f"{OUT}/assets/{f}")

posts = {(v["date"], v["ptitle"]) for v in sec.values() if v["kind"] == "post"}
stats = {"posts": len(posts), "photos": sum(len(photos_of(EN[p])) for p in order),
         "first": min(p[0] for p in posts)[:4], "last": max(p[0] for p in posts)[:4],
         "days": max(d for p in posts for d in (daynums(p[1]) or [0]))}

for lang in LANGS:
    ui = UI[lang]
    # -- project pages
    for i, pid in enumerate(order):
        p, translated = project(pid, lang)
        m = p["meta"]
        s = next(x for x in sections if x["id"] == m.get("section"))
        group = text(s["title"], lang)
        title, blurb = m.get("title", pid), m.get("description", "")
        toc, body = [], []
        if p["intro"]:
            body.append('<div class="intro">' + blocks_html(p["intro"], lang, title) + "</div>")
        for ci, c in enumerate(p["chapters"]):
            (a, b), days = chapter_info(c)
            log = (f'<span>{ui["day"]} {days[0] if days[0] == days[-1] else f"{days[0]}–{days[-1]}"}</span>' if days
                   else f'<span>{ui["story_page"]}</span>') + (f"<span>{span(a, b, lang)}</span>" if a else "")
            toc.append(f'<a href="#c{ci + 1}">{esc(c["h"])}</a>')
            body.append(f'<section class="chap" id="c{ci + 1}"><h2>{esc(c["h"])}</h2><div class="log mono">{log}</div>\n'
                        + blocks_html(c["blocks"], lang, f"{title}: {c['h']}") + "</section>")
        prev, nxt = (order[i - 1] if i else None), (order[i + 1] if i + 1 < len(order) else None)
        nav = '<nav class="pnav">' + (
            f'<a href="../{prev}/"><span class="mono">← {ui["prev"]}</span><b>{esc(project(prev, lang)[0]["meta"]["title"])}</b></a>'
            if prev else "<span></span>") + (
            f'<a href="../{nxt}/"><span class="mono">{ui["next"]} →</span><b>{esc(project(nxt, lang)[0]["meta"]["title"])}</b></a>'
            if nxt else "") + "</nav>"
        note = "" if translated else f'<p class="note">{ui["missing"]}</p>'
        head = (f'<header class="phead"><span class="eyebrow">{esc(group)}</span><h1>{esc(title)}</h1>'
                f'<p>{esc(blurb)}</p>{note}</header>')
        html_body = (head + f'<div class="layout"><div class="story">' + "\n".join(body) + "</div>"
                     f'<aside class="toc">{"".join(toc)}</aside></div>' + nav)
        photos = photos_of(p)
        page(url_of(lang, pid) + "index.html", lang, pid, f"{title} · {site['name']}", blurb, html_body,
             m.get("cover") or (photos[-1] if photos else ""), lightbox=True)

    # -- home
    h = site["home"]
    parts = [f'<header class="mast"><span class="eyebrow">{esc(text(h["eyebrow"], lang))}</span>'
             f'<h1>{esc(text(h["title"], lang))}</h1><p>{esc(text(h["intro"], lang))}</p>'
             f'<div class="stats mono"><span><b>{stats["posts"]}</b>{ui["posts"]}</span>'
             f'<span><b>{stats["days"]}</b>{ui["days"]}</span>'
             f'<span><b>{stats["photos"]:,}</b>{ui["photos"]}</span>'.replace(",", " " if lang == "ua" else ",")
             + f'<span><b>{stats["first"]}–{stats["last"]}</b>{ui["years"]}</span></div></header>']
    for s in sections:
        ids = [pid for pid in order if EN[pid]["meta"].get("section") == s["id"]]
        if not ids:
            continue
        cards = []
        for pid in ids:
            p, _ = project(pid, lang)
            m = p["meta"]
            photos = photos_of(p)
            dates = sorted(d for c in p["chapters"] for d in chapter_info(c)[0] if d)
            when = month_span(dates[0], dates[-1], lang) + " · " if dates else ""
            cover = m.get("cover") or (photos[-1] if photos else "")
            cards.append(f'<a class="card" href="{pid}/"><div class="ph" style="background-image:url(\'{esc(size(cover, "w600"))}\')"></div>'
                         f'<div class="tx"><h3>{esc(m["title"])}</h3><p>{esc(m.get("description", ""))}</p>'
                         f'<span class="mono">{when}{len(photos)} {ui["photos"]}</span></div></a>')
        parts.append(f'<section class="group"><h2>{esc(text(s["title"], lang))} <span class="mono">{len(ids)} {ui["projects"]}</span></h2>'
                     f'<div class="cards">{"".join(cards)}</div></section>')
    page(url_of(lang) + "index.html", lang, None, f"{site['name']} · {text(h['eyebrow'], lang)}",
         text(h["intro"], lang), "\n".join(parts),
         EN[order[-1]]["meta"].get("cover", ""))

# -- 404, sitemap, robots
page("404.html", "en", None, f"{UI['en']['notfound']} · {site['name']}", UI["en"]["notfound_text"],
     f'<header class="phead"><h1>{UI["en"]["notfound"]}</h1><p><a href="/">{UI["en"]["notfound_text"]}</a></p></header>')
urls = [url_of(l, pid) for l in LANGS for pid in [None] + order]
open(f"{OUT}/sitemap.xml", "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(f"{OUT}/robots.txt", "w").write(
    "User-agent: *\nDisallow: /\n" if site.get("noindex") else f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(f"{OUT}/.nojekyll", "w").write("")
print(f"site/: {len(order)} projects x {len(LANGS)} languages, {stats['photos']} photos, "
      f"Ukrainian translated: {sum(1 for p in order if p in P['ua'])}, noindex: {bool(site.get('noindex'))}")
