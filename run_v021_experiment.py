from __future__ import annotations
import argparse, json
from pathlib import Path
from vrg.experiment import run_fault_injection_experiment, run_natural_repair_experiment, FAULT_TYPES, DIFFICULTIES

ROOT=Path(__file__).resolve().parent
RUNS=ROOT/'outputs'/'hybrid_runs'
EXPS=ROOT/'outputs'/'experiments'

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--run-id',default='proofwriter_600_v019_reverified')
 p.add_argument('--type',choices=['fault','repair'],default='fault')
 p.add_argument('--sample-count',type=int,default=100)
 p.add_argument('--seed',type=int,default=2026)
 p.add_argument('--max-reasoning-steps',type=int,default=8)
 p.add_argument('--prefer-z3',action='store_true',help='Use Z3 instead of the faster finite-Horn backend')
 p.add_argument('--modes',default='no_repair,blind,guided,cascade')
 p.add_argument('--max-cases',type=int,default=0)
 args=p.parse_args(); source=RUNS/args.run_id; EXPS.mkdir(parents=True,exist_ok=True)
 if args.type=='fault':
  result=run_fault_injection_experiment(source,EXPS,sample_count=args.sample_count,seed=args.seed,fault_types=FAULT_TYPES,difficulties=DIFFICULTIES,prefer_z3=args.prefer_z3,max_reasoning_steps=args.max_reasoning_steps)
 else:
  result=run_natural_repair_experiment(source,EXPS,modes=[x.strip() for x in args.modes.split(',') if x.strip()],max_cases=args.max_cases,prefer_z3=args.prefer_z3)
 print(json.dumps(result,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
