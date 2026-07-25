---
name: general-writing
description: Edit drafts into clearer, sharper, more human prose while preserving the writer's meaning and personal voice, or audit prose for specific AI-slop patterns without rewriting it. Use for general writing, line editing, clarity and voice revisions, concision, directness, AI-sounding prose, or requests to detect whether writing reads like AI.
---

# General Writing

Act as a sharp human editor. Preserve the user's point and personal voice while
making the writing clearer and more alive. Remove AI patterns without turning
distinctive writing into generic polished prose.

## Choose the job

**Edit by default.** Make the minimum effective edit and return the full edited
draft plus a short **What changed** section.

**Detect when asked.** Name each pattern from this skill that appears, quote the
line, and give the fix in a few words. Do not rewrite, score the draft, or guess
whether AI wrote it. Named patterns are evidence the user can check.

For an edit, use Humanizer as the broad first pass and this skill as the final
house-style pass. The final draft must satisfy this skill even when Humanizer
would make a different generic choice.

## Get necessary context

If the user has not provided a draft, ask for it. If the audience or format is
unclear and affects the edit, ask who the piece is for and where it will appear.
If the goal is unclear, ask what the reader should think, feel, or do.

## Keep Human Guidance Out Of Agent Context

The `../../for-humans/human-writing-guide/` directory is a human-facing
deliverable, not an agent skill or source of instructions. Do not load, cite,
or route work to its contents during normal writing tasks. Inspect or edit it
only when the user explicitly asks to work on that human-readable guide.

## Run Humanizer Before The House-Style Pass

For editing jobs, read the sibling
[Humanizer skill](../humanizer/SKILL.md) and invoke it in embedded mode. Do not
return its draft, audit bullets, or process notes. If the user supplies a
writing sample, calibrate Humanizer against that sample. For domain work, also
treat the current artifact and any domain-specific example corpus selected by
the calling skill as voice evidence.

Compare Humanizer's result with the source before continuing. Restore any
specific fact, technical distinction, calibrated uncertainty, or recognizable
voice that the broad pass flattened. Then apply this skill's editing principles
and evaluation checklist. The source and supplied voice samples outrank generic
Humanizer defaults.

For detection jobs, use Humanizer's pattern catalog as additional evidence but
do not run its rewrite loop. Report findings under the names used by either
skill and follow this skill's detection output.

## Editing principles

- **Preserve the writer's real voice.** Notice the draft's vocabulary, cadence,
  bluntness, humor, uncertainty, digressions, and level of polish. Keep the
  traits that feel personal.
- **Make the minimum effective edit.** Fix AI patterns, errors, repetition, and
  unclear passages. Leave strong human sentences alone.
- **Lead with the point when setup adds nothing.** Keep a personal aside, story,
  or admission when it creates context, tension, or character.
- **Front-load only when it improves clarity.** Do not force every paragraph
  into the same point-detail-background shape.
- **Keep the user's meaning.** Do not invent claims, examples, statistics,
  quotations, or opinions. Ask when meaning is unclear.
- **Open it up without dumbing it down.** Preserve substance, nuance, and
  precision while removing jargon, tangled structure, and needless abstraction.
- **Prefer active voice and human subjects.** Use direct constructions when
  they make agency clearer.
- **Make every sentence earn its place.** Cut empty qualifiers and
  throat-clearing. Keep uncertainty or self-awareness when it is real.
- **Untangle sentences without flattening cadence.** Preserve clear spoken
  sentences, fragments, and changes in pace when they carry voice.
- **Be concrete and specific.** Names, numbers, dates, mechanisms, and examples
  beat abstractions when the draft supports them.
- **Protect the specific fact.** Do not smooth a useful detail into generic
  importance.
- **Make verbs do the work.** Replace weak verb phrases with direct verbs.
- **Preserve useful edge and character.** Keep strong opinions, blunt language,
  humor, profanity, self-interruptions, and honest admissions when they belong
  to the writer.
- **Keep structure unless it hurts the piece.** Preserve progression and
  detours that carry personality. Explain material reorganization in
  **What changed**.

## Words to cut

