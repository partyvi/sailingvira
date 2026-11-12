# CLAUDE.md: sailingvira

Project site for **Vira**, a 1978 Irwin Citation 34 being rebuilt by Viktor. The site turns the
day-by-day Blogger diary (https://irwin34.blogspot.com) into project stories.
The site will be published at **sailingvira.com**. The domain currently redirects to the blog.

## Agreed decisions (keep to these; ask before changing them)

- **Audience:** public. Irwin owners, DIY boaters, sailors, search engines. Every project gets its own page and URL.
- **Languages:** English and Ukrainian from the start (`/engine/` and `/ua/engine/`; folders and keys use `ua`, the HTML language code stays `uk`). Every update is written in both.
- **Structure:** 2 levels. 6 sections (`content/sections.yml`), 24 projects (`content/en/projects/`).
- **Tone:** first person, Viktor's voice, "telling the story by a campfire". Simple, human, short sentences,
  his small jokes and reactions. Keep ALL facts, numbers, part names and prices. No generic explanations,
  no teacher tone.
- **Photos:** ALL diary photos go into the stories, in the place they belong. Photos are loaded from
  Blogger (googleusercontent) URLs. They are not copied into the repo.
- **Diary links:** every chapter links back to its original Blogger post(s).
- **Blogger stays the diary** for now. Later the diary moves into the site, so leave room for a "Diary" section.
- **New topics:** a diary topic that fits no project goes to a "Small projects" catch-all first. Once it has
  about 3+ entries, suggest promoting it to its own project. Viktor decides.
- **CMS:** Viktor has full control (Pages CMS): text, chapters, photos, new projects and sections.
  The story format must stay easy to edit by hand.
- **Updates:** for now Viktor asks ("update the site"); later a scheduled check. For now every update goes
  as a pull request that Viktor reviews; later Claude may publish directly.
- **Launch:** the site stays hidden from search engines (noindex) until Phase 5.

## Roadmap

1. Source on GitHub (done: first commit).
2. Stories to CMS-friendly Markdown (front matter + readable photo blocks) (done).
3. New build: page per project, EN/UK, photos from Blogger, sitemap, noindex switch (done).
4. GitHub Actions deploys to GitHub Pages (done: .github/workflows/pages.yml).
5. Ukrainian translation of all stories.
6. Pages CMS set-up and test.
7. First real diary update as a PR.
8. Go public: sailingvira.com DNS to GitHub Pages, HTTPS, Search Console, link from Blogger.
Later: scheduled updates, auto-publish, diary moves into the site.

## How to work with Viktor

- Ask questions **one at a time**, and wait for the answer before the next.
- Go step by step. Propose, then wait for confirmation before large changes.
- Changes after the first commit go as pull requests. Viktor asked (12 Nov 2026) that Claude merges its own
  pull requests and keeps going; stop and ask only for decisions that are his.

## Repository layout

- `content/sections.yml`: the site sections (`id`, `order`, `title.en`, `title.ua`).
- `content/en/projects/<id>.md`: one story per project. The file name is the project id and URL slug.
  - Front matter: `title`, `section` (a section id), `order` (position inside the section),
    `description` (one line), `cover` (photo URL for the project card).
  - Body is plain Markdown:
    - `## Heading` starts a chapter. Text before the first heading is the intro.
    - Paragraphs are separated by a blank line. `- ` is a list item. Inline Markdown works.
    - `![](url)` is a photo. Photos one after another (blank lines allowed) form one gallery.
    - `Diary: [28 May 2022](post url)` links the gallery or paragraph above to its diary post.
      `Story page: [Title](page url)` links to a Blogger story page. Several such lines may follow each other.
      Chapter dates and day numbers come from these links (looked up in `data/sections.json`).
  - Photo URLs are stored at size `s1600`. The build makes the small grid size (`w600`) itself.
- Ukrainian goes in `content/ua/projects/<id>.md` with the same ids (`python3 tools/translate.py merge <id> ua FILE`).
- `data/classified.json`: every post and page of the blog, split into sections (headings), with text,
  photo ids, original photo URLs and the assigned project.
- `data/sections.json`: section key (`s123`) → date, post title, URL, project, photo ids.
- `data/photos.json`: photo id → Blogger photo URL.
- `content/site.yml`: site name, base URL, `noindex` switch, home page texts (EN/UK).
- `tools/build.py`: builds the static site into `site/` (`pip install -r requirements.txt`):
  `/<id>/` and `/ua/<id>/` pages, home pages, sitemap.xml, robots.txt, 404.html. A project without a
  Ukrainian file shows the English text with a note. Styles and the photo viewer are in `tools/assets/`.
- `tools/`: other pipeline scripts used to read new diary posts (see README).
