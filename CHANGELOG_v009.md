# v009 Changelog

## Persistent per-case Z3 session

- Added one tracked solver and one clean display solver per verification request.
- Trusted knowledge is asserted once with assumption guards.
- `K ∧ F` and `K ∧ ¬F` use target assumption labels.
- Unsat-core minimization reuses the same tracked solver.
- Added full-verification solver statistics.

## Input preflight

- Added `/preflight` UI and `/api/preflight`.
- Reports Parser coverage, question validity, strict Yes/No errors, duplicate IDs, semantic normalization and advisory relations.
- Added `sample_preflight_untranslatable`.

## Mutation robustness test

- Added `/mutation` UI and `/api/mutation-test`.
- Automatically injects polarity flips and novel predicates into valid reasoning atoms.
- Checks expected status and incremental/full parity.

## Audit package

- Added Graph button and `/api/audit-package`.
- Exports input/result JSON, node/edge CSV, Markdown/HTML report, node-level SMT2 queries and SHA-256 manifest.

## Validation

- 30 Python tests pass in Horn fallback environment.
- Graph, Batch, Benchmark, Preflight and Mutation JavaScript syntax checks pass.
- API smoke tests pass for all pages and new endpoints.
