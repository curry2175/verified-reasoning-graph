# v023 실행 가이드

## 1. 폴더 이동

```bat
cd /d "C:\Users\chefc\OneDrive\바탕 화면\YAI Challenge\verified_reasoning_graph_mvp_v023"
```

## 2. API Key 복사

```bat
copy "..\verified_reasoning_graph_mvp_v022\.env" ".env"
```

없으면:

```bat
SET_OPENAI_KEY_WINDOWS.bat
```

## 3. 서버 실행

```bat
RUN_WINDOWS.bat
```

## 4. Test Lab

```text
http://127.0.0.1:8765/test-lab?v=023
```

화면 제목이 `Individual Input Test Lab · v023`인지 확인하세요.

## 5. 권장 첫 테스트

```text
Context
Study_S is observational.
All observational studies are causality_limited.
All causality_limited studies are not causation_establishing.

Question
Study_S is causation_establishing.

Gold
False
```

먼저 `입력 점검 · API 0회`를 누르세요. 예상 Preview:

```text
observational(study_s)
study(study_s)
study(x) ∧ observational(x) → causality_limited(x)
study(x) ∧ causality_limited(x) → not causation_establishing(x)
```

`Global symbol table`에서 다음 네 predicate가 보여야 합니다.

```text
study/1
observational/1
causality_limited/1
causation_establishing/1
```

`Orphan antecedents: 없음`, `Question 연결됨`이어야 합니다.

그 후 `개별 Input 실행`을 누르세요. 이상적 결과:

```text
Answer  False
Context False
Gold    False
Graph   PASS
Repair  0
```

## 6. 저장된 Graph

```text
http://127.0.0.1:8765/case-browser
```

## 주의

v023은 명시적인 사실과 규칙의 vocabulary 정렬을 강화한 버전입니다.
`may`, `suggests`, `is associated with`, `proves`, `confounds` 같은 논문
Discussion의 epistemic relation을 완전히 표현하는 전용 ontology는 아직
후속 개발 대상입니다. 이해하지 못한 표현을 확정적 사실로 조용히 낮추지
않고 fallback 또는 차단 대상으로 표시합니다.
