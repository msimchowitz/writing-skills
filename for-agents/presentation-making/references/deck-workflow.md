# Content-to-deck workflow

Use this workflow for a new deck or a substantial rewrite.

## 1. Resolve the source

Identify the exact source material and read it completely. Follow referenced
figures, tables, definitions, citations, and appendices when they affect the
talk. Do not reconstruct a technical claim from memory when the source is
available.

Record:

- the audience, venue, time limit, and desired outcome;
- the central question or claim;
- the main learning or decision goals;
- the facts, derivations, examples, caveats, and evidence that must survive;
- the notation, figures, tables, and citations the deck requires;
- any supplied template, example deck, brand system, or format constraint.

## 2. Build the narrative

Write a slide plan before editing the presentation file. For each planned slide,
record:

- the point or audience move;
- the source passage, equation, figure, or evidence it represents;
- the intended layout family;
- whether it is static or part of a progressive build;
- details that belong in speaker notes.

Do not convert source pages or document sections one for one. Combine repeated
setup, split dense reasoning, and give difficult ideas enough visual space.
Preserve the source's logic unless a change makes the live explanation clearer.

A useful default arc is:

1. State the problem, question, or tension.
2. Introduce only the setup the audience needs.
3. Show the limitation, evidence, or stakes.
4. Present the key idea, result, or proposal.
5. Work through the reasoning or evidence.
6. End with the concrete conclusion, decision, or next step.

Use a different arc when the material calls for one.

## 3. Select the visual source

When an approved template or example deck exists, inspect it fully and use it as
the source for layouts, typography, spacing, colors, and recurring visual
devices. Copy and edit a suitable source slide instead of rebuilding its style.

For PowerPoint or Keynote:

- retain editable objects and inherited theme styles;
- use one source deck or theme;
- do not import stock layouts that conflict with the approved visual system.

For Beamer:

- retain the `.tex` source;
- use the project's shared style package;
- do not redefine shared spacing, colors, boxes, or page furniture in one deck.

## 4. Translate the content

- Keep one primary point or teaching move per slide.
- Write titles as conclusions, questions, or transitions when that helps the
  argument. Use concise topic labels for section dividers.
- Explain what an equation, figure, or result establishes, not only what it is.
- Reveal long derivations in steps that match the spoken explanation.
- Reuse source figures when legible. Redraw only when the original cannot work
  on a slide.
- Crop images without stretching them.
- Cite external figures, results, and quotations in a readable footer or in
  speaker notes.
- Move qualifications and proof details to notes when the audience does not
  need to read them at once.
- Never invent data, references, examples, or conclusions to fill a slide.

## 5. Build and verify

Build with tools appropriate to the file format. Keep temporary renders and
working files outside the final artifact directory when practical.

Then render the complete deck and use
[visual-design-review.md](visual-design-review.md). Inspect every slide at full
size, including every physical page created by overlays. Correct defects,
rerender, and inspect again.

## 6. Capture feedback

After review, record the user's exact feedback and whether it applies only to
this deck or to future decks. Convert repeated feedback into concise general
rules without erasing the original concern.

