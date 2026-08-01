# Hybrid VeriCoT–Verified Reasoning Graph MVP v028

v027은 프로젝트를 두 개의 상호 보완적인 층으로 정리합니다.

```text
통제된 논리 평가
ProofWriter / LegalBench / PubMedQA
→ parser, answer, public reasoning graph, verifier 성능 측정

실제 적용
Discussion Lab
→ 비정형 문단을 Typed Reasoning Graph로 변환하고 내부 논리 감사
```

실제 문서에서는 Premise, Rule, Evidence, Limitation, Conclusion이 미리 구분되어 있지 않습니다. 따라서 ProofWriter 같은 구조화 데이터는 실제 UI를 흉내 내기 위한 것이 아니라 **parser와 verifier를 분리해서 시험하는 component-level benchmark**로 사용합니다. 실제 사용자는 문단 전체를 Discussion Lab에 넣습니다.

## v027 핵심 기능

### Discussion Lab Semantic Inspector

Node를 클릭하면 원시 JSON보다 먼저 다음을 읽기 쉬운 카드로 표시합니다.

- 원문 source span과 정규화된 claim
- discourse role과 assertion type
- polarity, modality, certainty, causal strength
- population/time scope, effect magnitude, estimand
- study design, analysis method, eligibility, selection, exposure definition
- mediator, collider, competing-event 등 causal/methodological role
- supports, limits, contradicts 등 incoming/outgoing relations
- 관련 Issue와 최종 결론 영향

원시 JSON은 `고급 정보`에서만 펼쳐 봅니다.

### Graph Metrics

문단별로 다음 구조 지표를 계산합니다.

```text
Size:       nodes, edges, roots, leaves, conclusions, components
Depth:      maximum depth, mean conclusion depth, longest chain
Width:      maximum width, level별 width profile
Complexity: branching factor, density, relation-type diversity
Grounding:  grounded-edge ratio, evidence-to-conclusion ratio
Integrity:  unsupported / contradictory / weak-edge penalties
Fidelity:   source alignment, numeric preservation, provenance coverage
```

Width와 Depth는 정확도 점수가 아니라 **구조적 복잡성 지표**입니다. v027은 Complexity, Grounding, Integrity, Fidelity를 분리해 표시합니다.

### 세 데이터셋 통합 Evaluation

```text
ProofWriter
- Gold proof가 있는 통제된 다단계 논리 평가
- Unknown 제외, True/False만 Yes/No로 평가
- Answer + Context label + Graph PASS + Repair 측정

LegalBench
- 공식 Hugging Face evaluation split에서 정답이 명시적 Yes/No 또는 True/False인 행만 자동 선별
- 법률 domain-transfer 평가
- task 이름 필터 지원

PubMedQA
- Expert-labeled PQA-L 사용
- Maybe 제외, Yes/No만 평가
- Biomedical domain-transfer 평가
```

공통 출력:

- accuracy, macro-F1
- case별 public reasoning graph
- node/edge/depth/width
- grounding/integrity/fidelity scores
- answer mismatch와 graph failure 목록
- token/API usage
- checkpoint JSONL, summary JSON, HTML report

> v027의 LegalBench/PubMedQA Graph 평가는 사람이 보지 못하는 hidden chain-of-thought가 아니라, 모델이 명시적으로 출력한 짧은 public reasoning steps만 사용합니다.

## 빠른 실행

### 서버와 UI

```bat
RUN_WINDOWS.bat
```

```text
Discussion Lab       http://127.0.0.1:8765/discussion-lab?v=027
3-Dataset Evaluation http://127.0.0.1:8765/suite-evaluation?v=027
Test Lab             http://127.0.0.1:8765/test-lab?v=027
Case Browser          http://127.0.0.1:8765/case-browser?v=027
```

### 세 데이터셋 Pilot

```bat
RUN_THREE_DATASET_EVALUATION_WINDOWS.bat
```

기본값은 데이터셋당 strict-binary 20개, repair 0회입니다.

