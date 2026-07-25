---
name: grant-writing
description: Develop and revise grant proposals and fellowship applications by leading with the core problem, establishing team credibility through relevant achievements, and adapting sponsor fit for either for-profit company sponsors or nonprofit and philanthropic funders. Use for proposal narratives, specific aims, significance, innovation, approach, impact, broader impacts, milestones, sponsor questions, renewals, and fellowship applications.
---

# Grant Writing

Build the proposal from motivation outward. Make the reader care about the
problem before asking them to evaluate a technical intervention.

## Load guidance selectively

- Read [sponsor-types.md](references/sponsor-types.md) before planning a full
  proposal or rewriting sponsor fit. Classify the funder before drafting.
- Read [example-proposal-patterns.md](references/example-proposal-patterns.md)
  when planning the story, matching the author's established grant voice, or
  deciding how to use prior achievements.
- Before returning any drafted or revised proposal prose, read
  `../general-writing/SKILL.md` and
  `../general-writing/references/eval.md`. Its edit workflow runs Humanizer
  first and the house-style check second. Do not load or run Humanizer
  separately. Apply the ordered prose pass only after the argument, evidence,
  and sponsor fit are settled.

## Resolve optional example proposals

The bundled proposal patterns are sufficient by default. When the task calls
for inspecting original examples, such as matching the author's established
grant voice or checking how prior achievements were used:

1. Use an example directory explicitly supplied for the current task.
2. If no directory was supplied, ask: "Where is the folder containing the
   example proposals for this task? You can say `none` to use the bundled
   proposal patterns."
3. Accept a direct corpus directory under any name. Also accept a parent
   directory containing the conventional `example grants` child.
4. Confirm that the resolved directory is readable before relying on it.
5. If the user answers `none` or the directory is unavailable, use
   [example-proposal-patterns.md](references/example-proposal-patterns.md) and
   say that the original proposals were not inspected.

Do not search above the repository, infer a location from the user's home
directory, or copy private examples into this repository.

## Start with the funder and constraints

1. Read the solicitation, evaluation criteria, instructions, templates, and
   length limits in full.
2. Classify the primary funder:
   - **For-profit or company-sponsored:** center operational or strategic value,
     relevant company constraints, and credible paths to adoption.
   - **Nonprofit or philanthropic:** center the funder's vision, the scientific
     or societal problem, and the value created for the field or public.
3. Map every required question and scoring criterion to an explicit response.
4. Identify the audience's technical depth, decision authority, and likely
   objections.
5. Flag missing facts, evidence, commitments, or compliance details before
   polishing prose.

## Build the story

Use this default sequence unless the application form requires another order:

1. **Core problem and stakes.** State what is failing, blocked, or newly
   possible. Make the consequences concrete for the relevant audience.
2. **Why now.** Explain the change in capability, scale, evidence, or urgency
   that makes the problem timely.
3. **Limits of current approaches.** Identify the precise obstacle. Do not use a
   generic literature gap.
4. **Objective or thesis.** State the proposal's central idea in one or two
   sentences. Name it only when the name improves recall.
5. **Team credibility.** Select prior achievements that prove the team can
   execute this agenda. Connect each achievement to the proposed work.
6. **Approach.** Give enough technical detail to establish plausibility,
   novelty, and a concrete plan. Keep details subordinate to the problem.
7. **Execution and evaluation.** Define phases, milestones, risks, tests,
   outputs, and measures of success.
8. **Impact and fit.** Explain why success matters under the funder's actual
   goals, using the sponsor-type rules.
9. **Support requested.** State what the funding enables and why those resources
   are the binding need.

## Center motivation

- Spend the opening on the problem, its stakes, and why existing approaches
  fail under the conditions that matter.
- Describe the core problem in domain terms before introducing a model,
  architecture, optimizer, benchmark, or acronym.
- Connect technical challenges to real consequences: reliability, safety,
  scientific bottlenecks, deployment cost, access, coordination, or field-wide
  progress.
- Make the proposed intervention feel like the necessary response to the
  problem, not an idea searching for a use case.
- Delay implementation detail until the reader understands what must change and
  why.
- Include technical detail only when it proves feasibility, distinguishes the
  idea, clarifies risk, or supports evaluation.
- Return to the core problem at major transitions so phases and deliverables
  remain part of one story.

## Establish credibility

- Use past achievements as evidence, not as a detached biography.
- Select the few results most relevant to the proposed problem.
- State what was achieved, where it mattered, and how it prepares the team for
  the next step.
- Prefer concrete evidence such as prior methods, deployed systems, adoption,
  preliminary results, awards, datasets, or completed milestones.
- For renewals, lead with progress, what the work revealed, and why the next
  cycle is the natural continuation.
- Distinguish completed work, preliminary evidence, planned work, and
  speculation.

## Preserve the author's voice

- Use a direct, confident, technically serious tone for both corporate and
  nonprofit proposals.
- Write in the first person when describing the team's work and commitments.
- Prefer concrete mechanisms and outcomes to generic claims of importance.
- Make strong claims only when the supplied record supports them.
- Keep technical precision without writing the proposal as a paper abstract.
- Avoid sales language, generic praise of the sponsor, mission-statement
  paraphrase, and inflated claims.
- Keep the same voice across funder types; change the theory of value and the
  evidence of fit, not the prose personality.

## Protect factual integrity

- Do not invent preliminary results, citations, budgets, timelines, partner
  commitments, institutional capabilities, sponsor priorities, or existing
  relationships.
- Do not imply that exploratory work is complete.
- Use bracketed placeholders for missing facts that the author must supply.
- Preserve calibrated uncertainty while explaining how the plan manages it.
- Treat the solicitation and scoring rubric as higher priority than this skill.

## Final review

1. Confirm that the opening motivates the problem before describing the
   intervention.
2. Confirm that every technical section answers a question raised by the
   motivation.
3. Confirm that prior achievements support the proposed work rather than merely
   decorate the application.
4. Confirm that sponsor fit follows the correct corporate or nonprofit model.
5. Confirm that each review criterion has visible evidence.
6. Confirm that milestones measure outcomes, not only activity.
7. Run the complete general-writing workflow: Humanizer first, then the
   house-style check. Confirm afterward that the proposal retains the author's
   cadence, technical confidence, sponsor logic, and factual boundaries.
