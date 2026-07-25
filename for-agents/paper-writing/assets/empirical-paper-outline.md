# Empirical Paper Outline

Use the **method track** for a new algorithm and the **mechanism track** for a
paper whose main contribution explains an existing phenomenon.

## Abstract

1. Name the concrete practice or deployment problem.
2. State the bottleneck, misconception, or tradeoff.
3. Introduce the method, taxonomy, or controlled study.
4. State the strongest quantitative or qualitative finding.
5. State the mechanism, breadth, or deployment result.
6. State the design implication and scope.

## 1. Introduction

- Task and operational stakes
- Current practice
- Exact limitation or unexplained success
- Central question
- Core insight
- Claim-led contributions with section pointers
- One conceptual takeaway

For a mechanism paper, list the competing hypotheses explicitly. For a method
paper, name the tradeoff the method resolves.

## 2. Related Work Or Preliminaries

Choose order based on reader need:

- Put **related work first** when the method is unintelligible without locating
  it among close technical alternatives.
- Put **preliminaries first** when the paper introduces a useful abstraction or
  taxonomy.
- Move extended related work later when an early survey interrupts the
  argument.

## 3. Method Track: Formulation And Approach

- Formal problem and cost model
- Why the obvious approach fails
- Core method in one diagram and one objective
- Design decisions tied to failure modes
- Abbreviated algorithm
- Practical or stabilized variant

**Exit condition:** a domain expert can explain the method and why each major
component exists.

## 3. Mechanism Track: Hypotheses And Controls

- Decompose the system into candidate components.
- State each explanation as a testable hypothesis.
- Specify the control needed to isolate it.
- Report negative evidence without burying it.
- Introduce the minimal construction that retains only the supported
  components.

**Exit condition:** the reader can distinguish correlation, eliminated
explanations, and the proposed mechanism.

## 4. Experimental Setup

- Questions
- Tasks and why each regime is diagnostic
- Common initialization and held-fixed choices
- Baselines and tuning budget
- Metrics, seeds, uncertainty, and compute

Do not make the setup a catalog. Tie every benchmark to a scientific question.

## 5. Headline Results

- Broad comparison across representative regimes
- Hard cases that expose the claimed advantage
- Sample or compute efficiency where relevant
- Qualitative deployment or stress test
- Unfavorable result or boundary

State the comparator and regime before interpretation.

## 6. Understanding And Ablations

- Mechanism visualization
- Alternative explanation control
- Component ablation
- Sensitivity or tuning robustness
- Failure mode and stabilization
- Scope sentence for each inference

An ablation establishes that a component matters in the tested system; it does
not automatically establish the proposed causal mechanism.

## 7. Discussion Or Conclusion

- Supported central finding
- Practical consequence
- Main limitation
- Next technical question

Avoid repeating the abstract or adding a new application claim.

## Appendix

Recommended order:

1. Practitioner guide or best practices
2. Pseudocode and implementation
3. Full baseline definitions
4. Additional results and ablations
5. Environment, data, and evaluation details
6. Hyperparameters, compute, and wall-clock reporting
7. Qualitative examples and failures
8. Extended related work
