# v012

Premise가 주어진 문제의 AI reasoning 분석을 강화한 본선 버전입니다.

- Declared `depends_on`의 local Horn sufficiency 검증
- `insufficient_declared_support` Chain 상태 추가
- 추정 dependency의 unique/ambiguous/no-support 진단
- 후보 reasoning 경로 및 최소 Horn Proof 집합 표시
- Final 최소 Proof 전반에서 Node 필수성 분류
- reasoning 역할·오류 taxonomy
- compound Step 탐지 및 잘못된 단일 Predicate 변환 차단
- 투명한 Reasoning Quality Profile과 integrity score
- entity swap, argument swap, wrong declared parent Mutation 추가
- `/quality` 전용 분석 화면 추가
- Batch CSV/요약에 품질 지표 추가
- Audit CSV/HTML에 새 reasoning 진단 필드 추가
