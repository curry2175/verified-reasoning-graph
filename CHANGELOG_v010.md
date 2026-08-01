# v010 Changelog

## Real LLM / Dataset bridge

- Raw LLM response에서 numbered/bulleted/line/sentence 기반 reasoning Step 추출
- strict Yes/No final answer 추출
- 자동 Native Case JSON 생성 및 preflight 연결
- 혼합 JSONL Adapter 추가
  - native
  - context list/text
  - theory text
  - triples + rules 기반 ProofWriter-like
  - separate reasoning_steps
- Unknown/Maybe를 Yes/No로 자동 변환하지 않고 실패 기록

## Research evaluation

- Adapter 및 extraction strategy 분포
- Parser coverage와 error taxonomy
- Answer/Proof/Chain/valid-answer-invalid-reasoning 지표
- Reasoning Step proof/chain status 분포
- Dataset JSON, CSV, HTML, adapted JSONL export

## Audit verification

- Audit ZIP 필수 파일 및 안전한 path 검사
- SHA-256 manifest 재검증
- Manifest와 verified graph metadata 비교
- Z3 사용 가능 시 SMT2 replay 및 SAT/UNSAT parity 검사
- 변조 탐지 테스트 추가

## Chain provenance

- Step-level `depends_on` 및 Final `answer_depends_on` 지원
- Declared dependency와 Horn inferred dependency 동시 표시
- Declared path가 있으면 Chain 판정에 우선 사용
- Preflight에서 unknown/future dependency 검출
- Mutation test에서 baseline authored path를 lock하여 silent rerouting 방지

## UI / API

- `/ingest`
- `/dataset`
- `/audit-verify`
- `/api/ingest`
- `/api/dataset-adapt`
- `/api/dataset-evaluate`
- `/api/audit-verify`

## Validation

- Python tests: 39 passed
- HTML/JavaScript syntax: 8 pages passed
- API smoke tests passed
