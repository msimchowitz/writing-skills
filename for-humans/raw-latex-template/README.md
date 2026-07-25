# Raw LaTeX template

This directory is a standalone research-paper starter for people. It contains
no writing-guide text and is not an agent skill.

## Start a paper

Copy the directory from the repository root:

```sh
cp -R for-humans/raw-latex-template ../my-paper
cd ../my-paper
```

Update the title and authors in `main.tex`, then replace the prompts in `body/`
and `appendix/`. Keep paper-specific notation and method names in
`preamble/commands.tex`. Add entries to `references.bib` and uncomment the two
bibliography lines in `main.tex` when the paper has citations.

Build the paper with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The PDF is written to `build/main.pdf`. Add an unmodified venue package before
`preamble/project-style` in `main.tex` when preparing a conference submission.
Uncomment `preamble/drafting` only while author comments are needed.
