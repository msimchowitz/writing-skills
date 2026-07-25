# Raw LaTeX template

This standalone research-paper starter contains the LaTeX template without the
writing guide. It is for people and is not an agent skill. Its entry point,
preamble include graph, typography, title card, theorem styles, semantic
colors, reference commands, algorithms, and drafting machinery mirror the
human writing guide.

## Start a paper

Copy the directory from the repository root:

```sh
cp -R for-humans/raw-latex-template ../my-paper
cd ../my-paper
```

The editable entry point is the top-level `latex-template-main.tex`. Update its
title, running header, authors, and metadata, then replace the prompts in
`body/` and `appendix/`. The preamble enters through
`preamble/_preamble_includes.tex`.

The inherited `preamble/specific_macros.tex` and `preamble/algnames.tex` show
the paper-owned notation and method-name layers from the guide. Replace those
definitions for a new paper and remove unused aliases. Keep the other preamble
files when the new paper should retain the guide's visual conventions. For a
paper with citations, add entries to `references.bib` and uncomment the two
bibliography lines in `latex-template-main.tex`.

Build the paper with:

```sh
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build latex-template-main.tex
cp build/latex-template-main.pdf latex-template-main.pdf
cmp -s build/latex-template-main.pdf latex-template-main.pdf
```

The canonical PDF is `latex-template-main.pdf` in this outermost directory.
The matching build copy remains at `build/latex-template-main.pdf`. The default
`arxiv` and `customthms` toggles produce the same public visual system as the
guide. The false `arxiv` branch is a venue hook, not a complete standalone
style; load the unmodified venue package before the preamble includes and test
that mode separately.
