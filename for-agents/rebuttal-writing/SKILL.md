---
name: rebuttal-writing
description: Draft and edit concise, reviewer-specific author responses in clear academic English. Use for paper rebuttals, response letters, revise-and-resubmit memos, reviewer-response matrices, evidence triage, claim calibration, bounded concessions, or non-defensive rewrites of verbose response prose.
---

# Rebuttal Writing

Preserve the facts and evidence supplied for the task. Never invent completed
experiments, citations, manuscript edits, or reviewer positions.

Write so that a reviewer can identify the answer, support, and claim boundary
without rereading the paragraph.

## Select The Workflow

- For a complete rebuttal, read the manuscript, decision letter, every review,
  venue rules, and length limit. Copy
  [rebuttal-worksheet.md](assets/rebuttal-worksheet.md) into the working
  directory and fill it before drafting.
- For evidence planning, experiment claims, or high-risk concerns, read
  [evidence-and-risk.md](references/evidence-and-risk.md).
- For novelty, confounds, scope, theory, missing baselines, efficiency,
  qualitative evidence, or presentation concerns, read
  [response-patterns.md](references/response-patterns.md).
- For a prose-only rewrite, apply the style rules below without expanding the
  response strategy unless the user asks.

Map every reviewer comment to an explicit response. Keep reviewer quotations,
author responses, and proposed manuscript text visibly distinct. Flag missing
evidence or decisions for the authors instead of writing around them.

## Use A Calm Academic Voice

Aim for language that is:

- **formal but natural:** use standard technical English, not legalistic or
  ornate prose;
- **confident but bounded:** state supported conclusions directly and mark
  their limits;
- **respectful but not deferential:** engage the concern without praising the
  reviewer at length;
- **candid but not self-defeating:** acknowledge a defect or limitation
  plainly, then state what remains supported; and
- **technical but readable:** prefer ordinary verbs and concrete nouns over
  jargon, nominalizations, and intensifiers.

The tone should feel composed. Do not sound injured, excited, pleading,
triumphant, or eager to win an argument.

## Put The Answer In The First Sentence

Open with the response's actual position. Use one of these moves:

- **Correct:** "`X` is intentional because..."
- **Concede:** "This is a typo; the correct expression is..."
- **Narrow:** "We do not claim X. Our claim is limited to Y."
- **Qualify:** "X can be more efficient when it works. Our claim concerns Y."
- **Bound:** "We have not evaluated X, so we will restrict the statement to
  Y."

The first sentence must contain the technical answer. Treat any opening such
as "We thank the reviewer..." as text to delete. Do not begin with gratitude,
a recap of the paper, or a full restatement of the review. The reviewer should
not have to infer whether the authors agree, disagree, or lack evidence.

## Use A Four-Sentence Rhythm

For a substantive concern, prefer this sequence:

1. **Verdict:** answer the concern.
2. **Distinction:** explain the key reason or correct the premise.
3. **Support:** state the relevant result or paper evidence.
4. **Boundary or edit:** limit the inference or name the exact revision.

Use three to five sentences in most paragraphs. A typo, citation, or local
wording issue often needs only one or two.

Template:

> **[Short concern heading].** [Direct answer.] [Key distinction or reason.]
> [Concrete support.] [Narrow conclusion or exact manuscript edit.]

Omit any sentence that merely repeats the concern or announces what the next
sentence will do.

## Write Plain, Controlled English

- Use first-person plural and active verbs: "we compare," "we find," "we
  hypothesize," and "we will revise."
- Put the main clause first. Prefer "The equation is intentional" to "While we
  appreciate the concern, we would like to clarify that the equation is
  intentional."
- Give each sentence one job. Split a sentence that both explains the method
  and reports several results.
- Prefer short and medium-length sentences. Use a longer sentence only when
  the relationship between clauses matters.
- Use explicit contrast: "X supports Y; it does not establish Z."
- Prefer full forms such as "do not" and "cannot" to contractions.
- Use pronouns only when their referents are unmistakable. Repeat the key
  technical noun when "this" could refer to several claims.
- Keep parenthetical remarks rare. Move important qualifications into the
  sentence.
- Use parallel grammar in lists and comparisons.
- Use short noun-phrase headings such as "**Compute cost**" or
  "**Multimodality**."
- Do not use rhetorical questions, exclamation marks, or dramatic fragments.

Useful transitions include "Specifically," "In contrast," "However," and
"Therefore." Use them only when they express a real logical relation. Do not
start every sentence with a transition.

## Calibrate Claim Verbs

Make the verb match the strength of the evidence:

| Evidence status | Preferred language |
|---|---|
| Directly established | "shows" or "demonstrates" |
| Supports but does not isolate | "supports," "suggests," or "is consistent with" |
| Proposed mechanism | "we hypothesize" or "we conjecture" |
| Untested case | "we have not evaluated" |
| Planned manuscript change | "we will revise" |

Reserve "shows" and "demonstrates" for direct evidence. "We believe" does not
strengthen a claim; state the evidence or label the hypothesis instead.

Preserve time and status in the grammar:

- "Figure 4 reports..." for material already in the paper.
- "We ran..." for completed rebuttal evidence.
- "We will revise..." for a future edit.
- "We have not evaluated..." for missing evidence.

Never turn a plan into a result.

## Disagree Without Sounding Defensive

Correct the premise, not the reviewer.

Write:

