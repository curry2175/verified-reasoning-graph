# v021 — Corrected Fault Injection + Individual Test Lab

## Fault Injection evaluation corrections

1. **Strict empty-parent policy**
   - A model-authored reasoning step with `depends_on=[]` is no longer silently rerouted through inferred support.
   - If the claim is globally true but no direct parent is declared, it is recorded as:
     - `proof_status = valid`
     - `chain_status = insufficient_declared_support`

2. **Mutation validity gate and resampling**
   - Predicate/parent replacements that do not actually break the injected root are rejected and resampled.
   - Skipped candidates are written to `skipped_mutations.csv`.

3. **No local/upstream duplicates**
   - One-step chains are labeled `single_step` and generated once.
   - `answer_flip` is labeled `final_only` and generated once per case.
   - Exact mutation signatures are deduplicated.

4. **Structural rejection separated**
   - `step_deletion` is reported through the `structural_schema` channel.
   - Logical/semantic and structural/schema rejection rates are shown separately.

5. **Root and propagation metrics separated**
   - Root exact localization and root-set precision/recall.
   - Affected-node precision/recall/F1 using the downstream dependency closure.

## Individual Input Test Lab

New page: `http://127.0.0.1:8765/test-lab`

- Paste one context fact/rule per line.
- Enter a single question.
- Gold answer is optional.
- Run GPT generation, verification, optional Blind/Guided repair, and graph rendering in one click.
- Shows the original structured model output separately from the verified graph.
- Automatically saves every test under `outputs/test_lab/<run_id>/` and supports reopening prior tests.

## Case Browser

Page: `http://127.0.0.1:8765/case-browser`

- Browse all stored batch cases.
- Filter Initial FAIL, Final FAIL, repaired cases, and wrong answers.
- Open Initial, each stored Repair, or Selected Final graph.
- Inspect graph layers, node/edge metadata, and re-verification provenance.

## Validation

- Python automated tests: 76
- New coverage includes strict empty-parent behavior, mutation deduplication, corrected metric outputs, Test Lab persistence, and UI route availability.
