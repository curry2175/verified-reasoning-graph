# Comparative Evaluation Design · v028

## Primary research question

Does an explicit reasoning graph with structural/formal verification provide benefits beyond asking the same LLM to answer directly or to self-critique in free text?

## Conditions

### Answer task

1. `direct`: direct Yes/No answer with one brief reason
2. `self_critique`: re-check and revise the same direct answer without a graph
3. `graph`: independently generate a public reasoning graph and verify it
4. `graph_repair`: repair the same graph generation using verifier feedback

The model, input cases, and reasoning effort are matched. Graph and Graph+repair share the same initial graph generation for ProofWriter.

## Primary answer endpoints

- Accuracy and macro-F1
- Corrected initial errors
- Harmful regressions of initially correct answers
- Net correction = corrected errors − harmful regressions
- Paired accuracy delta
- McNemar exact test
- Paired bootstrap 95% confidence interval

The primary comparison should be `graph_repair` versus `direct`. Accuracy alone is not sufficient.

## Reasoning-error audit

Matched clean and oracle-confirmed faulty ProofWriter graphs are evaluated by:

1. Plain GPT critic
2. Checklist GPT critic
3. Formal Graph verifier

Primary endpoints:

- Error detection precision/recall/F1
- Clean false-positive rate
- Exact earliest root-error localization
- Node-level localization F1

This experiment tests the strongest intended contribution: detecting and locating defects that answer accuracy alone may miss.

## Discussion audit

The development benchmark contains 13 flawed paragraphs and 13 paired clean revisions. Methods:

1. Plain GPT critique
2. Structured non-graph critique
3. Discussion Typed Graph pipeline

Endpoints:

- Error-detection precision/recall/F1
- Clean false-positive rate
- Issue-type micro-F1
- Source-localization hit rate
- Exact source-span fidelity
- Duplicate issue count

The included benchmark is a development benchmark, not an external validation set. A publishable final study should use a held-out human-authored set annotated independently by at least two reviewers.

## Human usability packet

Each Discussion run exports blinded method outputs for reviewers. Suggested outcomes:

- Reviewer error-detection accuracy
- Review time
- Critical-error miss rate
- Usefulness score
- Reviewer confidence

Condition identity is stored separately in the answer key.

## Claims supported by different outcomes

- Higher answer accuracy/net correction: graph-guided repair improves final decisions.
- Higher error F1 and lower clean FP: graph verification improves audit reliability.
- Higher localization: graph structure identifies where an error begins.
- Lower regression rate: verifier-guided repair is safer than unconstrained self-critique.
- Faster/more accurate human review: graph UI improves practical audit utility.

Graph node count, width, depth, or visual complexity alone must not be used as evidence of superiority.