> `a_{t,0}` is intentional because only the fully denoised action is executed.

Do not write:

> The reviewer appears to have misunderstood our formulation.

Use "we agree" only when conceding a real point. Do not use it as a polite
preface to disagreement. Avoid "we would like to clarify"; make the
clarification directly.

Omit gratitude by default. If the user explicitly asks for a warmer tone, use
at most one short thank-you after the technical answer. Never ask for a higher
score or claim that a concern has been "fully addressed."

## Concede In A Bounded Way

Use this pattern:

> [Concede the narrow fact.] [State the repair or limitation.] [State the
> narrower claim that remains supported.]

Example:

> Q-learning can be more sample efficient when it is effective. We therefore
> restrict our claim to stability and final performance in the tested
> high-precision tasks.

Do not hide a concession behind praise or immediately erase it with "but."
A clean concession makes the remaining claim more credible.

## Phrase Evidence Economically

Name the comparison before interpreting it. When numbers are supplied, give
the value, comparator, and setting. Report an unfavorable result before
explaining the relevant tradeoff.

End with a scope sentence when the result is easy to overread:

> This supports X in the tested setting; it does not establish Y.

Avoid vague substitutes such as "performs similarly," "improves
significantly," or "may not necessarily generalize." State the comparison,
then state its limit.

## Describe Novelty Precisely

Use three clauses:

1. name the established ingredients;
2. state the exact new formulation, finding, or controlled comparison; and
3. explain what the prior ingredients did not already imply.

Prefer:

> Diffusion and PPO are established. The contribution is the two-level MDP
> formulation and the finding that their combination remains stable in the
> tested precision-sensitive tasks.

Avoid "highly novel," "fundamentally new," "the first," and "all you need"
unless the literature boundary is both verified and necessary. Surprise,
implementation effort, and author intent are not novelty arguments.

## Name Revisions Exactly

Prefer:

> We will replace "expressivity" with "high-Lipschitz behavior" in Section 3.

Avoid:

> We will improve the presentation and clarify this point.

Name the sentence, term, equation, figure, or section being changed. Use the
future tense only for a change that will actually be made.

## Grounded Language Models

The following examples distill recurring prose patterns in the OGPO, DPPO,
and Much Ado author-team responses. Copy the linguistic move, not the
technical content. Verify every symbol and fact against the current paper.

### OGPO: Neutral Correction

> **Why \(a_{t,0}\)?** \(a_{t,0}\) is intentional. The critic is trained on
> the fully denoised action executed in the environment; intermediate
> denoising states are not environment actions. We will state this
> distinction explicitly.

Language pattern: a declarative verdict, one clean contrast, and one exact
revision. The response never attributes the confusion to the reviewer.

### OGPO: Candid Tradeoff

> **Compute.** OGPO is slower per update. Its claim is sample efficiency, not
> cheaper gradient updates.

Language pattern: state the unfavorable fact first, then use "X, not Y" to
define the claim.

### DPPO: Compact Concession

> **Discounting.** This is a typo. The exponent should be
> \(\gamma_{\mathrm{ENV}}^{t'-t}\), and we will correct the equation.

Language pattern: no ceremonial apology, no defense, and no extra
explanation for a local error.

### DPPO: Bounded Qualification

> Q-learning can be more sample efficient when it is effective. Our claim is
> narrower: DPPO is more stable in the tested high-precision tasks.

Language pattern: concede first, then use "Our claim is narrower" to prevent
an overbroad reading.

### Much Ado: Scope A Categorical Claim

> We do not claim that generative control policies cannot be multimodal. Our
> claim is that multimodal fitting is not necessary to explain the measured
> gap in the benchmarks studied here.

Language pattern: paired "We do not claim X / Our claim is Y" sentences make
the boundary unmistakable.

### Much Ado: Accept A Confound Without Losing The Point

> Architecture matching explains part of the earlier gap. This is a result of
> the controlled comparison, not an unwanted confound.

Language pattern: accept the premise directly, then recast its scientific
meaning in one sentence.

### Much Ado: State A Negative Result Plainly

> A third MIP step did not materially improve performance, so we retain two
> steps for efficiency. This indicates saturation in the tested setting, not
> universal optimality.

Language pattern: report the null result without embarrassment and close with
a narrow inference.

## Remove Weak Rebuttal Phrasing

Replace:

- "We sincerely thank the reviewer for this insightful question" with the
  answer.
- "We would like to clarify that..." with the clarification.
- "The reviewer misunderstood..." with a neutral correction.
- "We strongly believe..." with evidence or a labeled hypothesis.
- "Our method is highly novel..." with the exact distinction.
- "The results improve significantly..." with the comparison.
- "It is important to note that..." with the point itself.
- "This fully addresses the concern..." with nothing.
- "We hope the reviewer will reconsider..." with nothing.

Also remove unsupported intensifiers: "clearly," "obviously," "strongly,"
"fundamentally," "remarkably," and "extremely."

## Run A Final Style Pass

Check that:

- each heading names one concern;
- each first sentence gives the answer;
- the English is plain, formal, and active;
- each sentence performs one function;
- every contrast has a clear X and Y;
- every claim verb matches the evidence;
- every limitation or hypothesis is explicit;
- every concession preserves only a defensible narrower claim;
- no generic gratitude delays the response;
- no sentence blames or pressures the reviewer;
- no technical detail appears unless it advances the answer; and
- every sentence earns its place under the venue limit.
