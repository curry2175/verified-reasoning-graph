# v007 Changelog

## Added

- `POST /api/incremental-verify`
- Conservative suffix partial revalidation
- Reuse of unchanged reasoning prefix
- Final-only revalidation for Yes/No answer edits
- Full fallback for premise, semantic-relation, and question edits
- Optional parity validation against a full verification
- Per-node `verification_origin`
- Incremental runtime and reuse metrics
- `sample_long_chain_incremental`

## Safety policy

- A parity mismatch automatically returns the full verification result.
- Counterfactual deletion metrics are not recomputed in the fast incremental path.
- The affected set is deliberately conservative: changed step through Final.

## Not yet implemented

- Persistent Z3 solver with `push()/pop()`
- Exact graph-local descendant/symbol affected set
- Cross-edit solver cache persisted across requests
