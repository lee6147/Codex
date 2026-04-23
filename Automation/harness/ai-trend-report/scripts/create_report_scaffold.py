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
      --hero: linear-gradient(135deg, #183a66 0%, #28539c 100%);
      --hero-text: #ffffff;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", "Noto Sans KR", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.7;
    }}
    .container {{
      width: min(980px, calc(100vw - 32px));
      margin: 32px auto 64px;
    }}
    h1, h2, h3 {{ line-height: 1.3; }}
    a {{ color: var(--link); }}
    .hero {{
      background: var(--hero);
      color: var(--hero-text);
      border-radius: 16px;
      padding: 36px;
      margin-bottom: 24px;
    }}
    .hero p {{
      margin: 8px 0 0;
      opacity: 0.9;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 20px;
    }}
    .meta-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-top: 16px;
    }}
    .stat {{
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 12px;
      padding: 14px 16px;
    }}
    .notice {{
      background: var(--warn);
      border-radius: 12px;
      padding: 14px 16px;
    }}
    .toc ol {{
      margin: 0;
      padding-left: 20px;
    }}
    .toc li {{
      margin: 6px 0;
    }}
    .card {{
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 18px;
      margin-top: 16px;
    }}
    .badge-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 10px 0 12px;
    }}
    .badge {{
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 999px;
      background: var(--accent);
      color: #204977;
    }}
    .meta-line {{
      color: var(--muted);
      font-size: 0.9rem;
      margin-top: 10px;
    }}
    .sources ul {{
      margin: 0;
      padding-left: 20px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header class="hero">
      <h1>{title}</h1>
      <p>생성일: {today} | 조사 기간: 여기에 조사 기간을 작성한다.</p>
      <div class="meta-grid">
        <div class="stat"><strong>핵심 포인트</strong><br>여기에 이번 보고서의 핵심 요약을 작성한다.</div>
        <div class="stat"><strong>조사 기준</strong><br>여기에 조사 기준 요약을 작성한다.</div>
        <div class="stat"><strong>메모</strong><br>여기에 기간 확장 여부 또는 확인 불가 메모를 작성한다.</div>
      </div>
    </header>

    <section class="panel toc">
      <h2>목차</h2>
      <ol>
        <li><a href="#section-1">섹션 1</a></li>
        <li><a href="#section-2">섹션 2</a></li>
        <li><a href="#sources">출처</a></li>
      </ol>
    </section>

    <section class="panel">
      <h2>요약</h2>
      <div class="notice">여기에 독자가 먼저 알아야 할 핵심 변화 2~3문장을 작성한다.</div>
    </section>

    <section class="panel" id="section-1">
      <h2>섹션 1</h2>
      <article class="card">
        <h3>여기에 첫 번째 카드 제목을 작성한다.</h3>
        <div class="badge-row">
          <span class="badge">배지 예시</span>
          <span class="badge">공식 글</span>
        </div>
        <p>여기에 첫 번째 카드 본문을 작성한다.</p>
        <p class="meta-line">발표일: YYYY-MM-DD | 출처: 예시 출처 | 링크: https://example.com</p>
      </article>
      <article class="card">
        <h3>여기에 두 번째 카드 제목을 작성한다.</h3>
        <div class="badge-row">
          <span class="badge">배지 예시</span>
        </div>
        <p>여기에 두 번째 카드 본문을 작성한다.</p>
        <p class="meta-line">실무 시사점: 여기에 실무 관점 요약을 작성한다.</p>
      </article>
    </section>

    <section class="panel" id="section-2">
      <h2>섹션 2</h2>
      <article class="card">
        <h3>여기에 추가 카드 제목을 작성한다.</h3>
        <p>여기에 추가 카드 본문을 작성한다.</p>
      </article>
    </section>

    <section class="panel sources" id="sources">
      <h2>출처</h2>
      <ul>
        <li>여기에 출처 목록을 작성한다.</li>
      </ul>
    </section>
  </div>
</body>
</html>
"""


MD_TEMPLATE = """# AI 코딩 도구 종합 평가 — {today}

#AI트렌드 #ClaudeCode #Cursor #Codex #개발생산성

> 이 문서는 [[01_official_tool_updates]], [[02_trending_github_repos]], [[03_ai_coding_tools_articles]] 의 내용을 종합하여 작성한다.

---

## 개요

- 여기에 이번 주 전체 흐름을 2~3개 불릿으로 요약한다.

---

## 1. Claude Code

### 강점

- 여기에 강점을 작성한다.

### 약점

- 여기에 약점을 작성한다.

### 추천 사용 시나리오

- 여기에 추천 사용 시나리오를 작성한다.

### 현재 시점 총평

여기에 현재 시점 총평을 작성한다.

---

## 2. Cursor

### 강점

- 여기에 강점을 작성한다.

### 약점

- 여기에 약점을 작성한다.

### 추천 사용 시나리오

- 여기에 추천 사용 시나리오를 작성한다.

### 현재 시점 총평

여기에 현재 시점 총평을 작성한다.

---

## 3. OpenAI Codex

### 강점

- 여기에 강점을 작성한다.

### 약점

- 여기에 약점을 작성한다.

### 추천 사용 시나리오

- 여기에 추천 사용 시나리오를 작성한다.

### 현재 시점 총평

여기에 현재 시점 총평을 작성한다.

---

## 도구 간 비교

| 항목 | Claude Code | Cursor | OpenAI Codex |
|------|-------------|--------|--------------|
| 주요 강점 | 여기에 작성한다 | 여기에 작성한다 | 여기에 작성한다 |
| 약점 | 여기에 작성한다 | 여기에 작성한다 | 여기에 작성한다 |
| 추천 사용자 | 여기에 작성한다 | 여기에 작성한다 | 여기에 작성한다 |

---

## 추천 사용자 유형

- 여기에 추천 사용자 유형을 작성한다.

## 이번 주 총평

여기에 이번 주 총평을 작성한다.

## 주요 트렌드 관찰

1. 여기에 첫 번째 트렌드를 작성한다.
2. 여기에 두 번째 트렌드를 작성한다.

## 다음 주 체크포인트

- 여기에 다음 주 체크포인트를 작성한다.
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
