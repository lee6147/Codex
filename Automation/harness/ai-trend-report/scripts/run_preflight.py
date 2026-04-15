#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

from create_report_scaffold import FILES, create_scaffold


def workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


def required_paths(root: Path) -> list[Path]:
    return [
        root / "codex.md",
        root / "harness" / "ai-trend-report" / "skill.md",
        root / "harness" / "ai-trend-report" / "agents" / "research-lanes.md",
        root / "harness" / "ai-trend-report" / "references" / "preflight.md",
        root / "harness" / "ai-trend-report" / "references" / "output-contract.md",
        root / "harness" / "ai-trend-report" / "references" / "source-policy.md",
        root / "harness" / "ai-trend-report" / "prompts" / "minimal-prompt.txt",
        root / "harness" / "ai-trend-report" / "prompts" / "automation-prompt.txt",
        root / "harness" / "ai-trend-report" / "prompts" / "safe-prompt.txt",
        root / "harness" / "ai-trend-report" / "scripts" / "create_report_scaffold.py",
        root / "harness" / "ai-trend-report" / "scripts" / "verify_outputs.py",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the local AI trend report harness.")
    parser.add_argument(
        "--output-base-dir",
        default=None,
        help="Base directory where the YYYY-MM-DD report folder should exist. Defaults to the workspace root.",
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Date folder name in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--ensure-scaffold",
        action="store_true",
        help="Create the dated report scaffold if it does not exist.",
    )
    args = parser.parse_args()

    root = workspace_root()
    base_dir = Path(args.output_base_dir).resolve() if args.output_base_dir else root
    target_dir = base_dir / args.date

    missing = [path for path in required_paths(root) if not path.exists()]
    if missing:
        print("[FAIL] Missing required harness files:")
        for path in missing:
            print(f" - {path}")
        return 1

    if args.ensure_scaffold:
        target_dir = create_scaffold(base_dir, args.date)

    report_file_paths = [target_dir / name for name in FILES]
    print(f"[OK] Workspace root: {root}")
    print(f"[OK] Output base directory: {base_dir}")
    print(f"[OK] Target date folder: {target_dir}")
    print("[OK] Required harness files are present.")

    if target_dir.exists():
        existing = sum(1 for path in report_file_paths if path.exists())
        print(f"[OK] Existing report files in target folder: {existing}/{len(report_file_paths)}")
    else:
        print("[WARN] Target date folder does not exist yet.")

    print("[NEXT] Read codex.md, then skill.md, then the reference files before research.")
    print("[NEXT] Run verify_outputs.py after writing the reports.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
