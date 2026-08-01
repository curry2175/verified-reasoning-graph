# v023 — Global Vocabulary Alignment and Connectivity Preflight

v023 fixes cross-sentence predicate drift in general-science and Discussion inputs.

## Problem addressed

A context such as:

```text
Study_S is observational.
All observational studies are causality_limited.
All causality_limited studies are not causation_establishing.
```

could previously be formalized with incompatible symbols such as
`observational`, `observational_study`, `causality_limited`, and
`causality_limited_study`. The natural-language answer could be correct while
formal verification incorrectly returned `Unknown`.

## New pipeline

```text
Scientific normalization
→ transparent lexical type premises
→ global symbol table
→ vocabulary-conditioned LLM fallback
→ modifier/head decomposition
→ alias alignment
→ orphan-antecedent diagnostics
→ query-connectivity preflight
→ GPT reasoning generation
→ VRG verification and repair
```

## Main changes

- Rewrites modifier+head universals compositionally:
  - `All observational studies are limited`
  - becomes `study(x) ∧ observational(x) → limited(x)`.
- Recognizes both `Study S` and `Study_S` as labelled entities and derives the
  transparent lexical premise `study(study_s)`.
- Supplies the global predicate vocabulary to the fallback formalizer.
- Aligns fallback-created near-duplicates such as `observational_study` to
  existing predicates instead of silently accepting a disconnected ontology.
- Reports the global symbol table, alignment decisions, orphan antecedents, and
  query-predicate connectivity in the Test Lab preview.
- Does not treat a disconnected query as automatically invalid: it may correctly
  imply `Unknown`. It blocks only detected symbol-drift patterns.

## Validation

- 82 Python tests passed.
- 17 inline JavaScript programs passed syntax checking.
- Test Lab, Case Browser, Experiment, Batch, and preview API routes passed smoke tests.
- The observational-study example now preflights without an LLM formalizer call
  and verifies to `False` with a valid reasoning graph.
