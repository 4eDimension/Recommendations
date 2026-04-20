SHELL := /bin/zsh

SOURCE_DOCX ?= /Applications/4D/Git/Recommendations/Preconisations_4D.docx
RAW_MARKDOWN ?= /tmp/recommendations_raw.md

.PHONY: help regenerate build serve

help:
	@echo "Targets disponibles:"
	@echo "  make regenerate SOURCE_DOCX=/chemin/vers/Preconisations_4D.docx"
	@echo "  make build"
	@echo "  make serve"

regenerate:
	python3 scripts/regenerate_site.py \
		--source-docx "$(SOURCE_DOCX)" \
		--repo-root . \
		--raw-markdown "$(RAW_MARKDOWN)"

build:
	python3 -m mkdocs build --strict

serve:
	python3 -m mkdocs serve
