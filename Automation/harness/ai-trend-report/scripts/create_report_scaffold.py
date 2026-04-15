#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


FILES = (
    "01_official_tool_updates.html",
    "02_trending_github_repos.html",
    "03_ai_coding_tools_articles.html",
    "04_ai_tools_review.md",
)


HTML_TEMPLATE = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7fb;
      --panel: #ffffff;
      --text: #18202a;
      --muted: #5f6b7a;
      --line: #d8dee8;
      --link: #0a66c2;
      --accent: #e8f1fb;
      --warn: #fff3cd;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", "Noto Sans KR", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.7;
    }}
    main {{
      width: min(960px, calc(100vw - 32px));
      margin: 32px auto 64px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 32px;
    }}
    h1, h2, h3 {{ line-height: 1.3; }}
    a {{ color: var(--link); }}
    .meta, .notice {{
      padding: 12px 14px;
      border-radius: 12px;
      margin: 16px 0;
    }}
    .meta {{ background: var(--accent); }}
    .notice {{ background: var(--warn); }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 10px;
      vertical-align: top;
      text-align: left;
    }}
    .muted {{ color: var(--muted); }}
  </style>
</head>
<body>
  <main>
    <h1>{title}</h1>
    <div class="meta">
      <strong>생성일</strong>: {today}<br>
      <strong>조사 기준</strong>: 여기에 조사 기준 요약을 작성한다.
    </div>
    <h2>목차</h2>
    <p class="muted">본문 작성 후 목차 링크를 정리한다.</p>
    <h2>본문</h2>
    <p>여기에 본문을 작성한다.</p>
    <h2>핵심 요약</h2>
    <p>여기에 핵심 요약을 작성한다.</p>
    <h2>출처</h2>
    <p>여기에 출처 목록을 작성한다.</p>
  </main>
</body>
</html>
"""


MD_TEMPLATE = """---
tags:
  - AI트렌드
  - ClaudeCode
  - Cursor
  - Codex
  - 개발생산성
created: {today}
---

# AI 도구 종합 평가

[[01_official_tool_updates]]
[[02_trending_github_repos]]
[[03_ai_coding_tools_articles]]

## 개요

## 도구별 평가

## 도구 간 비교

## 추천 사용자 유형

## 이번 주 총평

## 다음 주 체크포인트
"""


HTML_TITLES = {
    "01_official_tool_updates.html": "공식 업데이트 보고서",
    "02_trending_github_repos.html": "트렌딩 GitHub 레포지터리 보고서",
    "03_ai_coding_tools_articles.html": "AI 코딩 도구 아티클 요약",
}


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def create_scaffold(base_dir: str | Path = ".", date: str | None = None) -> Path:
    today = date or datetime.now().strftime("%Y-%m-%d")
    target_dir = Path(base_dir).resolve() / today
    target_dir.mkdir(parents=True, exist_ok=True)

    for name in FILES:
        path = target_dir / name
        if name.endswith(".html"):
            write_if_missing(path, HTML_TEMPLATE.format(title=HTML_TITLES[name], today=today))
        else:
            write_if_missing(path, MD_TEMPLATE.format(today=today))

    return target_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a dated AI trend report scaffold.")
    parser.add_argument(
        "base_dir",
        nargs="?",
        default=".",
        help="Directory where the dated report folder should be created.",
    )
    parser.add_argument(
        "--date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Override date folder name in YYYY-MM-DD format.",
    )
    args = parser.parse_args()

    print(create_scaffold(args.base_dir, args.date))


if __name__ == "__main__":
    main()
