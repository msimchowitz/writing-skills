# Contributing

The aim is to make these skills easier for another researcher and their agent
to use correctly. Prefer small changes that improve a concrete workflow,
trigger, reference, or verification step.

## Set up a working copy

Validate the repository first:

```sh
python3 scripts/validate-repo.py
```

Install by link while developing:

```sh
python3 scripts/install-skills.py
```

An installed link points back to this working copy, so edits are available to
the agent after it reloads its skill registry. Use `--copy` only when you want
an independent snapshot.

Create a branch for a focused change when working through Git:

```sh
git switch -c skill/short-description
```

## Change an existing skill

1. Read the complete `SKILL.md` and the references relevant to your change.
2. Write down at least two requests that should trigger the skill and one that
   should not.
3. Make the smallest change that resolves the observed problem.
4. Follow every relative link you add and test any command you prescribe.
5. Run the validator and exercise the skill on a representative task.
6. Review the output for factual preservation, useful scope, and unnecessary
   context loading.

Do not tune a skill to one draft by embedding private text or a machine-specific
path. Distill the transferable lesson into a reference and retain enough source
provenance for another contributor to evaluate it.

## Add a skill

Use lowercase hyphen-case and this minimum layout:

```text
for-agents/
  new-skill/
    SKILL.md
    agents/
      openai.yaml
```

Add `references/`, `assets/`, or `scripts/` only when the skill needs them.
Keep `SKILL.md` below 500 lines and use progressive disclosure instead of
loading every reference on every invocation.

The frontmatter must contain only supported fields and must describe both what
the skill does and when it should run:

```yaml
---
name: new-skill
description: State the capability and the requests that should trigger it.
---
```

In `agents/openai.yaml`, quote user-facing strings, keep
`short_description` between 25 and 64 characters, and mention
`$new-skill` in `default_prompt`.

Add the skill to the registry in `README.md`. If another skill invokes it, add
a relative sibling reference so the installer can include the dependency.

## Use example corpora

Private examples are optional and may live anywhere outside this repository.
Supply either the relevant corpus directory or a parent containing
`example-papers` or `example grants`. If a task needs original examples and no
path was supplied, the relevant skill must ask for one instead of guessing.
Do not commit the corpus.

When extracting a convention:

- compare several examples rather than one sentence;
- separate recurring choices from drafting residue;
- record where the evidence came from without copying confidential material;
- preserve exceptions when the best choice depends on paper or sponsor type;
- make the bundled reference useful when the original corpus is unavailable.

## Edit the human guide

The human guide is not a skill. Keep agent procedures in
`for-agents/improve-human-writing-guide` and natural instructions in
`for-humans/human-writing-guide`. After a guide change, compile and
inspect every page, then copy `build/main.pdf` to both `main.pdf` and
`writing-research-papers.pdf`.

## Before review

Confirm all of the following:

- `python3 scripts/validate-repo.py` passes.
- New local links resolve.
- No private or machine-specific paths were added.
- Triggering and non-triggering requests were tested.
- User-facing metadata still matches the skill.
- Third-party licenses and attribution remain intact.
- The human guide's published PDFs match the final build when it changed.

In the change description, state the problem, the behavioral change, the test
requests, and the validation commands you ran.
