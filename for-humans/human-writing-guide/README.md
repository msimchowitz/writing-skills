# Human instructions only

This directory contains a human-readable guide to writing research papers. It
is written for people, not for agents, and it is not a Codex skill.

Agents must not route writing tasks to this directory as though it were a
skill. Use the sibling `SKILL.md` files for agent guidance. The
`paper-writing` skill may point to this guide or consult the relevant chapter
when a user explicitly asks how to use the bundled LaTeX template, requests
teaching material, or wants human-readable instructions. Inspect or edit the
guide itself only when the user asks to work on it.

## Writing research papers

The current guide is `main.pdf`. The descriptive copy
`writing-research-papers.pdf` contains the same document. The editable source
begins in `main.tex`; chapter source lives in `body/` and `appendix/`.

## Build and publish

Build the source from this directory:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

After every completed build, publish the result at the top level:

```sh
cp build/main.pdf main.pdf
cp build/main.pdf writing-research-papers.pdf
```

`main.pdf` is the canonical output. Do not leave it older than
`build/main.pdf`.

For a visual check, render the pages with:

```sh
mkdir -p build/rendered
pdftoppm -png -r 120 build/main.pdf build/rendered/page
```

The project preserves the full preamble structure used by the OGPO arXiv
source. Its manuscript sections contain new writing-guide material informed by
the example papers described in `for-agents/paper-writing`. The private source
corpus is optional; its portable lookup convention is documented in the
[repository README](../../README.md).
