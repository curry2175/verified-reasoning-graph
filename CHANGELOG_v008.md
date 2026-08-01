# v008 Changelog

## Graph-local incremental revalidation

- Previous reasoning/proof graph descendants used as affected-set seeds.
- Predicate-flow reachability through premise and semantic bridge rules.
- Unaffected later reasoning nodes can be reused, not only a prefix.
- Final can be reused when the edited branch cannot affect the queried claim.
- Full parity validation and automatic full-result fallback retained.

## Z3 within-claim session reuse

- Knowledge is asserted once per revalidated claim.
- `K ∧ F` and `K ∧ ¬F` use `push()` / `pop()` on shared base solvers.
- Solver instance/check/assertion/minimization counters exposed in JSON.

## Edit diff

- Text, status, dependency and root-error changes.
- Final Proof/Chain before and after.

## Benchmark

- New `/benchmark` page and `/api/incremental-benchmark` endpoint.
- Four built-in edit scenarios.
- Repeated parity, runtime, speedup and scope-reduction metrics.

## New sample

- `sample_branched_graph_local.json`

## Validation

- 25 automated tests.
- Browser JavaScript syntax checks.
- FastAPI benchmark endpoint tested.
