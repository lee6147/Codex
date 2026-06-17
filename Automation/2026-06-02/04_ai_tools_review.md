---
created-date: 2026-06-02
source-status: live-verified
search-window:
  official: 2026-05-31..2026-06-02
  articles: 2026-05-27..2026-06-02
tags:
  - ai-trend
  - AI트렌드
---

# AI 肄붾뵫 ?꾧뎄 醫낇빀 ?됯?

# AI 코딩 도구 종합 평가 - 2026-06-02

## 연결 문서

- [[01_official_tool_updates]]
- [[02_trending_github_repos]]
- [[03_ai_coding_tools_articles]]

## 오늘의 결론

2026-06-02 기준으로 가장 의미 있는 공식 업데이트는 OpenAI의 `Codex CLI 0.136.0`이다. TUI 링크/표 표시, 세션 아카이브, app-server, 원격 실행, Windows 샌드박스, 인증/보안 수정이 한 번에 포함되어 운영형 코딩 agent의 기반 기능이 강화됐다.

Claude Code는 2026-05-31 `2.1.159`가 확인됐지만 공식 설명상 내부 인프라 개선이며 사용자 노출 변경은 없다. Cursor는 2026-05-31~2026-06-02 엄격 창 안의 새 공식 업데이트를 확인하지 못했고, 가장 가까운 공식 항목은 2026-05-29 `Cursor 3.6 Auto-review Run Mode`다.

기사량은 최근 2일 기준으로 부족했다. 따라서 기사 검색은 하네스 규칙에 따라 7일(2026-05-27~2026-06-02)로 확대했다. 이 범위에서 반복되는 핵심은 “모델 경쟁”보다 “agent harness, 승인 정책, 코드베이스 지도화, 비용/품질 관리, 보안 정책” 쪽으로 경쟁축이 이동하고 있다는 점이다.

## 도구별 평가

| 도구 | 오늘의 신호 | 평가 |
| --- | --- | --- |
| Codex | 2026-06-01 CLI 0.136.0 공식 릴리스 | 터미널 자동화, 세션 보관, app-server, Windows/보안 운영면에서 가장 직접적인 변화가 있다. |
| Claude Code | 2026-05-31 2.1.159 공식 릴리스 | 사용자 기능 변화는 없지만 2.1.x 계열의 agent/worktree/plugin 안정화 흐름은 계속된다. |
| Cursor | 엄격 창 내 신규 업데이트 확인 불가 | 2026-05-29 Auto-review Run Mode는 장시간 agent 실행과 승인 부담 감소 측면에서 계속 중요하다. |

## GitHub Trending 관찰

오늘 GitHub Trending daily/weekly에서는 `microsoft/markitdown`, `supermemoryai/supermemory`, `EveryInc/compound-engineering-plugin`, `revfactory/harness`, `Lum1104/Understand-Anything`, `colbymchenry/codegraph`, `affaan-m/ECC`가 특히 관련성이 높았다.

공통점은 모델 자체가 아니라 agent가 더 잘 읽고, 기억하고, 구조화하고, 검증하도록 돕는 주변 계층이라는 점이다. 문서 변환, 메모리 API, 코드 지식 그래프, domain-specific agent team, harness 최적화가 모두 같은 방향을 가리킨다.

## 기사/분석 관찰

- The New Stack의 2026-06-01 비교 글은 Claude Code, Cursor, Codex, Antigravity가 점점 비슷한 agentic coding blueprint로 수렴한다고 본다.
- XDA의 2026-05-28 30일 사용 후기는 Claude Code를 자율적 대화형 코딩에 강한 도구로, Codex를 bulk/background 작업에 강한 도구로, Cursor를 editor-native hybrid 경험에 강한 도구로 정리했다.
- Cursor Developer Habits Report는 agent session이 더 깊어지고, PR 크기와 AI-generated code survival share가 커지며, power-user 집중도가 높다는 데이터를 제시한다. 다만 정확한 게시일은 확인하지 못해 Spring 2026 공식 보고서로 표기했다.
- Torvalds 관련 The New Stack 기사는 AI가 생산성을 높이지만, 장기 유지보수 프로젝트에는 코드와 시스템 아키텍처 이해가 여전히 필요하다는 경고를 제공한다.

## 확인 불가 및 주의

- Cursor의 2026-05-31~2026-06-02 신규 공식 업데이트는 확인 불가.
- Cursor Developer Habits Report의 정확한 게시일은 확인 불가. 보고서 자체의 표기는 Spring 2026.
- GitHub Trending 총 star 수는 이번 HTML 파싱에서 안정적으로 추출되지 않아 사용하지 않았다. 기간별 star 수만 GitHub Trending 표시값으로 반영했다.
- 기사 검색은 최근 2일 분량이 낮아 7일로 확대했다.

## 출처

- OpenAI Codex changelog: https://developers.openai.com/codex/changelog/
- Claude Code changelog: https://code.claude.com/docs/en/changelog
- Cursor changelog: https://cursor.com/en-US/changelog
- GitHub Trending Daily: https://github.com/trending?since=daily
- GitHub Trending Weekly: https://github.com/trending?since=weekly
- The New Stack comparison: https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/
- XDA 30-day comparison: https://www.xda-developers.com/paid-cursor-codex-claude-code-30-days-only-one-made-faster-developer/
- Cursor Developer Habits Report: https://cursor.com/insights
- The New Stack Torvalds article: https://thenewstack.io/torvalds-ai-programming-productivity/
- Salt Security Salt Code announcement: https://salt.security/press-releases/salt-security-launches-salt-code-the-first-agentic-security-solution-to-enforce-security-policies-inside-ai-coding-assistants
