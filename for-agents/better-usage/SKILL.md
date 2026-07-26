---
name: better-usage
description: Diagnose and repair semantically mismatched word combinations while preserving the intended claim. Use when prose is grammatical but a verb does not literally fit its subject or object, a claim or section is given an action it cannot perform, an abstract relation is hidden by vague personification, or replacing one verb still leaves a sloppy relation that needs an intermediate noun.
---

# Better Usage

Choose words that express the relation the sentence actually asserts. A
sentence can be grammatical and still sound wrong because its subject cannot
perform the named action, its object or complement does not fit the relation
expressed by the verb, or an important intermediate has been omitted.

For a full semantic-usage pass, read
[compatibility-examples.md](references/compatibility-examples.md). Treat the
examples as a curated diagnostic set, not a substitution dictionary.

## Recover The Intended Relation

1. Identify the grammatical subject, main verb, and object or complement.
2. Paraphrase the intended relation without reusing the suspect verb.
3. Ask whether the subject can literally perform that action in this domain
   and whether the verb can take that object or complement with the intended
   meaning.
4. Distinguish an accidental mismatch from accepted technical shorthand or a
   deliberate metaphor that clarifies the idea.
5. Preserve the claim, uncertainty, and domain terminology while repairing the
   relation.

Do not stop after finding a more specific verb. A new verb can remain
semantically loose.

## Name A Missing Intermediate

When the subject and verb do not connect directly, identify the omitted link.
Useful questions include:

- What entity actually acts?
- What property, extent, interpretation, or consequence changes?
- Under which conditions does the relation hold?
- Who performs the inference or needs the information?

For example, a claim does not stop, and saying that conditions "limit the
claim" still leaves the affected dimension unnamed. Write "the conditions
limit the extent of the claim" or state that "the claim applies only under
these conditions." If the intended question concerns implications rather than
validity, ask where the consequences of the theorem end.

Insert an intermediate only when it names a real part of the relation. Do not
pile up abstract nouns merely to make the sentence sound exact.

## Respect Conventional Agency

Keep established scholarly shorthand when it is clear in context. A theorem
may state or imply a result, evidence may support a claim, a figure may show a
measurement, and an algorithm may choose an action. These verbs have stable
technical meanings.

Recast the sentence when the shorthand hides a distinction that matters. For
example, "the evidence explains the effect" may collapse two relations: the
evidence supports an explanation, while the authors or analysis provide it.

## Check The Repair

- Confirm that the revised subject can perform the verb.
- Confirm that the object or complement fits the relation expressed by the
  verb.
- Confirm that any intermediate noun identifies a necessary relation rather
  than adding nominal clutter.
- Recheck epistemic force. Do not turn support into proof or correlation into
  explanation.
- Compare with the source to ensure that the repair adds no fact, mechanism,
  condition, or conclusion.
- Do not add procedural detail, sequence, or emphasis merely to replace a
  metaphor. A semantic repair does not license unsupported texture such as
  "step by step."

## Invocation Boundary

When another writing skill invokes this skill, return only the revised prose
or the requested usage findings. Do not invoke Humanizer, general-writing, or
writing-cadence; the calling skill owns the larger prose pipeline.
