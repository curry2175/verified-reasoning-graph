# v027 변경 내역

## Discussion Lab 입력 길이

- 애플리케이션의 고정 30,000자 입력 제한을 제거했습니다.
- 기본값에서는 전체 입력 길이와 chunk 수에 별도 상한을 두지 않습니다.
- 긴 입력은 문단·문장 경계를 우선 보존하며 약 24,000자 단위로 자동 분할합니다.
- 각 chunk를 별도 structured-output 호출로 분석한 뒤 Node, Edge, Issue를 하나의 문서 Graph로 병합합니다.
- 병합 후 전체 원문을 대상으로 deterministic issue pattern과 Graph metric을 다시 계산합니다.
- 원문을 조용히 자르거나 버리지 않습니다.

## 투명성

- 결과에 `analysis_mode`, `chunk_count`, `input_char_count`, `api_call_count`를 저장합니다.
- UI에 입력 문자 수, 자동 분할 여부, chunk 수, API 호출 수를 표시합니다.
- Discussion Lab의 현재 검증 엔진을 `typed_graph_structural_rules`로 명시합니다.
- `z3_used: false`를 결과에 기록하고 UI에도 표시합니다.

## 설정

- `DISCUSSION_MAX_INPUT_CHARS=0`: 전체 입력 제한 없음(기본값)
- `DISCUSSION_CHUNK_CHARS=24000`: 내부 chunk 목표 크기
- `DISCUSSION_MAX_CHUNKS=0`: chunk 수 제한 없음(기본값)

Z3 기반 Horn/SMT 검증은 ProofWriter/Test Lab 계층에서 사용하며, Discussion Lab은 개방형 자연어 의미 관계를 Typed Graph와 구조 규칙으로 감사합니다.
