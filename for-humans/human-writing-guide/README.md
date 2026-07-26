# Writing research papers

This directory contains a guide for researchers turning technical evidence
into a paper that readers can follow and evaluate. It is for people, not an
installable agent skill.

Agent guidance lives in the sibling `SKILL.md` files. The `paper-writing` skill
may link to this guide for template instructions or teaching material, but the
guide itself contains no routing or tool instructions.

## Files

The canonical guide is `human-writing-guide-main.pdf`. The descriptive copy
`writing-research-papers.pdf` contains the same document. The editable source
is the top-level `human-writing-guide-main.tex`; chapter source lives in
`body/` and `appendix/`.

## Build and publish

Build the source from this directory:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build human-writing-guide-main.tex
```

After a successful build, publish the result at the top level:

```sh
cp build/human-writing-guide-main.pdf human-writing-guide-main.pdf
cp build/human-writing-guide-main.pdf writing-research-papers.pdf
```

The published `human-writing-guide-main.pdf` must match the named PDF in
`build/`.

For a visual check, render the pages with:

```sh
mkdir -p build/rendered
pdftoppm -png -r 120 build/human-writing-guide-main.pdf build/rendered/page
```

The project preserves the full preamble structure from the OGPO arXiv source.
Its writing advice draws on the example papers described in
`for-agents/paper-writing`. Private papers and source notes remain outside the
repository. The [repository README](../../README.md) documents the optional
corpus.
