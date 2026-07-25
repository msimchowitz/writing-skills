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

Resolve private examples in this order:

1. `$WRITING_SKILLS_EXAMPLES`
2. The sibling `../Examples` directory relative to the repository root
3. The distilled references bundled with the relevant skill

Do not fail merely because the private corpus is absent. Use the bundled
analysis and say when an original artifact was not inspected. Never copy
private corpus content into a contribution without explicit permission.

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

## Human guide changes

Use `improve-human-writing-guide` for every proposed or applied change to the
human guide. Its prose workflow is mandatory: run Humanizer in embedded mode,
then `general-writing` and its evaluation checklist before finalizing wording.
Compile from `for-humans/human-writing-guide` after every meaningful source
change:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Inspect the rendered PDF. Before finishing, publish the exact build at both
documented top-level names:

```sh
cp build/main.pdf main.pdf
cp build/main.pdf writing-research-papers.pdf
cmp -s build/main.pdf main.pdf
```

Do not edit generated files in `build/` by hand.

## Finish

Run:

```sh
python3 scripts/validate-repo.py
```

For installer changes, also smoke-test both link and copy modes in a temporary
directory. Report any test that could not be run.
