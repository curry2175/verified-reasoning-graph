from __future__ import annotations
import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path

from vrg.reverify_run import reverify_run_directory


def safe_extract(zf: zipfile.ZipFile, dest: Path) -> None:
    root = dest.resolve()
    for member in zf.infolist():
        target = (dest / member.filename).resolve()
        if root not in target.parents and target != root:
            raise ValueError(f"Unsafe ZIP member: {member.filename}")
    zf.extractall(dest)


def main() -> None:
    parser = argparse.ArgumentParser(description="Reverify a v018 ProofWriter run without new API calls")
    parser.add_argument("input", help="Run directory or run ZIP")
    parser.add_argument("--output-root", default="outputs/hybrid_runs")
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--no-z3", action="store_false", dest="prefer_z3", default=True, help="Use the finite Horn engine only")
    args = parser.parse_args()
    source = Path(args.input)
    temp = None
    try:
        if source.suffix.lower() == ".zip":
            temp = Path(tempfile.mkdtemp(prefix="vrg_reverify_"))
            with zipfile.ZipFile(source) as zf:
                safe_extract(zf, temp)
            candidates = [x for x in temp.iterdir() if x.is_dir() and (x / "cases").exists()]
            if not candidates and (temp / "cases").exists():
                candidates = [temp]
            if len(candidates) != 1:
                raise ValueError("ZIP must contain exactly one run directory with a cases folder")
            source_run = candidates[0]
        else:
            source_run = source
        def progress(i: int, total: int, rid: str) -> None:
            if i == 1 or i % 25 == 0 or i == total:
                print(f"[{i}/{total}] {rid}", flush=True)
        dest = reverify_run_directory(source_run, Path(args.output_root), new_run_id=args.run_id, prefer_z3=args.prefer_z3, progress=progress)
        archive = shutil.make_archive(str(dest), "zip", dest.parent, dest.name)
        print(f"Reverified run: {dest}")
        print(f"ZIP: {archive}")
        print("New API calls: 0")
    finally:
        if temp and temp.exists():
            shutil.rmtree(temp, ignore_errors=True)

if __name__ == "__main__":
    main()
