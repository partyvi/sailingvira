# CLAUDE.md: sailingvira

Project site for **Vira**, a 1978 Irwin Citation 34 being rebuilt by Viktor. The site turns the
day-by-day Blogger diary (https://irwin34.blogspot.com) into project stories.
The site will be published at **sailingvira.com**. The domain currently redirects to the blog.

## Agreed decisions (keep to these; ask before changing them)

- **Audience:** public. Irwin owners, DIY boaters, sailors, search engines. Every project gets its own page and URL.
- **Languages:** English and Ukrainian from the start (`/engine/` and `/uk/engine/`). Every update is written in both.
- **Structure:** 2 levels. 6 sections, 23 sub-projects (see `tools/structure.json`).
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
2. Stories to CMS-friendly Markdown (front matter + readable photo blocks).
3. New build: page per project, EN/UK, photos from Blogger, sitemap, noindex switch.
4. GitHub Actions deploys to GitHub Pages.
5. Ukrainian translation of all stories.
6. Pages CMS set-up and test.
7. First real diary update as a PR.
8. Go public: sailingvira.com DNS to GitHub Pages, HTTPS, Search Console, link from Blogger.
Later: scheduled updates, auto-publish, diary moves into the site.

## How to work with Viktor

- Ask questions **one at a time**, and wait for the answer before the next.
- Go step by step. Propose, then wait for confirmation before large changes.
- Changes after the first commit go as pull requests.

## Repository layout

- `stories/<project>.md`: one story per sub-project. The current format:
  - `## Heading` starts a chapter.
  - A plain line is a paragraph. `- ` is a list item.
  - `@s552 s553:1-3` is a photo gallery: all photos of diary section s552, then photos 1-3 of s553.
  - `skip: s27:13-30` marks photos as intentionally not shown (duplicates).
  - Photos of a referenced section that are not placed anywhere are appended automatically after its last reference.
- `data/classified.json`: every post and page of the blog, split into sections (headings), with text,
  photo ids, original photo URLs and the assigned project.
- `data/sections.json`: section key (`s123`) → date, post title, URL, project, photo ids.
- `data/photos.json`: photo id → Blogger photo URL.
- `tools/structure.json`: sections and sub-projects (id, title, one-line description).
- `tools/`: pipeline scripts (see README).
