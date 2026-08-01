# v021 실행 가이드

## 1. 서버 실행

```bat
cd /d "C:\Users\chefc\OneDrive\바탕 화면\YAI Challenge\verified_reasoning_graph_mvp_v021"
RUN_WINDOWS.bat
```

## 2. 개별 Input을 시험할 때

브라우저:

```text
http://127.0.0.1:8765/test-lab
```

입력:

- Context: 한 줄에 사실/규칙 하나
- Question: 판정할 문장 하나
- Gold answer: 선택 사항

`개별 Input 실행`을 누르면 다음이 한 화면에 표시됩니다.

```text
GPT structured output
→ Formalization
→ Proof/Chain verification
→ optional Blind/Guided repair
→ Initial/Repair/Final graph
```

## 3. 저장된 ProofWriter 600 Graph를 볼 때

```text
http://127.0.0.1:8765/case-browser
```

기본 Run:

```text
proofwriter_600_v019_reverified
```

Case를 클릭한 뒤 상단 선택 메뉴에서 다음을 전환할 수 있습니다.

- Initial Graph
- Stored Repair Graph
- Selected Final Graph

## 4. 교정된 Fault Injection 실행

```bat
RUN_V021_EXPERIMENT_WINDOWS.bat --type fault --sample-count 100 --seed 2026 --max-reasoning-steps 8
```

API 호출은 발생하지 않습니다.

결과:

```text
outputs\experiments\fault_v021_<timestamp>_2026\
```

핵심 파일:

- `summary.json`
- `fault_mutations.csv`
- `skipped_mutations.csv`
- `metrics_by_fault_type.csv`
- `metrics_by_difficulty.csv`
- `metrics_by_rejection_channel.csv`
- `paper_table.csv`
- `report.md`

## 5. Repair 비교는 Fault 결과를 검토한 뒤 실행

```bat
RUN_V021_EXPERIMENT_WINDOWS.bat --type repair --modes no_repair,blind,guided,cascade
```

Blind/Guided/Cascade에는 OpenAI API 호출이 발생합니다.
