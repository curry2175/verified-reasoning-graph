# v028 시작 가이드

## 1. 실행

```bat
cd /d "C:\Users\chefc\OneDrive\바탕 화면\YAI Challenge\verified_reasoning_graph_mvp_v028"
copy "..\verified_reasoning_graph_mvp_v027\.env" ".env"
RUN_WINDOWS.bat
```

비교평가 화면:

```text
http://127.0.0.1:8765/comparative-evaluation
```

## 2. 가장 작은 Pilot

```bat
RUN_COMPARATIVE_PILOT_WINDOWS.bat
```

기본값:

- 세 데이터셋 각각 10개
- Direct / Self-critique / Graph / Graph+repair
- ProofWriter clean 10개 + fault 10개
- Discussion clean/flawed 26개

여러 조건을 실행하므로 기존 three-dataset pilot보다 API 호출이 많습니다.

## 3. 평가별 분리 실행

```bat
RUN_ANSWER_COMPARISON_WINDOWS.bat
RUN_REASONING_AUDIT_COMPARISON_WINDOWS.bat
RUN_DISCUSSION_AUDIT_COMPARISON_WINDOWS.bat
```

## 4. 결과 파일

```text
outputs/comparative_evaluation/<run_id>/
├─ result.json
├─ report.html
├─ answer_cases.jsonl
├─ reasoning_audit_items.jsonl
├─ discussion_audit_cases.jsonl
├─ human_review_packet_blinded.csv
├─ human_review_answer_key.csv
└─ failures.json
```

## 5. 핵심 해석

Graph 방식이 우수하다는 주장은 다음 지표에서 비교군보다 우월할 때 가능합니다.

- Direct GPT보다 높은 paired net correction
- 낮은 harmful regression
- 높은 reasoning-error F1
- 낮은 clean false-positive rate
- 높은 root-node localization
- Discussion issue-type F1 및 source localization 향상

Graph width/depth 자체는 우수성 지표가 아닙니다.

## 6. 연구용 주의

`discussion_audit_benchmark_v028.jsonl`은 개발용 synthetic matched set입니다. 최종 논문에서는 별도의 독립 test set을 사람이 annotation하고, 개발 세트와 분리해야 합니다.
