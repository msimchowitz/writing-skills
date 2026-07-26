# Semantic compatibility examples

Use these examples to recognize recurring mismatches. Recover the intended
relation from context before borrowing a repair.

## Claims, theorems, and scope

| Loose or mismatched wording | Missing relation | More exact wording |
| --- | --- | --- |
| "the point where the claim stops" | A claim has conditions, extent, and consequences; it does not travel and stop. | "the conditions that limit the extent of the claim" |
| "where does the theorem stop?" | The question may concern applicability or consequences. | "Where does the theorem cease to apply?" or "Where do the consequences of the theorem end?" |
| "the assumptions limit the claim" | The affected dimension is unnamed. | "the assumptions limit the extent of the claim" or "the claim holds only under these assumptions" |
| "the theorem reaches nonlinear systems" | Applicability, not physical reach, is at issue. | "the theorem also applies to nonlinear systems" |
| "the guarantee travels to deployment" | The inference from analysis to deployment is missing. | "the guarantee continues to hold under the deployment conditions" |
| "the limitation weakens the result" | A limitation usually narrows interpretation or applicability. | "the limitation narrows the conditions under which the result applies" |

## Evidence and inference

| Loose or mismatched wording | Missing relation | More exact wording |
| --- | --- | --- |
| "the evidence explains the effect" | Evidence can support an explanation; an analysis or mechanism explains. | "the evidence supports our explanation of the effect" |
| "the results argue that stability matters" | Authors argue; results supply support. | "the results support the conclusion that stability matters" |
| "the experiment asks whether noise helps" | An experimental design tests a question. | "the experiment tests whether noise helps" |
| "the data decide between the hypotheses" | A test or inference uses data to discriminate. | "the likelihood-ratio test distinguishes between the hypotheses" |
| "the figure proves the mechanism" | A figure displays evidence and rarely proves a mechanism by itself. | "the measurements in Figure 3 support the proposed mechanism" |
| "the citation says that the method fails" | The cited source, not the citation marker, contains the statement. | "Smith et al. report that the method fails" |
| "the implication statement asks how far the consequences extend" | An analyst asks; a statement specifies or describes. | "the implication statement specifies the regime in which the consequence holds" |
| "retrieval provides an intervention on the hypothesis" | Retrieval changes the generation process; the resulting comparison tests the hypothesis. | "varying retrieval provides a way to test the hypothesis" |

## Documents and their readers

| Loose or mismatched wording | Missing relation | More exact wording |
| --- | --- | --- |
| "the section knows the answer" | Authors or an analysis establish an answer; a section states it. | "the section states the answer established by the analysis" |
| "the section decides the notation" | The authors make the decision; the section records it. | "we define the notation in this section" |
| "the result requires setup" | Readers need context in order to interpret the result. | "readers need this setup to interpret the result" |
| "the paragraph owns the point" | The prose develops a claim or supports an inference. | "the paragraph develops the paper's central claim" |
| "the sentence earns its place" | The sentence supplies information for a reader or argument. | "the sentence supplies evidence needed for the next inference" |
| "the prose does the work" | Name the actual rhetorical or logical function. | "the passage connects the assumption to the guarantee" |
| "the abstract walks readers through the paper" | An abstract explains an argument; the reader is not taking a tour. | "the abstract explains the problem, result, and conditions under which it holds" |
| "the qualifications fix the claim's extent" | Qualifications state, narrow, or delimit scope; they do not repair it. | "the qualifications specify the extent of the claim" |
| "the comparison recovers a lost detail" | Comparing drafts reveals the loss; an editor restores the detail. | "comparison with the source reveals a lost detail" |
| "the categories support later references" | Categories supply labels; writers and readers use those labels to refer back to the groups. | "the categories give the writer stable labels for later reference" |
| "an underspecified reader leaves priorities unclear" | The prompt's account of the reader is incomplete, not the person. | "missing reader context leaves priorities unclear" |
| "the defaults settle into a middle register" | Prose adopts a register; defaults may make that register more likely. | "the prose settles into a portable middle register" |
| "surface patterns identify their own causes" | Patterns can provide evidence about a cause; they do not perform the inference. | "surface patterns alone do not reveal their causes" |

## Models, methods, and data

| Loose or mismatched wording | Missing relation | More exact wording |
| --- | --- | --- |
| "the model understands the scene" | Name the demonstrated capability. | "the model identifies the objects and predicts their relative positions" |
| "the policy wants high reward" | The optimization objective favors actions; the policy has no desire. | "the policy is optimized to maximize reward" |
| "the loss encourages smooth actions" | Minimization of a term changes the learned solution. | "the smoothness term penalizes abrupt changes in action" |
| "the data want a larger model" | A diagnostic or comparison supports the choice. | "validation error continues to decrease as model size increases" |
| "the benchmark captures robustness" | A benchmark measures specified behavior under stated perturbations. | "the benchmark measures performance under lighting and viewpoint shifts" |
| "the method treats uncertainty like noise" | "Treats" can hide the implemented operation. | "the method models uncertainty as additive noise" |

## Accepted shorthand

Do not replace a familiar usage merely because it is not physically literal.
These combinations normally carry stable meanings in technical prose:

- a claim **holds**, **fails**, **applies**, or **depends on** an assumption;
- a theorem **states**, **establishes**, **guarantees**, or **implies** a result;
- evidence **supports**, **contradicts**, or **is consistent with** a claim;
- a paper **argues**, **shows**, or **reports** when the document clearly stands
  for its authors and contents;
- a figure **shows** values or a visible trend;
- an equation **implies** a consequence;
- an algorithm **selects** or **returns** an output; and
- a model **receives**, **processes**, **predicts**, or **estimates** quantities.

"The model sees an image" and similar field-specific shorthand may also be
natural. Replace it with "receives" or "processes" only when the input path or
capability distinction matters.
