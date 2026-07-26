---
name: paper-writing
description: Plan, draft, revise, and structure technical research papers while preserving claims, notation, evidence, citations, and author voice. Use for abstracts, introductions, related work, methods, theory, experiments, results, discussions, conclusions, figures, appendices, LaTeX project organization, or whole-manuscript design.
---

# Paper Writing

Preserve the facts and evidence supplied for the task. Never invent citations,
experiments, quantitative results, theorem conditions, novelty claims, or
completed revisions.

The `../../for-humans/human-writing-guide/` directory is a companion
written for people, not an agent skill. For ordinary drafting, use this skill
and its focused references. When the user asks how to use the bundled
OGPO-derived LaTeX template, wants material for teaching or onboarding, or
asks for a human-readable explanation, consult or point them to the relevant
part of the
[human guide](../../for-humans/human-writing-guide/human-writing-guide-main.pdf). If
that companion is not present in an installed copy, continue with this
skill's bundled references. Never route to the guide as though it were a
skill.

## Select The Workflow

- For an abstract-only request, read and follow the sibling
  [abstract-writing skill](../abstract-writing/SKILL.md). Let that skill own
  the final general-writing pass so the prose pipeline runs once.
- For other drafting or revision of scholarly prose, read the sibling
  [academic-voice skill](../academic-voice/SKILL.md) before the relevant
  paper-specific references.
- For a new paper or major restructure, copy
  [paper-plan.md](assets/paper-plan.md) into the project and complete it before
  drafting.
- For a theory-led paper, use
  [theory-paper-outline.md](assets/theory-paper-outline.md).
- For an empirical method or mechanism paper, use
  [empirical-paper-outline.md](assets/empirical-paper-outline.md).
- For a figure plan or figure review, use
  [figure-storyboard.md](assets/figure-storyboard.md).
- For the Simchowitz-group paper patterns distilled from DPPO, OGPO, Much Ado
  About Noising, and Action Chunking, read
  [group-paper-conventions.md](references/group-paper-conventions.md).
- For drafting or line-editing paper prose, read
  [sentence-style.md](references/sentence-style.md) before writing.
- For LaTeX structure, venue styles, project styles, toggles, macros, and
  source hygiene, read
  [latex-project-conventions.md](references/latex-project-conventions.md).
  For the exact theorem environments, heading toggles, algorithm-name macros,
  revision colors, title metadata, and other conventions in the bundled
  OGPO-derived template, also consult the template chapter in the
  [human guide](../../for-humans/human-writing-guide/human-writing-guide-main.pdf) when
  it is present.
  Copy [latex-paper-skeleton](assets/latex-paper-skeleton) only when creating a
  new LaTeX project. Rename its `paper-main.tex` entry point to a stable,
  descriptive `<project-name>-main.tex` before drafting. Adapt an existing
  repository in place otherwise.

## Resolve Optional Example Papers

The bundled paper conventions are sufficient by default. When the task calls
for inspecting original examples, such as matching the author's established
voice or checking a distilled convention:

1. Use an example directory explicitly supplied for the current task.
2. If no directory was supplied, ask: "Where is the folder containing the
   example papers for this task? You can say `none` to use the bundled
   conventions."
3. Accept a direct corpus directory under any name. Also accept a parent
   directory containing the conventional `example-papers` child.
4. Confirm that the resolved directory is readable before relying on it.
5. If the user answers `none` or the directory is unavailable, use
   [group-paper-conventions.md](references/group-paper-conventions.md) and say
   that the original papers were not inspected.

Do not search above the repository, infer a location from the user's home
directory, or copy private examples into this repository.

## Build The Argument Before The Prose

1. State the practical or scientific problem in one sentence.
2. State why the strongest current explanation or method is insufficient.
3. State the paper's central claim, demonstrated scope, and main limitation.
4. Build a claim-evidence map. Assign every major claim a theorem, controlled
   comparison, ablation, mechanism study, qualitative result, or explicit
   limitation.
5. Choose the paper architecture from the evidence rather than from a fixed
   section list.
6. Give each section one question to answer and each paragraph one inferential
   job.
7. Design Figure 1 as a compact version of the full argument, then make every
   later figure resolve one question left open by Figure 1.
8. Draft from the strongest evidence outward. Write the abstract and title only
   after the claim hierarchy is stable.

Treat the abstract as a reader's first encounter with the argument, not as a
compressed table of contents. It should establish the problem, central answer,
decisive evidence, and the conditions that govern the extent of the claim. Do
not give every section, benchmark, or implementation detail equal space.

## Use Claim-Led Sections

- Prefer informative section titles that state the result or question.
- Put setup before the first result that needs it, but do not front-load every
  definition.
- Present headline performance before mechanism studies and low-level
  ablations in empirical papers.
- Present the motivating failure or impossibility before the intervention in
  theory papers.
- Place related work early only when distinctions from prior methods are
  required to understand the approach. Otherwise place it after the main
  results to preserve momentum.
- Move implementation detail, full proofs, complete sweeps, hyperparameters,
  and secondary controls to the appendix while keeping decision-critical
  evidence in the main paper.
- End with supported scope, concrete limitations, and open questions. Do not
  introduce a new contribution in the conclusion.

## Write In A Direct Technical Voice

- Use active first-person verbs: "we show," "we find," "we compare," and "we
  hypothesize."
- Build contrast explicitly: established view, observed failure, new finding,
  consequence.
- Name the comparator, metric, regime, and evidence before interpreting a
  result.
- Distinguish direct evidence from interpretation and proposed mechanism.
- Use "shows" or "demonstrates" only for direct evidence; use "supports,"
  "suggests," or "is consistent with" for partial evidence.
- Use bold or italics to expose argumentative structure, not to decorate most
  sentences.
- Prefer concrete claims over generic statements of importance.
- Keep notation and method names semantic and consistent through macros.

## Preserve Technical Integrity

- Read the relevant manuscript, source, figures, captions, and appendix before
  editing claims.
- Preserve notation, assumptions, theorem quantifiers, experimental settings,
  citations, and calibrated uncertainty.
- Check that a figure caption and the surrounding paragraph make the same
  claim.
- Check that every abstract claim appears in the main paper and that every
  introduction contribution has visible evidence.
- Check the abstract separately from the body. Verify its inferential arc,
  evidence verbs, quantitative comparisons, and claim boundary against the
  supporting sections.
- Surface unresolved logical gaps or missing controls instead of writing around
  them.
- Make the minimum structural change needed unless the user requests a larger
  rewrite.

## Run The Final Voice Pass

After the argument, claims, notation, citations, and section order are stable:

1. Read [sentence-style.md](references/sentence-style.md).
2. Treat the current manuscript and any selected example papers as voice
   evidence.
3. Read the sibling
   [general-writing skill](../general-writing/SKILL.md) and its
   [evaluation checklist](../general-writing/references/eval.md).
4. Run its complete edit workflow. It invokes Humanizer in embedded mode before
   applying the house-style check, so do not run Humanizer separately.
5. Recheck every edited comparison, qualifier, number, citation, symbol, and
   claim boundary against the source.

Use `general-writing` as the prose enforcer, not as authority to simplify away
technical meaning. Preserve a term that is technically necessary even if it
appears on a general avoid-list. Preserve a logical contrast while removing
canned binary phrasing. The final house-style check may restore a construction
that Humanizer removed when the manuscript or example corpus shows that it is
part of the author's technical voice.

Report substantive changes to claims, evidence, or section structure separately
from line edits.
