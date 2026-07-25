# Human vs. agent writing

This directory contains a guide for people, not an installable agent skill.

The guide distills the advice in `for-agents/humanizer` and
`for-agents/general-writing`. It compares reader-centered prose with recurring
agent-like defaults and proposes testable explanations for those defaults.
The patterns support revision; they do not establish authorship.

Its full preamble, running header, title card, and public metadata commands
come from `../raw-latex-template`. The preamble enters through
`preamble/_preamble_includes.tex`; `preamble/commands.tex` adds only the two
labels used for worked revisions.

## Build the guide

The editable entry point is the top-level
`human-vs-agent-writing-main.tex`. Build it from this directory:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build human-vs-agent-writing-main.tex
```

The canonical PDF is `human-vs-agent-writing-main.pdf`. After a successful
build, publish both top-level copies:

```sh
cp build/human-vs-agent-writing-main.pdf human-vs-agent-writing-main.pdf
cp build/human-vs-agent-writing-main.pdf human-vs-agent-writing.pdf
cmp -s build/human-vs-agent-writing-main.pdf human-vs-agent-writing-main.pdf
```

Render the PDF for visual review:

```sh
mkdir -p build/rendered
pdftoppm -png -r 120 build/human-vs-agent-writing-main.pdf build/rendered/page
```

Inspect every page before publishing. Check the margins, page breaks,
headings, examples, page numbers, and table of contents.

## Sources

The document summarizes this repository's modified Humanizer and general
writing skills. Humanizer builds on Siqi Chen's `humanizer`, and general
writing builds on Peter Yang's `no-ai-slop`. Both upstream projects use the MIT
License. The repository's `ACKNOWLEDGMENTS.md` and the component license files
contain the full attribution.
