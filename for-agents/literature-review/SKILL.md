---
name: literature-review
description: Research, structure, draft, and verify source-grounded literature reviews, surveys, and related-work syntheses. Use for mapping a research area, comparing model or method lineages, reconstructing training recipes, building evidence tables, identifying disclosed and missing details, maintaining a living review, or writing a cited literature-review section or standalone LaTeX report.
---

# Literature Review

Build the review from a traceable evidence base. Never invent papers, authors,
dates, identifiers, datasets, model variants, training stages, numerical
results, or implementation details.

## Set The Review Contract

Copy [review-plan.md](assets/review-plan.md) into the project and complete it
before broad retrieval. Fix these decisions:

1. State the review question and intended reader.
2. Record the retrieval cutoff date.
3. Define the unit of analysis: paper, model family, release, checkpoint,
   dataset, method, or experiment.
4. State inclusion and exclusion rules.
5. Define the comparison axes before reading results.
6. Clarify whether "all" means every family, every named release, or every
   checkpoint.

Treat the contract as editable. Record scope changes rather than silently
expanding or shrinking the review.

## Build The Evidence Base

Copy [source-ledger.csv](assets/source-ledger.csv) and
[claim-evidence-matrix.csv](assets/claim-evidence-matrix.csv) into a
`research/` directory. Read
[evidence-workflow.md](references/evidence-workflow.md) before retrieval.

Prefer sources in this order:

1. Versioned papers and appendices.
2. Official repositories, model cards, data cards, and release notes.
3. Official project pages or technical blogs.
4. Independent papers that reproduce, compare, or critique the work.
5. Secondary summaries only for discovery or clearly attributed context.

Use stable paper, repository, or release URLs. Verify title, full author list,
year, identifier, and version before adding BibTeX. Read the method, training,
data, and appendix sections rather than relying on abstracts or search
snippets.

For each source:

- add one ledger row;
- record the exact page, section, table, or model-card heading supporting each
  important claim;
- label evidence as `reported`, `derived`, `inferred`, `conflicting`, or
  `not-disclosed`; and
- add each planned synthesis claim to the claim-evidence matrix before
  drafting it.

Do not turn an absent detail into a plausible recipe. State that the reviewed
sources do not disclose it.

## Reconstruct Technical Recipes

For a model or method lineage, extract the same schema from every generation:

- release and version;
- inherited backbone and changed components;
- modality encoders, adapters, tokenization, and fusion path;
- pretraining data types, mixture, scale, filtering, and synthetic data;
- stage order, frozen or trainable modules, objectives, and curriculum;
- context length, resolution, temporal treatment, or sampling policy;
- instruction tuning, preference optimization, reinforcement learning, and
  safety alignment;
- compute, optimizer, schedule, and other disclosed implementation details;
- evaluation evidence tied to each claimed change; and
- details that remain undisclosed.

Keep family-level statements separate from checkpoint-specific statements.
Do not transfer a recipe from one size, modality, or release to another unless
the source explicitly does so.

## Synthesize Across Sources

Organize the body around distinctions that answer the review question. Use a
chronological lineage only where inheritance matters; compare sources by
training stage, architecture, data, objective, alignment, or disclosure where
those axes carry the argument.

Each paragraph should:

1. state one synthesis claim;
2. identify the sources or releases being compared;
3. cite the evidence near the claim;
4. distinguish reported fact from interpretation; and
5. end with a supported consequence, boundary, or unresolved question.

Use tables for a complete taxonomy or structured comparison. Cite factual
cells or make the table's source mapping explicit. Do not use leaderboard
scores as evidence for a training mechanism unless an ablation or controlled
comparison supports that mechanism.

Include a limitations section that names search boundaries, inaccessible
artifacts, version ambiguity, contradictory reports, and undisclosed recipe
details. For a living review, state the cutoff date in both the manuscript and
the ledger.

## Write The Manuscript

For a research-paper or LaTeX deliverable, read the sibling
[`paper-writing`](../paper-writing/SKILL.md) skill, its
[`sentence-style`](../paper-writing/references/sentence-style.md) reference,
and its
[`latex-project-conventions`](../paper-writing/references/latex-project-conventions.md)
reference. Choose a stable, descriptive review slug and keep
`<review-name>-main.tex` as the top-level orchestration file. Put prose in
section files. Do not create a generic `main.tex`.

Draft the title and abstract after the comparison and disclosure boundaries
are stable. Use direct technical prose. Name exact model families, stages,
datasets, and objectives when the sources disclose them. Avoid promotional
release language.

After claims, citations, and structure are stable, run the complete sibling
[`general-writing`](../general-writing/SKILL.md) workflow. Let that skill run
Humanizer in embedded mode, then recheck every edited name, number, date,
qualifier, and citation against the evidence ledger.

## Audit And Build

Run the bundled audit from the project root:

```sh
python3 /path/to/literature-review/scripts/audit_review.py .
```

Resolve missing BibTeX keys, unresolved placeholders, and incomplete source
rows. Review uncited entries rather than deleting records needed by the
ledger.

Compile a LaTeX review with:

```sh
review_name=multimodal-model-review
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build "${review_name}-main.tex"
cp "build/${review_name}-main.pdf" "${review_name}-main.pdf"
cmp -s "build/${review_name}-main.pdf" "${review_name}-main.pdf"
```

Require a successful build and inspect the log for undefined references or
citations, LaTeX errors, and overfull boxes. Render the final PDF and inspect
every page after layout-sensitive changes. The named PDF in the project root
is the canonical deliverable; do not leave it only under `build/`. Report the
retrieval cutoff, source count, build result, remaining evidence gaps, and
final root artifact path.
