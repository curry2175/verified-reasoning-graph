from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from vrg.comparative_evaluation import run_comparative_evaluation
from vrg.evaluation_suite import BINARY_DATASETS


def main() -> int:
    parser = argparse.ArgumentParser(description="Paired evaluation of Direct GPT, self-critique, graph verification, graph repair, and Discussion audit.")
    parser.add_argument("--datasets", nargs="+", choices=BINARY_DATASETS, default=list(BINARY_DATASETS))
    parser.add_argument("--limit-per-dataset", type=int, default=20, help="Balanced pilot size per dataset; 0 means all eligible cases")
    parser.add_argument("--legal-tasks", nargs="*", default=[])
    parser.add_argument("--audit-cases", type=int, default=20, help="Number of clean ProofWriter graphs to pair with mutations")
    parser.add_argument("--model", default="gpt-5.6")
    parser.add_argument("--reasoning-effort", choices=["low", "medium", "high"], default="low")
    parser.add_argument("--max-output-tokens", type=int, default=3500)
    parser.add_argument("--seed", type=int, default=2028)
    parser.add_argument("--refresh-datasets", action="store_true")
    parser.add_argument("--skip-answer", action="store_true")
    parser.add_argument("--skip-audit", action="store_true")
    parser.add_argument("--skip-discussion", action="store_true")
    parser.add_argument("--discussion-benchmark", default="data/discussion_audit_benchmark_v028.jsonl")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    benchmark = Path(args.discussion_benchmark)
    if not benchmark.is_absolute():
        benchmark = root / benchmark
    result = run_comparative_evaluation(
        output_root=root / "outputs" / "comparative_evaluation",
        data_root=root / "data" / "downloaded" / "evaluation_suite",
        discussion_benchmark=benchmark,
        datasets=args.datasets,
        limit_per_dataset=args.limit_per_dataset,
        legal_tasks=args.legal_tasks,
        audit_cases=args.audit_cases,
        run_answer_comparison=not args.skip_answer,
        run_reasoning_audit=not args.skip_audit,
        run_discussion_audit=not args.skip_discussion,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        max_output_tokens=args.max_output_tokens,
        seed=args.seed,
        refresh_datasets=args.refresh_datasets,
    )
    print(json.dumps({"run_id": result["run_id"], "summary": result["summary"]}, ensure_ascii=False, indent=2))
    print(f"\nReport: {root / 'outputs' / 'comparative_evaluation' / result['run_id'] / 'report.html'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
