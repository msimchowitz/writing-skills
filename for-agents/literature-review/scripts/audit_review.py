#!/usr/bin/env python3
"""Audit citations, bibliography keys, placeholders, and a literature-review ledger."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


CITATION_RE = re.compile(
    r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|parencite|textcite)"
    r"(?:\[[^\]]*\]){0,2}\{([^}]*)\}"
)
BIB_KEY_RE = re.compile(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,")
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD)\b|\\authorcomment\b|Paper title|Author One|Author Two",
    re.IGNORECASE,
)
REQUIRED_LEDGER_FIELDS = {
    "source_id",
    "bib_key",
    "title",
    "year",
    "url",
    "claims_supported",
    "evidence_location",
    "disclosure_status",
}
VALID_DISCLOSURE_STATES = {
    "reported",
    "derived",
    "inferred",
    "conflicting",
    "not-disclosed",
}


def strip_latex_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())


def project_files(root: Path, suffix: str) -> list[Path]:
    return sorted(
        path
        for path in root.rglob(f"*{suffix}")
        if "build" not in path.parts and ".git" not in path.parts
    )


def find_ledger(root: Path, explicit: Path | None) -> Path | None:
    if explicit:
        return explicit
    candidates = [root / "research" / "source-ledger.csv", root / "source-ledger.csv"]
    return next((path for path in candidates if path.exists()), None)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path, help="Literature-review project root")
    parser.add_argument("--ledger", type=Path, help="Optional source-ledger CSV path")
    args = parser.parse_args()

    root = args.project.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    tex_files = project_files(root, ".tex")
    if not tex_files:
        errors.append("no .tex files found")

    citation_keys: set[str] = set()
    placeholders: list[str] = []
    for path in tex_files:
        text = strip_latex_comments(path.read_text(encoding="utf-8"))
        for match in CITATION_RE.finditer(text):
            citation_keys.update(
                key.strip() for key in match.group(1).split(",") if key.strip()
            )
        for line_number, line in enumerate(text.splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                placeholders.append(f"{path.relative_to(root)}:{line_number}")

    bib_files = project_files(root, ".bib")
    bib_keys: set[str] = set()
    for path in bib_files:
        bib_keys.update(BIB_KEY_RE.findall(path.read_text(encoding="utf-8")))

    missing_bib = sorted(citation_keys - bib_keys)
    uncited_bib = sorted(bib_keys - citation_keys)
    if missing_bib:
        errors.append(f"citation keys missing from bibliography: {', '.join(missing_bib)}")
    if uncited_bib:
        warnings.append(f"uncited bibliography keys: {', '.join(uncited_bib)}")
    if placeholders:
        errors.append(f"unresolved placeholders: {', '.join(placeholders)}")

    ledger_path = find_ledger(root, args.ledger)
    ledger_rows = 0
    if ledger_path is None:
        warnings.append("source ledger not found")
    else:
        with ledger_path.open(newline="", encoding="utf-8") as stream:
            reader = csv.DictReader(stream)
            headers = set(reader.fieldnames or [])
            missing_headers = sorted(REQUIRED_LEDGER_FIELDS - headers)
            if missing_headers:
                errors.append(
                    "source ledger missing columns: " + ", ".join(missing_headers)
                )
            for row_number, row in enumerate(reader, start=2):
                ledger_rows += 1
                missing_values = sorted(
                    field for field in REQUIRED_LEDGER_FIELDS if not row.get(field, "").strip()
                )
                if missing_values:
                    errors.append(
                        f"{ledger_path.name}:{row_number} missing values: "
                        + ", ".join(missing_values)
                    )
                state = row.get("disclosure_status", "").strip()
                if state and state not in VALID_DISCLOSURE_STATES:
                    errors.append(
                        f"{ledger_path.name}:{row_number} invalid disclosure_status: {state}"
                    )
                bib_key = row.get("bib_key", "").strip()
                if bib_key and bib_key not in bib_keys:
                    errors.append(
                        f"{ledger_path.name}:{row_number} unknown bib_key: {bib_key}"
                    )

    print(f"TeX files: {len(tex_files)}")
    print(f"Citations: {len(citation_keys)}")
    print(f"Bibliography entries: {len(bib_keys)}")
    print(f"Ledger rows: {ledger_rows}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
