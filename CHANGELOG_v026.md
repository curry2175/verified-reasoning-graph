# v026 변경 내역

## 1. 프로젝트 평가 프레임 정리

- ProofWriter: controlled component validation
- LegalBench/PubMedQA: domain-transfer validation
- Discussion Lab: real-world unstructured document application

## 2. Discussion Semantic Inspector

Node 클릭 UI에 원문, Semantic, Relations, Issues 탭을 추가했습니다.

- exact source span / normalized claim 분리
- polarity, modality, certainty, causal strength
- population/time scope, estimand, magnitude
- study design, analysis method, selection/exposure/eligibility roles
- causal DAG role와 methodological role

## 3. Graph metrics

`vrg/graph_metrics.py`를 추가했습니다.

- size, roots, leaves, components
- SCC-safe depth
- width profile / maximum width
- branching / density / relation diversity
- complexity / grounding / integrity / fidelity scores

## 4. Three-dataset evaluation suite

다음 파일을 추가했습니다.

```text
vrg/evaluation_suite.py
run_three_dataset_evaluation.py
RUN_THREE_DATASET_EVALUATION_WINDOWS.bat
static/suite_evaluation.html
```

지원 데이터셋:

- ProofWriter strict True/False
- LegalBench official evaluation-split Yes/No or True/False rows
- PubMedQA Yes/No, Maybe excluded

출력:

- checkpoint cases JSONL
- failures JSONL
- summary JSON
- HTML report
- token/API usage

## 5. API/UI routes

```text
/suite-evaluation
/api/evaluation-suite/run
/api/evaluation-suite/runs
/api/evaluation-suite/latest
/api/evaluation-suite/report/{run_id}
```

## 6. 테스트

- Python tests: 104 passed
- Python compilation: passed
- Discussion/Evaluation JavaScript syntax: passed
- API key and downloaded datasets excluded from release archive
