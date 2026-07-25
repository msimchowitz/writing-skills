#!/usr/bin/env python3
"""Install this repository's skills without overwriting existing entries."""

import argparse
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path


DEPENDENCY_RE = re.compile(
    r"(?<!\.\./)\.\./([a-z0-9][a-z0-9-]*)/"
)
COPY_IGNORE = shutil.ignore_patterns(
    ".DS_Store",
    "__pycache__",
    "*.pyc",
    "*.pyo",
)


def repository_root():
    return Path(__file__).resolve().parents[1]


def default_destination():
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        base = Path(os.path.expandvars(codex_home)).expanduser()
    else:
        base = Path.home() / ".codex"
    return base / "skills"


def expand_path(raw_path):
    return Path(os.path.expandvars(raw_path)).expanduser().resolve()


def discover_skills(skills_root):
    skills = {}
    if not skills_root.is_dir():
        return skills
    for child in sorted(skills_root.iterdir(), key=lambda path: path.name):
        if child.is_dir() and (child / "SKILL.md").is_file():
            skills[child.name] = child.resolve()
    return skills


def direct_dependencies(skill_path, known_names):
    content = (skill_path / "SKILL.md").read_text(encoding="utf-8")
    referenced = set(DEPENDENCY_RE.findall(content))
    return referenced.intersection(known_names)


def dependency_closure(requested, skills):
    known_names = set(skills)
    selected = set()
    pending = list(requested)

    while pending:
        name = pending.pop()
        if name in selected:
            continue
        selected.add(name)
        pending.extend(
            sorted(direct_dependencies(skills[name], known_names) - selected)
        )

    return selected


def destination_exists(path):
    return path.exists() or path.is_symlink()


def points_to_source(destination, source):
    if not destination.is_symlink():
        return False
    try:
        return destination.resolve() == source.resolve()
    except OSError:
        return False


def copy_skill(source, destination):
    destination_parent = destination.parent
    with tempfile.TemporaryDirectory(
        prefix=".writing-skills-install-", dir=str(destination_parent)
    ) as temporary:
        staged = Path(temporary) / destination.name
        shutil.copytree(source, staged, ignore=COPY_IGNORE)
        staged.replace(destination)


def install_one(source, destination, copy_mode, dry_run):
    if destination_exists(destination):
        if not copy_mode and points_to_source(destination, source):
            return "current", "already linked"
        return "conflict", "destination already exists"

    action = "COPY" if copy_mode else "LINK"
    if dry_run:
        return "planned", action

    try:
        if copy_mode:
            copy_skill(source, destination)
        else:
            relative_source = os.path.relpath(source, start=destination.parent)
            destination.symlink_to(relative_source, target_is_directory=True)
    except OSError as error:
        return "error", str(error)

    return "installed", action


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Install skill directories found under for-agents/. "
            "Existing destinations are never overwritten."
        )
    )
    parser.add_argument(
        "skills",
        nargs="*",
        help="skill names to install; omit to install every discovered skill",
    )
    parser.add_argument(
        "--dest",
        metavar="PATH",
        help=(
            "skill directory to use; defaults to "
            "${CODEX_HOME:-$HOME/.codex}/skills"
        ),
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="copy independent snapshots instead of creating links",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show the operations without changing the filesystem",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="list discovered skills and exit",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    root = repository_root()
    skills_root = root / "for-agents"
    skills = discover_skills(skills_root)
    if not skills:
        print(
            "ERROR: no skill directories found under for-agents/",
            file=sys.stderr,
        )
        return 1

    if args.list:
        for name in skills:
            print(name)
        return 0

    requested = args.skills or list(skills)
    unknown = sorted(set(requested) - set(skills))
    if unknown:
        parser.error(
            "unknown skill name(s): "
            + ", ".join(unknown)
            + "; use --list to inspect available names"
        )

    selected = dependency_closure(requested, skills)
    added_dependencies = sorted(selected - set(requested))
    destination_root = (
        expand_path(args.dest) if args.dest else default_destination().resolve()
    )

    print(f"Repository: {root}")
    print(f"Skill source: {skills_root}")
    print(f"Destination: {destination_root}")
    print(f"Mode: {'copy' if args.copy else 'link'}")
    if added_dependencies:
        print("Added dependencies: " + ", ".join(added_dependencies))

    if not args.dry_run:
        destination_root.mkdir(parents=True, exist_ok=True)

    counts = {
        "installed": 0,
        "planned": 0,
        "current": 0,
        "conflict": 0,
        "error": 0,
    }

    for name in sorted(selected):
        source = skills[name]
        destination = destination_root / name
        status, detail = install_one(
            source=source,
            destination=destination,
            copy_mode=args.copy,
            dry_run=args.dry_run,
        )
        counts[status] += 1
        print(f"{status.upper():8} {name}: {detail}")

    if counts["conflict"] or counts["error"]:
        if counts["error"] and not args.copy:
            print(
                "A platform that restricts symlinks may require --copy.",
                file=sys.stderr,
            )
        print(
            "Installation stopped short of replacing existing or failed entries.",
            file=sys.stderr,
        )
        return 1

    if args.dry_run:
        print(f"Dry run complete: {counts['planned']} operation(s) planned.")
    else:
        print(
            "Install complete: "
            f"{counts['installed']} installed, {counts['current']} already current."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