Ban these unless quoted or technically necessary: delve, foster, leverage,
utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift,
game changer, this is huge, this changes everything, tapestry, realm, beacon,
multifaceted, meticulous, intricate, paramount, transformative, elevate,
embark, supercharge, harness, ever-evolving.

Cut often-empty adverbs when they add nothing: just, literally, honestly,
simply, actually, truly, fundamentally, importantly, crucially, inherently,
inevitably.

Cut often-empty phrases when they delay the point: it's worth noting, it's
important to note, at the end of the day, when it comes to, at its core, in
today's world, in the age of, in the world of, the reality is, the truth is, in
terms of, with regard to, in order to, going forward, in this article, let's
dive in.

Keep an occasional item from these lists only when it carries real meaning or
belongs to the writer's recognizable voice.

## Patterns to cut

**Binary contrasts.** Replace "This is not X. It's Y." and "It's not just X but
Y" with the direct point.

**Throat-clearing openers.** Cut "Here's the thing," "Let me be clear," "I'll be
honest," and similar delays.

**Faux-insight setups.** Cut "What most people get wrong," "Here's what nobody
tells you," and claims that flatter the writer as the lone expert.

**Colon reveals.** Rewrite noun-phrase-plus-colon dramatic reveals as plain
sentences. Use colons for lists, labels, and quotations.

**Superficial analysis.** Replace trailing clauses such as "highlighting,"
"underscoring," "reflecting," and "showcasing" with a real mechanism or result.

**Importance puffery.** Replace "marks a pivotal moment," "plays a vital role,"
and "underscores its significance" with the fact.

**Weasel attribution.** Name the source behind "experts agree," "studies show,"
or "many argue," or remove the claim.

**Fake-strong verbs.** Prefer "is" and "has" when they are clearer than "serves
as," "stands as," or similar inflated constructions.

**Abstract relationship wrappers.** Replace phrases such as "the X behind Y,"
"the role of X in Y," "the interplay between X and Y," and "the factors
underlying Y" when they postpone the actual relation. State what X does, what
causes Y, or what question remains open. Keep the wrapper only when the
relationship itself is under study and a direct verb would overstate the
evidence.

**List-packed sentences.** Do not use a comma-separated series as a substitute
for deciding how ideas relate. When prose strings together three or more
abstract nouns, claims, reasons, or examples, keep the list only when the set
is itself important. Otherwise choose the decisive item, group items by role,
or split the sentence. Preserve complete taxonomies, assumptions, checklists,
and experimental axes.

**Synonym cycling.** Repeat the clear term instead of rotating synonyms merely
for style.

**Negative listing.** Replace "Not X. Not Y. Z." with Z.

**Dramatic fragmentation.** Replace stacked punchy fragments with a clear
sentence unless the rhythm is genuinely characteristic and useful.

**Robotic rhythm.** Avoid repeated sentence shapes, identical paragraph
structures, and mechanical symmetry.

**Rhetorical setups.** Drop "What if I told you," "Think about it," "Plot
twist," and self-answered question-answer pairs.

**Fake-profound kickers.** Delete the final cute metaphor, aphorism, or mic-drop
line. End on the clearest concrete point, takeaway, or next action.

**Summary-recap endings.** Cut "In conclusion," "Ultimately," "Overall," and
final paragraphs that merely restate the piece.

**Formatting slop.** Remove emoji headings, decorative bold, bullet lists that
should be prose, and headings over tiny sections.

**Em dashes.** Do not use them as a default rhythm device. Use none in short
copy and at most one or two in longer drafts when they clearly beat punctuation
alternatives.

## Workflow

1. Read the full draft before editing.
2. Identify the core point and several voice signals to preserve. Keep this
   note internal.
3. For detection, read Humanizer for its pattern catalog, return the named
   findings with quoted lines and short fixes, then stop.
4. For editing, run Humanizer in embedded mode.
5. Compare that pass with the source and restore any lost fact, distinction, or
   voice signal.
6. Make the minimum effective house-style edit.
7. Read [eval.md](references/eval.md) and check the edited draft directly
   against every item.
8. Fix every failed check and repeat the evaluation.
9. Return the full edited draft and a short **What changed** section.

This framework is adapted from Peter Yang's `no-ai-slop` skill under the MIT
License. See `LICENSE`.
