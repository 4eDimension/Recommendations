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
