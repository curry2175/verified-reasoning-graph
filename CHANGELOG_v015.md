# v015 — OpenAI API Automated ProofWriter Reasoning Graph

v015 continues the main premise-based branch from v014 and removes the manual AI-output copy/paste requirement.

## Added

- OpenAI Responses API integration using the official Python SDK.
- Structured Outputs schema for:
  - atomic reasoning steps,
  - model-declared direct parent IDs,
  - final True / False / Unknown,
  - final answer dependencies.
- One-click `GPT 생성 + 자동 분석` workflow:
  - ProofWriter JSON → GPT generation → VRG Z3/Horn verification → Knowledge Graph/Fingerprint.
- Gold-label leakage prevention: the dataset answer and options are never sent to GPT.
- Server-side API-key loading from `.env`; the key is never returned to browser JavaScript.
- Model, reasoning effort, repetition count, output-token cap, and optional prompt instruction controls.
- Run-level model, latency, token usage, response ID, exact prompt, structured output, and warnings.
- Up to five independent generation runs with an in-page run selector.
- Outputs:
  - `proofwriter_gpt_run.json`
  - `proofwriter_gpt_output.json`
  - the existing analysis, adapted-case, and verified-graph JSON files.
- `SET_OPENAI_KEY_WINDOWS.bat` and `.env.example`.

## Safety and interpretation

- Generated steps are an inspectable answer explanation, not access to the model's private hidden reasoning.
- GPT-declared parent IDs are treated as claims and are rechecked by the existing local-support sufficiency logic.
- Unknown/invalid parent references are recorded as diagnostics and omitted from executable dependencies.
- Open-world semantics remain deterministic in the verifier: True if query is derivable, False if its explicit opposite is derivable, Unknown if neither is derivable.
