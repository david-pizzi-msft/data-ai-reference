#!/usr/bin/env python3
"""Check curated docs against their Microsoft Learn sources.

Each curated page records the Learn page's last-updated date in a
"Source & freshness" admonition, for example:

    !!! info "Source & freshness"
        Curated summary of the [official Microsoft Learn documentation](URL).
        Verified against Learn's last update: **2026-05-11**. ...

This script extracts every (URL, recorded-date) pair from docs/, fetches the
live page, reads its ``ms.date`` meta tag, and reports any page whose recorded
date is behind the live date (i.e. the source changed and the summary may need
review).

Exit code 0 = all up to date, 1 = at least one page is stale or could not be
checked. Run it manually or from CI (see .github/workflows).
"""
from __future__ import annotations

import pathlib
import re
import sys
import urllib.request

DOCS_DIR = pathlib.Path(__file__).resolve().parent.parent / "docs"
USER_AGENT = "data-ai-reference-source-check/1.0"

# Captures the Learn URL and the recorded date from the compact source tag:
#   *Curated from [Microsoft Learn](URL) · Updated 2025-10-06*
PAIR_RE = re.compile(
    r"Curated from \[Microsoft Learn\]\((https://learn\.microsoft\.com[^)]+)\)"
    r"\s*\u00b7\s*Updated\s*(\d{4}-\d{2}-\d{2})",
)
MS_DATE_RE = re.compile(r'<meta\s+name="ms\.date"\s+content="(\d{4}-\d{2}-\d{2})')


def fetch_ms_date(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    match = MS_DATE_RE.search(html)
    return match.group(1) if match else None


def main() -> int:
    pairs: list[tuple[pathlib.Path, str, str]] = []
    for md in sorted(DOCS_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for url, recorded in PAIR_RE.findall(text):
            pairs.append((md, url, recorded))

    if not pairs:
        print("No source-tracked pages found.")
        return 0

    stale = 0
    errors = 0
    stale_rows: list[str] = []
    for md, url, recorded in pairs:
        rel = md.relative_to(DOCS_DIR.parent).as_posix()
        try:
            live = fetch_ms_date(url)
        except Exception as exc:  # network / HTTP error
            print(f"ERROR  {rel}\n       {url}\n       could not fetch: {exc}")
            errors += 1
            continue
        if live is None:
            print(f"ERROR  {rel}\n       {url}\n       no ms.date found on page")
            errors += 1
        elif live > recorded:
            print(f"STALE  {rel}\n       {url}\n       recorded {recorded} -> Learn now {live}")
            stale_rows.append(f"| `{rel}` | {url} | {recorded} | {live} |")
            stale += 1
        elif live < recorded:
            print(f"ahead  {rel} (recorded {recorded} newer than Learn {live}) - verify")
        else:
            print(f"ok     {rel} ({recorded})")

    print(f"\n{len(pairs)} page(s) checked - {stale} stale, {errors} error(s).")

    if stale_rows:
        report = (
            "The scheduled freshness check found curated pages whose Microsoft "
            "Learn source has a newer `ms.date` than the date recorded on our "
            "page. Review and update these summaries to match the latest Learn "
            "content.\n\n"
            "## Stale pages\n\n"
            "| Page | Learn source | Recorded date | Learn date |\n"
            "| --- | --- | --- | --- |\n"
            + "\n".join(stale_rows)
            + "\n\n## What to do\n\n"
            "For each page above:\n\n"
            "1. Re-read the linked Learn page and update the summary where it "
            "has changed.\n"
            "2. Bump the date in that page's `Curated from ... Updated <date>` "
            "line to the new Learn date.\n"
            "3. Run `python scripts/check_sources.py` and confirm it reports "
            "`ok` for every page.\n"
        )
        pathlib.Path("source-check-report.md").write_text(report, encoding="utf-8")
        print("\nWrote source-check-report.md")

    return 1 if (stale or errors) else 0


if __name__ == "__main__":
    sys.exit(main())
