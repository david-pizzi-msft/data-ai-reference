# Copilot instructions for data-ai-reference

This repo is a **MkDocs Material** documentation site — a personal quick-reference for
Microsoft Fabric, Fabric IQ, and Agentic AI. There is no application code; the product
is the published site at <https://david-pizzi-msft.github.io/data-ai-reference/>.

## Golden rules

- **Edit Markdown under `docs/` only.** Never edit anything in `site/` — it is generated
  output from `mkdocs build` and is overwritten on every build.
- **Register every new page in `mkdocs.yml` `nav`.** A page that is not in `nav` will not
  appear in navigation, and `mkdocs build --strict` (used in CI) fails on warnings such as
  pages missing from `nav` or broken links.
- Keep content **concise and scannable** — this is reference material pulled up during
  customer calls, not long-form prose. Prefer short intros, bullet points, and tables.

## Project layout

- `docs/` — all authored content, grouped by topic: `fabric/`, `fabric-iq/`, `agentic-ai/`.
  Each section has an `index.md` (Material `navigation.indexes` uses these as section landing
  pages).
- `docs/assets/` — images and the Microsoft logo. `docs/stylesheets/extra.css` — custom CSS.
- `mkdocs.yml` — site config, theme, markdown extensions, and the `nav` tree.
- `scripts/check_sources.py` — freshness checker (see below).
- `.github/workflows/deploy.yml` — builds with `mkdocs build --strict` and deploys to Pages
  on push to `main`.
- `.github/workflows/check-sources.yml` — runs the freshness check weekly (Mon 07:00 UTC).

## Content conventions

- Page title is a single top-level `# Heading`.
- Link to the canonical Microsoft Learn page near the top (e.g. `[Official docs](URL)`).
- Use Material admonitions (`!!! note`, `!!! info`), tabbed blocks (`pymdownx.tabbed`), and
  fenced code via `pymdownx.superfences`. These extensions are already enabled in `mkdocs.yml`.
- Unfinished pages use a placeholder line like `` `Placeholder — add your notes here.` `` —
  keep that pattern for stubs.

### Source freshness tags (important)

Curated pages that summarise a Learn article carry a tracking line in this **exact** format,
which `scripts/check_sources.py` parses with a regex:

```
*Curated from [Microsoft Learn](https://learn.microsoft.com/...) · Updated YYYY-MM-DD*
```

- The separator is a middle dot `·` (U+00B7), and the date is the Learn page's `ms.date`.
- When updating a curated summary, bump the date to match the live Learn `ms.date`.
- Do not change this line's structure — the checker depends on it.

## Local workflow

```bash
pip install -r requirements.txt
mkdocs serve          # hot-reload preview at http://127.0.0.1:8000
mkdocs build --strict # mirror CI; must pass before pushing
python scripts/check_sources.py  # verify curated pages aren't behind Learn
```

Push to `main` → GitHub Actions auto-deploys. There are no tests beyond the strict build
and the source-freshness check.
