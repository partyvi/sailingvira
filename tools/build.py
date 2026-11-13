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
CARD = re.compile(r"^Card:\s*\[([^\]]+)\]\(([^)\s]+)\)\s*(?:\|\s*(.*))?$")
PAIR = re.compile(r"^Was/now:\s*!\[([^\]]*)\]\(([^)\s]+)\)\s*!\[([^\]]*)\]\(([^)\s]+)\)\s*(?:\|\s*(.*))?$")
ITEM = re.compile(r"^Item:\s*!\[([^\]]*)\]\(([^)\s]+)\)\s*\[([^\]]+)\]\(([^)\s]+)\)\s*(?:\|\s*([^|]*))?(?:\|\s*(\S*))?\s*$")
ITEM_UI = {"en": ("Story", "Download", "Files coming soon"), "ua": ("Історія", "Завантажити", "Файли скоро")}
PAIR_UI = {"en": ("Was", "Now"), "ua": ("Було", "Стало")}
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
        if ln.startswith("|"):
            flush(); t = target()
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue
            if not (t and "table" in t[-1]):
                t.append({"table": []})
            t[-1]["table"].append([inline(c) for c in cells]); continue
        m = CARD.match(ln)
        if m:
            flush(); t = target()
            if not (t and "cards" in t[-1]):
                t.append({"cards": []})
            t[-1]["cards"].append((m.group(1), m.group(2), inline(m.group(3) or ""))); continue
        if ln in ("[videos]", "[contact form]"):
            flush(); target().append({"special": ln.strip("[]")}); continue
        m = ITEM.match(ln)
        if m:
            flush(); t = target()
            if not (t and "items" in t[-1]):
                t.append({"items": []})
            t[-1]["items"].append(m.groups()); continue
        m = PAIR.match(ln)
        if m:
            flush(); t = target()
            if not (t and "pairs" in t[-1]):
                t.append({"pairs": []})
            t[-1]["pairs"].append((m.group(2), m.group(1), m.group(4), m.group(3), inline(m.group(5) or ""))); continue
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


def load_pages(lang):
    """Site pages (The Boat, Workshop, ...): content/<lang>/pages/<id>.md with title, description, slug, tab."""
    d, out = f"{B}/content/{lang}/pages", {}
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".md"):
                meta, body = read_md(f"{d}/{fn}")
                intro, chapters = parse_body(body)
                out[fn[:-3]] = {"meta": meta, "intro": intro, "chapters": chapters}
    return out


PG = {lang: load_pages(lang) for lang in ["en", "ua"]}

sections = sorted(yaml.safe_load(open(f"{B}/content/sections.yml", encoding="utf-8")), key=lambda s: s["order"])
P = {lang: load_projects(lang) for lang in LANGS}
EN = P["en"]
order = []  # project ids in site order
for s in sections:
    order += [pid for pid, p in sorted(EN.items(), key=lambda x: x[1]["meta"].get("order", 99))
              if p["meta"].get("section") == s["id"]]


# ---------------------------------------------------------------- helpers
UPDATED = {"en": "Last updated", "ua": "Оновлено"}
MONTHS_FULL = {"en": ["January", "February", "March", "April", "May", "June", "July", "August",
                      "September", "October", "November", "December"],
               "ua": ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня",
                      "вересня", "жовтня", "листопада", "грудня"]}


def fmt_full(d, lang):
    return f"{int(d[8:10])} {MONTHS_FULL[lang][int(d[5:7]) - 1]} {d[:4]}"


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


