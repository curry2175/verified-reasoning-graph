# v025 실행 가이드

## 1. 기존 서버 종료

v024를 실행한 명령창에서:

```bat
Ctrl + C
```

## 2. 폴더 이동

```bat
cd /d "C:\Users\chefc\OneDrive\바탕 화면\YAI Challenge\verified_reasoning_graph_mvp_v025"
```

## 3. API Key 복사

```bat
copy "..\verified_reasoning_graph_mvp_v024\.env" ".env"
```

`.env`가 없다면:

```bat
SET_OPENAI_KEY_WINDOWS.bat
```

## 4. 서버 실행

```bat
RUN_WINDOWS.bat
```

## 5. Discussion Lab

```text
http://127.0.0.1:8765/discussion-lab?v=025
```

새 화면에서 확인할 점:

- 결과 상단의 입력 preview / input hash / run ID
- Issue 그룹과 하위 진단
- 검증 수준: 형식 충돌 / 구조적 비지지 / 방법론 위험 / 모델 제안
- Node 클릭 시 원문 직접 인용과 시스템 정규화 의미가 분리됨
- 원문 수치와 source fidelity 경고

## 6. 기존 Test Lab

```text
http://127.0.0.1:8765/test-lab?v=025
```

True / False / Unknown이 명시된 논리 문제는 계속 이 화면을 사용합니다.

## 7. 테스트 실행

```bat
run_tests_windows.bat
```

또는:

```bat
.venv\Scripts\python.exe -m pytest -q
```
