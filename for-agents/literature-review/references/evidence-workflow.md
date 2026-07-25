# Evidence Workflow

## Source hierarchy

Use primary sources for architecture, data, training, and release claims.
Different primary artifacts answer different questions:

- A versioned paper or appendix is strongest for the method and experimental
  setup it documents.
- An official model card is strongest for the exact checkpoint, license,
  intended use, and release-specific configuration it names.
- A tagged repository or release note is strongest for implementation changes
  tied to that version.
- An official technical blog can establish release chronology and claims, but
  treat promotional comparisons cautiously.
- An independent paper is needed for reproduction, criticism, or a comparison
  the originating team did not run.

Use secondary pages to find sources, not to replace an available primary
artifact.

## Retrieval record

Record a cutoff date before searching. For every included source, save:

- stable identifier and URL;
- title, full authors, year, and version;
- source type and whether it is primary;
- model family, release, or method covered;
- exact evidence location;
- claims supported; and
- any mismatch between versions or artifacts.

Do not cite a search-result snippet. Open the artifact and verify the claim in
context.

## Evidence states

Use these labels consistently:

- `reported`: the source states the fact directly;
- `derived`: the value follows deterministically from reported values, and the
  derivation is recorded;
- `inferred`: the interpretation combines evidence but is not stated by the
  source;
- `conflicting`: included sources disagree or describe different versions; and
- `not-disclosed`: the reviewed primary sources do not provide the detail.

Write inferred claims as interpretations. Do not cite one source as if it
reported a cross-source inference.

## Training-recipe extraction

For each model or method, extract:

| Axis | Evidence to capture |
| --- | --- |
| Identity | family, release, checkpoint, parameter scale, date |
| Inheritance | base model, reused weights, predecessor components |
| Architecture | encoders, adapters, decoder, fusion, tokenization |
| Data | modality, source classes, scale, mixture, filtering, synthesis |
| Stages | order, trainable modules, frozen modules, initialization |
| Objectives | next-token, contrastive, reconstruction, preference, RL |
| Curriculum | resolution, sequence length, temporal sampling, task mix |
| Alignment | instruction data, preference data, reward, safety treatment |
| Optimization | compute, batch, optimizer, schedule, duration |
| Evidence | ablations or controlled comparisons tied to recipe choices |
| Gaps | recipe details absent from the reviewed sources |

Use `not-disclosed` for missing values. Do not fill a cell from a related model
unless the source explicitly transfers that setting.

## Claim-evidence discipline

Give each major synthesis claim an identifier. Map it to source IDs and exact
locations before drafting. A claim is ready only when:

1. the wording matches the evidence state;
2. the citation covers the whole claim;
3. family-level and checkpoint-level scopes agree;
4. dates and versions are unambiguous; and
5. conflicting evidence is represented rather than averaged away.

Put citations next to the supported sentence or table cell. A citation at the
end of a long paragraph should not be asked to support several unrelated
claims.

## Coverage and stopping

Track search coverage by family, release, source type, and comparison axis.
Stop broad retrieval when additional searches mostly duplicate included
primary sources and every in-scope unit has either evidence or an explicit
gap. This is a saturation rule, not proof that no source exists.

For a living review, preserve the ledger and record the next search date.