def youtube_videos():
    """Latest videos of the channel in site.yml, read from YouTube at build time. Empty when offline."""
    import urllib.request, xml.etree.ElementTree as ET
    url = site.get("youtube_url", "")
    if not url:
        return []
    try:
        get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=15).read().decode("utf-8", "replace")
        cid = re.search(r'"(?:channelId|externalId)":"(UC[\w-]{22})"', get(url)).group(1)
        ns = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
        root = ET.fromstring(get(f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"))
        return [{"id": e.find("yt:videoId", ns).text, "title": e.find("a:title", ns).text,
                 "date": e.find("a:published", ns).text[:10]} for e in root.findall("a:entry", ns)]
    except Exception as err:  # offline or YouTube changed: the page shows the channel link only
        print(f"YouTube videos not loaded: {err}")
        return []


VIDEOS = youtube_videos()
FORM_UI = {"en": {"name": "Your name", "email": "Your email (so I can answer)", "msg": "Message", "send": "Send",
                  "off": "The contact form opens soon. Until then, leave a comment on any diary post."},
           "ua": {"name": "Ваше ім'я", "email": "Ваш email (щоб я міг відповісти)", "msg": "Повідомлення", "send": "Надіслати",
                  "off": "Форма зв'язку скоро запрацює. А поки залиште коментар під будь-яким записом щоденника."}}


def special_html(kind, lang):
    if kind == "videos":
        yt = esc(site.get("youtube_url", ""))
        if not VIDEOS:
            return f'<p><a class="dl" href="{yt}" target="_blank" rel="noopener">YouTube @sailingvira ↗</a></p>'
        return '<div class="items vids">' + "".join(
            f'<a class="item" href="https://www.youtube.com/watch?v={esc(v["id"])}" target="_blank" rel="noopener">'
            f'<span class="ph" style="background-image:url(\'https://i.ytimg.com/vi/{esc(v["id"])}/hqdefault.jpg\')"><b>▶</b></span>'
            f'<span class="tx"><h3>{esc(v["title"])}</h3><span class="mono">{fmt(v["date"], lang)}</span></span></a>'
            for v in VIDEOS) + f'</div><p><a class="dl" href="{yt}" target="_blank" rel="noopener">YouTube @sailingvira ↗</a></p>'
    if kind == "contact form":
        f, action = FORM_UI[lang], site.get("contact_form", "")
        if not action:
            return f'<p class="pending">{f["off"]}</p>'
        return (f'<form class="cform" action="{esc(action)}" method="POST">'
                f'<label for="cf-name">{f["name"]}</label><input id="cf-name" name="name" required autocomplete="name">'
                f'<label for="cf-email">{f["email"]}</label><input id="cf-email" name="email" type="email" required autocomplete="email">'
                f'<label for="cf-msg">{f["msg"]}</label><textarea id="cf-msg" name="message" rows="7" required></textarea>'
                f'<input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">'
                f'<button type="submit">{f["send"]}</button></form>')
    return ""


def blocks_html(blocks, lang, alt, rel=""):
    h = []
    for b in blocks:
        if "table" in b:
            rows = b["table"]
            h.append('<div class="tbl"><table><thead><tr>' + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr></thead><tbody>"
                     + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:]) + "</tbody></table></div>")
        elif "cards" in b:
            h.append('<div class="lcards">' + "".join(
                f'<a class="lcard" href="{esc(u if re.match(r"https?://", u) else rel + url_of(lang) + u)}"'
                f'{" target=_blank rel=noopener" if re.match(r"https?://", u) else ""}><b>{esc(t)}</b><span>{d}</span><i>→</i></a>'
                for t, u, d in b["cards"]) + "</div>")
        elif "special" in b:
            h.append(special_html(b["special"], lang))
        elif "items" in b:
            st, dl, soon = ITEM_UI[lang]
            cards = []
            for alt_, img, t, u, note, f in b["items"]:
                href = u if re.match(r"https?://", u) else rel + url_of(lang) + u
                btn = (f'<a class="dl" href="{esc(f)}" target="_blank" rel="noopener">{dl} ↓</a>' if f
                       else f'<span class="dl soon">{soon}</span>')
                cards.append(f'<div class="item"><a class="ph" href="{esc(href)}" style="background-image:url(\'{esc(size(img, "w600"))}\')" aria-label="{esc(t)}"></a>'
                             f'<div class="tx"><h3><a href="{esc(href)}">{esc(t)}</a></h3><p>{inline(note or "")}</p>'
                             f'<div class="act"><a class="st" href="{esc(href)}">{st} →</a>{btn}</div></div></div>')
            h.append('<div class="items">' + "".join(cards) + "</div>")
        elif "pairs" in b:
            was, now = PAIR_UI[lang]
            for u1, a1, u2, a2, cap in b["pairs"]:
                fig = lambda u, a, lab: (f'<button data-big="{esc(size(u, "s1600"))}" aria-label="{UI[lang]["open"]}">'
                                         f'<img src="{esc(size(u, "w800"))}" loading="lazy" alt="{esc(a or alt)}"><span>{lab}</span></button>')
                h.append(f'<figure class="pair"><div class="gal pairg">{fig(u1, a1, was)}{fig(u2, a2, now)}</div>'
                         + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>")
        elif "p" in b:
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
         "opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500"
         "&family=Roboto+Condensed:wght@500;600;700&display=swap")


