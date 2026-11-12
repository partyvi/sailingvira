"""Build the site from content/.

Usage: python3 tools/build.py [repo_dir]

Reads content/sections.yml and content/<lang>/projects/*.md (YAML front matter + Markdown body),
and writes site/index.html. Photos are loaded from their Blogger URLs.

Body format (see CLAUDE.md):
  ## Heading            starts a chapter
  ![](url)              a photo; photos one after another form one gallery
  Diary: [date](url)    link(s) to the diary post(s) behind the gallery or paragraph above
  Story page: [t](url)  link to a Blogger story page
  - item                list item
  anything else         paragraph (Markdown inline: **bold**, [links](url) ...)
"""
import json, os, re, sys
import yaml, markdown

B = sys.argv[1] if len(sys.argv) > 1 else "."
LANG = "en"
OUT = f"{B}/site"
os.makedirs(OUT, exist_ok=True)

sec = json.load(open(f"{B}/data/sections.json"))
POSTS = {}  # diary url -> (date, title, is_page)
for v in sec.values():
    POSTS.setdefault(v["url"], (v["date"], v["ptitle"], v["kind"] == "page"))

IMG = re.compile(r"^!\[[^\]]*\]\(([^)\s]+)\)\s*$")
SRC = re.compile(r"^(Diary|Story page):\s*(.*)$")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


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
    html = markdown.markdown(text)
    return re.sub(r"^<p>(.*)</p>$", r"\1", html, flags=re.S)


def read_md(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    return (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, txt)


def parse_body(body):
    intro, chapters, cur = [], [], None
    para = []

    def target():
        return cur["blocks"] if cur else intro

    def flush():
        if para:
            target().append({"p": inline(" ".join(para))})
            para.clear()

    for raw in body.split("\n"):
        ln = raw.strip()
        if not ln:
            flush()
            continue
        if ln.startswith("## "):
            flush()
            cur = {"h": ln[3:].strip(), "blocks": [], "links": []}
            chapters.append(cur)
            continue
        m = IMG.match(ln)
        if m:
            flush()
            t = target()
            if not (t and "g" in t[-1] and not t[-1]["src"]):
                t.append({"g": [], "src": []})
            t[-1]["g"].append(m.group(1))
            continue
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
            flush()
            t = target()
            if not (t and "ul" in t[-1]):
                t.append({"ul": []})
            t[-1]["ul"].append(inline(ln[2:]))
            continue
        para.append(ln)
    flush()
    return intro, chapters


sections = yaml.safe_load(open(f"{B}/content/sections.yml", encoding="utf-8"))
sections.sort(key=lambda s: s["order"])
projects = {}
pdir = f"{B}/content/{LANG}/projects"
for fn in sorted(os.listdir(pdir)):
    if not fn.endswith(".md"):
        continue
    meta, body = read_md(f"{pdir}/{fn}")
    pid = fn[:-3]
    intro, chapters = parse_body(body)
    out = []
    for c in chapters:
        info = [POSTS[u] for u in c["links"] if u in POSTS]
        dates = sorted(d for d, _, _ in info)
        days = sorted({n for _, t, page in info if not page for n in daynums(t)})
        out.append({"h": c["h"], "from": dates[0] if dates else None, "to": dates[-1] if dates else None,
                    "days": [days[0], days[-1]] if days else None,
                    "blocks": [{"g": [[size(u, "w600"), size(u, "s1600")] for u in b["g"]], "src": b["src"]}
                               if "g" in b else b for b in c["blocks"]]})
    photos = [u for c in chapters for b in c["blocks"] if "g" in b for u in b["g"]]
    projects[pid] = {"title": meta.get("title", pid), "blurb": meta.get("description", ""),
                     "section": meta.get("section"), "order": meta.get("order", 99),
                     "cover": size(meta["cover"], "w600") if meta.get("cover") else
                              (size(photos[-1], "w600") if photos else ""),
                     "intro": intro, "chapters": out, "n": len(photos)}

structure = []
for s in sections:
    subs = sorted((p for p in projects.items() if p[1]["section"] == s["id"]), key=lambda p: p[1]["order"])
    for pid, p in subs:
        p["group"] = s["title"][LANG]
    structure.append({"id": s["id"], "title": s["title"][LANG], "subs": [pid for pid, _ in subs]})

posts = {(v["date"], v["ptitle"]) for v in sec.values() if v["kind"] == "post"}
stats = {"posts": len(posts), "photos": sum(p["n"] for p in projects.values()),
         "first": min(p[0] for p in posts), "last": max(p[0] for p in posts),
         "days": max(d for p in posts for d in (daynums(p[1]) or [0]))}
data = {"structure": structure, "subs": projects, "stats": stats}
tpl = open(f"{B}/tools/template.html", encoding="utf-8").read()
open(f"{OUT}/index.html", "w", encoding="utf-8").write(
    tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
print(f"site/index.html: {len(projects)} projects, {stats['photos']} photos, {os.path.getsize(OUT + '/index.html')} bytes")
