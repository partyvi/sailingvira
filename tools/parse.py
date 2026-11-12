# Parse Blogger feed JSON into posts -> sections -> blocks (text / img)
import json, re, html, sys
from html.parser import HTMLParser
D = sys.argv[1]
BLOCK = {"p","div","br","li","tr","h1","h2","h3","h4","h5","h6","table","ul","ol","blockquote"}
HEAD = {"h1","h2","h3","h4"}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.blocks=[]; s.buf=""; s.head=None; s.skip=0; s.bold=0; s.boldbuf=""; s.links=[]
    def flush(s, kind="t"):
        t = re.sub(r"\s+"," ",s.buf).strip()
        if t: s.blocks.append({"k":kind,"t":t})
        s.buf=""
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag in ("style","script"): s.skip+=1; return
        if tag in HEAD: s.flush(); s.head=tag
        elif tag in BLOCK: s.flush()
        if tag=="img" and a.get("src"):
            s.flush(); s.blocks.append({"k":"img","src":a["src"],"w":a.get("data-original-width"),"h":a.get("data-original-height")})
        if tag=="a" and a.get("href") and "googleusercontent" not in a["href"] and "bp.blogspot" not in a["href"]:
            s.links.append(a["href"])
    def handle_endtag(s,tag):
        if tag in ("style","script"): s.skip-=1; return
        if tag in HEAD: s.flush("h"); s.head=None
        elif tag in BLOCK: s.flush()
    def handle_data(s,d):
        if not s.skip: s.buf+=d
def parse(c):
    p=P(); p.feed(c); p.flush()
    # merge: caption detection left to later
    return p.blocks, p.links
out=[]
for f,kind in [("feed_1.json","post"),("feed_151.json","post"),("pages.json","page")]:
    for e in json.load(open(f"{D}/{f}"))["feed"].get("entry",[]):
        url=[l["href"] for l in e["link"] if l["rel"]=="alternate"][0]
        blocks,links=parse(e["content"]["$t"])
        # split into sections at headings
        secs=[{"title":None,"blocks":[]}]
        for b in blocks:
            if b["k"]=="h":
                secs.append({"title":b["t"],"blocks":[]})
            else: secs[-1]["blocks"].append(b)
        secs=[s for s in secs if s["blocks"] or s["title"]]
        out.append({"kind":kind,"id":e["id"]["$t"].split("-")[-1],"date":e["published"]["$t"][:10],"title":e["title"]["$t"].strip(),"url":url,
                    "labels":[x["term"] for x in e.get("category",[])],"sections":secs,"links":links})
out.sort(key=lambda p:(p["kind"],p["date"]))
json.dump(out,open(f"{D}/parsed.json","w"),ensure_ascii=False,indent=0)
import collections
c=collections.Counter(len(p["sections"]) for p in out)
print(len(out), sorted(c.items()))
print(sum(1 for p in out for s in p["sections"]), "sections")
