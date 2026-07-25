# Writing Skills

This repository contains reusable writing skills for agents and a separate
research-paper guide for people. It is designed to be shared within a lab:
students can install the skills from their own copy, edit that copy, and
validate changes without depending on one person's directory layout.

The repository separates its audiences:

- `for-agents/` contains every installable skill.
- `for-humans/` contains finished guides and their editable source.
- Repository documentation and maintenance scripts remain at the top level.

## Quick start

From the repository root:

```sh
python3 scripts/validate-repo.py
python3 scripts/install-skills.py --dry-run
python3 scripts/install-skills.py
```

The installer links every skill into
`${CODEX_HOME:-$HOME/.codex}/skills`. Linking is the default because edits in
this repository then take effect in the installed skills. Restart the agent
after the first installation so it can discover them.

The installer never replaces an existing destination. Resolve any reported
conflict yourself, then run it again. To install a snapshot instead of links,
or to target another agent's skill directory, use:

```sh
python3 scripts/install-skills.py --copy --dest /path/to/skills
```

You can name one or more skills after the command. Referenced sibling skills
are included automatically:

```sh
python3 scripts/install-skills.py paper-writing grant-planning
```

Run `python3 scripts/install-skills.py --list` for the discovered names.

## Skill registry

| Skill | Purpose |
| --- | --- |
| [`writing`](for-agents/writing/SKILL.md) | Route a writing task to the smallest relevant skill. |
| [`general-writing`](for-agents/general-writing/SKILL.md) | Edit for clarity, directness, cadence, and personal voice. |
| [`humanizer`](for-agents/humanizer/SKILL.md) | Detect and remove broad AI-writing patterns. |
| [`prompt-improving`](for-agents/prompt-improving/SKILL.md) | Clarify a prompt while preserving the user's prompting style. |
| [`presentation-making`](for-agents/presentation-making/SKILL.md) | Plan, create, and visually review presentations. |
| [`rebuttal-writing`](for-agents/rebuttal-writing/SKILL.md) | Draft concise, evidence-led responses to reviewers. |
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

When access to the corpus is appropriate, set `WRITING_SKILLS_EXAMPLES` to an
`Examples` directory:

```sh
export WRITING_SKILLS_EXAMPLES="$HOME/path/to/Examples"
```

The expected subdirectories are `example-papers` and `example grants`. If the
variable is unset, agents may also look for a sibling `../Examples` directory
relative to this repository. Do not add private proposals, downloaded arXiv
trees, or large local corpora to this repository.

## Human guide

[`human-writing-guide`](for-humans/human-writing-guide/README.md)
is a LaTeX project and finished PDF for people. It is intentionally not an
agent skill and must not contain a `SKILL.md`. Its README documents the build
and publication workflow.

## Improving the skills

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a skill and
[AGENTS.md](AGENTS.md) before asking an agent to work in this repository. Run
the validator before and after an edit:

```sh
python3 scripts/validate-repo.py
```

The validator checks skill metadata, local links, portable paths, instruction
size, and the published human-guide PDF.

## Licensing

The `for-agents/humanizer` and `for-agents/general-writing` directories include
their own license files. Preserve those files and their attribution. This
repository does not currently declare one license for all remaining material;
confirm permission before redistributing it outside the lab.
