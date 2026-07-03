#!/usr/bin/env python3
"""Write a PDF-specific MkDocs config with a dated cover subtitle."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

import yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="mkdocs.yml")
    parser.add_argument("--output", default="_mkdocs_pdf.yml")
    args = parser.parse_args()

    source = Path(args.input)
    target = Path(args.output)
    config = yaml.safe_load(source.read_text())

    build_date = datetime.now().strftime("%B %-d, %Y")
    subtitle = f"A rendering of Read the Docs as of {build_date}"

    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "to-pdf" in plugin:
            plugin["to-pdf"]["cover_subtitle"] = subtitle
            break
    else:
        raise SystemExit("to-pdf plugin not found in MkDocs config")

    target.write_text(yaml.safe_dump(config, sort_keys=False))


if __name__ == "__main__":
    main()
