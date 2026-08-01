# v027 실행 가이드

## 1. 설치 및 서버 실행

Windows Anaconda Prompt:

```bat
cd /d "C:\Users\chefc\OneDrive\바탕 화면\YAI Challenge\verified_reasoning_graph_mvp_v027"
copy "..\verified_reasoning_graph_mvp_v026\.env" ".env"
RUN_WINDOWS.bat
```

처음 실행하거나 `.env`가 없다면 `SET_OPENAI_KEY_WINDOWS.bat`을 사용합니다.

## 2. Discussion Lab

```text
http://127.0.0.1:8765/discussion-lab?v=027
```

비정형 Discussion/AI paragraph를 그대로 붙여넣습니다. Premise와 Question으로 미리 나누지 않습니다.

Node를 클릭하면 다음 탭을 확인합니다.

- `원문`: source span, 정규화 claim, fidelity
- `Semantic`: polarity, modality, scope, causal/method role
- `Relations`: 들어오고 나가는 graph relation
- `Issues`: 관련 오류와 검증 수준

상단의 Depth와 Width는 graph 구조를 설명하며 정확도 자체를 뜻하지 않습니다.

## 3. Evaluation UI

```text
http://127.0.0.1:8765/suite-evaluation?v=027
```

처음에는 다음 설정을 권장합니다.

```text
Datasets: ProofWriter + LegalBench + PubMedQA
Limit per dataset: 20
Reasoning: low
Repair: 0
```

실행 후 표에서 다음을 분리해서 봅니다.

- Accuracy / Macro-F1
- Graph depth / width
- Grounding / Integrity / Fidelity
- Tokens

## 4. CLI Pilot

```bat
RUN_THREE_DATASET_EVALUATION_WINDOWS.bat
```

동일한 직접 명령:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py --limit-per-dataset 20 --model gpt-5.6 --reasoning-effort low --repair-iterations 0
```

## 5. 확대 실행

데이터셋당 100개:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py --limit-per-dataset 100 --model gpt-5.6 --reasoning-effort low --repair-iterations 0
```

전체 strict-binary eligible case:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py --limit-per-dataset 0 --model gpt-5.6 --reasoning-effort low --repair-iterations 0
```

API 비용과 실행시간 때문에 Pilot → 100 cases → Full 순서가 안전합니다.

## 6. 개별 데이터셋

ProofWriter만:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py --datasets proofwriter --limit-per-dataset 100
```

LegalBench의 특정 task만:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py --datasets legalbench --legal-tasks hearsay --limit-per-dataset 100
```

PubMedQA만:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py --datasets pubmedqa --limit-per-dataset 100
```

## 7. 결과 파일

```text
outputs/evaluation_suite/<run_id>/
```

`report.html`을 브라우저로 열면 데이터셋별 정답·Graph 지표를 비교할 수 있습니다. `failures.jsonl`에는 answer mismatch, graph failure, 실행 오류가 모입니다.


## 긴 Discussion 입력

- 고정 30,000자 입력 제한이 없습니다.
- 기본적으로 약 24,000자 단위로 문단·문장 경계를 보존해 자동 분할합니다.
- 전체 입력 한도를 다시 설정하려면 `.env`에 `DISCUSSION_MAX_INPUT_CHARS=<숫자>`를 지정합니다. `0` 또는 미설정은 제한 없음입니다.
- chunk 크기는 `DISCUSSION_CHUNK_CHARS`로 변경할 수 있습니다. 기본값은 24000입니다.
- Discussion Lab 검증기는 현재 Typed Graph 구조 규칙을 사용하며 Z3는 사용하지 않습니다.
