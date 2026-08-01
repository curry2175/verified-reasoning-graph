# v022 — Scientific Formalization Preflight

## 문제

v021에서는 일반 과학 문장이 문법적으로는 parse되었지만 의미가 달라지는 경우가 있었습니다.

- `Treatment A reduces inflammation.` → 잘못된 subject/predicate 경계
- `All treatments that reduce inflammation reduce fibrosis progression.` → Rule이 아닌 Atom으로 오인
- GPT 답은 맞아도 verifier의 Context label이 `Unknown`이 되어 불필요한 Repair 발생

## 수정

1. **Formalization Preview**
   - `/test-lab`에서 API 호출 없이 원문, 정규화문, 논리식, warning을 확인합니다.
2. **General science / Discussion mode**
   - labelled multiword entity와 명시적 관계절 규칙을 보수적으로 정규화합니다.
3. **Lexical type premise**
   - `Treatment A`에서 `Treatment_A is a treatment.`를 투명한 파생 premise로 추가합니다.
   - provenance는 `lexical_entity_type`으로 저장됩니다.
4. **Semantic anomaly gate**
   - parse 성공만으로 채택하지 않습니다.
   - quantifier가 entity로 흡수되거나, 관계절이 rule이 되지 않거나, negation이 사라지는 경우를 차단합니다.
5. **Pre-generation validation**
   - Context와 Query를 먼저 형식화합니다.
   - unresolved item이 있으면 GPT answer generation 전에 중단합니다.
6. **Shared formalized input**
   - General science mode에서는 GPT와 verifier가 같은 정규화 Context 및 premise ID를 사용합니다.
7. **Accurate usage count**
   - formalizer, generation, grounder, repair API 호출을 중복 없이 합산합니다.

## 검증 예시

```text
Treatment A reduces inflammation.
All treatments that reduce inflammation reduce fibrosis progression.
```

은 다음으로 정규화됩니다.

```text
p1: Treatment_A reduces inflammation.
p2: If something is a treatment and it reduce inflammation, then it reduce fibrosis progression.
p3: Treatment_A is a treatment.  [lexical_entity_type]
```

Query:

```text
Treatment_A reduces fibrosis progression.
```

Canonical logic:

```text
reduce(treatment_a, inflammation)
treatment(treatment_a)
(treatment(x) AND reduce(x, inflammation)) -> reduce(x, fibrosis_progression)
```
