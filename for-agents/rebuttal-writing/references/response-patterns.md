# Response Patterns

## Novelty Or "Simple Combination"

1. Acknowledge which ingredients are established.
2. Name the precise new formulation, result, or scientific finding.
3. Explain why the result was not implied by prior work.
4. Contrast with the nearest prior method on one concrete axis.
5. Cite evidence for the claimed consequence.
6. Narrow the novelty claim if the algorithmic component is simple.

Do not substitute "we were surprised" for the non-obviousness argument.

## Alternative Explanation Or Confound

1. Restate the alternative explanation fairly.
2. Identify the control needed to isolate it.
3. Report the control and quantitative outcome.
4. State what is ruled out and what remains possible.

Examples include architecture mismatch, sampling choice, dataset
multimodality, pretraining quality, task precision, or compute budget.
Prefer the reviewer's proposed counterfactual when it is valid. Hold the
trained model, sampling method, architecture, data, or starting checkpoint
fixed according to the explanation being tested.

## Generality And Scope

1. State the exact regime evaluated.
2. Add representative evidence from the missing regime when feasible.
3. Avoid using one saturated benchmark as universal evidence.
4. Restrict the abstract and conclusions to the demonstrated regime.
5. Identify untested regimes as limitations.

## Theory Or Terminology

1. Separate a notation error from a conceptual error.
2. Define the quantity being measured.
3. State assumptions and what the theorem actually proves.
4. Replace overloaded terminology.
5. Move intuition out of theorem language when rigor is insufficient.

## Missing Baseline

1. Explain the baseline's relevance.
2. Use its original setup or justify adaptations.
3. Match data, architecture, pretraining, and evaluation where possible.
4. Report performance and failure modes.
5. Avoid dismissing a baseline solely because it performed poorly.

## Efficiency Or Compute

Report both sample efficiency and resource efficiency:

- environment interactions;
- wall-clock time;
- inference steps or function evaluations;
- training memory;
- hardware; and
- whether execution and learning can overlap.

Concede compute overhead when present. Explain when it matters without
relabeling it as free.
When methods use different numbers of score or model evaluations per step,
compare both equal-step and equal-total-compute settings.

## Qualitative Or Media Evidence

1. State whether the evidence is illustrative or systematic.
2. Report resolution, horizon, prompts or controls, seeds, and selection
   procedure in text.
3. Include failures and an uncurated output index when feasible.
4. Preserve the media in a durable supplement; do not rely on an ephemeral
   anonymous project page.
5. Avoid converting "the shown examples work" into a population-level
   robustness, scalability, or generalization claim.

## Presentation Concern

Treat confusion as evidence that the paper failed to communicate. State:

- the intended logical chain;
- what will move, shrink, or be added;
- the exact section or figure affected; and
- how the revision exposes the main contribution earlier.

Show a proposed outline or rewritten excerpt when clarity is decision-critical.
Promising that prose will improve is not evidence that it can fit or read well.
## Follow-Up

Use:

> We wanted to check whether our response resolved your technical concerns.
> If any point remains unclear, we would appreciate a concrete question and
> will address it directly.

Do not mention expected ratings, acceptance, or other reviewers' scores.
