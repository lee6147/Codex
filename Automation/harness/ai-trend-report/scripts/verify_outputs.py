#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

from create_report_scaffold import FILES


HTML_REQUIRED_SNIPPETS = (
    '<html lang="ko">',
    '<meta charset="utf-8">',
    "<h1>",
    "생성일",
    "출처",
)

HTML_PLACEHOLDERS = (
    "여기에 조사 기준 요약을 작성한다.",
    "여기에 본문을 작성한다.",
    "여기에 핵심 요약을 작성한다.",
    "여기에 출처 목록을 작성한다.",
)

MD_REQUIRED_SNIPPETS = (
    "[[01_official_tool_updates]]",
    "[[02_trending_github_repos]]",
    "[[03_ai_coding_tools_articles]]",
    "# AI 도구 종합 평가",
)

MD_PLACEHOLDERS = (
    "## 개요\n\n## 도구별 평가",
    "## 다음 주 체크포인트",
)


def find_missing_snippets(text: str, required_snippets: tuple[str, ...]) -> list[str]:
    return [snippet for snippet in required_snippets if snippet not in text]


def find_present_placeholders(text: str, placeholders: tuple[str, ...]) -> list[str]:
    return [snippet for snippet in placeholders if snippet in text]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify generated AI trend report outputs.")
    parser.add_argument(
        "--output-base-dir",
        default=".",
        help="Base directory containing the YYYY-MM-DD output folder.",
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Date folder name in YYYY-MM-DD format.",
    )
    args = parser.parse_args()

    target_dir = Path(args.output_base_dir).resolve() / args.date
    if not target_dir.exists():
        print(f"[FAIL] Output folder does not exist: {target_dir}")
        return 1

    failures: list[str] = []

    for name in FILES:
        path = target_dir / name
        if not path.exists():
            failures.append(f"Missing file: {path}")
            continue

        text = path.read_text(encoding="utf-8")
        if name.endswith(".html"):
            missing = find_missing_snippets(text, HTML_REQUIRED_SNIPPETS)
            if missing:
                failures.append(f"{name}: missing required snippets: {', '.join(missing)}")
            placeholders = find_present_placeholders(text, HTML_PLACEHOLDERS)
            if placeholders:
                failures.append(f"{name}: still contains scaffold placeholders")
        else:
            missing = find_missing_snippets(text, MD_REQUIRED_SNIPPETS)
            if missing:
                failures.append(f"{name}: missing required snippets: {', '.join(missing)}")
            placeholders = find_present_placeholders(text, MD_PLACEHOLDERS)
            if placeholders:
                failures.append(f"{name}: still looks like the scaffold template")

            if "#AI트렌드" not in text and "- AI트렌드" not in text:
                failures.append(f"{name}: missing AI트렌드 tag or equivalent frontmatter entry")

    if failures:
        print(f"[FAIL] Verification failed for {target_dir}")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print(f"[OK] Output verification passed for {target_dir}")
    print("[OK] All expected files exist and no scaffold placeholders were found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
