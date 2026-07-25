# Theory-Led Paper Outline

## Abstract

1. Name the problem and setting.
2. State the failure or impossibility that makes the problem nontrivial.
3. Name the interventions or new lens.
4. State the guarantees and their regimes.
5. State the empirical or conceptual validation.
6. State the implication and boundary.

## 1. Introduction

**Job:** make the theorem necessary before making it technical.

- Establish the practice or phenomenon.
- Explain the unresolved failure mode.
- State the sharp question.
- Introduce the minimal interventions in ordinary language.
- Give contribution blocks with theorem pointers.
- State surprising consequences and scope.

**Exit condition:** the reader knows what fails, what changes, and what each
main theorem establishes.

## 2. Preliminaries

**Job:** define only objects used immediately by the first result.

- Problem setting and interaction protocol
- Evaluation metric
- Baseline error or failure notion
- Stability, smoothness, or coverage assumptions

Motivate every nonstandard definition with one sentence of operational meaning.
Move generic background and proof machinery to the appendix.

## 3. First Regime: [Claim-Led Title]

**Job:** establish the simpler intervention under the more favorable regime.

- Intervention definition or algorithm
- Informal theorem
- Mechanism figure
- Formal result
- Interpretation and tightness
- Representative validation

## 4. Second Regime: [Claim-Led Title]

**Job:** address the harder regime and explain why the first intervention no
longer suffices.

- Counterexample or boundary of Section 3
- Stronger intervention
- Informal theorem
- Formal result
- Mechanism or proof roadmap
- Consequences and limitation

## 5. Experimental Validation

**Job:** test predictions specific to the theory.

- Question for each experiment
- Regime diagnostic
- Controlled intervention
- Prediction and observed result
- Failure case or boundary

Do not use generic benchmark breadth as a substitute for testing the theorem's
mechanism.

## 6. Related Work

Organize by the distinctions used in the paper:

- approaches requiring stronger interaction or oracles;
- approaches with different stability or coverage assumptions; and
- analyses that yield weaker or incomparable guarantees.

State exact differences without claiming that prior work "does not address" a
topic unless the literature boundary is verified.

## 7. Discussion And Limitations

- Restate the supported conceptual lesson.
- Name assumptions that may fail in practice.
- Separate technical looseness from practical limitation.
- Name the next question opened by the result.

## Appendix

Recommended order:

1. Extended discussion and related work
2. Domain primer
3. Proof preliminaries
4. Proofs in main-text order
5. Additional regimes or lower bounds
6. Experimental details and full results
