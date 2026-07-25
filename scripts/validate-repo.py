#!/usr/bin/env python3
"""Validate the structure and portability of the writing-skills repository."""

import argparse
import ast
import filecmp
import re
import sys
from pathlib import Path
from urllib.parse import unquote


MAX_SKILL_NAME_LENGTH = 64
MAX_SKILL_LINES = 500
MAX_DESCRIPTION_LENGTH = 1024
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
}
REQUIRED_REPOSITORY_FILES = {
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "scripts/install-skills.py",
    "scripts/validate-repo.py",
}
TEXT_SUFFIXES = {
    ".bib",
    ".gitignore",
    ".json",
    ".md",
    ".py",
    ".sty",
    ".tex",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
EXCLUDED_PARTS = {".git", "build", "__pycache__"}
FRONTMATTER_NAME_RE = re.compile(r"^[a-z0-9-]+$")
FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
SIBLING_SKILL_RE = re.compile(
    r"(?<!\.\./)\.\./([a-z0-9][a-z0-9-]*)/"
)
PLACEHOLDER_RE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:TODO|TBD|FIXME|XXX)(?:\s*:|\s*$)",
    re.IGNORECASE,
)
MACHINE_PATH_PATTERNS = (
    ("macOS user home", re.compile(r"/Users/[A-Za-z0-9._-]+/")),
    ("Linux user home", re.compile(r"/home/[A-Za-z0-9._-]+/")),
    (
        "Windows user home",
        re.compile(r"[A-Za-z]:\\Users\\[A-Za-z0-9._ -]+\\"),
    ),
    (
        "assumed home subdirectory",
        re.compile(r"~/(?:Desktop|Documents|Downloads)/"),
    ),
    (
        "fixed repository layout",
        re.compile("Documents/" + "writing-skills"),
    ),
)
FIXED_CORPUS_LOCATOR_PATTERNS = (
    (
        "fixed example-corpus environment variable",
        re.compile("WRITING_SKILLS_" + "EXAMPLES"),
    ),
    (
        "repository-relative example corpus",
        re.compile(r"(?:\.\./)+Examples(?:/|\b)"),
    ),
)


class Report:
    def __init__(self):
        self.errors = []
        self.link_count = 0
        self.text_file_count = 0

    def error(self, path, message, line=None):
        location = str(path)
        if line is not None:
            location += f":{line}"
        self.errors.append(f"{location}: {message}")


def repository_root():
    return Path(__file__).resolve().parents[1]


def relative(path, root):
    try:
        return path.resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return path


def read_text(path, root, report):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        report.error(relative(path, root), f"cannot read as UTF-8: {error}")
        return None


def parse_scalar(raw_value):
    value = raw_value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
        return parsed
    return value


def parse_frontmatter(path, root, report):
    text = read_text(path, root, report)
    if text is None:
        return None, None

    lines = text.splitlines()
    display_path = relative(path, root)
    if not lines or lines[0].strip() != "---":
        report.error(display_path, "SKILL.md must begin with YAML frontmatter")
        return None, text

    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        report.error(display_path, "frontmatter has no closing --- line")
        return None, text

    frontmatter_lines = lines[1:closing_index]
    fields = {}
    index = 0
    while index < len(frontmatter_lines):
        line = frontmatter_lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if line[0].isspace():
            index += 1
            continue

        match = FRONTMATTER_KEY_RE.match(line)
        if not match:
            report.error(
                display_path,
                f"cannot parse frontmatter line: {line}",
                line=index + 2,
            )
            index += 1
            continue

        key = match.group(1)
        raw_value = (match.group(2) or "").strip()
        if key in fields:
            report.error(display_path, f"duplicate frontmatter key '{key}'")

        if raw_value in {"|", ">"}:
            block = []
            index += 1
            while index < len(frontmatter_lines):
                block_line = frontmatter_lines[index]
                if block_line and not block_line[0].isspace():
                    break
                block.append(block_line.strip())
                index += 1
            separator = "\n" if raw_value == "|" else " "
            fields[key] = separator.join(block).strip()
            continue

        fields[key] = parse_scalar(raw_value)
        index += 1

    unexpected = sorted(set(fields) - ALLOWED_FRONTMATTER_KEYS)
    if unexpected:
        report.error(
            display_path,
            "unsupported frontmatter key(s): " + ", ".join(unexpected),
        )
    return fields, text


