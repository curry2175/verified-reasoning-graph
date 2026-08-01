# Hybrid architecture map

| Stage | Default component | LLM call condition | Graph/provenance output |
|---|---|---|---|
| Reasoning generation | OpenAI Responses API structured output | Always for automated run | `generation_source=openai_structured_output`, declared parent IDs |
| Context/query parsing | Deterministic controlled-English parser | Only parser failures | original/formalized text, source, confidence, notes, vocabulary |
| Step parsing | Deterministic parser | Only failed Step | same provenance fields per Node |
| Logical validation | Z3 when available; Horn fallback | Never delegated to LLM | Proof status, SMT query, selected proof dependencies |
| Authored-chain validation | Horn support + declared-parent sufficiency | Never delegated to LLM | authored/inferred dependencies, chain status |
| Premise grounding | Existing graph first | Only diagnosed failed Nodes | advisory parent suggestions and optional premise candidates |
| Self-reflection | No call on PASS | Only failed attempt, up to configured maximum | repair packet, repaired output, attempt Graph |
| Diff | Deterministic graph comparison | Never | changed Node/Edge, repair status |

## Trust boundaries

- Context premises are trusted only because the task supplies them.
- Prior reasoning Nodes enter trusted Proof knowledge only after validation.
- LLM formalization is a candidate representation and remains traceable to the original text.
- LLM inferred premises are advisory by default and are not automatically asserted.
- Z3 proves consequences of the formalized premises; it does not prove that the natural-language premises are true in the real world.

## v018 Operational execution layer

The core Universal Graph schema remains backward-compatible with v016. v018 adds a dataset execution layer around each independent hybrid run:

```text
Dataset JSON/JSONL
  → immutable dataset fingerprint
  → Pilot selection or full selection
  → per-record Hybrid VeriCoT–VRG run
  → atomic case file write
  → append-only checkpoint index
  → summary regeneration
  → resume remaining indexes
```

A full resume never repeats completed indexes. Failed indexes can be retried according to `retry_failed`.
