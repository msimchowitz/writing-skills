# Simchowitz-Group Paper Conventions

This guide distills recurring choices from four papers and their arXiv source:

| Paper | ArXiv version | Archetype | Argumentative spine |
| --- | --- | --- | --- |
| *Diffusion Policy Policy Optimization* | 2409.00588v3 | Empirical method | Fine-tuning need -> unexpected method -> broad performance -> mechanism -> hardware |
| *Action Chunking and Exploratory Data Collection Yield Exponential Improvements in Behavior Cloning for Continuous Control* | 2507.09061v5 | Theory plus validation | Fundamental failure -> two minimal interventions -> guarantees by regime -> validation |
| *Much Ado About Noising: Dispelling the Myths of Generative Robotic Control* | 2512.01809v3 | Empirical mechanism | Popular explanations -> controlled falsification -> component taxonomy -> minimal replacement -> mechanism |
| *OGPO: Sample Efficient Full-Finetuning of Generative Control Policies* | 2605.03065v4 | Empirical method and study | Deployment bottleneck -> sample-cost asymmetry -> decoupled method -> stabilization -> comparisons -> mechanism |

The source corpus is optional and is not stored in this repository. When the
original papers are needed, use the first available location:

1. `$WRITING_SKILLS_EXAMPLES/example-papers`
2. `../Examples/example-papers`, relative to the repository root

If neither location exists, use this distilled guide and state that the
original papers were not inspected during the current task. When the corpus is
available, treat it as evidence about a house style, not as text to copy.

## Shared Argument Pattern

The strongest common pattern is:

1. Establish a concrete robotics or learning problem.
2. Identify a mismatch, failure mode, or tradeoff in the prevailing account.
3. State a sharp central question.
4. Introduce the smallest conceptual move that resolves the mismatch.
5. Establish the headline result across the relevant regimes.
6. Investigate why the result occurs through controls, ablations, or theory.
7. State the demonstrated scope and the remaining limitation.

The method papers do not stop at "our method is better." DPPO studies
exploration, stability, robustness, and hardware behavior. OGPO studies critic
exploitation, policy extraction, and retained diversity. Much Ado makes the
mechanism study the paper itself. Action Chunking connects interventions to
control-theoretic mechanisms and statistical guarantees.

## Section Architectures

### Theory-Led Paper

The Action Chunking structure is:

1. Introduction
2. Preliminaries
3. First intervention and guarantee
4. Second intervention and guarantee
5. Experimental validation
6. Related work
7. Discussion and limitations
8. Appendix: extended discussion, control background, proofs, experiments

Use this architecture when the paper begins from a failure or impossibility and
has multiple results that apply in distinct regimes. Title result sections with
the conclusion, such as "Action-Chunking Suffices in Open-Loop Stable
Systems," rather than "Main Result I."

### Empirical Method Paper

The DPPO structure is:

1. Introduction
2. Related work
3. Formulation
4. Approach
5. Experiments
6. Properties and mechanism
7. Hardware deployment
8. Conclusion and future work
9. Appendix: implementation, ablations, baselines, full details

The OGPO structure is:

1. Introduction
2. Preliminaries
3. Named method
4. Stabilized or practical variants
5. Headline comparisons
6. Understanding and ablations
7. Related work
8. Conclusion and limitations
9. Appendix: practitioner guide, pseudocode, derivations, baselines,
   environment details, hyperparameters

Use early related work when the method must be located among close technical
alternatives before the formulation. Use late related work when an early
literature survey would delay the method and evidence.

### Empirical Mechanism Paper

The Much Ado structure is:

1. Introduction with explicit hypotheses
2. Preliminaries and component taxonomy
3. Controlled tests of explanations that do not account for performance
4. Minimal policy that isolates the successful components
5. Mechanistic explanation of what does work
6. Related work
7. Discussion
8. Appendix: full comparisons, theory, controls, and task details

This structure works when the contribution is explanatory. Organize the main
body by hypotheses and causal distinctions, not by a chronological log of
experiments.

## Abstract Convention

Use six moves, normally in one paragraph:

1. **Context:** name the concrete problem or successful practice.
2. **Tension:** state the limitation, misconception, or missing explanation.
3. **Intervention:** name the method, taxonomy, or theoretical lens.
4. **Headline result:** give the strongest supported comparison or guarantee.
5. **Mechanism or breadth:** state why it works or where it was validated.
6. **Implication:** state what changes in understanding or design.

Lead with the result when space is tight. Do not spend the first half of the
abstract on broad field importance. Include a website or code link only when
the venue permits it.

## Introduction Convention

Use the following sequence:

1. Open on the task and its operational importance.
2. Narrow to the exact methodological practice.
3. Explain what fails in the current view.
4. Pose the paper's question or tradeoff.
5. State the central insight in ordinary language.
6. Present contributions as claims with evidence, not a list of activities.
7. Close with the main conceptual takeaway.

Named contribution blocks work when the paper has several separable claims.
Each block should contain:

- a claim-led heading;
- the exact result;
- the evidence or section pointer; and
- the consequence.

Avoid duplicating the same contribution in prose, a list, a box, and a figure.
Choose one primary signposting device and use the others sparingly.

## Experimental Narrative

Use this order unless the scientific question requires another:

