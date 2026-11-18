#!/usr/bin/env python3
"""Change "Main heading" (<h1>) to "Heading" (<h2>) inside Viktor's diary posts (Bing: "More than one h1 tag").

Blogger already makes the page title the one <h1>; headings inside the post text should be <h2>/<h3>.
Only <h1 ...> / </h1> tags in post bodies change. Titles, dates, URLs, labels, comments and pages are untouched.

Needs a Blogger API token: a network secret for host www.googleapis.com (Authorization: Bearer <token from
Google's OAuth Playground, scope https://www.googleapis.com/auth/blogger>). The proxy adds it to requests.

  python3 tools/blogger_fix_h1.py              # dry run: list posts with <h1> in the text, change nothing
  python3 tools/blogger_fix_h1.py --one ID     # change one post (the test), then read it back
  python3 tools/blogger_fix_h1.py --all        # change every post that still has <h1>, then read each back
"""
import json, re, sys, time, urllib.request, urllib.error

BLOG = "3730742912744811408"
API = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG}/posts"
OPEN, CLOSE = re.compile(r"<h1(?=[\s>])", re.I), re.compile(r"</h1\s*>", re.I)


def call(url, method="GET", body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer from-proxy"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=60).read())
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {url} -> HTTP {e.code}: {e.read()[:300]!r}\n(401/403: the token is missing or expired; get a new one)")


def posts():
    out, tok = [], ""
    while True:
        r = call(f"{API}?maxResults=50&fetchBodies=true&status=live" + (f"&pageToken={tok}" if tok else ""))
        out += r.get("items", [])
        tok = r.get("nextPageToken")
        if not tok:
            return out


def fixed(html):
    return CLOSE.sub("</h2>", OPEN.sub("<h2", html))


def change(p):
    new = fixed(p["content"])
    call(f"{API}/{p['id']}", "PATCH", {"content": new})
    back = call(f"{API}/{p['id']}?fetchBody=true")
    left = len(OPEN.findall(back.get("content", "")))
    print(f"  {'OK ' if left == 0 else 'LEFT %d' % left} {back.get('url', p['id'])}")
    return left == 0


def main():
    ps = posts()
    todo = [p for p in ps if OPEN.search(p.get("content", ""))]
    print(f"{len(ps)} live posts, {len(todo)} with <h1> in the text")
    if len(sys.argv) == 1:
        for p in todo:
            print(f"  {len(OPEN.findall(p['content'])):3d}  {p['id']}  {p['published'][:10]}  {p['title'][:70]}")
        print("Dry run: nothing changed.")
    elif sys.argv[1] == "--one":
        p = next((x for x in todo if x["id"] == sys.argv[2]), None) or sys.exit("That post id has no <h1> (or is not live).")
        change(p)
    elif sys.argv[1] == "--all":
        bad = 0
        for p in todo:
            bad += not change(p)
            time.sleep(1.5)  # stay well inside Blogger's rate limit
        print(f"Done: {len(todo) - bad} posts fixed, {bad} need a look.")


if __name__ == "__main__":
    main()