PHOTOS = json.load(open(f"{B}/data/photos.json"))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_tabs import TABS  # noqa: E402
TAB = {k: (slug, lab) for k, slug, lab in TABS}


def asset(u, rel):
    """A banner setting: full URL, or a path inside the site."""
    return u if re.match(r"https?://", u or "") else rel + (u or "")


def tab_href(key, lang, rel):
    slug = TAB[key][0]
    return site.get("diary_url") or site["blog_url"] if slug is None else (rel + url_of(lang) + slug or "./")


def page(slug, lang, title, desc, body, image="", lightbox=False, tab=None, home=False, path=None):
    path = path or url_of(lang) + slug + "index.html"
    rel = "../" * path.count("/")
    home_href = rel + url_of(lang) or "./"
    alts = "".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{BASE}/{url_of(l)}{slug}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{BASE}/{slug}">'
    robots = '<meta name="robots" content="noindex, nofollow">' if site.get("noindex") else ""
    lang_links = "".join(
        f'<a href="{rel + url_of(l) + slug or "./"}" hreflang="{HTML_LANG[l]}"{" aria-current=page" if l == lang else ""}>{ {"en": "EN", "ua": "УКР"}[l]}</a>'
        for l in LANGS)
    tabs = "".join(
        f'<a href="{esc(tab_href(k, lang, rel))}"{" aria-current=page" if k == tab else ""}'
        f'{" target=_blank rel=noopener" if TAB[k][0] is None else ""}>{lab[lang]}</a>' for k, _, lab in TABS)
    og_img = f'<meta property="og:image" content="{esc(size(image, "w1200"))}">' if image else ""
    lb = ""
    if lightbox:
        lb = (f'<div class="lb" id="lb" hidden><img id="lbimg" alt=""><div class="bar"><span id="lbcap"></span>'
              f'<span class="ctl"><button id="lbprev" aria-label="{UI[lang]["prev"]}">←</button>'
              f'<button id="lbnext" aria-label="{UI[lang]["next"]}">→</button>'
              f'<button id="lbclose">{UI[lang]["close"]}</button></span></div></div>'
              f'<script src="{rel}assets/app.js?v={ASSET_V}"></script>')
    banner = asset(site.get("banner_home" if home else "banner_strip"), rel)
    hero = f'<div class="hero-t"><h1>{esc(text(site["home"]["title"], lang))}</h1></div>' if home else ""
    doc = f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{BASE}/{url_of(lang)}{slug}">{alts}
