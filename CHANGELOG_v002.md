# v002 변경 사항

## 해결한 문제

v001 결과에서는 다음과 같이 LLM Step `s1`이 최종 결론 경로에서 사라졌습니다.

- `p1`과 `s1`의 논리식이 동일함
- Z3 unsat core가 `s1` 대신 원본 `p1`을 선택함
- 따라서 `s1.reaches_final = false`처럼 표시됨

이것은 theorem proving 관점에서는 맞지만, LLM Output의 reasoning 흐름을 Graph로 표현하려는 목적에는 맞지 않았습니다.

## v002의 해결 방식

Graph를 세 종류 관계로 분리했습니다.

1. `source_match`
   - LLM Step이 어떤 원문 Premise를 그대로 사용했는지 표시
2. `reasoning_dependency`
   - LLM Output 내부의 단계별 추론 경로
3. `proof_support` / `proof_conflict`
   - Z3가 실제 논리 판정에 사용한 전제

## sample_valid에서 기대되는 핵심 결과

```text
p1 --source_match--> s1
s1 + p2 --reasoning_dependency--> s2
s2 + p3 --reasoning_dependency--> s3
s3 + p4 --reasoning_dependency--> s4
s4 --reasoning_dependency--> final
```

동시에 Z3 proof view에서는 다음처럼 나올 수 있습니다.

```text
p1 + p2 --proof_support--> s2
```

즉, `s1`을 거치지 않아도 원문 `p1`으로 같은 결론을 증명할 수 있습니다.

따라서 `s1`은:

- `chain_reaches_final = true`
- `chain_impact_level = critical`
- `logical_final_changes_if_removed = false`
- `alternative_proof_exists = true`

가 됩니다.

## 검증

- Python 기본 테스트: 7/7 통과
- FastAPI `/api/verify` 요청 확인
- 브라우저 JavaScript 문법 검사 통과
- 현재 제작 환경에는 z3-solver가 없어 자동 테스트는 Horn fallback으로 수행
- 사용자가 v001에서 Z3 backend 작동을 이미 확인했으며, Z3 engine의 핵심 판정 코드는 유지함
