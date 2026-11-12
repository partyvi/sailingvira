#!/usr/bin/env python3
"""Keep the Upgrades log page in step with Viktor's Blogger page
"What is improved vs original?".

data/upgrades_blog.json holds the list as it was on the blog at the last sync
(sections and items, raw, before typo fixes). Comparing the live page with
this copy shows only what Viktor really changed on the blog, so the typo fixes
and the Ukrainian translation on the site are left alone.

  python3 tools/sync_upgrades.py check   # print what changed on the blog (exit 1 if anything did)
  python3 tools/sync_upgrades.py save    # store the live list as the new copy (after updating the pages)

The pages themselves (content/en/pages/upgrades.md, content/ua/pages/upgrades.md)
are updated by hand or by Claude: copy new items word for word with their year,
fix only typos, translate them for the UA page (see CLAUDE.md, lists rule).
"""
import html
from html.parser import HTMLParser
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAP = ROOT / "data" / "upgrades_blog.json"
PAGE = "https://irwin34.blogspot.com/p/what-is-improved-vs-original.html"
FEED = "https://irwin34.blogspot.com/feeds/pages/default?alt=json&max-results=150"


def text(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def fetch():
    with urllib.request.urlopen(FEED, timeout=60) as r:
        feed = json.load(r)["feed"]
    for e in feed.get("entry", []):
        links = [l["href"] for l in e["link"] if l["rel"] == "alternate"]
        if links and links[0] == PAGE:
            return e["content"]["$t"], e["updated"]["$t"]
    sys.exit(f"page not found in the blog feed: {PAGE}")


class _Parser(HTMLParser):
    """Section titles are the text just before each top-level <ul> (a <p>, a
    heading or a bare <span>); items are its top-level <li>, with any nested
    list folded into the item's text."""
    BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "br"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.sections, self.depth, self.pending, self.item = [], 0, [], None

    def handle_starttag(self, tag, attrs):
        if tag == "ul":
            if self.depth == 0:
                title = text(" ".join(self.pending))
                self.sections.append({"title": title, "items": []})
                self.pending = []
            self.depth += 1
        elif tag == "li" and self.depth == 1:
            self.item = []
        elif tag in self.BLOCK and self.depth == 0:
            self.pending = []

    def handle_endtag(self, tag):
        if tag == "ul":
            self.depth = max(0, self.depth - 1)
        elif tag == "li" and self.depth == 1 and self.item is not None:
            t = text(" ".join(self.item))
            if t:
                self.sections[-1]["items"].append(t)
            self.item = None

    def handle_data(self, data):
        if self.depth == 0:
            self.pending.append(data)
        elif self.item is not None:
            self.item.append(data)


def parse(body):
    """Sections in page order: [{"title": ..., "items": [...]}]."""
    p = _Parser()
    p.feed(body)
    return [s for s in p.sections if s["items"]]


def diff(old, new):
    lines = []
    olds = {s["title"]: s["items"] for s in old}
    news = {s["title"]: s["items"] for s in new}
    for t in news:
        if t not in olds:
            lines.append(f"+ section: {t}")
            lines += [f"  + {i}" for i in news[t]]
            continue
        added = [i for i in news[t] if i not in olds[t]]
        removed = [i for i in olds[t] if i not in news[t]]
        if added or removed:
            lines.append(f"~ section: {t}")
            lines += [f"  + {i}" for i in added] + [f"  - {i}" for i in removed]
    for t in olds:
        if t not in news:
            lines.append(f"- section: {t}")
    if not lines and [s["title"] for s in old] != [s["title"] for s in new]:
        lines.append("~ section order changed: " + " | ".join(s["title"] for s in new))
    return lines


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    body, updated = fetch()
    live = parse(body)
    if not live:
        sys.exit("no sections found on the blog page; the page layout may have changed")
    if cmd == "save":
        SNAP.write_text(json.dumps({"page": PAGE, "updated": updated, "sections": live},
                                   ensure_ascii=False, indent=1) + "\n")
        print(f"saved {sum(len(s['items']) for s in live)} items, blog page updated {updated}")
        return
    old = json.loads(SNAP.read_text())["sections"] if SNAP.exists() else []
    changes = diff(old, live)
    print(f"blog page updated {updated}")
    print("\n".join(changes) if changes else "no changes")
    sys.exit(1 if changes else 0)


if __name__ == "__main__":
    main()
