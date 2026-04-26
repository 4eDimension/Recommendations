#!/usr/bin/env python3
"""Regenerate the Recommendations MkDocs site from a DOCX source.

Pipeline:
1. Convert DOCX to markdown with pandoc and extract media.
2. Split markdown into chapter files using a fixed chapter list.
3. Normalize known pandoc artifacts (underline markers and escaped apostrophes).
4. Regenerate mkdocs.yml navigation from chapter list.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path


CHAPTER_TITLES = [
    "Introduction",
    "Recommandations générales",
    "Numéros de port",
    "Processeur",
    "Système d'exploitation",
    "Mémoire",
    "Disque dur",
    "Sauvegarde / Opérations de maintenance",
    "Réseau",
    "Web",
    "Machine physique ou virtuelle",
    "Marque / Modèle de machine",
    "Tests / Recette / Déploiement",
    "Propriétés de la base",
    "Général",
    "Compilateur",
    "Base de données / Stockage des données",
    "Base de données / Mémoire",
    "Sauvegarde / Périodicité",
    "Sauvegarde / Configuration",
    "Sauvegarde / Sauvegarde & restitution",
    "Client-Serveur / Option réseau",
    "Client-Serveur / Configuration IP",
    "Web / Configuration",
    "Web / Options (I)",
    "Web / Options (II)",
    "Compatibilité",
    "Sécurité",
    "4D Server",
    "Serveur Web",
    "Serveur SOAP",
    "Serveur SQL",
    "Système de mot de passe 4D",
    "Mécanisme de mise à jour logicielle",
    "Système de sauvegarde et de journalisation",
    "Protection additionnelle",
    "Surveillance du serveur",
]

CHAPTER_TITLES_EN = [
    "Introduction",
    "General recommendations",
    "Port numbers",
    "Processor",
    "Operating system",
    "Memory",
    "Hard disk",
    "Backup / Maintenance operations",
    "Network",
    "Web",
    "Physical or virtual machine",
    "Manufacturer / Model of machine",
    "Tests / Acceptance / Deployment",
    "Properties of the database",
    "General",
    "Compiler",
    "Database / Data storage",
    "Database / Memory",
    "Backup / Frequency",
    "Backup / Configuration",
    "Backup / Backup & restore",
    "Client-Server / Network option",
    "Client-Server / IP Configuration",
    "Web / Configuration",
    "Web / Options (I)",
    "Web / Options (II)",
    "Compatibility",
    "Security",
    "4D Server",
    "Web server",
    "SOAP server",
    "SQL server",
    "4D password system",
    "Software update mechanism",
    "Backup and logging system",
    "Additional Protection",
    "Server monitoring",
]

LANG_CONFIG: dict = {
    "fr": {
        "chapter_titles": CHAPTER_TITLES,
        "site_name": "Préconisations 4D",
        "site_description": "Guide de préconisations 4D",
        "site_url": "https://4edimension.github.io/Recommendations/",
        "docs_dir": "docs",
        "mkdocs_file": "mkdocs.yml",
        "language": "fr",
        "search_lang": "fr",
        "git_locale": "fr",
        "index_link_text": "Commencer la lecture",
        "index_chapter2_slug": "02-recommandations-generales",
        "index_chapter2_title": "Recommandations générales",
        "nav_sections": [
            ("Démarrage", 1, 3),
            ("Infrastructure", 3, 13),
            ("Configuration base", 13, 18),
            ("Exploitation et réseau", 18, 23),
            ("Web et sécurité", 23, 28),
            ("Serveurs", 28, None),
        ],
        "toggle_auto": "Basculer en mode clair",
        "toggle_light": "Basculer en mode sombre",
        "toggle_dark": "Basculer en mode clair",
    },
    "en": {
        "chapter_titles": CHAPTER_TITLES_EN,
        "site_name": "4D Recommendations",
        "site_description": "4D Recommendations Guide",
        "site_url": "https://4edimension.github.io/Recommendations/en/",
        "docs_dir": "docs_en",
        "mkdocs_file": "mkdocs_en.yml",
        "language": "en",
        "search_lang": "en",
        "git_locale": "en",
        "index_link_text": "Start reading",
        "index_chapter2_slug": "02-general-recommendations",
        "index_chapter2_title": "General recommendations",
        "nav_sections": [
            ("Getting Started", 1, 3),
            ("Infrastructure", 3, 13),
            ("Base Configuration", 13, 18),
            ("Operations and Network", 18, 23),
            ("Web and Security", 23, 28),
            ("Servers", 28, None),
        ],
        "toggle_auto": "Switch to light mode",
        "toggle_light": "Switch to dark mode",
        "toggle_dark": "Switch to light mode",
    },
}


def normalize_text(value: str) -> str:
    value = value.replace("’", "'").replace("`", "'")
    value = "".join(
        ch for ch in unicodedata.normalize("NFD", value) if unicodedata.category(ch) != "Mn"
    )
    value = re.sub(r"\s+", " ", value.lower().strip())
    return value


def slugify(value: str) -> str:
    value = normalize_text(value).replace("'", "")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "chapitre"


def run_pandoc(source_docx: Path, raw_markdown: Path, docs_assets: Path) -> None:
    if shutil.which("pandoc") is None:
        raise RuntimeError("pandoc is not installed or not found in PATH")

    docs_assets.mkdir(parents=True, exist_ok=True)
    command = [
        "pandoc",
        str(source_docx),
        "--extract-media",
        str(docs_assets),
        "-t",
        "markdown",
        "-o",
        str(raw_markdown),
    ]
    subprocess.run(command, check=True)


def collect_boundaries(lines: list[str], chapter_titles: list[str]) -> list[tuple[int, str]]:
    heading_re = re.compile(r"^(#{1,6})\s*(.*)$")
    title_lookup = {normalize_text(title): title for title in chapter_titles}

    boundaries: list[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        match = heading_re.match(line)
        if not match:
            continue
        title = match.group(2).strip()
        if not title:
            continue

        normalized = normalize_text(title)
        if normalized == normalize_text("Table des matières"):
            continue
        if normalized in title_lookup:
            boundaries.append((idx, title_lookup[normalized]))

    dedup: dict[str, tuple[int, str]] = {}
    for idx, title in boundaries:
        normalized = normalize_text(title)
        if normalized not in dedup:
            dedup[normalized] = (idx, title)

    ordered: list[tuple[int, str]] = []
    missing: list[str] = []
    for title in chapter_titles:
        normalized = normalize_text(title)
        entry = dedup.get(normalized)
        if entry is None:
            missing.append(title)
        else:
            ordered.append(entry)

    if missing:
        raise RuntimeError(
            "Missing chapter headings in converted markdown: " + ", ".join(missing)
        )

    return ordered


def clean_chapter_content(text: str, docs_dir_name: str = "docs") -> tuple[str, int, int]:
    # Convert [text]{.underline} into HTML underline for MkDocs rendering.
    underline_pat = re.compile(r"\[(.*?)\]\{\.underline\}")
    text, underline_count = underline_pat.subn(r"<u>\1</u>", text)

    # Remove escaped apostrophes introduced by pandoc export.
    apostrophe_count = text.count("\\'")
    text = text.replace("\\'", "'")

    # Remove image attribute blocks generated by pandoc when they leak into page text.
    # Example: ![](../assets/media/image.png){width="7.8in"\nheight="4.0in"}
    text = re.sub(r"(!\[[^\]]*\]\([^\)]+\))\{[^}]*\}", r"\1", text, flags=re.DOTALL)

    # Python-Markdown is stricter than some renderers.
    # Normalize bullet indentation so nested levels stay nested in HTML:
    # level-2 bullets: 2 -> 4 spaces, level-3 bullets: 4 -> 8 spaces.
    text = re.sub(r"(?m)^    (?=[-*]\s)", "        ", text)
    text = re.sub(r"(?m)^  (?=[-*]\s)", "    ", text)

    # Fix image paths (docs_dir_name/assets/ → ../assets/ relative to chapitres/)
    text = text.replace(f"({docs_dir_name}/assets/", "(../assets/")
    text = text.replace(f"]({docs_dir_name}/assets/", "](../assets/")
    text = text.replace(f'"{docs_dir_name}/assets/', '"../assets/')

    # Normalize heading levels and remove duplicates
    text = normalize_heading_levels(text)
    text = remove_duplicate_headings(text)

    return text, underline_count, apostrophe_count


def normalize_heading_levels(text: str) -> str:
    """Ensure the first heading is H1, then maintain hierarchy H1→H2→H3+ for remaining headings."""
    lines = text.split('\n')
    if not lines:
        return text
    
    first_heading_idx = None
    first_level = None
    
    # Find the first heading
    heading_re = re.compile(r'^(#{1,6})\s')
    for idx, line in enumerate(lines):
        match = heading_re.match(line)
        if match:
            first_heading_idx = idx
            first_level = len(match.group(1))
            break
    
    if first_heading_idx is None:
        return text  # No headings found
    
    # Calculate shift needed to make first heading H1
    shift = 1 - first_level
    
    if shift == 0:
        return text  # Already starts at H1
    
    # Apply shift to all headings
    result = []
    for idx, line in enumerate(lines):
        match = heading_re.match(line)
        if match:
            current_level = len(match.group(1))
            new_level = max(1, min(6, current_level + shift))
            new_hashes = '#' * new_level
            rest = line[len(match.group(1)):]
            result.append(new_hashes + rest)
        else:
            result.append(line)
    
    return '\n'.join(result)


def remove_duplicate_headings(text: str) -> str:
    """Remove consecutive duplicate headings and filter empty headings."""
    lines = text.split('\n')
    if not lines:
        return text
    
    heading_re = re.compile(r'^(#{1,6})\s+(.*)$')
    result = []
    last_heading = None
    
    for line in lines:
        match = heading_re.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            
            # Skip empty headings
            if not title:
                continue
            
            # Skip if it's the same heading (level + title) as the last one
            current = (level, title)
            if current == last_heading:
                continue
            
            last_heading = current
        else:
            last_heading = None  # Reset on non-heading lines
        
        result.append(line)
    
    return '\n'.join(result)


def write_chapters(lines: list[str], boundaries: list[tuple[int, str]], chapters_dir: Path, docs_dir_name: str = "docs") -> tuple[list[tuple[str, str]], int, int]:
    if chapters_dir.exists():
        for file in chapters_dir.glob("*.md"):
            file.unlink()
    else:
        chapters_dir.mkdir(parents=True, exist_ok=True)

    chapter_files: list[tuple[str, str]] = []
    total_underline = 0
    total_apostrophes = 0

    for index, (start, title) in enumerate(boundaries):
        end = boundaries[index + 1][0] if index + 1 < len(boundaries) else len(lines)
        chunk = "\n".join(lines[start:end]).rstrip() + "\n"

        chunk, underline_count, apostrophe_count = clean_chapter_content(chunk, docs_dir_name)
        total_underline += underline_count
        total_apostrophes += apostrophe_count

        filename = f"{index + 1:02d}-{slugify(title)}.md"
        chapter_path = chapters_dir / filename
        chapter_path.write_text(chunk, encoding="utf-8")
        chapter_files.append((title, f"chapitres/{filename}"))

    return chapter_files, total_underline, total_apostrophes


def write_index_page(docs_dir: Path, chapters_dir: Path, chapter_files: list[tuple[str, str]], config: dict) -> None:
    if not chapter_files:
        raise RuntimeError("No chapter files generated; cannot build index.md")

    intro_relative = chapter_files[0][1]
    intro_filename = Path(intro_relative).name
    intro_path = chapters_dir / intro_filename
    if not intro_path.exists():
        raise FileNotFoundError(f"Missing introduction chapter file: {intro_path}")

    index_path = docs_dir / "index.md"
    intro_text = intro_path.read_text(encoding="utf-8").rstrip()
    link_text = config["index_link_text"]
    chapter2_slug = config["index_chapter2_slug"]
    chapter2_title = config["index_chapter2_title"]
    start_link = f"\n\n{link_text}: [{chapter2_title}](chapitres/{chapter2_slug}.md)\n"
    index_path.write_text(intro_text + start_link, encoding="utf-8")
    # Remove the standalone intro file – it is embedded in index.md and must not
    # appear as an unreferenced page (causes strict-mode warnings).
    intro_path.unlink(missing_ok=True)


def grouped_navigation(chapter_files: list[tuple[str, str]], config: dict) -> list[tuple[str, list[tuple[str, str]]]]:
    sections = []
    for name, start, end in config["nav_sections"]:
        entries = chapter_files[start:end]
        if entries:
            sections.append((name, entries))
    return sections


def write_mkdocs_config(mkdocs_path: Path, chapter_files: list[tuple[str, str]], config: dict) -> None:
    grouped_sections = grouped_navigation(chapter_files, config)
    docs_dir_name = config["docs_dir"]
    lang = config["language"]
    search_lang = config["search_lang"]
    git_locale = config["git_locale"]
    nav_lines = [
        f'site_name: "{config["site_name"]}"',
        f'site_description: "{config["site_description"]}"',
        f'site_url: "{config["site_url"]}"',
        'repo_url: "https://github.com/4eDimension/Recommendations"',
        'repo_name: "4eDimension/Recommendations"',
        f"docs_dir: {docs_dir_name}",
        "theme:",
        "  name: material",
        f"  language: {lang}",
        "  custom_dir: docs/overrides",
        "  palette:",
        "    - media: \"(prefers-color-scheme)\"",
        "      toggle:",
        "        icon: material/brightness-auto",
        f'        name: {config["toggle_auto"]}',
        "    - media: \"(prefers-color-scheme: light)\"",
        "      scheme: default",
        "      primary: blue",
        "      accent: light blue",
        "      toggle:",
        "        icon: material/weather-night",
        f'        name: {config["toggle_light"]}',
        "    - media: \"(prefers-color-scheme: dark)\"",
        "      scheme: slate",
        "      primary: blue",
        "      accent: light blue",
        "      toggle:",
        "        icon: material/weather-sunny",
        f'        name: {config["toggle_dark"]}',
        "  features:",
        "    - navigation.tabs",
        "    - navigation.tabs.sticky",
        "    - navigation.sections",
        "    - navigation.expand",
        "    - navigation.tracking",
        "    - navigation.top",
        "    - toc.follow",
        "    - content.code.copy",
        "    - search.suggest",
        "    - search.highlight",
        "    - search.share",
        "plugins:",
        "  - search:",
        f"      lang: {search_lang}",
        "      separator: '[\\\\s\\\\-]+'",
        "  - git-revision-date-localized:",
        f"      locale: {git_locale}",
        "      type: date",
        "      fallback_to_build_date: true",
        "markdown_extensions:",
        "  - toc:",
        "      permalink: true",
        "      toc_depth: 3",
        "  - attr_list",
        "  - admonition",
        "  - tables",
        "  - meta",
        "extra_css:",
        "  - assets/stylesheets/translate-switch.css",
        "extra:",
        "  generator: false",
        "nav:",
        '  - "Introduction": index.md',
    ]

    for section_name, entries in grouped_sections:
        nav_lines.append(f'  - "{section_name}":')
        for title, relative_path in entries:
            nav_lines.append(f'    - "{title}": {relative_path}')

    mkdocs_path.write_text("\n".join(nav_lines) + "\n", encoding="utf-8")


def write_sitemap(docs_dir: Path, chapter_files: list[tuple[str, str]], config: dict) -> None:
    base_url = config["site_url"]
    urls = [base_url]
    for _, relative_path in chapter_files[1:]:
        slug = Path(relative_path).stem + "/"
        urls.append(base_url + "chapitres/" + slug)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append("  </url>")
    lines.append("</urlset>")

    (docs_dir / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Regenerate docs/chapitres and mkdocs.yml from a DOCX file."
    )
    parser.add_argument(
        "--source-docx",
        required=True,
        help="Path to the source .docx file",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--raw-markdown",
        default="/tmp/recommendations_raw.md",
        help="Temporary markdown output path (default: /tmp/recommendations_raw.md)",
    )
    parser.add_argument(
        "--lang",
        choices=["fr", "en"],
        default="fr",
        help="Language to generate (fr or en, default: fr)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    source_docx = Path(args.source_docx).resolve()
    raw_markdown = Path(args.raw_markdown).resolve()

    lang = args.lang
    config = LANG_CONFIG[lang]
    docs_dir_name = config["docs_dir"]
    docs_dir = repo_root / docs_dir_name
    docs_assets = docs_dir / "assets"
    chapters_dir = docs_dir / "chapitres"
    mkdocs_path = repo_root / config["mkdocs_file"]

    if not source_docx.exists():
        raise FileNotFoundError(f"DOCX source not found: {source_docx}")

    # For EN, copy shared CSS/JS assets from docs/assets so MkDocs can serve them
    if lang == "en":
        fr_assets = repo_root / "docs" / "assets"
        for subdir in ("stylesheets", "javascripts"):
            src = fr_assets / subdir
            dst = docs_assets / subdir
            if src.exists():
                shutil.copytree(src, dst, dirs_exist_ok=True)

    run_pandoc(source_docx, raw_markdown, docs_assets)

    lines = raw_markdown.read_text(encoding="utf-8").splitlines()
    boundaries = collect_boundaries(lines, config["chapter_titles"])
    chapter_files, underline_count, apostrophe_count = write_chapters(
        lines, boundaries, chapters_dir, docs_dir_name
    )
    write_index_page(docs_dir, chapters_dir, chapter_files, config)
    write_mkdocs_config(mkdocs_path, chapter_files, config)
    write_sitemap(docs_dir, chapter_files, config)

    print(f"Generated {len(chapter_files)} chapter files in {chapters_dir}")
    print(f"Updated {mkdocs_path}")
    print(f"Underline marker replacements: {underline_count}")
    print(f"Escaped apostrophes fixed: {apostrophe_count}")
    print(f"Raw markdown output: {raw_markdown}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
