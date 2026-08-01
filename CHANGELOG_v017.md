# v017 — ProofWriter Pilot → Full Operational Runner

## 목적

v016의 Hybrid VeriCoT–VRG 검증, Universal Graph layer, autoformalization, premise grounding, graph-guided repair를 유지하면서 실제 ProofWriter 전체 Dataset을 안정적으로 실행할 수 있도록 운영 계층을 추가했습니다.

## 추가 기능

- JSON / JSON array / JSONL / wrapper object 입력
- Pilot 10 실행
- 동일 Run ID에서 나머지 전체 재개
- 완료 Case 자동 skip
- 실패 Case 선택적 retry
- Case별 결과 즉시 저장
- `index.jsonl` append-only checkpoint
- 서버 재시작 후 resume
- API 오류 exponential retry
- 1–4 worker 병렬 실행
- 전체 Token 상한
- 실패 수 상한
- checkpoint pause
- 진행 상태 polling UI
- Summary JSON/CSV 및 Predictions JSONL
- 전체 Run ZIP export
- CLI runner 및 Windows BAT

## 저장 구조

```text
outputs/hybrid_runs/<run_id>/
├─ dataset.jsonl
├─ settings.json
├─ state.json
├─ index.jsonl
├─ summary.json
├─ summary.csv
├─ predictions.jsonl
├─ cases/*.json
└─ errors/*.json
```

## 검증

- 전체 Python tests: 62/62
- Pilot 10 → 동일 Run full resume simulation: pass
- Token-limit checkpoint stop: pass
- Existing v001–v016 regression: pass
- FastAPI route smoke: pass
- 14 HTML inline JavaScript syntax checks: pass
