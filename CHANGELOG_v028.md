# v028 Changelog

## 목적

동일 모델과 동일 사례에서 Graph 기반 파이프라인을 Direct GPT 및 free-form self-critique와 직접 비교할 수 있도록 평가 구조를 변경했습니다.

## Paired answer comparison

- Direct GPT
- Self-critique of the same direct answer
- Public reasoning Graph + verifier
- Graph + verifier-guided repair
- 가능한 범위의 Yes/No stratified sampling
- Correction rate
- Harmful regression rate
- Net correction
- Accuracy delta
- Paired bootstrap 95% CI
- McNemar exact test
- 조건별 token/API 사용량

ProofWriter의 Graph와 Graph+repair는 같은 최초 Graph generation을 공유합니다.

## Reasoning-error audit

- Clean ProofWriter reasoning과 oracle-confirmed fault mutation의 matched controls
- Plain GPT critic
- Checklist GPT critic
- Formal Z3 Graph verifier
- Detection precision/recall/F1
- Clean false-positive rate
- Exact root-error localization
- Node localization F1
- Fault-type breakdown

## Discussion audit

- 13개 flawed paragraph + 13개 matched clean paragraph
- Plain free-form critic
- Structured non-graph critic
- Discussion Typed Graph pipeline
- Error detection F1
- Issue-type micro-F1
- Clean false-positive rate
- Source localization
- Exact source-span fidelity
- Human-review blinded packet/answer key export

## 새 파일

- `vrg/comparative_evaluation.py`
- `run_comparative_evaluation.py`
- `RUN_COMPARATIVE_PILOT_WINDOWS.bat`
- `RUN_ANSWER_COMPARISON_WINDOWS.bat`
- `RUN_REASONING_AUDIT_COMPARISON_WINDOWS.bat`
- `RUN_DISCUSSION_AUDIT_COMPARISON_WINDOWS.bat`
- `static/comparative_evaluation.html`
- `data/discussion_audit_benchmark_v028.jsonl`
- `V028_START_GUIDE.md`

## 해석 제한

내장 Discussion benchmark는 개발 과정에서 만든 synthetic matched set입니다. 최종 연구 결론에는 독립된 human-authored external test set과 blinded human annotation이 필요합니다.
