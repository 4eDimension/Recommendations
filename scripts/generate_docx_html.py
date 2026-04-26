#!/usr/bin/env python3
"""Generate standalone DOCX-faithful HTML exports from source DOCX files.

Outputs to site/export/ (FR) and site/en/export/ (EN) so they are
published alongside the MkDocs site on GitHub Pages.

Usage:
    python3 scripts/generate_docx_html.py [--site-dir <path>]

Arguments:
    --site-dir  Path to the MkDocs output directory (default: site/)
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

EXPORTS = [
    {
        "docx": REPO_ROOT / "Preconisations_4D.docx",
        "output_rel": "export/preconisations-fr.html",
        "title": "Préconisations 4D",
        "lang": "fr",
    },
    {
        "docx": REPO_ROOT / "Recommendations-4D-apps-EN.docx",
        "output_rel": "en/export/recommendations-en.html",
        "title": "4D Application Recommendations",
        "lang": "en",
    },
]


def check_pandoc() -> None:
    if shutil.which("pandoc") is None:
        print("ERROR: pandoc is not installed.", file=sys.stderr)
        print("Install with: sudo apt-get install -y pandoc  (Linux)", file=sys.stderr)
        print("          or: brew install pandoc             (macOS)", file=sys.stderr)
        sys.exit(1)


def postprocess_html(html: str) -> str:
    """Fix common DOCX→HTML artefacts.

    1. Remove empty heading tags (Word section breaks → <h1></h1>).
    2. Remove the DOCX-generated TOC section (heading "Table des matières" /
       "Table of Contents" + following <p> blocks) that duplicates the
       Pandoc-generated <nav id="TOC">.
    3. Remove dead entries from the Pandoc-generated <nav id="TOC">:
       - <li> with empty <a> text (corresponding to removed empty headings)
       - <li> pointing to "Table des matières" / "Table of Contents"
    """
    # 1. Strip empty headings (any level, optional attributes, optional whitespace)
    html = re.sub(r'<h[1-6][^>]*>\s*</h[1-6]>', '', html)

    # 2. Remove DOCX TOC section:
    #    <h…>…Table des matières… / …Table of Contents…</h…>
    #    followed by zero or more <p …>…</p> blocks (the TOC link lines)
    #    The pattern stops at the first non-<p> element (the real Introduction).
    html = re.sub(
        r'<h\d[^>]*>[^<]*(?:Table\s+(?:des\s+mati[eè]res|of\s+Contents))[^<]*</h\d>'
        r'(?:\s*<p[^>]*>(?:(?!<p|<h\d).)*?</p>)*',
        '',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 3a. Remove <li> items in the Pandoc TOC whose <a> text is empty
    #     (= entries for the removed empty headings)
    html = re.sub(r'<li><a\s[^>]*>\s*</a></li>', '', html)

    # 3b. Remove <li> items pointing to the DOCX TOC heading
    html = re.sub(
        r'<li><a\s[^>]*>\s*Table\s+(?:des\s+mati[eè]res|of\s+Contents)\s*</a></li>',
        '',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    return html


def generate_html(docx: Path, output: Path, css: Path, title: str, lang: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "pandoc",
        str(docx),
        "--standalone",
        "--embed-resources",
        "--from", "docx",
        "--to", "html5",
        "--toc",
        "--toc-depth=2",
        "--css", str(css),
        "--metadata", f"title={title}",
        "--metadata", f"lang={lang}",
        "-o", str(output),
    ]

    print(f"  Generating {output.relative_to(REPO_ROOT)} …")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: pandoc failed for {docx.name}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

    # Post-process: fix DOCX artefacts (empty headings, duplicate TOC)
    raw = output.read_text(encoding="utf-8")
    cleaned = postprocess_html(raw)
    output.write_text(cleaned, encoding="utf-8")

    size_kb = output.stat().st_size // 1024
    print(f"  Done — {size_kb} KB")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--site-dir",
        default=str(REPO_ROOT / "site"),
        help="MkDocs output directory (default: site/)",
    )
    args = parser.parse_args()

    site_dir = Path(args.site_dir)
    css = REPO_ROOT / "docs" / "assets" / "stylesheets" / "docx-faithful.css"

    check_pandoc()

    if not css.exists():
        print(f"ERROR: CSS file not found: {css}", file=sys.stderr)
        sys.exit(1)

    print("Generating DOCX-faithful HTML exports …")
    for export in EXPORTS:
        docx: Path = export["docx"]  # type: ignore[assignment]
        if not docx.exists():
            print(f"  WARNING: DOCX not found, skipping: {docx}", file=sys.stderr)
            continue
        output = site_dir / export["output_rel"]
        generate_html(
            docx=docx,
            output=output,
            css=css,
            title=export["title"],  # type: ignore[arg-type]
            lang=export["lang"],  # type: ignore[arg-type]
        )

    print("Export generation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