def validate_frontmatter(skill_dir, root, report):
    skill_file = skill_dir / "SKILL.md"
    fields, text = parse_frontmatter(skill_file, root, report)
    if fields is None or text is None:
        return

    display_path = relative(skill_file, root)
    name = fields.get("name")
    description = fields.get("description")

    if not isinstance(name, str) or not name:
        report.error(display_path, "frontmatter requires a nonempty string name")
    else:
        if not FRONTMATTER_NAME_RE.fullmatch(name):
            report.error(display_path, f"name '{name}' is not lowercase hyphen-case")
        if (
            name.startswith("-")
            or name.endswith("-")
            or "--" in name
            or len(name) > MAX_SKILL_NAME_LENGTH
        ):
            report.error(display_path, f"name '{name}' has an invalid hyphen layout")
        if name != skill_dir.name:
            report.error(
                display_path,
                f"frontmatter name '{name}' does not match folder '{skill_dir.name}'",
            )

    if not isinstance(description, str) or not description.strip():
        report.error(
            display_path, "frontmatter requires a nonempty string description"
        )
    else:
        if len(description) > MAX_DESCRIPTION_LENGTH:
            report.error(
                display_path,
                f"description exceeds {MAX_DESCRIPTION_LENGTH} characters",
            )
        if "<" in description or ">" in description:
            report.error(display_path, "description cannot contain angle brackets")

    line_count = len(text.splitlines())
    if line_count > MAX_SKILL_LINES:
        report.error(
            display_path,
            f"SKILL.md has {line_count} lines; maximum is {MAX_SKILL_LINES}",
        )


def quoted_yaml_string(raw_value):
    value = raw_value.strip()
    if len(value) < 2 or value[0] != value[-1] or value[0] not in {"'", '"'}:
        return None
    try:
        parsed = ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return None
    return parsed if isinstance(parsed, str) else None


def validate_openai_yaml(skill_dir, root, report):
    metadata_file = skill_dir / "agents" / "openai.yaml"
    display_path = relative(metadata_file, root)
    if not metadata_file.is_file():
        report.error(display_path, "missing agents/openai.yaml")
        return

    text = read_text(metadata_file, root, report)
    if text is None:
        return
    lines = text.splitlines()

    interface_index = None
    for index, line in enumerate(lines):
        if line == "interface:":
            interface_index = index
            break
    if interface_index is None:
        report.error(display_path, "missing top-level interface block")
        return

    fields = {}
    for index in range(interface_index + 1, len(lines)):
        line = lines[index]
        if line and not line[0].isspace():
            break
        match = re.match(r"^\s{2}([a-z_]+):\s*(.+?)\s*$", line)
        if not match:
            continue
        key = match.group(1)
        raw_value = match.group(2)
        value = quoted_yaml_string(raw_value)
        if value is None:
            report.error(
                display_path,
                f"interface.{key} must be a quoted string",
                line=index + 1,
            )
            continue
        fields[key] = value

    for required in ("display_name", "short_description", "default_prompt"):
        if not fields.get(required):
            report.error(display_path, f"missing interface.{required}")

    short_description = fields.get("short_description", "")
    if short_description and not 25 <= len(short_description) <= 64:
        report.error(
            display_path,
            "interface.short_description must contain 25 to 64 characters",
        )

    default_prompt = fields.get("default_prompt", "")
    expected_invocation = f"${skill_dir.name}"
    if default_prompt and expected_invocation not in default_prompt:
        report.error(
            display_path,
            f"interface.default_prompt must mention {expected_invocation}",
        )


def validate_sibling_references(skill_dir, known_skills, root, report):
    skill_file = skill_dir / "SKILL.md"
    text = read_text(skill_file, root, report)
    if text is None:
        return
    for name in sorted(set(SIBLING_SKILL_RE.findall(text))):
        if name not in known_skills:
            report.error(
                relative(skill_file, root),
                f"references unknown sibling skill '{name}'",
            )


def validate_placeholders(skill_dir, root, report):
    candidates = [skill_dir / "SKILL.md"]
    for directory_name in ("assets", "references"):
        directory = skill_dir / directory_name
        if directory.is_dir():
            candidates.extend(directory.rglob("*.md"))

    for path in candidates:
        text = read_text(path, root, report)
        if text is None:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if PLACEHOLDER_RE.match(line):
                report.error(
                    relative(path, root),
                    "unresolved instruction placeholder",
                    line=line_number,
                )


def iter_text_files(root):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.name == ".gitignore" or path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def local_link_target(raw_target):
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        target = target.split(None, 1)[0]
    return target


def is_within(path, root):
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except (OSError, ValueError):
        return False


def validate_markdown_links(path, text, root, report):
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = local_link_target(match.group(1))
        if not target or target.startswith("#"):
            continue
        if target.startswith(("https://", "http://", "mailto:")):
            continue
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
            line_number = text.count("\n", 0, match.start()) + 1
            report.error(
                relative(path, root),
                f"nonportable URI in Markdown link: {target}",
                line=line_number,
            )
            continue

        path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not path_part:
            continue
        link_path = Path(path_part)
        line_number = text.count("\n", 0, match.start()) + 1
        report.link_count += 1

        if link_path.is_absolute():
            report.error(
                relative(path, root),
                f"absolute local Markdown link: {target}",
                line=line_number,
            )
            continue

        resolved = (path.parent / link_path).resolve()
        if not is_within(resolved, root):
            report.error(
                relative(path, root),
                f"Markdown link escapes the repository: {target}",
                line=line_number,
            )
        elif not resolved.exists():
            report.error(
                relative(path, root),
                f"broken local Markdown link: {target}",
                line=line_number,
            )


