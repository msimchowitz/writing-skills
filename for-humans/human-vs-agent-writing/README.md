# Human writing and agent defaults

This directory contains an expository comparison of good human prose and common
agent defaults. It explains why agent writing can remain fluent while
feeling choppy or semantically sloppy. It is for people, not an installable
agent skill.

The article draws on `for-agents/humanizer`, `for-agents/general-writing`,
`for-agents/better-usage`, `for-agents/writing-cadence`, and
`for-agents/academic-voice`, together with the non-autoregressive, abstract,
and paper writing skills. It treats agent-like patterns as properties of
passages, then develops possible explanations in terms of audience
specification, training, and local prediction. The patterns support analysis
and revision; they do not establish authorship.

The project inherits its preamble and running header from
`../raw-latex-template`. The title card and public metadata commands come from
the same template. The preamble enters through
`preamble/_preamble_includes.tex`; `preamble/commands.tex` defines only the two
labels used for worked revisions.

## Build the article

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
