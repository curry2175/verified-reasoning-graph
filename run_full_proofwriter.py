from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from vrg.operational_batch import OperationalBatchManager, TERMINAL_STATUSES
from vrg.dataset_download import download_proofwriter_600


def main() -> int:
    parser = argparse.ArgumentParser(description="Checkpointed Hybrid VeriCoT–VRG runner for ProofWriter JSON/JSONL datasets")
    parser.add_argument("--dataset", type=Path, help="ProofWriter JSON or JSONL file. Omit when using --dataset-source or resuming --run-id.")
    parser.add_argument("--dataset-source", choices=["renma-proofwriter-600"], help="Automatically download a supported dataset source")
    parser.add_argument("--refresh-dataset", action="store_true", help="Force a fresh dataset download")
    parser.add_argument("--run-id", help="Existing run ID to resume")
    parser.add_argument("--mode", choices=["pilot", "full", "range"], default="pilot")
    parser.add_argument("--pilot-count", type=int, default=10)
    parser.add_argument("--start-index", type=int, default=1)
    parser.add_argument("--end-index", type=int)
    parser.add_argument("--model", default="gpt-5.6")
    parser.add_argument("--reasoning-effort", choices=["low", "medium", "high"], default="low")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--repair-iterations", type=int, default=1)
    parser.add_argument("--repair-mode", choices=["blind", "guided"], default="blind")
    parser.add_argument("--max-total-tokens", type=int, default=0, help="0 means unlimited")
    parser.add_argument("--max-failures", type=int, default=0, help="0 means unlimited")
    parser.add_argument("--no-formalizer", action="store_true")
    parser.add_argument("--no-grounder", action="store_true")
    parser.add_argument("--retry-failed", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    manager = OperationalBatchManager(root / "outputs")
    payload = {
        "run_id": args.run_id,
        "mode": args.mode,
        "pilot_count": args.pilot_count,
        "start_index": args.start_index,
        "end_index": args.end_index,
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "max_workers": args.workers,
        "max_retries": args.retries,
        "retry_failed": args.retry_failed,
        "max_repair_iterations": args.repair_iterations,
        "repair_mode": args.repair_mode,
        "use_llm_formalizer": not args.no_formalizer,
        "use_premise_grounder": not args.no_grounder,
        "allow_external_premises": False,
        "prefer_z3": True,
        "max_total_tokens": args.max_total_tokens,
        "max_failures": args.max_failures,
    }
    if args.dataset:
        payload["dataset_text"] = args.dataset.read_text(encoding="utf-8-sig")
    elif args.dataset_source == "renma-proofwriter-600":
        downloaded = download_proofwriter_600(root / "data" / "downloaded", refresh=args.refresh_dataset)
        payload["dataset_text"] = downloaded.dataset_path.read_text(encoding="utf-8-sig")
        payload["dataset_source"] = downloaded.as_dict()
        print(f"Dataset: {downloaded.source_dataset}/{downloaded.split} ({downloaded.row_count} rows, cached={downloaded.cached})")
    elif not args.run_id:
        parser.error("Use --dataset FILE or --dataset-source renma-proofwriter-600 for a new run")

    status = manager.start(payload)
    run_id = status["run_id"]
    print(f"Run ID: {run_id}")
    print(f"Mode: {args.mode}")
    last_line = None
    try:
        while True:
            status = manager.status(run_id)
            summary = status["summary"]
            line = (
                f"status={status['status']} processed={summary['processed_records']}/{summary['total_records']} "
                f"pass={summary['final_pass_count']} failed={summary['failed_records']} "
                f"tokens={summary['total_tokens']} api_calls={summary['total_api_calls']}"
            )
            if line != last_line:
                print(line, flush=True)
                last_line = line
            if status["status"] in TERMINAL_STATUSES:
                print(json.dumps(status, ensure_ascii=False, indent=2))
                return 0 if status["status"] not in {"error"} else 1
            time.sleep(2)
    except KeyboardInterrupt:
        manager.pause(run_id)
        print(f"\nPause requested. Resume with: python run_full_proofwriter.py --run-id {run_id} --mode {args.mode}")
        return 130


if __name__ == "__main__":
    sys.exit(main())
