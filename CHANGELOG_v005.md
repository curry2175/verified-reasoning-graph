# v005 changes

## Safe Semantic Layer

v005 introduces three explicitly different predicate relations:

- `same_as`: approved canonicalization before SMT/Horn verification.
- `implies`: approved directional bridge rule added to Z3 and Horn knowledge.
- `related_to`: advisory relationship only. It is shown in the graph but never used to prove a claim.

## Transparency

Each node now records:

- formal representation before semantic preprocessing,
- formal representation after preprocessing,
- applied `same_as` relations,
- semantic relations needed before SMT verification,
- advisory related-only hints,
- whether a semantic relation is proof-usable.

## Graph

Semantic relations appear as `m1`, `m2`, ... nodes. New edge types:

- `semantic_normalization`
- `semantic_bridge`
- `semantic_related`

## New samples

- `sample_semantic_same_as`
- `sample_semantic_implies`
- `sample_semantic_related`

## Tests

15 fallback tests pass in the build environment. Z3-specific execution should be confirmed on a machine with `z3-solver` installed.
