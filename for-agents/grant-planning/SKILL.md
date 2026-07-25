---
name: grant-planning
description: Ideate, structure, compare, and select grant narratives before application drafting. Use for grant strategy, story options, concept notes, project framing, scientific questions, literature and arXiv source review, combinations of applicants' prior work, team differentiation, feasibility arguments, scope decisions, outcomes, risks, or replanning an existing proposal before writing final application prose.
---

# Grant Planning

Plan the scientific argument before drafting application answers. Produce a
decision document that explains why the problem matters, why this team can make
unusual progress, and why the proposed scope is executable.

## Load supporting skills selectively

- Read `../grant-writing/SKILL.md` when the funder and call are known. Follow
  its sponsor-type guidance while planning fit and impact.
- Read the solicitation, scoring criteria, application questions, and supplied
  funder notes before generating stories.
- Before returning a polished planning document, read
  `../general-writing/SKILL.md` and
  `../general-writing/references/eval.md`.
- Use [planning-template.md](references/planning-template.md) for a substantial
  planning document or a comparison of multiple stories.

## Keep planning distinct from drafting

- Decide the problem, thesis, evidence, team logic, feasibility, and scope
  before writing application prose.
- Use provisional language for unresolved design choices.
- Preserve competing stories when they represent genuinely different
  scientific centers of gravity.
- Do not polish a weak story into apparent coherence. Surface the missing
  premise, evidence, or team connection.
- Hand the selected plan to `grant-writing` only after its logic survives
  comparison and risk review.

## Build the evidence inventory

Read the relevant project files and source material. Record:

1. The funder's stated vision, scope, exclusions, review criteria, and budget.
2. The concrete problem or risk the call is trying to change.
3. The applicants' relevant prior results, methods, code, datasets, testbeds,
   collaborators, and preliminary evidence.
4. The scientific assets each applicant contributes.
5. The intervention ideas that follow from those assets.
6. The available personnel, compute, time, access, and budget.
7. The facts that remain unverified and the decisions the applicants must make.

Distinguish source-backed facts, interpretations, hypotheses, and open
questions. Do not promote an analogy into a result.

## Download and contain arXiv sources

For literature-dependent planning, download the LaTeX source for each relevant
arXiv paper when it is available. Prefer the source archive over relying only
on the rendered PDF because the `.tex`, bibliography, and appendix files are
easier to search and verify.

1. From the grant repository root, create the dedicated
   `Background/papers/` directory.
2. Extract each source archive into its own
   `<short-title>-<arxiv-id>/` subdirectory. Record the arXiv ID, version,
   source URL, and local path in the evidence inventory.
3. Resolve the current version through
   `https://export.arxiv.org/api/query?id_list=<arxiv-id>`, then download the
   reproducible, versioned archive from
   `https://export.arxiv.org/e-print/<arxiv-id>v<version>`.
4. Reject archive entries with absolute paths, `..` traversal, or links that
   could write outside the paper's directory.
5. Keep searchable source files such as `.tex`, `.bib`, `.bbl`, `.sty`, and
   source metadata visible to Git.
6. Add only paper-local binary media to the grant repository's `.gitignore`:

   ```gitignore
   # Binary media bundled with downloaded arXiv sources
   /Background/papers/**/*.pdf
   /Background/papers/**/*.jpeg
   /Background/papers/**/*.jpg
   /Background/papers/**/*.png
   ```

Do not ignore the whole `Background/papers/` directory, and do not add
repository-wide patterns such as `*.pdf` or `*.jpg`. If a source archive
contains another large binary-media format, add a similarly scoped pattern
under `/Background/papers/` only. Never treat the downloaded source as proof by
itself: inspect the relevant source passage and distinguish the paper's result
from the proposal's interpretation.

## Build the motivation spine

Answer these questions before naming a method:

1. What concrete failure, risk, or scientific blockage exists?
2. Who or what is exposed to the consequence?
3. Through what mechanism does the failure arise?
4. Why do current methods, benchmarks, or institutions miss it?
5. Why is the problem important and tractable now?
6. What changes if the project succeeds?
7. What minimum result would still change scientific understanding?
8. What would a clean negative result teach?

Prefer a causal account to a list of concerns. The motivation should make the
research question feel necessary before the reader encounters the proposed
intervention.

## Combine prior work into a research advantage

For each relevant prior work, extract:

- the established result;
- the mechanism or concept it contributes;
- the concrete asset it supplies;
- the limitation that creates room for the proposed work;
- the claim it supports in the new plan.

Combine prior works through a scientific dependency, not a bibliography list.
Show how one applicant's work defines the target, evidence, or environment
while another applicant's work supplies theory, measurement, intervention, or
evaluation.

Apply the removal test: explain what becomes materially weaker if either
applicant is removed. Replace generic claims of complementarity with distinct
responsibilities and shared scientific questions.

## Establish feasibility

- Identify the strongest empirical foothold: a prior result, codebase, dataset,
  testbed, theorem, or pilot.
- Define the first decisive experiment or analysis.
- Match the number of aims and interventions to the budget and duration.
- Separate required components from optional extensions.
- Name the main technical and scope risks without softening them.
- Give each risk a mitigation, fallback, or useful boundary condition.
- Explain why the available team and resources can complete the work.
- Treat milestones as scientific decision points, not activity lists.

## Generate substantive story options

Make each story a coherent answer to one core problem. Do not create variety by
renaming the same approach.

For each story, specify:

1. Working title and one-sentence thesis.
2. Core problem, stakes, and why now.
3. Scientific question and central hypothesis.
4. Why current approaches fail.
5. How the applicants' prior work combines.
6. Why this team is unusually positioned to execute.
7. Focused research plan at the level of aims and decisive tests.
8. Feasibility evidence and required resources.
9. Best-case, minimum valuable, and informative negative outcomes.
10. Main risks, mitigations, funder fit, and scope boundary.

Spend more space on motivation, team synthesis, and feasibility than on
implementation details during planning. Include technical detail only when it
changes the scientific thesis or credibility of execution.

## Compare and select

Compare stories against:

- importance and clarity of the core problem;
- direct fit to the call;
- strength of preliminary evidence;
- necessity of the applicant combination;
- novelty of the scientific question;
- feasibility at the requested tier;
- generalizability of the result;
- risk of being judged out of scope;
- ability to produce a valuable result if the main hypothesis fails.

State the strongest story, the strongest backup, and whether parts of one story
should become an aim or intervention inside another. Do not combine stories
when doing so produces a list of disconnected methods.

## Prepare the drafting handoff

End with:

- the recommended scientific spine;
- the evidence and claims safe to use;
- the role of each applicant;
- the essential aims and outcomes;
- the facts and choices still requiring confirmation;
- a map from the plan to the application questions.

Then invoke `grant-writing` to draft the application in the funder's required
format. Preserve the planning document as the source of truth for the argument.
