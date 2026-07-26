# Bundled Research-Paper Guide

Use this reference only when maintaining the repository's human-readable
research-paper guide.

## Boundary And Companion Role

The guide lives under the human-artifact root:
[`human-writing-guide`](../../../for-humans/human-writing-guide/README.md).
It is a LaTeX project for people and must not contain `SKILL.md`.

`paper-writing` remains the agent-facing skill. It may point a user to the
guide, or consult the relevant chapter, when the request explicitly concerns
the bundled LaTeX template, teaching, onboarding, or human-readable
instructions. It must not route an ordinary drafting task to the guide.

## Source Map

- `human-writing-guide-main.tex` owns chapter order, the bibliography, and
  appendix order.
- `body/template.tex` explains the full OGPO-derived LaTeX template.
- `body/latex.tex` covers general source organization.
- `references.bib` stores citations for source papers.
- `preamble/` is the authority for every documented template command.
- `README.md` records the human/agent boundary and build workflow.

When a new chapter is added, include it explicitly from
`human-writing-guide-main.tex`. Do not place long prose directly in the entry
point.

## Template Chapter Requirements

Audit the current preamble before changing the template chapter. At minimum,
the chapter must explain:

- the include order and ownership of each preamble file;
- `definition` and `theorem` environments, including the fact that the
  template does not define short `defn` or `thm` environments;
- numbered, starred, informal, and modified theorem forms that actually work;
- `arxiv`, `customthms`, `toreturn`, and any active venue toggles;
- the different behavior of `colorpar`, `togglepar`, and `colorbold`;
- semantic theorem, link, term, takeaway, and method colors;
- `algofont`, neutral method names, colored names, and title forms;
- `color-edits.sty`, `addauthor`, edit/comment/delete commands, and the
  `suppress` and `showdeletions` options;
- the `algorithm` and `algorithmic` package dependency in each build mode;
- generated character macros, paired delimiters, and collision risks;
- `AIbox` and its narrow summary role; and
- public title metadata, its logo files, and its arXiv-only definitions.

Document the source as it exists. The non-arXiv branch is a venue hook, not a
complete standalone style, and should be described that way.

## Source-Paper Citations

The current guide draws on four arXiv papers:

| Key | arXiv |
| --- | --- |
| `ren2024diffusion` | `2409.00588` |
| `zhang2025actionchunking` | `2507.09061` |
| `pan2025muchado` | `2512.01809` |
| `patil2026ogpo` | `2605.03065` |

Verify current metadata and versions against arXiv before changing an entry.
Use full author lists. Cite each paper near the first substantive claim drawn
from it, not only in a general acknowledgments sentence.

## Build, Inspect, And Publish

From the guide root:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build human-writing-guide-main.tex
```

Require:

- no LaTeX errors;
- no undefined references or citations;
- no overfull boxes introduced by the change;
- a readable table of contents and bibliography; and
- visual inspection of every rendered page.

Render with:

```sh
mkdir -p build/rendered
pdftoppm -png -r 120 build/human-writing-guide-main.pdf build/rendered/page
```

Publish the final bytes at the outermost guide level:

```sh
cp build/human-writing-guide-main.pdf human-writing-guide-main.pdf
cp build/human-writing-guide-main.pdf writing-research-papers.pdf
cmp -s build/human-writing-guide-main.pdf human-writing-guide-main.pdf
cmp -s build/human-writing-guide-main.pdf writing-research-papers.pdf
```

The task is not complete if the finished PDF exists only under `build/`.
