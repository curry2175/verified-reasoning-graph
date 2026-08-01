# v026 Three-Dataset Evaluation Design

## 연구 프레임

### Layer 1 — Controlled logical validation

ProofWriter의 구조화된 facts/rules/query를 사용해 다음을 평가합니다.

- binary answer accuracy
- context-derived label agreement
- explicit reasoning dependency
- verifier Graph PASS
- repair success/cost

사용자 정책에 따라 Gold `Unknown`은 제외합니다.

### Layer 2 — Domain-transfer validation

LegalBench와 PubMedQA에서 다음을 평가합니다.

- strict binary answer accuracy
- public reasoning step source grounding
- source span fidelity
- graph structure and stability
- domain별 오류 패턴

LegalBench는 공식 Hugging Face evaluation split을 우선 사용하고 명시적 Yes/No 또는 True/False label만 포함합니다. 네트워크/API 장애 때만 GitHub 파일을 fallback으로 사용하며, train split fallback은 metadata에 경고를 기록합니다. PubMedQA는 `Maybe`를 제외합니다.

### Layer 3 — Real-world application

Discussion Lab은 정답 label이 없는 실제 비정형 문단을 분석합니다. 따라서 benchmark accuracy 대신 다음을 평가합니다.

- source alignment
- node/edge extraction fidelity
- issue precision/recall on annotated paragraphs
- graph stability across runs
- human usefulness

## 공통 Answer Metrics

```text
Accuracy
Macro-F1
Yes precision / recall / F1
No precision / recall / F1
```

클래스 분포가 불균형할 수 있으므로 accuracy만 보지 않고 macro-F1을 함께 사용합니다.

## Graph Metrics

### Structural complexity

```text
Node count
Edge count
Maximum depth
Mean conclusion depth
Maximum width
Width profile
Mean branching factor
Density
Connected components
```

Depth는 SCC를 하나의 component로 축약한 DAG에서 계산하므로 cycle이 있어도 무한대로 증가하지 않습니다.

### Grounding

```text
Grounded-edge ratio
Evidence-to-conclusion ratio
Claims reachable from evidence
Source-span coverage
```

### Integrity

```text
Unsupported conclusion penalty
Contradiction penalty
Weak/model-suggested edge penalty
Blocked/untranslatable penalty
```

### Fidelity

```text
Exact source alignment
Numeric preservation
Provenance coverage
Source span validity
```

### Important interpretation

- 높은 depth는 정교한 추론일 수도 있고 불필요한 intermediate claim의 결과일 수도 있습니다.
- 높은 width는 근거 다양성일 수도 있고 duplicate node의 결과일 수도 있습니다.
- 따라서 complexity는 grounding/integrity/fidelity와 함께 해석합니다.

## Dataset-specific interpretation

### ProofWriter

정답과 proof가 비교적 명확하므로 answer와 formal verification을 모두 강하게 해석할 수 있습니다.

### LegalBench

여러 task가 서로 다른 법률 능력을 측정합니다. 전체 평균뿐 아니라 task별 결과를 반드시 함께 봅니다. 현재 runner는 strict binary row만 자동 선별합니다.

### PubMedQA

질문·초록 context에서 yes/no 결론을 생성합니다. biomedical domain robustness를 평가하지만, ProofWriter처럼 gold proof graph가 있는 것은 아니므로 Graph 평가는 source-grounding 중심입니다.

## Recommended run sequence

```text
Smoke:  5 cases/dataset
Pilot: 20 cases/dataset
Scale: 100 cases/dataset
Full:  all eligible binary cases
```

Repair 효과를 비교하려면 동일 case set에서 `repair=0`과 `repair=1`을 별도 run으로 실행합니다. Gold label은 reasoning generation prompt에 포함하지 않습니다.
