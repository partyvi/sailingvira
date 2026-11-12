# Sailing Vira

The rebuild of *Vira*, a 1978 Irwin Citation 34: the diary from
[irwin34.blogspot.com](https://irwin34.blogspot.com), regrouped by project and told as stories.
The site will be published at **sailingvira.com**.

## What's here

| Path | What it is |
|---|---|
| `content/sections.yml` | The site sections and their order. |
| `content/en/projects/` | One story per project: front matter plus plain Markdown (format in `CLAUDE.md`). |
| `data/` | The blog split into dated sections with photo ids, and the photo URL list. |
| `tools/build.py` | Builds the site into `site/`. |
| `tools/` (other scripts) | Read the blog and sort new diary posts into projects. |

## Build

```bash
pip install -r requirements.txt
python3 tools/build.py .
```

The result is in `site/index.html`.

## Reading the blog (used for updates)

Every script takes the folder it works in as its argument.

1. Download the blog feed into `data/` (`feed_1.json`, `feed_151.json`, `pages.json`).
2. `python3 tools/parse.py data`: split posts into sections, then `data/parsed.json`.
3. `python3 tools/classify.py data`: assign each section to a project, then `data/classified.json`.
4. `python3 tools/dump.py data`: one text dump per project, and `data/sections.json`.
5. `python3 tools/fetch_imgs.py data`: optional, downloads photos to `data/img/` (not committed).