def validate_text_files(root, report):
    for path in iter_text_files(root):
        text = read_text(path, root, report)
        if text is None:
            continue
        report.text_file_count += 1

        if path.suffix.lower() == ".md":
            validate_markdown_links(path, text, root, report)

        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in MACHINE_PATH_PATTERNS:
                if pattern.search(line):
                    report.error(
                        relative(path, root),
                        f"machine-specific path ({label})",
                        line=line_number,
                    )
            for label, pattern in FIXED_CORPUS_LOCATOR_PATTERNS:
                if pattern.search(line):
                    report.error(
                        relative(path, root),
                        f"noninteractive example-corpus locator ({label})",
                        line=line_number,
                    )


def validate_human_guide(root, report):
    humans_root = root / "for-humans"
    guide = humans_root / "human-writing-guide"
    template = humans_root / "raw-latex-template"
    if not humans_root.is_dir():
        report.error(Path("for-humans"), "missing human-artifact directory")
        return

    for skill_file in humans_root.rglob("SKILL.md"):
        report.error(
            relative(skill_file, root),
            "for-humans must not contain an agent skill",
        )

    required_template_files = (
        ".gitignore",
        "README.md",
        "main.tex",
        "references.bib",
        "body/abstract.tex",
        "body/introduction.tex",
        "body/preliminaries.tex",
        "body/method.tex",
        "body/experiments.tex",
        "body/related-work.tex",
        "body/discussion.tex",
        "appendix/reproducibility.tex",
        "preamble/commands.tex",
        "preamble/drafting.sty",
        "preamble/project-style.sty",
        "figures/.gitkeep",
    )
    if not template.is_dir():
        report.error(relative(template, root), "missing raw LaTeX template")
    else:
        for template_file in required_template_files:
            path = template / template_file
            if not path.is_file():
                report.error(
                    relative(path, root),
                    "missing raw LaTeX template file",
                )

    if not guide.is_dir():
        report.error(
            relative(guide, root),
            "missing bundled human writing guide",
        )
        return

    if not (guide / "README.md").is_file():
        report.error(
            relative(guide / "README.md", root),
            "the human guide requires its boundary and build instructions",
        )

    main_pdf = guide / "main.pdf"
    alias_pdf = guide / "writing-research-papers.pdf"
    build_pdf = guide / "build" / "main.pdf"

    if not main_pdf.is_file():
        report.error(relative(main_pdf, root), "missing canonical human-guide PDF")
    if not alias_pdf.is_file():
        report.error(relative(alias_pdf, root), "missing descriptive PDF alias")
    if main_pdf.is_file() and alias_pdf.is_file():
        if not filecmp.cmp(main_pdf, alias_pdf, shallow=False):
            report.error(
                relative(alias_pdf, root),
                "descriptive PDF does not match main.pdf",
            )
    if build_pdf.is_file() and main_pdf.is_file():
        if not filecmp.cmp(build_pdf, main_pdf, shallow=False):
            report.error(
                relative(main_pdf, root),
                "main.pdf is stale relative to build/main.pdf",
            )


def discover_skills(root):
    skills_root = root / "for-agents"
    if not skills_root.is_dir():
        return {}
    return {
        child.name: child
        for child in sorted(skills_root.iterdir(), key=lambda path: path.name)
        if child.is_dir() and (child / "SKILL.md").is_file()
    }


def validate_repository(root):
    report = Report()

    for required in sorted(REQUIRED_REPOSITORY_FILES):
        path = root / required
        if not path.is_file():
            report.error(Path(required), "missing repository collaboration file")

    skills_root = root / "for-agents"
    skills = discover_skills(root)
    if not skills:
        report.error(Path("for-agents"), "no agent skill directories found")

    for skill_file in root.rglob("SKILL.md"):
        if ".git" in skill_file.parts:
            continue
        if skill_file.parent.parent != skills_root:
            report.error(
                relative(skill_file, root),
                "SKILL.md must belong to an immediate child of for-agents",
            )

    for skill_dir in skills.values():
        validate_frontmatter(skill_dir, root, report)
        validate_openai_yaml(skill_dir, root, report)
        validate_sibling_references(skill_dir, set(skills), root, report)
        validate_placeholders(skill_dir, root, report)

    validate_text_files(root, report)
    validate_human_guide(root, report)
    return report, len(skills)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Validate writing skills, collaboration files, and PDFs."
    )
    parser.add_argument(
        "--root",
        metavar="PATH",
        help="repository root; defaults to the parent of this script",
    )
    return parser


def main():
    args = build_parser().parse_args()
    root = (
        Path(args.root).expanduser().resolve()
        if args.root
        else repository_root()
    )
    if not root.is_dir():
        print(f"ERROR: repository root does not exist: {root}", file=sys.stderr)
        return 2

    report, skill_count = validate_repository(root)
    if report.errors:
        print(f"Validation failed with {len(report.errors)} error(s):")
        for error in sorted(report.errors):
            print(f"- {error}")
        return 1

    print(
        "Validation passed: "
        f"{skill_count} skills, "
        f"{report.text_file_count} text files, "
        f"{report.link_count} local Markdown links."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
