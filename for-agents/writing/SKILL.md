---
name: writing
description: Route writing and editing work to the smallest relevant focused skill. Use when a request involves improving prompts, general prose, AI-pattern removal, human-readable writing guides, presentations, reviewer rebuttals, research papers, grant strategy, or grant proposals and no narrower writing skill has already been selected.
---

# Writing Router

Select the primary deliverable, load only the matching sibling skill, and follow
that skill before acting. Keep unrelated writing guidance out of context.

## Route the request

1. Identify the artifact the user is producing or revising.
2. Infer the primary writing job from the artifact and requested outcome.
3. Read the selected `SKILL.md` completely.
4. Do not read the other sibling skills unless the request has a second,
   materially distinct deliverable.

| Primary job | Load |
| --- | --- |
| Clarify and rewrite a prompt while preserving the user's natural prompting style | `../prompt-improving/SKILL.md` |
| Run the standalone Wikipedia-derived AI-pattern removal pass or explicitly invoke Humanizer | `../humanizer/SKILL.md` |
| Edit prose for clarity, voice, directness, or AI-sounding patterns; audit prose without rewriting | `../general-writing/SKILL.md` |
| Create, revise, compile, or review a human-readable writing guide or its PDF | `../improve-human-writing-guide/SKILL.md` |
| Plan, create, revise, or review slides, speaker notes, PowerPoint, Keynote, or Beamer decks | `../presentation-making/SKILL.md` |
| Answer reviewer comments or write a response letter, author response, or point-by-point rebuttal | `../rebuttal-writing/SKILL.md` |
| Plan, draft, or revise a research paper, abstract, introduction, related work, methods, results, or conclusion | `../paper-writing/SKILL.md` |
| Ideate, compare, reframe, or select grant stories, concept notes, scientific questions, team strategy, feasibility, or scope before application drafting | `../grant-planning/SKILL.md` |
| Draft or revise grant or fellowship application prose, including aims, significance, approach, impact, broader impacts, and sponsor responses | `../grant-writing/SKILL.md` |

## Control context

- Load one primary skill by default.
- Never treat `../../for-humans/human-writing-guide/` as a skill. The
  `paper-writing` skill may point to it or consult the relevant chapter for an
  explicit template-use, teaching, or human-instruction request. Inspect or
  edit the guide itself only when the user asks to work on that human-readable
  artifact.
- Do not load `general-writing` automatically for every domain task. Add it only
  when the user explicitly requests voice editing or AI-slop removal, or when
  the selected domain skill directs a final prose pass.
- When a selected skill invokes `general-writing`, let `general-writing` own
  the Humanizer dependency and pass order. Do not load or run Humanizer a
  second time.
- If the user explicitly invokes a subskill, bypass this router and use that
  subskill directly.
- If the artifact spans categories, choose the skill governing the requested
  output. For example, route a presentation about a paper to
  `presentation-making`, not `paper-writing`.
- If two outputs are requested, complete them in stages and load each skill only
  for its stage.
- Preserve repository instructions, templates, factual claims, notation,
  citations, and format constraints. A routed skill supplements those
  requirements; it does not override them.

## Handle ambiguity

Infer the route when the artifact makes it clear. Ask one concise question only
when choosing the wrong skill would materially change the work.
