# Sailing Vira

The rebuild of *Vira*, a 1978 Irwin Citation 34: the diary from
[irwin34.blogspot.com](https://irwin34.blogspot.com), regrouped by project and told as stories.
The site will be published at **sailingvira.com**.

## What's here

| Path | What it is |
|---|---|
| `stories/` | One story per project, in a light Markdown format (see `CLAUDE.md`). |
| `data/` | The blog split into dated sections with photo ids, and the photo URL list. |
| `tools/structure.json` | The sections and projects of the site. |
| `tools/` | Scripts that read the blog and build the site. |

## Pipeline (current, will change in Phase 2–3)

Every script takes the folder it works in as its argument.

1. Download the blog feed into `data/` (`feed_1.json`, `feed_151.json`, `pages.json`).
2. `python3 tools/parse.py data`: split posts into sections, then `data/parsed.json`.
3. `python3 tools/classify.py data`: assign each section to a project, then `data/classified.json`.
4. `python3 tools/fetch_imgs.py data`: download photos, then `data/img/` (not committed).
5. `python3 tools/dump.py data`: one text dump per project, used for writing stories, then `data/sections.json`.
6. `python3 tools/build.py .`: build the site into `site/`.
