"""Helper for translating a project story into another language.

  python3 tools/translate.py export <id>            -> prints the text lines to translate (one per line)
  python3 tools/translate.py merge <id> <lang> FILE -> writes content/<lang>/projects/<id>.md

The text lines are: title, description, then every heading, paragraph and list item in order.
Photo lines and Diary / Story page lines are copied unchanged from the English file.
"""
import re, sys, os

IMG = re.compile(r"^!\[[^\]]*\]\([^)]+\)\s*$")
SRC = re.compile(r"^(Diary|Story page):")


def units(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    fm, body = m.group(1), m.group(2)
    out = [("fm", "title"), ("fm", "description")]
    for i, ln in enumerate(body.split("\n")):
        s = ln.strip()
        if s and not IMG.match(s) and not SRC.match(s):
            out.append(("body", i))
    return fm, body, out


def get_fm(fm, key):
    m = re.search(rf'^{key}: (.*)$', fm, re.M)
    v = m.group(1)
    return v[1:-1].replace('\\"', '"') if v.startswith('"') else v


def text_of(fm, body, u):
    if u[0] == "fm":
        return get_fm(fm, u[1])
    ln = body.split("\n")[u[1]]
    return ln


cmd, pid = sys.argv[1], sys.argv[2]
en = f"content/en/projects/{pid}.md"
fm, body, us = units(en)
if cmd == "export":
    for u in us:
        print(text_of(fm, body, u))
elif cmd == "merge":
    lang, src = sys.argv[3], sys.argv[4]
    tr = [l.rstrip("\n") for l in open(src, encoding="utf-8").read().strip("\n").split("\n")]
    if len(tr) != len(us):
        sys.exit(f"{pid}: {len(tr)} lines translated, {len(us)} expected")
    lines = body.split("\n")
    out = f"content/{lang}/projects/{pid}.md"
    if os.path.exists(out):  # keep photo descriptions already written in this language
        old = {m.group(2): m.group(1) for m in (re.match(r"^!\[([^\]]*)\]\(([^)\s]+)\)", l.strip()) for l in open(out, encoding="utf-8")) if m and m.group(1)}
        lines = [re.sub(r"^!\[[^\]]*\]\(([^)\s]+)\)", lambda m: f"![{old[m.group(1)]}]({m.group(1)})", l) if IMG.match(l.strip()) and re.search(r"\(([^)\s]+)\)", l).group(1) in old else l for l in lines]
    for u, t in zip(us, tr):
        if u[0] == "body":
            orig = lines[u[1]]
            for pre in ("## ", "- "):  # keep the Markdown marker even if the translation dropped it
                if orig.startswith(pre) and not t.startswith(pre):
                    t = pre + t
            lines[u[1]] = t
    q = lambda s: '"' + s.replace('"', '\\"') + '"'
    fm2 = re.sub(r'^title: .*$', lambda _: "title: " + q(tr[0]), fm, flags=re.M)
    fm2 = re.sub(r'^description: .*$', lambda _: "description: " + q(tr[1]), fm2, flags=re.M)
    os.makedirs(f"content/{lang}/projects", exist_ok=True)
    open(f"content/{lang}/projects/{pid}.md", "w", encoding="utf-8").write(f"---\n{fm2}\n---\n" + "\n".join(lines))
    print(f"content/{lang}/projects/{pid}.md")
