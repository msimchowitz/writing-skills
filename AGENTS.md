# Instructions for agents

These instructions apply to the whole repository.

## Repository boundaries

- Immediate child directories under `for-agents/` containing `SKILL.md` are
  installable agent skills.
- Everything under `for-humans/` is for people and must not contain
  `SKILL.md`. Do not route ordinary writing tasks there. `paper-writing` may
  point to the guide or consult the relevant chapter for explicit
  template-use, teaching, or human-instruction requests. Otherwise load the
  focused agent references.
- Keep private papers, proposals, downloaded arXiv source, and user drafts
  outside this repository.
- Preserve license and attribution files, especially in `humanizer` and
  `general-writing`.

## Before editing

1. Read the selected `SKILL.md` in full.
2. Read only the references or assets needed for the requested change.
3. Check sibling skills before changing a shared workflow. The `writing` skill
   owns routing; `general-writing` owns the Humanizer-first prose pipeline.
4. Run `python3 scripts/validate-repo.py` to establish a clean baseline.
5. Inspect the working tree and preserve unrelated changes.

## Skill design

- Keep the frontmatter `name` equal to the folder name.
- Put trigger conditions and the complete operating procedure in `SKILL.md`.
- Move detailed domain knowledge, long examples, and checklists into
  `references/`; place reusable starter files in `assets/`.
- Use relative links. Never add a username, home-directory path, or assumed
  `Documents` layout.
- Keep instructions direct and testable. State what an agent must inspect,
  produce, preserve, and verify.
- Keep `SKILL.md` under 500 lines. Add an abstraction only when it removes
  repeated instructions or gives one skill clear ownership of a workflow.
- Update `agents/openai.yaml` when a skill's name or user-facing scope changes.
  The default prompt must mention the exact `$skill-name`.

## Optional corpora

Keep private corpora outside this repository. When a task would benefit from
original examples, use a directory the user supplied for that task. If no
directory was supplied, ask where the relevant example folder lives and make
clear that the user can answer `none`.

Accept either the corpus directory itself or a parent containing the relevant
`example-papers` or `example grants` directory. Do not search above the
repository or assume a home-directory layout. If the corpus is unavailable,
use the distilled reference bundled with the relevant skill and say that the
original artifacts were not inspected. Never copy private corpus content into
a contribution without explicit permission.

## Cross-skill behavior

- Let `writing` route requests; do not duplicate full domain instructions in
  the router.
- Let `general-writing` invoke Humanizer and then enforce the author's house
  style. Domain skills should call that workflow once rather than reimplement
  it.
- Keep planning and drafting separate where the repository already does so,
  especially for `grant-planning` and `grant-writing`.
- Preserve factual claims, citations, notation, and format constraints during
  prose edits.

## Named LaTeX artifacts

- Keep each LaTeX entry point in the outermost project directory.
- Use a stable, descriptive `<project-name>-main.tex` filename, never a generic
  `main.tex`.
- Compile to `build/<project-name>-main.pdf`, then copy that exact PDF to
  `<project-name>-main.pdf` in the outermost project directory.
- Do not finish a writing task with the canonical PDF named `main.pdf` or
  available only under `build/`.

## Human guide changes

Use `improve-human-writing-guide` for every proposed or applied change to the
human guide. Its prose workflow is mandatory: run Humanizer in embedded mode,
then `general-writing` and its evaluation checklist before finalizing wording.
Compile from `for-humans/human-writing-guide` after every meaningful source
change:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build human-writing-guide-main.tex
```

Inspect the rendered PDF. Before finishing, publish the exact build at both
documented top-level names:

```sh
cp build/human-writing-guide-main.pdf human-writing-guide-main.pdf
cp build/human-writing-guide-main.pdf writing-research-papers.pdf
cmp -s build/human-writing-guide-main.pdf human-writing-guide-main.pdf
```

Do not edit generated files in `build/` by hand.

## Finish

Run:

```sh
python3 scripts/validate-repo.py
```

For installer changes, also smoke-test both link and copy modes in a temporary
directory. Report any test that could not be run.
