# v024 변경 내역

## 1. Discussion Reasoning Lab

새 주소:

```text
http://127.0.0.1:8765/discussion-lab
```

자연스러운 Discussion/AI 문단을 그대로 입력하면 한 번의 구조화 API 호출로 다음을 생성합니다.

- Observation / Evidence / Claim / Mechanism / Limitation / Conclusion Node
- supports / contradicts / limits / causes / mediates / precedes
- necessary_for / not_necessary_for / exclusive_through / generalizes_to Edge
- direct/semantic contradiction
- causal overclaim
- temporal inversion
- scope overreach
- necessity violation
- exclusivity conflict
- evidence–conclusion strength mismatch

이 기능은 외부 사실 또는 참고문헌의 실재 여부를 확인하지 않습니다. 문단 내부의 논리·인과·범위·확실성 구조만 감사합니다.

## 2. 사용자 친화적 Node / Edge 설명

Test Lab, Case Browser, Discussion Lab에서 Node 또는 Edge를 클릭하면 기본적으로 다음이 카드로 표시됩니다.

- 원문
- 쉬운 의미
- Node 역할과 상태
- 검증 결과 또는 문제 설명
- 직접 근거와 오류 영향 Node
- 최종 결론 영향
- 범위·시간·확실성

원시 JSON은 `고급 정보 · 원시 JSON`을 펼칠 때만 표시됩니다.

## 3. 기존 기능 보존

- v023 Global vocabulary alignment
- ProofWriter True / False / Unknown 검증
- Z3 proof 및 authored chain 분리
- Blind / Guided / Cascade repair
- Case Browser 및 fault experiment

Discussion Lab은 기존 정리 증명 verifier와 분리되어 동작합니다.
