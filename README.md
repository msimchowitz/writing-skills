# Writing Skills

This repository is the lab's shared home for writing tools. Agents can load its
reusable skills. Lab members can also read the research-writing guides or start
a paper from the standalone LaTeX template.

Each lab member works from their own copy, so they can edit and validate the
skills without relying on one person's directory layout.

The layout keeps agent instructions separate from material written for people.
Every installable skill lives in `for-agents/`. Finished guides and their
editable source live in `for-humans/`, alongside the raw LaTeX template.
Repository documentation and maintenance scripts remain at the top level.

## Quick start

From the repository root:

```sh
python3 scripts/validate-repo.py
python3 scripts/install-skills.py --dry-run
python3 scripts/install-skills.py
```

The installer links every skill into
`${CODEX_HOME:-$HOME/.codex}/skills`. Edits in this repository then take
effect in the installed skills. Restart the agent after the first installation
so it can discover them.

The installer never replaces an existing destination. Resolve any reported
conflict yourself, then run it again. To install a snapshot instead of links,
or to target another agent's skill directory, use:

```sh
python3 scripts/install-skills.py --copy --dest /path/to/skills
```

You can name one or more skills after the command. The installer includes
referenced sibling skills automatically:

```sh
python3 scripts/install-skills.py paper-writing grant-planning
```

Run `python3 scripts/install-skills.py --list` for the discovered names.

## Skill registry

| Skill | Purpose |
| --- | --- |
| [`writing`](for-agents/writing/SKILL.md) | Route a writing task to the smallest relevant skill. |
| [`general-writing`](for-agents/general-writing/SKILL.md) | Edit for clarity and natural cadence without flattening the writer's voice. |
| [`humanizer`](for-agents/humanizer/SKILL.md) | Detect and remove broad AI-writing patterns. |
| [`prompt-improving`](for-agents/prompt-improving/SKILL.md) | Clarify a prompt while preserving the user's prompting style. |
| [`presentation-making`](for-agents/presentation-making/SKILL.md) | Plan, create, and visually review presentations. |
| [`rebuttal-writing`](for-agents/rebuttal-writing/SKILL.md) | Draft concise, evidence-led responses to reviewers. |
| [`literature-review`](for-agents/literature-review/SKILL.md) | Research and verify source-grounded literature reviews and surveys. |
| [`paper-writing`](for-agents/paper-writing/SKILL.md) | Plan and revise technical research papers. |
| [`grant-planning`](for-agents/grant-planning/SKILL.md) | Develop and compare grant stories before drafting. |
| [`grant-writing`](for-agents/grant-writing/SKILL.md) | Draft motivated proposals for nonprofit or company sponsors. |
| [`improve-human-writing-guide`](for-agents/improve-human-writing-guide/SKILL.md) | Revise, compile, inspect, and publish human-facing guides. |

Each installable folder under `for-agents/` has a `SKILL.md` and
`agents/openai.yaml`. Detailed references and reusable templates stay beside
the skill that owns them.

## Optional example corpus

The repository includes distilled lessons from the lab's example papers and
grants, but not the private source corpus. A student can use every skill without
those files.

`paper-writing` and `grant-writing` use an example directory named in the
request. Without one, the skill asks for the relevant folder; answer `none` to
use only the bundled analysis. The path may name the corpus itself or a parent
containing `example-papers` or `example grants`.

The skills do not infer an example location from the repository layout.
Private proposals belong elsewhere, as do downloaded arXiv trees. Keep any
large local corpus outside this repository too.

## For people

[`human-writing-guide`](for-humans/human-writing-guide/README.md) is an
editable LaTeX guide to research-paper writing with a finished PDF.

[`human-vs-agent-writing`](for-humans/human-vs-agent-writing/README.md)
explains recurring differences between reader-centered prose and agent-like
defaults. Its pattern map connects practical revision advice to testable
hypotheses.

[`raw-latex-template`](for-humans/raw-latex-template/README.md) is a
standalone paper project. Copy the directory to begin a draft. The project
splits a paper into modular section files and uses semantic macros. Writers can
turn on drafting comments when they need them.

These projects are for people and contain no `SKILL.md`. Each README documents
its build and publication workflow. Every LaTeX project keeps a descriptive
`*-main.tex` entry point and matching `*-main.pdf` in its outermost directory;
the `build/` copy is not the published artifact.

## Improving the skills

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a skill and
[AGENTS.md](AGENTS.md) before asking an agent to work in this repository. Run
the validator before and after an edit:

```sh
python3 scripts/validate-repo.py
```

For skills, the validator checks metadata, instruction size, and local links;
it also rejects machine-specific paths. For the human-facing projects, it
checks the template and the published guide PDF.

## License and acknowledgments

This repository is released under the [MIT License](LICENSE). Components that
include their own MIT license notices retain those notices and copyright
statements. This work draws on the projects and communities named in
[ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md).
