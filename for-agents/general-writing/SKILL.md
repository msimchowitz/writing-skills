---
name: general-writing
description: Edit drafts into clearer, sharper, more human prose while preserving the writer's meaning and personal voice, or audit prose for specific AI-slop patterns without rewriting it. Use for general writing, line editing, clarity and voice revisions, concision, directness, AI-sounding prose, or requests to detect whether writing reads like AI.
---

# General Writing

Act as a sharp human editor. Preserve the user's point and personal voice while
making the writing clearer and more alive. Remove AI patterns without turning
distinctive writing into generic polished prose.

## Choose the response

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

For editing requests, read the sibling
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

For detection requests, use Humanizer's pattern catalog as additional evidence but
do not run its rewrite loop. Report findings under the names used by either
skill and follow this skill's detection output.

## Cover every README

When a writing skill creates or edits README prose, route every README in that
task's scope through this Humanizer-first pipeline. Run Humanizer in embedded
mode on each complete README, then apply this skill's house style and
evaluation checklist to each file. Do not use one README as a sample or skip a
secondary README. Preserve code blocks, commands, tables, link targets, and
functional checklists. Do not expand the task to unrelated READMEs.

## Review structural text separately

Do not treat display text as metadata. Review the document title and subtitle,
then every section and subsection heading. Captions, callout titles, table or
figure labels, list labels, and navigation text must pass the same Humanizer
and house-style checks as body prose. Read each element with the material it
frames. A heading should name the actual topic or reader task; a caption should
state what the figure shows or supports. Leave code, data, and link targets
unchanged unless the user asks to edit them.

## Editing principles

- **Preserve the writer's real voice.** Notice the draft's vocabulary, cadence,
  bluntness, humor, uncertainty, digressions, and level of polish. Keep the
  traits that feel personal.
- **Write for a particular reader.** Make structure, detail, and emphasis serve
  the understanding, verification, decision, or action that reader needs. Name
  the effect instead of adding a generic "for the reader."
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
- **Make each sentence useful to the reader.** Keep a needed claim, condition,
  example, transition, or moment of voice. Cut empty qualifiers and
  throat-clearing.
- **Untangle sentences without flattening cadence.** Preserve clear spoken
  sentences, fragments, and changes in pace when they carry voice.
- **Be concrete and specific.** Names, numbers, dates, mechanisms, and examples
  beat abstractions when the draft supports them.
- **Protect the specific fact.** Do not smooth a useful detail into generic
  importance.
- **Use direct verbs.** Replace weak verb phrases with precise actions.
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
underlying Y" when they postpone the actual relation. Name X's action, Y's
cause, or the open question. Keep the wrapper only when the
relationship itself is under study and a direct verb would overstate the
evidence.

**Question-word and fused-relative clause wrappers.** Avoid non-question
headings, subjects, and sentence-internal object clauses introduced by "what,"
"how," "why," "when," "where," "which," "who," or "whether" when a direct
noun phrase or declarative statement preserves the meaning. For example,
replace "Each contribution should state what the study learned" with "Each
contribution should state the outcome of the study." Keep a genuine question
or unresolved relation when a direct replacement would change the claim.

**Mechanical relative clauses.** A local repair can be grammatical and still
make the full sentence stiff or indirect. Replace "Include only the setup that
is required by the result" with "Include only the setup needed to interpret
the result." The first version forces a passive relation and treats the result
as if it requires setup. The revision states the setup's purpose. "Give readers
only the setup they need to interpret the result" also works when the reader
should be explicit. Read the whole sentence instead of preserving active or
passive voice merely to keep one noun in a preferred grammatical position.
Keep a relative clause when it identifies an important actor, assigns
responsibility, or preserves a distinction that a shorter construction would
lose.

**Readerless corporate shorthand.** Replace workplace metaphors that make
advice sound firm while hiding its purpose. For example, replace "Give each
section one job" with "Each section should help the reader answer one
question." Likewise, replace "Every sentence must earn its place" with "Each
sentence should give the reader information needed to follow or verify the
argument." Do not mechanically mention the reader in every sentence. State
the actual question, inference, evidence, decision, or action supported by the
passage. Keep corporate terms when the subject is an actual organization and
technical ownership when it identifies a real authority.

**Loose catalogs and list-packed sentences.** Require every series to have a
governing relation that the reader can name. Flag loosely related objects even
when each noun is concrete, the grammar is parallel, and the list has only
three items. Keep the series only when its items form a meaningful set and the
whole set matters in this passage. Otherwise choose the decisive item, group
items under an explicit relation, or state their different roles in separate
clauses or sentences. Do not disguise an arbitrary catalog by trimming it to
three items or moving it between bullets and commas. Scan neighboring
sentences too. If several use the same "X includes A and B" frame, recast some
around actions or relationships so list syntax does not become the paragraph's
only rhythm. Treat an ordinary prose paragraph with more than one sentence
built around a series of three or more items as unfinished. Keep that pattern
only when each series is a complete reference set that readers must scan or
count. Never leave two list-shaped sentences adjacent, even across a paragraph
break; a new paragraph does not create variation by itself. Otherwise let a
non-list sentence carry the main point and redistribute the details into
examples or separate claims. Add sentences when needed to preserve every
source detail without preserving catalog rhythm. Preserve complete taxonomies
and checklists. A procedure should also remain intact, as should explicitly
stated assumptions or experimental axes.

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

**List sprawl.** Do not introduce a vertical list longer than five items during
an edit. Group related details before listing them, and use prose when the
items form an argument rather than a reference set. Preserve a complete
procedure or checklist when readers need every step. Keep taxonomies and
option sets intact for scanning.

**Em dashes.** Do not use them as a default rhythm device. Use none in short
copy and at most one or two in longer drafts when they clearly beat punctuation
alternatives.

## Workflow

1. Read the full draft before editing.
2. Identify the core point, intended reader, reader outcome, and several voice
   signals to preserve. Keep this note internal.
3. For detection, read Humanizer for its pattern catalog, return the named
   findings with quoted lines and short fixes, then stop.
4. For editing, run Humanizer in embedded mode. Apply the README coverage rule
   above to every README in scope. Inventory and review the title, section and
   subsection headings, captions, and other reader-visible labels separately.
5. Compare that pass with the source and restore any lost fact, distinction, or
   voice signal.
6. Make the minimum effective house-style edit.
7. Read [eval.md](references/eval.md) and check the edited draft directly
   against every item.
8. Fix every failed check and repeat the evaluation.
9. Return the full edited draft and a short **What changed** section.

This framework is adapted from Peter Yang's `no-ai-slop` skill under the MIT
License. See `LICENSE`.
