# v015 — ProofWriter 3-way Real Dataset Bridge

v015 continues the main premise-based reasoning-graph branch from v013.

## Added

- Dedicated `/proofwriter` workflow for an original ProofWriter JSON record plus raw AI output.
- Native `True / False / Unknown` normalization, including `A / B / C` option labels.
- Open-world three-way classification:
  - True: the query is derivable.
  - False: the explicit opposite is derivable.
  - Unknown: neither side is derivable.
- Automatic extraction of the queried statement from the standard ProofWriter question wrapper.
- Automatic sentence splitting of the `context` field into `p1 ... pn`.
- ProofWriter grammar extensions:
  - `All blue, green people are red.`
  - `If someone is quiet and red then they are blue.`
  - `If someone is red and not white then they are big.`
- Compact inferred path selection to avoid unnecessarily expanded cyclic Horn paths.
- Reasoning Fingerprint:
  - graph depth, width, density and linearity;
  - logical/authored premise utilization;
  - distractor premises;
  - relevant and irrelevant reasoning steps;
  - benign path multiplicity versus genuine alternative proofs;
  - bottleneck and error-blast-radius summaries.
- Downloads for the full analysis, adapted VRG case and verified graph.
- Included the real record `ProofWriter_AttNeg-OWA-D5-270_Q8` as the built-in integration sample.

## Verification

- 52 Python tests passed.
- All HTML JavaScript syntax checks passed.
- FastAPI smoke tests passed.
- Built-in record result:
  - context label: False;
  - selected minimum context proof: `p1, p12, p15, p16`;
  - premise utilization: 4/17 (23.53%);
  - distractors: 13;
  - root reasoning errors: 0.