직접 실행:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py ^
  --datasets proofwriter legalbench pubmedqa ^
  --limit-per-dataset 20 ^
  --legal-tasks hearsay ^
  --model gpt-5.6 ^
  --reasoning-effort low ^
  --repair-iterations 0
```

LegalBench task를 제한하려면:

```bat
.venv\Scripts\python.exe run_three_dataset_evaluation.py ^
  --datasets legalbench ^
  --legal-tasks hearsay ^
  --limit-per-dataset 50
```

전체 eligible case를 실행하려면 `--limit-per-dataset 0`을 사용합니다. 먼저 pilot 결과를 확인한 뒤 확대하는 것을 권장합니다.

## 결과 폴더

```text
outputs/evaluation_suite/<run_id>/
├─ cases.jsonl
├─ failures.jsonl
├─ summary.json
├─ report.html
└─ run_config.json
```

데이터셋 다운로드 캐시는 다음에 저장되며 Git에는 포함되지 않습니다.

```text
data/downloaded/evaluation_suite/
```

## 평가 해석 원칙

```text
Answer accuracy
≠
Graph quality
```

정답을 맞혔더라도 source grounding이 약하거나 unsupported conclusion을 포함할 수 있습니다. 반대로 Graph가 단순하고 충실해도 답이 틀릴 수 있습니다. 따라서 최소한 다음을 별도로 보고합니다.

1. Answer correctness
2. Graph grounding
3. Graph logical integrity
4. Source fidelity
5. Structural complexity

자세한 실행법은 `V027_START_GUIDE.md`, 평가 설계는 `EVALUATION_3_DATASETS_V027.md`, 변경사항은 `CHANGELOG_v027.md`를 참고하세요.


## v027 긴 Discussion 입력과 검증 엔진

Discussion Lab은 더 이상 30,000자 고정 입력 제한을 사용하지 않습니다. 기본값에서 `DISCUSSION_MAX_INPUT_CHARS=0`, `DISCUSSION_MAX_CHUNKS=0`으로 전체 입력 길이와 chunk 수에 애플리케이션 상한을 두지 않습니다. 긴 문서는 기본 약 24,000자 단위로 문단·문장 경계를 우선 보존해 자동 분할하고, 각 결과를 하나의 문서 Graph로 병합합니다.

Discussion Lab은 현재 Z3를 직접 사용하지 않습니다. OpenAI structured output으로 Typed Claim Graph를 추출한 뒤 deterministic Graph pattern과 방법론 규칙으로 재검사합니다. Z3/Horn 검증은 형식화된 predicate와 규칙이 있는 ProofWriter/Test Lab 계층에서 사용합니다.

아주 긴 문서는 chunk 수에 비례해 API 호출 수와 비용이 증가합니다. LLM이 생성한 직접 Edge는 출처 안전성을 위해 기본적으로 chunk 내부에 유지되며, 병합 후 전체 원문 기반 deterministic pattern 검사가 다시 실행됩니다.


## v028 · 비교군 기반 우수성 평가

v028은 Graph가 단순히 생성 가능하다는 평가를 넘어, 동일 사례에서 다음 조건을 직접 비교합니다.

- Direct GPT
- Direct GPT + free-form self-critique
- Public reasoning graph + verifier
- Graph + verifier-guided repair

핵심 결과는 Accuracy만이 아니라 Correction rate, harmful regression rate, net correction, paired bootstrap confidence interval, McNemar exact test로 보고합니다.

ProofWriter clean/fault reasoning audit에서는 Plain critic, checklist critic, formal Graph verifier의 오류 precision/recall/F1, clean false-positive rate, root-node localization을 비교합니다.

Discussion audit에는 13개 오류 유형의 flawed paragraph와 의미가 대응되는 13개 clean control을 포함합니다. Plain critique, structured critique, Discussion Graph를 issue F1, clean false-positive, source localization, source fidelity로 비교합니다. 이 26개 세트는 개발용 synthetic benchmark이며, 최종 주장에는 독립적인 human-annotated external test set이 추가되어야 합니다.

실행:

```bat
RUN_COMPARATIVE_PILOT_WINDOWS.bat
```

웹 화면: `http://127.0.0.1:8765/comparative-evaluation`
