# CHANGELOG v015

v015는 v012의 Premise-given reasoning analyzer를 **검증 가능한 평가 도구**로 확장합니다.

## 추가

- Gold reasoning benchmark JSONL schema
- Step Proof/Chain 상태 accuracy, macro-F1, confusion matrix
- 여러 acceptable parent path 중 하나를 맞히는 Parent-path 평가
- Parent edge best-F1 및 dependency confidence calibration
- Root-error localization precision/recall/F1
- Reasoning role accuracy
- Final Proof/Chain accuracy
- 자동 Review Queue CSV
- 보수적 Compound Step 원자화
  - 명시적 문장/세미콜론 경계만 분리
  - 모든 조각이 Parser에서 번역될 때만 자동 적용
  - `origin_step_id`와 원문 mapping 보존
- 새 화면
  - `/evaluation`
  - `/atomize`
- 새 출력
  - `gold_evaluation.json`
  - `gold_cases.csv`
  - `gold_nodes.csv`
  - `review_queue.csv`
  - `atomized_case.json`

## 중요한 해석

내장 Gold 8개는 코드 회귀와 metric wiring을 확인하는 smoke benchmark입니다. 동일한 샘플을 기준으로 사람이 작성한 정답이므로, 이것만으로 분석기의 외적 타당도가 입증되지는 않습니다. 실제 연구 단계에서는 독립적으로 이중 Annotation한 LLM output corpus가 필요합니다.
