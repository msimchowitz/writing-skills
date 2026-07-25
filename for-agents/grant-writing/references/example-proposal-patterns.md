# Patterns from the example proposals

Use this analysis to match the author's established grant-writing choices
without copying sponsor-specific claims into unrelated applications.

## Contents

- [Source corpus](#source-corpus)
- [Amazon proposal](#amazon-proposal)
- [BNY proposal](#bny-proposal)
- [Jane Street renewal](#jane-street-renewal)
- [Shared choices](#shared-choices)
- [Adapt rather than copy](#adapt-rather-than-copy)

## Source corpus

The examples are three LaTeX proposals from the author's private corpus. The
corpus is optional and is not stored in this repository. When the original
files are needed, use the first available location:

1. `$WRITING_SKILLS_EXAMPLES/example grants`
2. `../Examples/example grants`, relative to the repository root

If neither location exists, use this distilled analysis. Do not imply that the
original proposals were inspected during the current task.

- Amazon: *Workspace Models for Long-Horizon Memory and Fleet-Level
  Adaptation*
- BNY: *Deep Learning Optimization for Reliable Long-Horizon Deployment*
- Jane Street: *Renewal of Funding: Recursion for Sequence Alignment*

## Amazon proposal

The Amazon proposal builds the research problem from warehouse manipulation and
fleet deployment. It opens with long-horizon tasks, then names the information
a robot must retain and the constraints that make standard solutions
unattractive: latency, inference cost, bandwidth, and brittleness at fleet
scale.

The proposal makes several deliberate choices:

- Treat Amazon's operations as a design constraint, not a closing use case.
- Introduce the technical objective only after the operational problem is
  concrete.
- Establish the lab's authority early through closely related achievements,
  including joint work with an Amazon Scholar.
- Connect the proposed method to a recurring principle from the lab's past
  research.
- Organize the agenda into phases that move from workcell memory to fleet
  adaptation.
- Evaluate both scientific performance and sponsor-relevant constraints such
  as memory, latency, and accelerator cost.
- End with concrete deliverables and a proposed mode of collaboration.

The company appears throughout the problem, architecture, evaluation, and
impact. Sponsor fit is structural rather than appended.

## BNY proposal

The BNY proposal begins with the broad failure of AI systems over long
deployment horizons, then makes the stakes vivid through severe real-world
failures. It narrows that problem to financial systems through fraud signals,
risk assessment, and live decision-making.

Its main choices are:

- Motivate a broad technical pathology before presenting the optimizer.
- Use past research, industry trials, adoption, and invited presentations to
  establish authority.
- Propose a drop-in intervention that matches an enterprise sponsor's need for
  practical adoption.
- Translate technical performance into reliability on rare, high-stakes cases.
- Connect open evaluations and optimizer code to a path for sponsor testing and
  operational use.
- State personnel and deliverables explicitly.

The story keeps one technical theme, test-time feedback, across motivation,
prior work, method, sponsor value, and deliverables.

## Jane Street renewal

The Jane Street proposal uses a renewal structure. It opens with the prior
project, explains how the research produced a sharper core problem, and then
shows concrete progress before requesting the next cycle.

Its main choices are:

- Lead with stewardship of prior funding and the intellectual progression of
  the work.
- Motivate multimodal alignment before explaining the architecture.
- Use a financial example to make an abstract sequence problem relevant to the
  sponsor without rewriting the entire agenda around finance.
- Present implemented systems, baselines, tools, and early results as evidence
  that the next plan is credible.
- Separate current status, next steps, evaluation, qualifications, and the
  funding request.
- Name both the student lead and the advising expertise that make execution
  plausible.

For a renewal, demonstrated progress carries more weight than a fresh promise.

## Shared choices

Across the three proposals:

1. **Lead with a real problem.** Explain the failure mode and stakes before the
   intervention.
2. **State a sharp objective early.** Give the reader a compact thesis after
   motivation.
3. **Use achievements as proof.** Connect prior work directly to the proposed
   agenda.
4. **Make the sponsor specific.** Tie the problem, constraints, evaluation, or
   adoption path to the company.
5. **Keep one story.** Repeat the same core problem through prior work,
   approach, phases, and impact.
6. **Show a credible path.** Pair ambition with prototypes, preliminary
   evidence, baselines, milestones, and named personnel.
7. **Write with technical confidence.** Use direct claims, concrete mechanisms,
   first-person ownership, and precise examples.

## Adapt rather than copy

- Do not transfer company-benefit language to nonprofit proposals.
- Do not emphasize connections to a nonprofit funder as a reason to award the
  grant.
- Do not let sponsor references crowd out the scientific problem.
- Do not turn prior achievements into a CV paragraph; use only evidence that
  advances the proposal's logic.
- Do not preserve technical density when it displaces motivation.
- Do not copy superlatives or adoption claims unless the current record
  supports them.
