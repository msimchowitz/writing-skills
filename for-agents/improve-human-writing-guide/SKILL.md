---
name: improve-human-writing-guide
description: Create, revise, audit, compile, and publish human-readable writing guides while keeping them separate from agent-facing skills. Use for the bundled human writing guide, other LaTeX or PDF writing manuals, or requests to turn writing-skill knowledge into instructions for people. Includes corpus-based voice matching, ordered Humanizer and general-writing passes, rendered-PDF verification, README maintenance, and the required top-level main.pdf publication step.
---

# Improve Human Writing Guide

Write for people. Keep the guide's prose and examples in the human-facing
project; keep agent procedures in this skill.

## Load Only The Relevant Guidance

1. Read the target guide in full, including its source, README, and current
   rendered PDF.
2. Read [Humanizer](../humanizer/SKILL.md), then
   [general-writing](../general-writing/SKILL.md) and its
   [evaluation checklist](../general-writing/references/eval.md).
3. When the guide concerns research papers, read
   [sentence-style.md](../paper-writing/references/sentence-style.md) and
   [group-paper-conventions.md](../paper-writing/references/group-paper-conventions.md).
4. When the guide covers another domain, read that sibling skill and only the
   references needed to understand its substantive conventions.
5. Read representative source artifacts from the user's corpus. Treat those
   artifacts as stronger voice evidence than generic style rules.
6. For the bundled research-paper guide, read
   [bundled-paper-guide.md](references/bundled-paper-guide.md) before editing
   its source, citations, template chapter, or published PDFs.

Inspect `../../for-humans/human-writing-guide/` only for an explicit
request to create, revise, compile, or review that human-readable guide.

## Keep Human And Agent Instructions Separate

- Do not add `SKILL.md` to a human-guide directory.
- Do not write routing, tool-use, or context-loading instructions into the
  human guide.
- Keep a prominent README notice that the guide is for people and is not an
  agent skill.
- Allow `paper-writing` to point to the guide or consult a relevant chapter for
  an explicit template-use, teaching, or human-instruction request. This
  companion relationship does not turn the guide into a skill.
- Store reusable agent workflow in this skill. Translate the substantive
  advice into natural prose for the guide.

## Revise From Evidence

1. Identify the guide's reader and the decision each section should help that
   reader make.
2. Compare the guide with the selected corpus. Record recurring sentence
   shapes, transitions, section conventions, examples, and punctuation.
3. Audit the guide for factual gaps, unsupported prescriptions, duplication,
   and advice that conflicts with the corpus.
4. Run Humanizer in embedded mode as a broad pattern pass.
5. Apply general-writing afterward as the final house-style pass. Restore any
   technical distinction or personal cadence that Humanizer flattened.
6. Pay particular attention to abstract wrappers such as "the X behind Y,"
   list-packed prose, rule-of-three phrasing, canned contrasts, signposting,
   and metaphorical headings.
7. Keep complete taxonomies, theorem assumptions, experimental axes, and
   checklists when the full set matters.
8. Preserve the existing template, preamble, source organization, citations,
   and technical claims unless the user requests a structural change.

## Document A LaTeX Template From Its Source

When a guide explains a concrete template:

1. Read the actual entry point, include order, style files, macros, and examples
   that use them. Do not infer an interface from a command's name.
2. State the exact environment and command names. Distinguish supported
   commands from inherited helpers that require project-specific definitions.
3. Explain build-mode behavior, including what each toggle changes and what a
   venue style must supply.
4. Cover theorem and reference environments, semantic colors, method-name
   fonts, author-edit commands, algorithms, notation helpers, and public title
   metadata when the template provides them.
5. Include short source examples that compile under the current template.
6. Name hazards directly, such as macros hidden by a clean-build option,
   logo-dependent metadata, nonuniform legacy aliases, and packages loaded in
   only one build mode.
7. Re-audit the chapter when the preamble changes. The source is authoritative;
   the prose must not describe an interface the template no longer has.

When the guide draws structural or stylistic claims from papers, add
source-paper citations near their first substantive use. Verify the title,
authors, year, arXiv identifier, and current version against arXiv metadata.
Keep the BibTeX in the guide's bibliography and compile until every citation is
resolved.

## Build And Inspect The Guide

For the bundled LaTeX guide, work from
`../../for-humans/human-writing-guide/` and compile after every meaningful
source change:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Require a successful exit. Check `build/main.log` for LaTeX errors, undefined
references or citations, and overfull boxes. Fix every overfull box introduced
by the change. Confirm the page count with `pdfinfo`.

Render the completed PDF and inspect every page:

```sh
mkdir -p build/rendered
pdftoppm -png -r 120 build/main.pdf build/rendered/page
```

Check margins, page breaks, headings, tables, examples, headers, footers, and
the table of contents at normal reading size. Recompile after any correction.

## Always Publish Main.pdf

After the final successful compile, always replace the top-level `main.pdf`
with the completed build:

```sh
cp build/main.pdf main.pdf
cp build/main.pdf writing-research-papers.pdf
cmp -s build/main.pdf main.pdf
cmp -s build/main.pdf writing-research-papers.pdf
```

`main.pdf` must live directly in the outermost human-guide directory, not only
inside `build/`. Do not finish while either top-level PDF is stale or missing.
Keep `build/main.pdf` in place so the build directory remains inspectable.

## Finish The Review

1. Read the rendered text at speaking pace.
2. Re-run the Humanizer pattern audit without accepting generic edits
   automatically.
3. Run the complete general-writing evaluation and fix every failed check.
4. Confirm that the README names the editable entry point, canonical PDF, build
   command, and publication step.
5. Run `python3 scripts/validate-repo.py` from the repository root when the
   guide belongs to this writing-skills repository.
6. Report the final PDF path, page count, build result, and any inherited
   template warnings.
