# v018 — ProofWriter dataset auto-download

## Added

- One-click download of `renma/ProofWriter`, `default`, `validation` (600 rows).
- No Git, Git LFS, `datasets`, pandas, or pyarrow dependency.
- Pagination through Hugging Face Dataset Viewer `/rows` API in chunks of at most 100 rows.
- Required-field, answer-label, duplicate-ID, and incomplete-download validation.
- Cached local JSONL and provenance metadata under `data/downloaded/`.
- One-click **download + Pilot 10** flow in `/hybrid-batch`.
- Pilot-to-full resume remains checkpoint-compatible; the full phase starts at the first unfinished record.
- CLI source option: `--dataset-source renma-proofwriter-600`.
- `DOWNLOAD_AND_RUN_PROOFWRITER_WINDOWS.bat` convenience launcher.
- Download status/file API endpoints.

## Scope clarification

The automatic source is the 600-row validation subset matching the project's current A/B/C ProofWriter adapter. It is not the much larger 845,496-row expanded `tasksource/proofwriter` corpus.
