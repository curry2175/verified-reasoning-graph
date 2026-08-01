# v003 변경 사항

## 사용자 결과에서 확인된 점

업로드된 두 오류 사례에서 다음이 정상 확인되었습니다.

- 근거 없는 `Bob is a doctor.`는 `Ungrounded`
- `Bob is not kind.`는 `Contradiction`
- 두 오류가 최종 답에 사용되지 않을 때 Final은 계속 Valid

하지만 기존 샘플은 오류 Node가 고립되어 있어 오류 전파를 시험하지 못했습니다.

## 추가된 기능

### Proof status와 Chain status 분리

- `proof_status`: 문제 전체에서 현재 주장 자체가 증명되는가
- `chain_status`: LLM이 실제로 작성한 부모 경로가 정상인가

### 상위 오류 전파

LLM이 잘못된 Node를 사용해 다음 Step을 만들면 다음처럼 표시합니다.

```text
proof_status = valid
chain_status = blocked_by_upstream_error
```

### 오류 근원 추적

각 차단 Node에 다음 필드가 추가되었습니다.

- `blocking_parent_nodes`
- `upstream_error_nodes`
- `reasoning_conflict_dependencies`

### 새 Edge

- `reasoning_conflict`
- `error_propagation`

### 새 샘플

- `sample_alternative_path_ungrounded`
- `sample_alternative_path_contradiction`

두 샘플 모두 최종 답은 다른 올바른 경로로 증명되지만, LLM이 작성한 경로는 잘못된 상위 Node에 의존합니다.

## 검증

- Python 테스트: 8/8 통과
- 브라우저 JavaScript 문법 검사 통과
- Controlled-English 샘플 결과 생성 확인
- 제작 환경에서는 Horn fallback으로 자동 테스트
- Windows에서는 `z3-solver` 설치 후 Z3 backend 우선 사용
