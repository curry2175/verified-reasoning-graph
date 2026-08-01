# v022 실행 가이드

## 1. 실행

```bat
cd /d "C:\Users\chefc\OneDrive\바탕 화면\YAI Challenge\verified_reasoning_graph_mvp_v022"
RUN_WINDOWS.bat
```

## 2. 개별 과학 문장 테스트

브라우저:

```text
http://127.0.0.1:8765/test-lab
```

설정:

```text
Input mode: General science / Discussion
GPT formalizer: ON
Repair: 0 (첫 정상 작동 확인 시)
```

입력:

```text
Context
Treatment A reduces inflammation.
All treatments that reduce inflammation reduce fibrosis progression.

Question
Treatment A reduces fibrosis progression.

Gold
True
```

먼저 `입력 점검 · API 0회`를 누릅니다. 다음이 보여야 합니다.

```text
p1: reduce(treatment_a, inflammation)
p2: (treatment(x) and reduce(x, inflammation)) -> reduce(x, fibrosis_progression)
p3: treatment(treatment_a) [derived lexical type]
question: reduce(treatment_a, fibrosis_progression)
```

그 다음 `개별 Input 실행`을 누릅니다.

## 3. Controlled English 모드

ProofWriter형 문장을 원문 그대로 검사하려면 `Controlled English`를 선택합니다.

## 4. 중요한 범위

v022는 명시적인 사실과 규칙을 Graph로 만드는 중간 단계입니다. `may`, `suggests`, `is associated with`, `proves` 같은 과학적 강도 표현은 조용히 일반 사실로 낮추지 않고 GPT formalizer 대상으로 표시합니다. 이는 아직 완전한 Article/Discussion ontology가 구현되었다는 뜻은 아닙니다.
