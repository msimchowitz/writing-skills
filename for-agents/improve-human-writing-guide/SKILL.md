---
name: improve-human-writing-guide
description: Create, revise, audit, compile, and publish human-readable writing guides while keeping them separate from agent-facing skills. Use for the bundled human writing guide, other LaTeX or PDF writing manuals, or requests to turn writing-skill knowledge into instructions for people. Includes corpus-based voice matching, ordered Humanizer and general-writing passes, rendered-PDF verification, README maintenance, and the required named top-level PDF publication step.
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
4. When the guide contains an abstract, read the sibling
   [abstract-writing skill](../abstract-writing/SKILL.md) and revise the
   abstract for understanding rather than section-by-section coverage.
5. When the guide covers another domain, read that sibling skill and only the
   references needed to understand its substantive conventions.
6. Read representative source artifacts from the user's corpus. Treat those
   artifacts as stronger voice evidence than generic style rules.
7. For the bundled research-paper guide, read
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
- Treat suggested wording as guide work even when no file changes. Run the
  ordered Humanizer and general-writing passes before returning it.

## Revise From Evidence

1. Identify the guide's reader and the decision each section should help that
   reader make.
2. Compare the guide with the selected corpus. Record recurring sentence
   shapes, transitions, section conventions, examples, and punctuation.
3. Compare contributor notes or another guide with the existing guide before
   adding anything. Merge repeated advice into the strongest existing passage
   or checklist item, and remove wording the new source supersedes. Add a
   section only for a new reader decision, worked example, or substantive
   rule. Do not preserve a source's tab or heading structure when doing so
   would duplicate the guide.
4. Audit the guide for factual gaps, unsupported prescriptions, duplication,
   and advice that conflicts with the corpus.
5. When source notes give a draft and feedback but no finished revision, label
   any reconstructed revision as a teaching edit. Keep context-specific claims
   inside the example until the evidence supports a general rule.
6. Credit contributors at the appropriate granularity while keeping private
   source files outside the repository.
7. Run Humanizer in embedded mode as a broad pattern pass.
8. Audit the title and any subtitle as their own writing layer. Do the same
   for the abstract, every section and subsection heading, caption, callout
   title, table or figure label, and other reader-visible display text. Read
   each element with the material it frames instead of assuming the body-prose
   pass caught it.
9. Apply general-writing afterward as the final house-style pass. Restore any
   technical distinction or personal cadence that Humanizer flattened.
10. Pay particular attention to abstract wrappers such as "the X behind Y,"
   non-question clauses such as "what X does" and "how Y works," list-packed
   prose, long decorative lists, rule-of-three phrasing, canned contrasts,
   signposting, metaphorical headings, and readerless corporate shorthand such
   as assigning prose a job, ownership, or responsibility. Replace that
   shorthand with the precise effect on the intended reader.
11. Keep complete taxonomies, theorem assumptions, experimental axes, and
   checklists when the full set matters.
12. Preserve the existing template, preamble, source organization, citations,
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

For every LaTeX guide, keep a descriptive `<guide-name>-main.tex` entry point
in the outermost guide directory. Compile to a named PDF under `build/`, then
publish the matching `<guide-name>-main.pdf` in that outermost directory.
Never use `main.tex` or `main.pdf` as the canonical artifact name.

For the bundled LaTeX guide, work from
`../../for-humans/human-writing-guide/` and compile after every meaningful
source change:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build human-writing-guide-main.tex
```

Require a successful exit. Check `build/human-writing-guide-main.log` for
LaTeX errors, undefined references or citations, and overfull boxes. Fix every
overfull box introduced by the change. Confirm the page count with `pdfinfo`.

Render the completed PDF and inspect every page:

```sh
mkdir -p build/rendered
pdftoppm -png -r 120 build/human-writing-guide-main.pdf build/rendered/page
```

Check margins, page breaks, headings, tables, examples, headers, footers, and
the table of contents at normal reading size. Recompile after any correction.

## Always Publish The Named PDF

After the final successful compile, always replace the named top-level PDF
with the completed build:

```sh
cp build/human-writing-guide-main.pdf human-writing-guide-main.pdf
cmp -s build/human-writing-guide-main.pdf human-writing-guide-main.pdf
```

`human-writing-guide-main.pdf` must live directly in the outermost human-guide
directory, not only inside `build/`. Do not finish while the top-level PDF is
stale or missing. Keep the named build PDF in place so the build directory
remains inspectable.

## Finish The Review

1. Read the rendered text at speaking pace.
2. Re-run the Humanizer pattern audit without accepting generic edits
   automatically.
3. Run the complete general-writing evaluation and fix every failed check.
4. If the guide has an abstract, compare it with the final guide and confirm
   that it represents the main points as one reader-facing argument rather
   than a section inventory or an earlier draft.
5. Confirm that the README names the editable entry point, canonical PDF, build
   command, and publication step.
6. Run `python3 scripts/validate-repo.py` from the repository root when the
   guide belongs to this writing-skills repository.
7. Report the final PDF path, page count, build result, and any inherited
   template warnings.