1. Questions or hypotheses
2. Evaluation regimes and why each is diagnostic
3. Baselines and controlled comparison rules
4. Headline performance
5. Stress tests or deployment
6. Mechanism studies
7. Ablations of design decisions
8. Efficiency, failure modes, and limitations

State what is held fixed. Much Ado's central comparisons depend on controlling
architecture; DPPO and OGPO compare common initializations and task settings.
The prose should distinguish a performance comparison from a mechanism test.

## Appendix Convention

The appendices are designed for use, not only archival completeness. Common
high-value sections include:

- practitioner guide or best practices;
- pseudocode and implementation details;
- formal definitions and proofs;
- complete baseline descriptions;
- full ablations and per-task results;
- environment and dataset details;
- hyperparameters and compute;
- qualitative failures; and
- extended related work.

Put a table of contents before a long appendix in the arXiv version. Keep the
main paper self-contained for the central claim.

## Figure System

### Figure 1

Figure 1 acts as a graphical abstract. Across the corpus it combines two or
three of:

- the method or intervention;
- a headline result;
- a mechanism or conceptual explanation; and
- a concrete task image.

The figure must let a reader answer: What is new? What improves? Why might it
work? Use left-to-right narrative order and stable semantic colors.

### Per-Paper Figure Lessons

- **Action Chunking:** The first-page figure pairs the two interventions in one
  conceptual frame. Later diagrams make abstract control concepts visible,
  while targeted sweeps test theory-specific predictions. The visual sequence
  moves from intervention, to mechanism, to controlled validation.
- **DPPO:** The overview joins the nested MDP construction to concrete robot
  tasks and names three claimed properties. Benchmark grids establish breadth,
  trajectory plots investigate structured exploration, and ordered hardware
  frames distinguish successful behavior from a precise failure mode.
- **Much Ado About Noising:** Figure 1 contains the whole explanatory argument:
  rejected hypotheses, a component taxonomy, and a minimal policy matching the
  stronger model. Later figures alternate controlled comparisons with diagrams
  of the proposed mechanism, so negative and positive findings remain visibly
  distinct.
- **OGPO:** Figure 1 combines method, sample-efficiency curves, and a mechanism
  visualization. A later side-by-side method diagram clarifies the algorithmic
  distinction, benchmark curves establish the performance claim, and
  action-distribution embeddings with critic-gradient arrows support the
  mechanism claim.

### Later Figures

Use distinct figure roles:

- **Concept figure:** make a theoretical object or mechanism visible.
- **Controlled comparison:** isolate one disputed explanation.
- **Headline benchmark:** compare methods across representative regimes.
- **Mechanism figure:** visualize trajectories, distributions, gradients, or
  intermediate computation.
- **Qualitative sequence:** show ordered frames with success and failure
  annotations.
- **Ablation:** remove or vary one decision while holding the rest fixed.

Do not ask one figure to serve all roles.

### Visual Choices

Recurring visual choices include:

- wide multi-panel compositions with a shared reading direction;
- method colors held constant across plots;
- neutral gray for context and baselines, with one or two accent colors for the
  paper's method and key alternative;
- shaded uncertainty on learning curves;
- direct labels and panel headings;
- task images beside abstract diagrams;
- arrows that encode computation or causal direction; and
- long, self-contained captions organized by **Left**, **Middle**, and
  **Right** or by panel letters.

Use the visual system consistently, but improve legibility when the source
figures become dense. A figure that only works at screen zoom is not ready.

### Caption Formula

Write captions in this order:

1. one-sentence claim or purpose;
2. panel-by-panel setup;
3. comparison and metric;
4. main observation;
5. narrow interpretation or caveat; and
6. pointer to details when needed.

The caption should support the figure without reproducing the full results
paragraph. Define nonstandard symbols and state seeds or uncertainty either in
the caption or the immediately adjacent text.

## Prose Style

The recurring voice is direct, contrastive, and claim-led:

- "Current methods trade off X and Y."
- "In contrast, we..."
- "We find that..."
- "Surprisingly,..."
- "This supports X; it does not establish Y."

Use first-person plural and active verbs. Name the mechanism rather than saying
that a method "works well." Use explicit paired distinctions such as
"distribution learning, not control performance" or "sample efficiency, not
cheaper gradient updates."

Bold and italics expose structure:

- bold for a takeaway, contribution label, or panel cue;
- italics for a defined concept, contrast term, or scoped emphasis; and
- monospace or small caps for algorithm names only when applied consistently.

Do not rely on emphasis to repair a weak sentence. A paper should remain
understandable if all bold and italics are removed.

The preferred sentence cadence is documented separately in
`sentence-style.md`. Once the technical draft is stable, use the sibling
`general-writing` skill to enforce that cadence, remove filler and AI-slop, and
preserve the author's established vocabulary and level of polish.

## What Not To Copy

The archives contain drafting residue that should not become convention:

- duplicate package loads;
- commented-out alternate manuscripts;
- unresolved TODOs;
- manual negative spacing used before the layout is stable;
- local copies of vendor packages such as `fancyhdr.sty`;
- source-specific macro sprawl; and
- claims or grammar that have not passed a final edit.

Preserve the argument patterns and modular source organization, not incidental
build artifacts.
