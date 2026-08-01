# v025 변경 내역

v025는 v024 Discussion Lab에서 수집한 13개 스트레스 테스트를 하나의 일반화된 schema와 회귀 테스트 세트로 통합합니다.

## 1. 원문 충실성 감사

Node마다 다음을 분리합니다.

- `source_text`: 모델이 제시한 원문 인용
- `matched_source_span`: 실제 입력에서 가장 가까운 문장
- `normalized_claim`: 논리 비교용 정규화 의미
- `inferred_details`: 원문에 직접 적혀 있지 않은 시스템 해석
- `source_fidelity_status`: exact / paraphrased / partial / unmatched
- `numeric_mentions`: 45%, p=0.04, 12 months 등의 원문 수치

모델이 `associated`를 `statistically associated`로 바꾸거나 `45%`를 `almost half`로 바꾸면 UI에 인용 충실성 경고가 표시됩니다.

## 2. Node 역할의 이중 구조

기존 Observation / Evidence / Mechanism / Limitation / Conclusion에 더해 다음 역할을 추가했습니다.

- Study design
- Analysis method
- Eligibility criterion
- Selection criterion
- Exposure definition

따라서 landmark 포함 기준, post-treatment adjustment, KM censoring 같은 분석 조건을 생물학적 mechanism으로 잘못 분류하지 않습니다.

Node에는 별도로 `causal_role`과 `methodological_role`이 기록됩니다.

## 3. 검증 강도 분리

모든 Issue를 다음 네 단계로 구분합니다.

1. `formal_conflict`: 문단 내부의 직접 또는 의미상 충돌
2. `rule_confirmed_unsupported`: 구조적으로 결론이 지지되지 않음
3. `structural_methodological_risk`: Graph에서 확인되는 방법론적 편향 위험
4. `model_suggested_concern`: 사람의 추가 검토가 필요한 모델 제안

`구조 확인`이라는 하나의 모호한 표기를 사용하지 않습니다.

## 4. 확장된 오류 taxonomy

- magnitude inflation
- subgroup significance fallacy
- unsupported treatment-effect heterogeneity
- attrition / completer bias
- landmark survivor selection
- time-zero mismatch
- post-treatment mediator adjustment
- estimand mismatch
- collider-selection risk
- noninferiority / equivalence interpretation error
- competing-risk misclassification
- multiplicity and selective reporting
- failed replication versus reproducibility
- biomarker/surrogate to therapeutic-benefit overreach

## 5. Issue 그룹화

유사한 하위 진단을 상위 Issue 그룹으로 묶습니다. 예를 들어 necessity violation과 exclusivity conflict가 같은 결론을 가리키면 하나의 상위 카드 아래에서 표시됩니다.

## 6. UI 안전성과 가독성

- 새 실행을 누르면 이전 결과를 즉시 숨김
- 분석 대상 원문의 preview, input hash, run ID 표시
- 요청 실패 시 이전 결과 대신 명확한 오류 카드 표시
- Node 상세에서 원문 직접 인용과 시스템 정규화 의미를 분리
- 수치, 분석집단, 시간범위, estimand, 방법론적 역할을 카드로 표시
- 원시 JSON은 접힌 고급 정보에만 표시

## 7. 회귀 테스트

`data/discussion_regression_cases_v025.jsonl`에 사용자와 함께 수집한 13개 문단을 고정했습니다.

- 기존 Python tests: 85
- v025 신규 tests: 12
- 합계: 97 tests
