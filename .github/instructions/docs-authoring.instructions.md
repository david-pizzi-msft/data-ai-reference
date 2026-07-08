---
applyTo: "docs/**/*.md"
---

# Authoring docs pages

These rules apply to every Markdown page under `docs/`. The site is **MkDocs Material**
and is built with `mkdocs build --strict` in CI, so warnings (missing nav entries, broken
links) fail the build.

## Structure

- Start with a single top-level `# Title` heading — one per page.
- Put the canonical Microsoft Learn link near the top, e.g. `[Official docs](URL)`.
- Keep it concise and scannable: short intro, then bullets and tables. This is call-time
  reference material, not long-form prose.
- For an unfinished page, use the stub line `` `Placeholder — add your notes here.` ``.

## Workshop / lab log pages

Pages under `docs/fabric/learning-journey/workshops/` are a personal working log. Use only
these trailing sections — a `## Notes` section (running observations) and a `## Key takeaways`
section (populated once the lab is done). Do **not** add a `## Follow-ups` section; it was
never used and has been removed.


## After adding or renaming a page

- Add it to the `nav` tree in `mkdocs.yml` — unlisted pages don't appear in navigation and
  trip the strict build.
- Section landing pages are `index.md` files (Material `navigation.indexes`).

## Material features available (already enabled in `mkdocs.yml`)

- Admonitions: `!!! note`, `!!! info`, and collapsible `pymdownx.details`.
- Tabbed content: `pymdownx.tabbed` (alternate style).
- Fenced code with copy + annotations via `pymdownx.superfences`.
- Tables, `attr_list`, `md_in_html`, emoji, and image lightbox (`glightbox`).

## Curated-summary freshness tag

When a page summarises a Microsoft Learn article, end it with this **exact** line — the
separator is a middle dot `·` (U+00B7) and the date is the Learn page's `ms.date`:

```
*Curated from [Microsoft Learn](https://learn.microsoft.com/...) · Updated YYYY-MM-DD*
```

`scripts/check_sources.py` parses this with a regex, so do not alter its structure. When you
revise a summary, bump the date to match the live Learn `ms.date`.

## Don't

- Never edit files under `site/` — that's generated build output.
- Don't break the strict build with broken internal links or images.
