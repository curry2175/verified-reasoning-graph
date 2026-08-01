# v016 — Hybrid VeriCoT–VRG

v015의 ProofWriter GPT 자동화를 기반으로, VeriCoT에서 영감을 받은 검증 루프와 기존 VRG의 풍부한 Graph layer를 통합했습니다.

## 핵심 추가

- Deterministic parser 우선, 실패한 항목에만 GPT controlled-English formalization fallback
- formalization source/confidence/original text/formalized text/new vocabulary provenance
- 실패 Node에 대한 GPT premise grounding
- 외부·암묵 premise는 기본적으로 advisory candidate이며 자동 Proof 근거로 사용하지 않음
- Blind / Guided graph repair packet
- 최대 0–3회의 GPT self-reflection 후 자동 재검증
- Before/After Graph diff 및 Node repair status
- Universal Verified Graph schema/viewer
- 항상 표시되는 상태 Legend와 Layer toggle
- 기존 Graph 상태/관계 보존:
  - Given, Valid, Contradiction, Ungrounded, Untranslatable
  - Blocked by upstream error, insufficient declared support
  - Approved semantic rule, advisory related-only
  - 원문 일치, AI-declared reasoning, inferred reasoning
  - 충돌 경로, 오류 전파, Z3 proof support, alternative proof, Semantic 관계
- ProofWriter JSONL batch API

## 구현상 중요한 원칙

1. Gold label은 GPT 생성 또는 repair prompt에 보내지 않습니다.
2. LLM formalizer는 최종 판정자가 아니라 deterministic parser가 읽을 수 있는 controlled-English 후보 생성기입니다.
3. LLM-inferred premise는 기본적으로 advisory이며 사용자가 승인하지 않는 한 trusted knowledge가 아닙니다.
4. Graph에는 AI가 선언한 경로, 시스템이 복원한 경로, Z3/Horn proof source를 별도 edge layer로 보존합니다.
5. 이 구현은 VeriCoT의 아이디어를 재구성한 hybrid MVP이며, 원 논문의 공식 구현 복제본은 아닙니다.
