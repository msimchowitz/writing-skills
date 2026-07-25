# LaTeX Project Conventions

## Bundled Template Companion

These conventions apply across paper repositories. When a task concerns the
full OGPO-derived template bundled with this repository, the human-readable
guide in
`../../../for-humans/human-writing-guide/human-writing-guide-main.pdf`
documents its exact theorem environments, paragraph-heading toggles, semantic
colors, algorithm-name macros, author-edit commands, title metadata, and
build-mode caveats. Consult that chapter only for a template-specific or
human-instruction request; this file remains the agent-facing source of general
LaTeX project rules.

## Recommended Layout

```text
paper/
|-- paper-main.tex
|-- paper-main.pdf
|-- references.bib
|-- body/
|   |-- abstract.tex
|   |-- introduction.tex
|   |-- preliminaries.tex
|   |-- method.tex
|   |-- experiments.tex
|   |-- related-work.tex
|   `-- discussion.tex
|-- appendix/
|   |-- reproducibility.tex
|   |-- proofs.tex
|   `-- additional-results.tex
|-- figures/
`-- preamble/
    |-- project-style.sty
    |-- commands.tex
    `-- drafting.sty
```

Treat `paper` as a placeholder for a stable, descriptive project slug. Keep
`<project-name>-main.tex` in the outermost project directory as an
orchestration file. It should define the build mode, title, authors, section
order, bibliography, and appendix order. Put manuscript prose in `body/` and
`appendix/`.

## Use The Venue Style Correctly

A conference `.sty` or `.cls` file is vendor code:

1. Keep it unmodified.
2. Load it once, before project-specific styling.
3. Do not place notation, author comments, spacing hacks, or custom theorem
   prose inside it.
4. Keep its `.bst` file beside it when the venue supplies one.
5. Record the venue version rather than silently replacing the file.
6. Remove local copies of standard packages such as `fancyhdr.sty` unless the
   venue archive explicitly requires them.

For arXiv, switch only presentation and metadata. Do not maintain a second set
of scientific claims. A build toggle may control the title block, anonymity,
website links, acknowledgments, page limits, or appendix placement; it should
not change a result.

Recommended order:

```tex
\documentclass[11pt]{article}

% Venue mode:
% \usepackage{venue_conference}

\usepackage{preamble/project-style}
\input{preamble/commands}
```

If the venue uses a class rather than a package, replace `article` with that
class and keep `project-style` conservative.

## Separate Style From Semantics

Use `project-style.sty` for stable presentation dependencies:

- fonts and encoding when the venue permits them;
- mathematics and theorem infrastructure;
- figures, tables, captions, and subfigures;
- citations and cross-references;
- hyperlinks; and
- reusable environments.

Use `commands.tex` for paper semantics:

- method and baseline names;
- state, action, policy, and distribution notation;
- task aliases; and
- repeated operators.

Use `drafting.sty` for author comments and revision colors. Load it explicitly
only during drafting. A final build should either omit it or make every comment
macro fail loudly. Do not let colored edits survive by accident.

## Use Toggles Sparingly

The corpus uses `etoolbox` toggles for arXiv and venue builds. Keep toggles near
the top of the named entry point and give each one a single responsibility.

Good uses:

- anonymous versus public author block;
- arXiv title card and project links;
- short versus full appendix;
- venue-specific acknowledgments; and
- theorem styling permitted only outside the venue template.

Bad uses:

- alternate claims;
- different experimental numbers;
- paragraphs that have diverged across versions; and
- dozens of local spacing branches.

Build every supported mode before release.

## Publish The Named PDF

Compile from the project root. For an entry point named `paper-main.tex`, use:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build paper-main.tex
cp build/paper-main.pdf paper-main.pdf
cmp -s build/paper-main.pdf paper-main.pdf
```

Replace `paper` with the actual project slug. Keep the matching
`<project-name>-main.pdf` in the outermost project directory. A PDF available
only under `build/`, or published as a generic `main.pdf`, is not the final
artifact.

## Keep Macros Semantic

Prefer:

```tex
\newcommand{\method}{\textsc{Method}\xspace}
\newcommand{\state}{s}
\DeclareMathOperator*{\argmaxop}{arg\,max}
```

Avoid macros that only hide arbitrary formatting or whole sentences. A method
rename should require one edit; understanding a paragraph should not require
opening three macro files.

Use one canonical command for each algorithm and symbol. Do not mix raw names,
small caps, and colored aliases.

## Manage Figures Deliberately

- Store original editable assets outside the paper only if the repository has
  a documented generation path; store final PDF or PNG assets in `figures/`.
- Prefer vector PDF for diagrams and plots, and PNG for raster task images.
- Use a shared plotting palette and method-to-color map.
- Keep labels readable at final column width.
- Put figure placement and caption text in the section file that argues from
  the figure.
- Give every figure a stable, descriptive label.
- Avoid repeated `\vspace` tuning until the content and venue mode are stable.

## Submission Audit

- Build from a clean directory.
- Search for `TODO`, author comments, revision colors, missing references, and
  undefined citations.
- Confirm the venue style and bibliography style are the intended versions.
- Confirm all figures are included in the source bundle.
- Confirm arXiv and venue modes contain the same claims and numbers.
- Check that appendix references resolve in both modes.
- Inspect the rendered PDF at final size, not only in source.

The reusable skeleton in `assets/latex-paper-skeleton/` follows these rules but
intentionally omits any venue-owned style file.