<meta property="og:type" content="article"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{BASE}/{url_of(lang)}{slug}">{og_img}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{rel}assets/style.css?v={ASSET_V}">
</head>
<body>
<header class="banner{" home" if home else ""}" style="background-image:url('{esc(banner)}')">
<div class="band"><a class="brand" href="{home_href}">{esc(site["name"])}</a>
<span class="lang">{lang_links}</span>
<nav class="tabs" aria-label="{"Sections" if lang == "en" else "Розділи"}">{tabs}</nav></div>
{hero}</header>
<div class="wrap">
{body}
<footer class="foot mono"><a href="{esc(site.get("diary_url") or site["blog_url"])}" target="_blank" rel="noopener">{UI[lang]["blog"]} ↗</a>
<a href="{esc(site.get("youtube_url", ""))}" target="_blank" rel="noopener">YouTube ↗</a>
<span>© {esc(site["name"])}</span></footer>
</div>
{lb}
</body>
</html>
"""
    os.makedirs(os.path.dirname(f"{OUT}/{path}") or OUT, exist_ok=True)
    open(f"{OUT}/{path}", "w", encoding="utf-8").write(doc)


def cards_html(ids, lang, rel):
    ui, cards = UI[lang], []
    for pid in ids:
        p, _ = project(pid, lang)
        m = p["meta"]
        photos = photos_of(p)
        dates = sorted(d for c in p["chapters"] for d in chapter_info(c)[0] if d)
        when = month_span(dates[0], dates[-1], lang) + " · " if dates else ""
        cover = m.get("cover") or (photos[-1] if photos else "")
        cards.append(f'<a class="card" href="{rel}{pid}/"><div class="ph" style="background-image:url(\'{esc(size(cover, "w600"))}\')"></div>'
                     f'<div class="tx"><h3>{esc(m["title"])}</h3><p>{esc(m.get("description", ""))}</p>'
                     f'<span class="mono">{when}{len(photos)} {ui["photos"]}</span></div></a>')
    return f'<div class="cards">{"".join(cards)}</div>'


def groups_html(tab, lang, rel):
    out = []
    for s in sections:
        if s.get("tab", "projects") != tab:
            continue
        ids = [pid for pid in order if EN[pid]["meta"].get("section") == s["id"]]
        if ids:
            out.append(f'<section class="group"><h2>{esc(text(s["title"], lang))} <span class="mono">{len(ids)} {UI[lang]["projects"]}</span></h2>'
                       + cards_html(ids, lang, rel) + "</section>")
    return "\n".join(out)


def tab_of(pid):
    s = next((x for x in sections if x["id"] == EN[pid]["meta"].get("section")), {})
    return s.get("tab", "projects")


def latest_posts(n=5):
    """Newest diary posts from the saved blog data (the Home page refreshes them live from Blogger)."""
    seen, out = set(), []
    for v in sorted(sec.values(), key=lambda v: v["date"], reverse=True):
        if v["kind"] != "post" or v["url"] in seen:
            continue
        seen.add(v["url"])
        img = next((PHOTOS[i] for x in sec.values() if x["url"] == v["url"] for i in x["imgs"] if i in PHOTOS), "")
        out.append((v["date"], v["ptitle"].strip(), v["url"], img))
        if len(out) == n:
            break
    return out


PAGES = {  # simple pages, filled in step by step
    "boat": {"en": ("The Boat", "The Irwin Citation 34: what she is, what I like and dislike about her, and every upgrade I made."),
             "ua": ("Човен", "Irwin Citation 34: що це за човен, що мені в ньому подобається і ні, і всі мої покращення.")},
    "workshop": {"en": ("Workshop", "3D models, drawings and electronics from the rebuild, free to download."),
                 "ua": ("Майстерня", "3D-моделі, креслення й електроніка з відновлення, можна завантажити безкоштовно.")},
    "videos": {"en": ("Videos", "Sailing and project videos from the Sailing Vira channel."),
               "ua": ("Відео", "Відео з плавань і проєктів на каналі Sailing Vira.")},
    "about": {"en": ("About me", "Who is behind Vira."), "ua": ("Про мене", "Хто стоїть за «Вірою».")},
    "contact": {"en": ("Contact", "Questions about the boat or the projects? Write to me."),
                "ua": ("Контакти", "Питання про човен чи проєкти? Пишіть.")},
}
SOON = {"en": "This page is being built. Come back soon.", "ua": "Ця сторінка ще будується. Зазирніть трохи згодом."}
HOME_UI = {
    "en": {"projects_t": "Projects", "projects_p": "Everything I rebuilt on Vira, one story per project.",
           "all": "All {n} projects →", "sail_p": "Days on the water: from Lake Travis to Galveston Bay.",
           "diary_t": "Latest from the diary", "diary_all": "Open the diary →", "go": "Open →"},
    "ua": {"projects_t": "Проєкти", "projects_p": "Усе, що я відновив на «Вірі», по історії на кожен проєкт.",
           "all": "Усі {n} проєкти →", "sail_p": "Дні на воді: від озера Тревіс до Галвестонської затоки.",
           "diary_t": "Свіже зі щоденника", "diary_all": "Відкрити щоденник →", "go": "Відкрити →"},
}


# ---------------------------------------------------------------- build
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f"{OUT}/assets")
for f in os.listdir(f"{B}/tools/assets"):
    shutil.copy(f"{B}/tools/assets/{f}", f"{OUT}/assets/{f}")

posts = {(v["date"], v["ptitle"]) for v in sec.values() if v["kind"] == "post"}
stats = {"posts": len(posts), "photos": sum(len(photos_of(EN[p])) for p in order),
         "first": min(p[0] for p in posts)[:4], "last": max(p[0] for p in posts)[:4],
         "days": max(d for p in posts for d in (daynums(p[1]) or [0]))}
LATEST = latest_posts()

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
        page(f"{pid}/", lang, f"{title} · {site['name']}", blurb, html_body,
             m.get("cover") or (photos[-1] if photos else ""), lightbox=True, tab=tab_of(pid))

    # -- projects and sailing lists
    for key, slug in (("projects", "projects/"), ("sailing", "voyages/")):
        label = TAB[key][1][lang]
        lead = HOME_UI[lang]["projects_p"] if key == "projects" else HOME_UI[lang]["sail_p"]
        page(slug, lang, f"{label} · {site['name']}", lead,
             f'<header class="phead"><h1>{esc(label)}</h1><p>{esc(lead)}</p></header>' + groups_html(key, lang, "../"),
             tab=key)

    # -- site pages from content/<lang>/pages (fall back to English)
    for gid, enp in PG["en"].items():
        pg = PG[lang].get(gid) or enp
        m = {**enp["meta"], **{k: v for k, v in pg["meta"].items() if v}}
        slug, rel = m["slug"], "../" * (url_of(lang) + m["slug"]).count("/")
        title, blurb = m.get("title", gid), m.get("description", "")
        body, toc = [], []
        if pg["intro"]:
            body.append('<div class="intro">' + blocks_html(pg["intro"], lang, title, rel) + "</div>")
        for ci, c in enumerate(pg["chapters"]):
            (a, b2), days = chapter_info(c)
            log = f'<div class="log mono"><span>{span(a, b2, lang)}</span></div>' if a else ""
            toc.append(f'<a href="#c{ci + 1}">{esc(c["h"])}</a>')
            body.append(f'<section class="chap" id="c{ci + 1}"><h2>{esc(c["h"])}</h2>{log}\n'
                        + blocks_html(c["blocks"], lang, f"{title}: {c['h']}", rel) + "</section>")
        note = "" if gid in PG[lang] or lang == "en" else f'<p class="note">{ui["missing"]}</p>'
        eyebrow = f'<span class="eyebrow">{esc(m["eyebrow"])}</span>' if m.get("eyebrow") else ""
        head = f'<header class="phead">{eyebrow}<h1>{esc(title)}</h1><p>{esc(blurb)}</p>{note}</header>'
        if m.get("portrait"):  # e.g. About me: a photo next to the title (assets/... or a full URL)
            src = m["portrait"] if m["portrait"].startswith("http") else rel + m["portrait"]
            head = (f'<div class="phead-p">{head}<img class="portrait" src="{esc(src)}" '
                    f'alt="{esc(m.get("eyebrow") or title)}" width="500" height="620"></div>')
        if m.get("updated"):  # e.g. the Upgrades log, kept in step with the blog page
            body.append(f'<p class="updated mono">{UPDATED[lang]}: {fmt_full(str(m["updated"]), lang)}</p>')
        side = f'<aside class="toc">{"".join(toc)}</aside>' if len(toc) > 2 else ""
        page(slug, lang, f"{title} · {site['name']}", blurb,
             head + f'<div class="layout{"" if side else " one"}"><div class="story">' + "\n".join(body) + f"</div>{side}</div>",
             m.get("cover", ""), lightbox=True, tab=m.get("tab"))

    # -- simple pages (being built) for tabs without a content page
    have = {PG["en"][g]["meta"].get("slug") for g in PG["en"]}
    for key, t in PAGES.items():
        if TAB[key][0] in have:
            continue
        label, lead = t[lang]
        extra = ""
        if key == "videos":
            extra = f'<p><a href="{esc(site.get("youtube_url", ""))}" target="_blank" rel="noopener">YouTube: @sailingvira ↗</a></p>'
        page(TAB[key][0], lang, f"{label} · {site['name']}", lead,
             f'<header class="phead"><h1>{esc(label)}</h1><p>{esc(lead)}</p></header>'
             f'<p class="pending">{SOON[lang]}</p>{extra}', tab=key)

    # -- home
    h, hu = site["home"], HOME_UI[lang]
    mosaic = "".join(
        f'<a href="{pid}/" title="{esc(project(pid, lang)[0]["meta"]["title"])}">'
        f'<i style="background-image:url(\'{esc(size(EN[pid]["meta"].get("cover", ""), "s200-c"))}\')"></i></a>'
        for pid in order)
    proj_n = sum(1 for pid in order if tab_of(pid) == "projects")
    rows = "".join(
        f'<a class="drow" href="{esc(u)}" target="_blank" rel="noopener"><i style="background-image:url(\'{esc(size(img, "w240"))}\')"></i>'
        f'<span><b>{esc(t)}</b><span class="mono">{fmt(d, lang)}</span></span></a>' for d, t, u, img in LATEST)
    sail_cover = EN["sailing"]["meta"].get("cover", "")
    boat_cover = EN["hull-bottom"]["meta"].get("cover", "")
    root = "../" if lang == "ua" else ""  # home page -> site root, for assets/

    def simple(key):  # a tile; a photo on top if content/site.yml has tile_<key>
        img = site.get(f"tile_{key}")
        ph = (f'<div class="ph" style="background-image:url(\'{esc(asset(img, root))}\')"></div>' if img else "")
        return (f'<a class="tile" href="{TAB[key][0]}">{ph}<h2>{PAGES[key][lang][0]}</h2>'
                f'<p>{esc(PAGES[key][lang][1])}</p><span class="go">{hu["go"]}</span></a>')
    video_tile = simple("videos")
    if VIDEOS:
        v = VIDEOS[0]
        video_tile = (f'<a class="tile" href="videos/"><div class="ph" style="background-image:url(\'https://i.ytimg.com/vi/{esc(v["id"])}/hqdefault.jpg\')"></div>'
                      f'<h2>{PAGES["videos"][lang][0]}</h2><p>{esc(v["title"])}</p><span class="go">{hu["go"]}</span></a>')
    diary_feed = (site.get("diary_url") or site["blog_url"]).rstrip("/")
    months = json.dumps(UI[lang]["months"], ensure_ascii=False)
    body = f"""<header class="mast"><span class="eyebrow">{esc(text(h["eyebrow"], lang))}</span>
