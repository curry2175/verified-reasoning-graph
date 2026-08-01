# v021 Experiment Guide

## 1. 실행

```bat
cd /d "C:\path\verified_reasoning_graph_mvp_v021"
RUN_WINDOWS.bat
```

브라우저:

```text
http://127.0.0.1:8765/experiment
```

## 2. API 0회 Fault Injection

빠른 Pilot 권장값:

```text
정상 Case 수: 10
Seed: 2026
최대 reasoning steps: 8
Fault types: 전체
Difficulty: local + upstream
```

확장 실험:

```text
정상 Case 수: 100
Seed: 고정
최대 reasoning steps: 8
```

명령창:

```bat
RUN_V021_EXPERIMENT_WINDOWS.bat --type fault --sample-count 100 --seed 2026 --max-reasoning-steps 8
```

실험은 동기식으로 실행됩니다. 정상 Case 수와 Chain 길이가 커질수록 시간이 증가합니다. 결과는 Case가 아니라 Experiment 단위로 `outputs/experiments`에 저장됩니다.

## 3. Natural Failure Repair

Dashboard에서 다음 조건을 선택합니다.

```text
no_repair
blind
guided
cascade
```

`no_repair`는 API 0회입니다. Blind, Guided, Cascade는 실제 OpenAI API를 호출합니다. Gold answer는 Prompt에 포함되지 않습니다.

명령창:

```bat
RUN_V021_EXPERIMENT_WINDOWS.bat --type repair --modes no_repair,blind,guided,cascade
```

## 4. 핵심 지표

- Valid graph acceptance rate
- Invalid graph rejection rate
- False acceptance and false rejection
- Root-error localization rate
- Node precision, recall, F1
- Edge localization recall
- Graph recovery
- Answer recovery
- Harmful repair
- API calls and token use

## 5. 포함된 예시 결과

프로젝트에는 다음이 포함됩니다.

- 10개 정상 Case, 140개 Mutation Pilot
- 7개 자연 Initial FAIL의 No-repair baseline
- 교정된 ProofWriter 600 Graph 전체

Pilot 결과는 소규모 기능 점검이며 최종 연구 결과로 해석하면 안 됩니다.
