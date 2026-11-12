"""Make the Blogger theme for the Boat diary, so the diary looks like part of the site.

  python3 tools/blogger_theme.py [repo_dir] [out_file]

Writes site/blogger-theme.xml by default (the site build calls this too). Viktor pastes it in Blogger:
Theme -> (arrow next to Customize) -> Edit HTML -> select all -> paste -> Save.

Links point to `live_url` from content/site.yml (the address the site is served from now), or to
`base_url` when `live_url` is empty. Re-run and paste again after the site moves to sailingvira.com.
"""
import json, os, sys
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_tabs import TABS  # noqa: E402

B = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = sys.argv[2] if len(sys.argv) > 2 else f"{B}/site/blogger-theme.xml"
site = yaml.safe_load(open(f"{B}/content/site.yml", encoding="utf-8"))
SITE = (site.get("live_url") or site["base_url"]).rstrip("/")
NAME = site["name"]


def x(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;").replace('"', "&quot;")


tabs = "".join(
    f"<a data-slug='{x(slug)}' data-en='{x(lab['en'])}' data-ua='{x(lab['ua'])}' href='{x(SITE + '/' + slug)}'>{x(lab['en'])}</a>"
    if slug is not None else
    f"<a aria-current='page' data-en='{x(lab['en'])}' data-ua='{x(lab['ua'])}' expr:href='data:blog.homepageUrl'>{x(lab['en'])}</a>"
    for key, slug, lab in TABS)

FONTS = ("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&amp;family=Source+Serif+4:ital,"
         "opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&amp;family=IBM+Plex+Mono:wght@400;500&amp;family=Roboto+Condensed:wght@500;600;700&amp;display=swap")

CSS = """
:root{--bg:#F2F5F6;--paper:#FFFFFF;--ink:#10222E;--muted:#56666F;--line:#D3DCE0;--accent:#0E6A87;--brass:#8C6A1C;
  --f-display:"Barlow Condensed","Roboto Condensed","Arial Narrow",system-ui,sans-serif;--f-body:"Source Serif 4",Georgia,serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}
@media (prefers-color-scheme:dark){:root{--bg:#0B151B;--paper:#11202A;--ink:#E3EBEE;--muted:#93A4AD;--line:#243540;
  --accent:#62B9D6;--brass:#D2AE5A;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.6}
a{color:var(--accent)}
.banner{display:flex;flex-direction:column;justify-content:space-between;aspect-ratio:5/1;min-height:150px;max-height:260px;width:100%;max-width:100%;
  background:#10222E center/cover no-repeat}
.band{display:flex;flex-wrap:wrap;align-items:center;gap:6px 22px;background:rgba(16,34,46,.62);color:#fff;
  padding:10px max(16px,env(safe-area-inset-right,0px)) 10px max(16px,env(safe-area-inset-left,0px))}
.band .brand{font-family:var(--f-display);font-size:24px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;text-decoration:none}
.band .lang{order:3;display:flex;gap:4px}
.band .lang a{font-family:var(--f-mono);font-size:12.5px;color:#DCE7EC;text-decoration:none;padding:2px 6px;border:1px solid transparent;border-radius:4px;cursor:pointer}
.band .lang a.on{border-color:rgba(255,255,255,.45);color:#fff}
.tabs{order:2;flex:1;display:flex;gap:2px 18px;overflow-x:auto;scrollbar-width:none;min-width:0}
.tabs a{font-family:var(--f-display);font-size:18px;font-weight:500;letter-spacing:.04em;text-transform:uppercase;color:#E8F1F4;
  text-decoration:none;white-space:nowrap;padding-block:2px;border-bottom:2px solid transparent}
.tabs a:hover{color:#fff}
.tabs a[aria-current]{color:#fff;border-bottom-color:#E0B85C}
@media (max-width:860px){.band .lang{order:2;margin-left:auto}.tabs{order:3;flex-basis:100%}}
.wrap{max-width:900px;margin:0 auto;padding:8px max(16px,env(safe-area-inset-right,0px)) 48px max(16px,env(safe-area-inset-left,0px))}
.mono{font-family:var(--f-mono);font-size:12.5px;color:var(--muted);font-variant-numeric:tabular-nums}
h1,h2,h3{font-family:var(--f-display);line-height:1.05;margin:0;text-wrap:balance}
.phead{display:grid;gap:8px;padding-block:28px 12px}
.eyebrow{font-family:var(--f-mono);font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--brass)}
.phead h1{font-size:clamp(40px,7vw,68px);font-weight:700;text-transform:uppercase}
.phead p{margin:0;color:var(--muted);font-size:18px}
.post .phead h1{font-size:clamp(28px,4.2vw,42px);text-transform:none;line-height:1.1}
.post .body h2,.post .body h3{margin:1.2em 0 .4em}
.note{margin:16px 0 0;padding:10px 14px;border:1px dashed var(--line);border-radius:6px;color:var(--muted);font-size:15px}
.note[hidden]{display:none}
.list{display:grid;gap:2px;margin-top:12px}
.year{font-family:var(--f-display);font-size:30px;font-weight:600;padding:22px 0 6px;border-bottom:1px solid var(--line);margin-bottom:6px}
.row{display:grid;grid-template-columns:96px minmax(0,1fr);gap:14px;align-items:center;padding:8px 0;text-decoration:none;color:inherit;border-bottom:1px solid var(--line)}
.row i{display:block;aspect-ratio:4/3;border-radius:3px;background:var(--line) center/cover no-repeat}
.row b{display:block;font-weight:600;line-height:1.3}
.row:hover b{color:var(--accent)}
.post .body{overflow-wrap:anywhere}
.post .body img{max-width:100%;height:auto;border-radius:4px}
.post .body a:has(img){display:inline-block}
.post .body iframe{max-width:100%}
.labels{display:flex;flex-wrap:wrap;gap:6px;margin-top:22px}
.labels a{font-family:var(--f-mono);font-size:12px;padding:2px 8px;border:1px solid var(--line);border-radius:99px;text-decoration:none;color:var(--muted)}
.post+.post{margin-top:40px;padding-top:20px;border-top:1px solid var(--line)}
.post h2 a{color:inherit;text-decoration:none}
.comments{margin-top:36px;padding-top:16px;border-top:1px solid var(--line);display:grid;gap:14px}
.comments h3{font-size:24px;font-weight:600;text-transform:uppercase}
.comment{background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:10px 14px}
.pager{display:flex;justify-content:space-between;gap:16px;margin-top:40px;padding-top:16px;border-top:1px solid var(--line);
  font-family:var(--f-display);font-size:20px;text-transform:uppercase}
.pager a{text-decoration:none}
.foot{margin-top:56px;padding-top:18px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;gap:6px 20px}
.foot a{color:var(--muted)}
a:focus-visible{outline:2px solid #E0B85C;outline-offset:2px}
"""

JS = """
(function () {
  var SITE = %(site)s, T = {
    en: {title: "Boat diary", lead: "Every work day on Vira, as it happened. Newest first.", loading: "Loading…",
         all: "All posts", comment: "Leave a comment", label: "Label", notfound: "This post could not be loaded.",
         months: ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]},
    ua: {title: "Щоденник", lead: "Кожен робочий день на «Вірі», як він був. Нові записи зверху.", loading: "Завантажую…",
         all: "Усі записи", comment: "Залишити коментар", label: "Мітка", notfound: "Цей запис не вдалося завантажити.",
         months: ["січ","лют","бер","кві","тра","чер","лип","сер","вер","жов","лис","гру"]}};
  var lang = "en", mode = "", posts = [], cur = null, labelName = "";
  try { lang = localStorage.getItem("sv_lang") || (/\\/ua\\//.test(document.referrer) ? "ua" : "en"); } catch (e) {}
  var root = document.getElementById("sv-js");
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]; }); }
  function day(d) { var m = T[lang].months; return (+d.slice(8, 10)) + " " + m[+d.slice(5, 7) - 1] + " " + d.slice(0, 4); }
  function alt(x) { var l = (x.link || []).filter(function (k) { return k.rel === "alternate"; })[0]; return l ? l.href : ""; }
  function thumb(x) { return x.media$thumbnail ? x.media$thumbnail.url.replace(/\\/s72-[^/]*\\//, "/w300-h225-c/").replace(/=s72-[^/]*$/, "=w300-h225-c") : ""; }

  function apply() {
    document.documentElement.lang = lang === "ua" ? "uk" : "en";
    [].forEach.call(document.querySelectorAll("#sv-tabs a"), function (a) {
      a.textContent = a.getAttribute("data-" + lang);
      var s = a.getAttribute("data-slug");
      if (s !== null) a.href = SITE + "/" + (lang === "ua" ? "ua/" : "") + s;
    });
    var b = document.getElementById("sv-brand"); if (b) b.href = SITE + "/" + (lang === "ua" ? "ua/" : "");
    [].forEach.call(document.querySelectorAll(".lang a"), function (a) { a.className = a.getAttribute("data-l") === lang ? "on" : ""; });
  }
  [].forEach.call(document.querySelectorAll(".lang a"), function (a) {
    a.addEventListener("click", function (ev) {
      ev.preventDefault(); lang = a.getAttribute("data-l");
      try { localStorage.setItem("sv_lang", lang); } catch (e) {}
      apply(); render();
    });
  });

  function render() {
    if (!root) return;
    var t = T[lang], h = "";
    if (mode === "list") {
      h = '<header class="phead"><span class="eyebrow">Irwin Citation 34 · 1978</span><h1>' + esc(labelName || t.title) + "</h1>" +
          (labelName ? '<p><a href="/">' + t.all + "</a></p>" : "<p>" + t.lead + "</p>") +
          (lang === "ua" ? '<p class="note">Щоденник ведеться англійською. Історії проєктів українською є на сайті.</p>' : "") + "</header>";
      if (!posts.length) h += '<p class="mono">' + t.loading + "</p>";
      var year = "";
      h += '<div class="list">';
      posts.forEach(function (p) {
        var y = p.d.slice(0, 4);
        if (y !== year) { year = y; h += '<h2 class="year">' + y + "</h2>"; }
        h += '<a class="row" href="' + esc(p.u) + '"><i style="background-image:url(\\'' + esc(p.t) + '\\')"></i><span><b>' + esc(p.title) +
             '</b><span class="mono">' + day(p.d) + "</span></span></a>";
      });
      h += "</div>";
    } else if (mode === "post") {
      if (!cur) { h = '<p class="mono">' + t.loading + "</p>"; }
      else if (cur === "none") { h = '<p class="note">' + t.notfound + ' <a href="/">' + t.all + "</a></p>"; }
      else {
        var ids = (cur.id.$t.match(/blog-(\\d+)\\.(?:post|page)-(\\d+)/) || []);
        h = '<article class="post"><header class="phead"><span class="eyebrow">' + day(cur.published.$t) + "</span><h1>" + esc(cur.title.$t) +
            '</h1></header><div class="body">' + (cur.content ? cur.content.$t : "") + "</div>";
        if (cur.category) h += '<div class="labels">' + cur.category.map(function (c) {
          return '<a href="/search/label/' + encodeURIComponent(c.term) + '">' + esc(c.term) + "</a>"; }).join("") + "</div>";
        if (ids[2] && /\\.post-/.test(cur.id.$t)) h += '<section class="comments"><a href="https://www.blogger.com/comment/fullpage/post/' + ids[1] + "/" + ids[2] +
            '" target="_blank" rel="noopener">' + t.comment + "</a></section>";
        h += '<nav class="pager"><span></span><a href="/">' + t.all + "</a><span></span></nav></article>";
        document.title = cur.title.$t + " · " + t.title + " · Sailing Vira";
      }
    }
    root.innerHTML = h;
  }

  function each(url, onEntries, done) {
    (function page(start) {
      fetch(url + (url.indexOf("?") < 0 ? "?" : "&") + "alt=json&max-results=150&start-index=" + start)
        .then(function (r) { return r.json(); })
        .then(function (d) { var e = d.feed.entry || []; if (onEntries(e) === false) return done(); if (e.length === 150) page(start + 150); else done(); })
        .catch(function () { done(); });
    })(1);
  }
  function list(feed) {
    mode = "list"; render();
    each(feed, function (e) {
      e.forEach(function (x) { var u = alt(x); if (u) posts.push({title: x.title.$t || "(no title)", u: u, d: x.published.$t, t: thumb(x)}); });
      render();
    }, render);
  }
  function post(kind) {
    mode = "post"; render();
    var want = location.pathname;
    each("/feeds/" + kind + "/default", function (e) {
      for (var i = 0; i < e.length; i++) {
        var u = alt(e[i]); if (u && u.replace(/^https?:\\/\\/[^/]+/, "") === want) { cur = e[i]; return false; }
      }
    }, function () { if (!cur) cur = "none"; render(); });
  }

  apply();
  // The Blogger widget shows posts when it works; otherwise the page builds itself from the blog's own feed.
  var widgetPosts = document.querySelector("#main .post");
  var p = location.pathname, m;
  if (p === "/" || p === "") list("/feeds/posts/summary");
  else if (!widgetPosts) {
    if (/^\\/\\d{4}\\/\\d{2}\\/.+\\.html$/.test(p)) post("posts");
    else if (/^\\/p\\/.+\\.html$/.test(p)) post("pages");
    else if ((m = p.match(/^\\/search\\/label\\/(.+)$/))) { labelName = decodeURIComponent(m[1]); list("/feeds/posts/summary/-/" + encodeURIComponent(labelName)); }
    else list("/feeds/posts/summary");
  }
})();
"""

theme = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateVersion='1.0.0' expr:dir='data:blog.languageDirection' lang='en' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<!-- Sailing Vira diary theme. Made by tools/blogger_theme.py in the sailingvira repo; edit there, not here. -->
<head>
<meta content='width=device-width, initial-scale=1, viewport-fit=cover' name='viewport'/>
<b:include data='blog' name='all-head-content'/>
<title><b:if cond='data:view.isHomepage'>Boat diary · {x(NAME)}<b:else/><data:view.title.escaped/> · Boat diary · {x(NAME)}</b:if></title>
<link href='https://fonts.googleapis.com' rel='preconnect'/>
<link href='{FONTS}' rel='stylesheet'/>
<b:skin version='1.0.0'><![CDATA[{CSS}]]></b:skin>
</head>
<body>
<header class='banner' style='background-image:url({x(SITE)}/assets/banner-strip.webp)'>
<div class='band'><a class='brand' href='{x(SITE)}/' id='sv-brand'>{x(NAME)}</a>
<span class='lang'><a class='on' data-l='en' href='#'>EN</a><a data-l='ua' href='#'>УКР</a></span>
<nav aria-label='Sections' class='tabs' id='sv-tabs'>{tabs}</nav></div>
</header>
<div class='wrap'>
<div id='sv-js'/>
<b:section class='main' id='main' showaddelement='yes'>
<b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='2' visible='true'>
<b:widget-settings>
<b:widget-setting name='showDateHeader'>false</b:widget-setting>
<b:widget-setting name='showShareButtons'>false</b:widget-setting>
<b:widget-setting name='showComments'>true</b:widget-setting>
<b:widget-setting name='showLabels'>true</b:widget-setting>
<b:widget-setting name='showTimestamp'>true</b:widget-setting>
<b:widget-setting name='showAuthor'>false</b:widget-setting>
<b:widget-setting name='postsPerAd'>1</b:widget-setting>
<b:widget-setting name='showInlineAds'>false</b:widget-setting>
</b:widget-settings>
<b:includable id='main' var='this'>
<b:if cond='data:view.isHomepage'>
<b:else/>
  <b:if cond='data:view.isMultipleItems'>
    <header class='phead'><span class='eyebrow'><a expr:href='data:blog.homepageUrl'>Boat diary</a></span><h1><data:view.title.escaped/></h1></header>
  </b:if>
  <b:loop values='data:posts' var='post'>
  <article class='post'>
    <header class='phead'>
      <span class='eyebrow'><time expr:datetime='data:post.date.iso8601'><b:eval expr='data:post.date format &quot;d MMM yyyy&quot;'/></time></span>
      <b:if cond='data:view.isSingleItem'><h1><data:post.title/></h1><b:else/><h2><a expr:href='data:post.url'><data:post.title/></a></h2></b:if>
    </header>
    <div class='body'><data:post.body/></div>
    <b:if cond='data:post.labels'><div class='labels'><b:loop values='data:post.labels' var='label'><a expr:href='data:label.url'><data:label.name/></a></b:loop></div></b:if>
    <b:if cond='data:view.isSingleItem'>
      <section class='comments' id='comments'>
        <b:if cond='data:post.numberOfComments != 0'><h3>Comments</h3>
          <b:loop values='data:post.comments' var='comment'><div class='comment'><div class='mono'><data:comment.author/> · <data:comment.timestamp/></div><div><data:comment.body/></div></div></b:loop>
        </b:if>
        <b:if cond='data:post.allowNewComments'><a expr:href='data:post.addCommentUrl' target='_blank'>Leave a comment</a></b:if>
      </section>
    </b:if>
  </article>
  </b:loop>
  <nav class='pager'>
    <b:if cond='data:newerPageUrl'><a expr:href='data:newerPageUrl'>← Newer</a><b:else/><span/></b:if>
    <a expr:href='data:blog.homepageUrl'>All posts</a>
    <b:if cond='data:olderPageUrl'><a expr:href='data:olderPageUrl'>Older →</a><b:else/><span/></b:if>
  </nav>
</b:if>
</b:includable>
</b:widget>
</b:section>
<footer class='foot mono'><a href='{x(SITE)}/'>{x(NAME)}</a><a href='{x(site.get("youtube_url", ""))}' target='_blank'>YouTube</a><span>© {x(NAME)}</span></footer>
</div>
<script>//<![CDATA[{JS % {"site": json.dumps(SITE)}}//]]></script>
</body>
</html>
"""
os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
open(OUT, "w", encoding="utf-8").write(theme)
print(f"{OUT}: links to {SITE}")