<p>{esc(text(h["intro"], lang))}</p>
<div class="stats mono"><span><b>{stats["posts"]}</b>{ui["posts"]}</span><span><b>{stats["days"]}</b>{ui["days"]}</span>
<span><b>{f'{stats["photos"]:,}'.replace(",", " " if lang == "ua" else ",")}</b>{ui["photos"]}</span>
<span><b>{stats["first"]}–{stats["last"]}</b>{ui["years"]}</span></div></header>
<div class="tiles">
<div class="tile wide"><h2><a href="projects/">{hu["projects_t"]}</a></h2><p>{hu["projects_p"]}</p>
<div class="mosaic">{mosaic}</div><a class="go" href="projects/">{hu["all"].format(n=proj_n)}</a></div>
<a class="tile" href="boat/"><div class="ph" style="background-image:url('{esc(size(boat_cover, "w600"))}')"></div>
<h2>{PAGES["boat"][lang][0]}</h2><p>{esc(PAGES["boat"][lang][1])}</p><span class="go">{hu["go"]}</span></a>
<a class="tile" href="voyages/"><div class="ph" style="background-image:url('{esc(size(sail_cover, "w600"))}')"></div>
<h2>{TAB["sailing"][1][lang]}</h2><p>{hu["sail_p"]}</p><span class="go">{hu["go"]}</span></a>
<div class="tile wide"><h2><a href="{esc(diary_feed)}" target="_blank" rel="noopener">{hu["diary_t"]}</a></h2>
<div class="diary" id="diary">{rows}</div><a class="go" href="{esc(diary_feed)}" target="_blank" rel="noopener">{hu["diary_all"]}</a></div>
{simple("workshop")}{video_tile}{simple("about")}{simple("contact")}
</div>
<script>
window.svDiary = function (d) {{
  var e = (d.feed && d.feed.entry) || [], m = {months}, box = document.getElementById("diary"), h = "";
  e.forEach(function (x) {{
    var l = (x.link || []).filter(function (k) {{ return k.rel === "alternate"; }})[0];
    if (!l) return;
    var t = (x.title.$t || "").replace(/[<&]/g, function (c) {{ return c === "<" ? "&lt;" : "&amp;"; }});
    var p = x.published.$t, dt = (+p.slice(8, 10)) + " " + m[+p.slice(5, 7) - 1] + " " + p.slice(0, 4);
    var img = x.media$thumbnail ? x.media$thumbnail.url.replace(/s72-c/, "w240-h180-c") : "";
    h += '<a class="drow" href="' + l.href + '" target="_blank" rel="noopener"><i style="background-image:url(\\'' + img + '\\')"></i><span><b>' + t + '</b><span class="mono">' + dt + '</span></span></a>';
  }});
  if (h) box.innerHTML = h;
}};
</script>
<script src="{esc(diary_feed)}/feeds/posts/default?alt=json-in-script&amp;max-results=5&amp;callback=svDiary" async></script>"""
    page("", lang, f"{site['name']} · {text(h['eyebrow'], lang)}", text(h["intro"], lang), body,
         site.get("banner_home", ""), tab="home", home=True)

# -- 404, sitemap, robots
page("", "en", f"{UI['en']['notfound']} · {site['name']}", UI["en"]["notfound_text"],
     f'<header class="phead"><h1>{UI["en"]["notfound"]}</h1><p><a href="{BASE}/projects/">{UI["en"]["notfound_text"]}</a></p></header>',
     path="404.html")
slugs = [""] + [s for k, s, _ in TABS if s] + [f"{pid}/" for pid in order] + [g["meta"]["slug"] for g in PG["en"].values()]
urls = [url_of(l) + s for l in LANGS for s in dict.fromkeys(slugs)]
open(f"{OUT}/sitemap.xml", "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{BASE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(f"{OUT}/robots.txt", "w").write(
    "User-agent: *\nDisallow: /\n" if site.get("noindex") else f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(f"{OUT}/.nojekyll", "w").write("")
os.system(f'{sys.executable} "{B}/tools/blogger_theme.py" "{B}" "{OUT}/blogger-theme.xml"')
print(f"site/: {len(order)} projects x {len(LANGS)} languages, {stats['photos']} photos, "
      f"Ukrainian translated: {sum(1 for p in order if p in P['ua'])}, noindex: {bool(site.get('noindex'))}")
