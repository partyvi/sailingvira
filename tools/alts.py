"""Helper for photo descriptions (alt text) in the stories.

  python3 tools/alts.py context <id>          -> one line per photo: number, chapter, diary text next to it
  python3 tools/alts.py apply <id> <lang> FILE -> sets ![description](url) in content/<lang>/projects/<id>.md,
                                                 one description per line of FILE, photos in order

The description is plain text; it is the photo's alt text and the caption in the photo viewer.
"""
import json, re, sys

IMG = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)\)\s*$")


def key(url):
    """Photo URL without its size part, so diary and story URLs match."""
    url = re.sub(r"/[swh]\d+[^/]*/([^/]+)$", r"/\1", url)
    return re.sub(r"=[swh]\d+[^/]*$", "", url)


def diary_context():
    ctx = {}
    for post in json.load(open("data/classified.json", encoding="utf-8")):
        for sec in post["sections"]:
            before, last = [], None
            for b in sec["blocks"]:
                if b["k"] == "img":
                    k = key(b["src"])
                    ctx.setdefault(k, {"before": " ".join(before), "after": "", "title": sec.get("title") or ""})
                    last, before = k, []
                elif b["k"] == "t":
                    before.append(b["t"])
                    if last and not ctx[last]["after"]:
                        ctx[last]["after"] = b["t"]
    return ctx


cmd, pid = sys.argv[1], sys.argv[2]
if cmd == "context":
    ctx, chap, n = diary_context(), "", 0
    for ln in open(f"content/en/projects/{pid}.md", encoding="utf-8"):
        if ln.startswith("## "):
            chap = ln[3:].strip()
        m = IMG.match(ln.strip())
        if m:
            n += 1
            c = ctx.get(key(m.group(2)), {})
            txt = c.get("before") or ("(after) " + c.get("after", "")) or c.get("title", "")
            print(f"{n}|{chap}|{txt[:260]}")
elif cmd == "apply":
    lang, src = sys.argv[3], sys.argv[4]
    alts = [a.strip() for a in open(src, encoding="utf-8").read().strip("\n").split("\n")]
    path = f"content/{lang}/projects/{pid}.md"
    lines = open(path, encoding="utf-8").read().split("\n")
    idx = [i for i, ln in enumerate(lines) if IMG.match(ln.strip())]
    if len(alts) != len(idx):
        sys.exit(f"{pid}/{lang}: {len(alts)} descriptions, {len(idx)} photos")
    for i, a in zip(idx, alts):
        a = a.replace("[", "(").replace("]", ")")
        lines[i] = f"![{a}]({IMG.match(lines[i].strip()).group(2)})"
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(path)
