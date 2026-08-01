# v006 Changelog

- JSONL 기반 Batch Evaluation 추가
- `/batch` 전용 UI 추가
- `/api/batch-verify` 및 결과 다운로드 endpoint 추가
- 한 Case가 실패해도 나머지 Case 실행을 계속하는 오류 격리 추가
- Answer accuracy, Proof/Chain valid rate, reasoning error rate 계산
- `valid_answer_but_invalid_reasoning` 집계 추가
- Final Proof/Chain 및 root error type 분포 추가
- 평균, 중앙값, p95, 전체 runtime 측정 추가
- Case별 CSV와 전체 JSON 자동 저장
- counterfactual 계산을 Batch에서 선택적으로 비활성화 가능
- 내장 9개 평가 Case를 `data/batch_sample.jsonl`로 제공
