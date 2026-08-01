# v019 — ProofWriter canonical verification and Case Browser

## Critical verifier correction

v018 parsed all ProofWriter context and query text back into logic from natural language. This caused relation errors such as `chases → chas`, compound entities such as `bald eagle` being split, and occasional loss of negative polarity.

v019 adds a ProofWriter-specific canonicalization layer:

- uses `raw_logic_programs` to recover predicate and entity vocabulary;
- parses the exact natural-language context shown to the model;
- cross-validates each natural premise against its raw logic entry;
- uses raw logic only when the two agree;
- marks `context_over_raw_mismatch` when the natural context and raw formula conflict;
- marks `context_parser_raw_missing` when the natural premise is absent from raw logic;
- preserves original text while verifying canonical underscore entities;
- fixes relation lemmatization such as `chases → chase` and `sees → see`;
- preserves compound entities such as `bald_eagle` through the final query verifier.

The 600 supplied records were checked: the corrected context-derived label agrees with the dataset label in 600/600 cases.

## Offline re-verification

`REVERIFY_V018_RUN_WINDOWS.bat` and `reverify_existing_run.py` reuse all stored GPT outputs. They make **zero new OpenAI API calls**.

Selection policy:

1. if the initial stored output passes the corrected verifier, ignore repairs triggered only by the old parser;
2. otherwise select the first stored repair that passes the corrected verifier;
3. if no stored attempt passes, retain the last attempt for inspection.

The original v018 run is never overwritten. A new `<run_id>_v019_reverified` run is created.

## Case Browser

Open:

```text
http://127.0.0.1:8765/case-browser
```

Features:

- select saved runs;
- filter Initial FAIL, Final FAIL, Repair-used, and wrong-answer cases;
- search by Case ID;
- switch between Initial, stored Repair, and selected Final Graph;
- use all previous Universal Graph views and edge layers;
- import a v018 Run ZIP and reverify it directly;
- display canonicalization provenance and raw/natural mismatch information.

## Compatibility

- Existing v018 batch runs remain readable.
- New runs use schema version `0.19.0`.
- The OpenAI API key is required only for new generation or new repair calls, not for offline re-verification or Case Browser viewing.
