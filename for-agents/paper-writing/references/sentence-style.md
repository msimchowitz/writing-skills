# Preferred Sentence Style

This guide describes the sentence patterns recurring across the example
papers. Use it for research prose, then apply the sibling `general-writing`
skill as the final line edit.

## Default Shape

Default to a declarative sentence with the main subject and verb near the
front:

> We compare [methods] under [controlled setting].

> Action chunking limits [specific failure] under [assumption].

Use a fronted dependent clause only when it supplies a necessary condition,
contrast, or cause:

> Although [established result], [new result].

> When [regime holds], [intervention] guarantees [outcome].

> Because [mechanism], [observed consequence].

Do not put generic scene-setting before the main clause. A sentence beginning
with "While," "Although," "Given," or "Because" must change how the main claim
is interpreted.

## One Main Inference Per Sentence

A sentence may contain a claim and its essential condition, mechanism, or
qualification. Split it when it also tries to report a second result or a broad
implication.

Prefer:

> OGPO reuses environment data through an off-policy critic. It optimizes the
> denoising process with on-policy updates, where additional samples are
> computationally cheap.

Avoid packing the method, every result, the mechanism, and the implication into
one sentence.

Long sentences are acceptable when all clauses serve one logical relation.
Short sentences should carry a real claim, not manufacture drama.

## Paragraph Cadence

Most technical paragraphs should perform three or four moves:

1. **Claim:** state the paragraph's point.
2. **Reason or distinction:** explain why the point holds or what it contrasts
   with.
3. **Evidence:** give the theorem, comparison, measurement, or example.
4. **Scope or consequence:** state the supported inference.

Do not force all four moves when two suffice. Vary sentence length and syntax so
the prose does not become mechanical. End on a consequence, boundary, or
transition, not a generic recap.

## Preferred Subjects And Verbs

Use **we** for author actions:

- we introduce;
- we compare;
- we show;
- we find;
- we hypothesize; and
- we leave [question] open.

Use the technical object as subject when it has the relevant behavior:

- the critic supplies the terminal reward;
- action chunking stabilizes the learned policy; and
- the control isolates architecture from parameterization.

Prefer direct verbs to nominalizations. Write "we compare" instead of "we
conduct a comparison" and "the policy fails" instead of "the policy exhibits a
failure."

## Contrast Without A Canned Template

Contrast is central to this voice, but it should express a scientific
distinction.

Prefer:

> Current methods trade off sample efficiency and full-policy improvement.

> Distribution learning explains less of the performance gap than supervised
> iterative computation.

> The experiment supports manifold adherence as a useful proxy in these tasks;
> it does not establish a general causal theory.

Avoid repetitive "This is not X. It is Y," "not only X but also Y," and
"rather than merely X, we Y" constructions. Preserve a precise scope contrast
when it prevents an overclaim.

## Quantitative Sentences

Order quantitative evidence as:

1. comparison;
2. metric;
3. result;
4. setting or uncertainty; and
5. interpretation, if supported.

Template:

> Compared with [baseline], [method] improves [metric] from [A] to [B] on
> [setting], averaged over [seeds/trials]. This supports [narrow inference].

Do not replace values with "substantially," "significantly," or "performs
better" when the values are available. Reserve "significant" for a defined
statistical claim.

## Theory Sentences

State the regime before the consequence when the claim depends on it:

> Under [assumptions], [intervention] guarantees [bound].

Separate theorem content from interpretation:

> Theorem 2 bounds [quantity] by [rate]. Thus, in [regime], the error does not
> grow with [variable].

Preserve quantifiers, conditioning, asymptotic terms, and theorem scope exactly.
Do not turn an intuition into theorem language.

## Mechanism Sentences

Separate observation from explanation:

> We observe [measured behavior]. We hypothesize that [mechanism] causes this
> behavior because [support].

Use "shows" for direct evidence, "supports" for partial evidence, and
"suggests" or "is consistent with" for an interpretation. Do not use "we
believe" as a substitute for evidence.

## Definitions And Terms

Introduce a term, then give its operational meaning:

> We call this property manifold adherence: the policy keeps predicted actions
> near plausible action sets under perturbed observations.

Repeat the canonical technical term instead of cycling through synonyms. Use a
pronoun only when its referent is unambiguous.

## Punctuation And Rhythm

- Use commas to mark a real clause boundary, not every pause.
- Use semicolons sparingly to join claims whose relationship matters.
- Use colons for definitions, lists, labels, or quotations, not dramatic
  reveals.
- Keep parentheses for notation, citations, and genuinely secondary detail.
- Use em dashes rarely; prefer a period, comma, or parentheses.
- Use a research question only when it is the paper's actual organizing
  question, not as a rhetorical setup.
- Avoid stacked fragments and runs of identically shaped sentences.

## Final Sentence Audit

- Is the main subject and verb easy to find?
- Does every opening clause constrain or motivate the main claim?
- Does the sentence make one main inference?
- Is the agent explicit?
- Does the verb match the evidence?
- Are comparison, metric, and setting visible?
- Is uncertainty or scope preserved?
- Could a shorter sentence improve clarity without flattening cadence?
- Does the paragraph vary naturally rather than follow a repeated template?
