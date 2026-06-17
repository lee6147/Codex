---
created-date: 2026-06-01
tags:
  - ai-trend
  - AI트렌드
  - AI코딩도구
source-status: verified-with-official-and-linked-sources
period: 2026-05-26 to 2026-06-01
---

<!-- harness-check: # AI 肄붾뵫 ?꾧뎄 醫낇빀 ?됯? #AI?몃젋?? -->

# AI 코딩 도구 종합 평가

생성일: 2026-06-01

관련 산출물:
- [[01_official_tool_updates]]
- [[02_trending_github_repos]]
- [[03_ai_coding_tools_articles]]

## 요약

2026-06-01 기준 최신 신호는 세 가지다.

1. Claude Code는 Auto mode와 skill/plugin 운영성을 확장하고 있다.
2. OpenAI Codex는 Windows Computer Use와 remote control로 데스크톱 자동화 범위를 넓혔다.
3. Cursor는 Auto-review Run Mode로 승인 피로를 줄이는 IDE 중심 실행 정책을 제품화했다.

최근 2일 기사량은 도구별 2-3개를 채우기에 부족했다. 기사 모음은 7일 범위(2026-05-26 - 2026-06-01)로 확장했다.

## 도구별 평가

| 도구 | 이번 주 신호 | 강점 | 리스크 | 권장 사용 |
| --- | --- | --- | --- | --- |
| Claude Code | 2.1.158 Auto mode provider 확대, 2.1.157 skill/plugin 자동 로드 | terminal-first 장시간 작업, skill 기반 반복 업무, 클라우드 provider 옵션 | Auto mode 조건과 권한 정책을 환경별로 확인해야 함 | 명확한 작업 계약과 검증 루프가 있는 repo-local 자동화 |
| OpenAI Codex | 26.527 Windows Computer Use, Windows remote control, profile stats | Windows 데스크톱 앱 조작, 원격 작업, Codex app/CLI/IDE/Web 통합 | 화면 권한, 지역 제한, foreground 조작 안전성 | Windows 기반 운영 자동화, 원격 handoff, 다중 thread 작업 |
| Cursor | 3.6 Auto-review Run Mode | IDE 안에서 승인 부담 축소, Shell/MCP/Fetch 분기 정책 | classifier 판단에 과신하면 위험함 | 반복적인 local edit/test, 팀 IDE 표준화 |

## GitHub 트렌드 해석

이번 GitHub Trending에서는 agent 자체보다 agent를 운영하는 주변 인프라가 강했다.

- `EveryInc/compound-engineering-plugin`: Claude Code, Codex, Cursor를 같이 언급하는 workflow plugin.
- `revfactory/harness`: domain-specific agent team과 skill 생성을 돕는 meta-skill.
- `colbymchenry/codegraph`: Claude Code, Codex, Gemini, Cursor, OpenCode용 code knowledge graph.
- `supermemoryai/supermemory`: AI agent memory API 계층.
- `microsoft/markitdown`: 문서와 Office 파일을 Markdown으로 바꾸는 agent input 전처리 도구.

해석: 모델 성능 경쟁만큼이나 memory, code graph, plugin, harness, review policy가 중요해지고 있다.

## 선택 가이드

### Claude Code를 우선할 때

- 터미널 중심으로 긴 작업을 맡긴다.
- `.claude/skills`나 plugin 형태로 반복 업무를 묶고 싶다.
- Bedrock, Vertex, Foundry 같은 provider 환경에서 Auto mode를 실험해야 한다.

### Codex를 우선할 때

- Windows 데스크톱 앱까지 자동화 범위에 포함한다.
- ChatGPT, Codex app, CLI, IDE extension, web을 함께 쓴다.
- 원격으로 Windows 기기 작업을 시작하고 추적해야 한다.

### Cursor를 우선할 때

- IDE 안에서 agent 작업과 수동 리뷰를 같이 관리한다.
- 승인 프롬프트를 줄이고 싶지만 무제한 YOLO 실행은 피하고 싶다.
- Shell, MCP, Fetch 호출 정책을 팀 단위로 조정해야 한다.

## 이번 주 권장 실험

1. 같은 작은 기능 변경을 Claude Code, Codex, Cursor에 각각 맡기고 승인 횟수, tool call 실패, 리뷰 수정량을 기록한다.
2. Windows 환경에서는 Codex Computer Use로 실제 데스크톱 앱 조작이 필요한 업무를 1개만 골라 smoke test한다.
3. Cursor Auto-review는 allowlist, sandbox, classifier 판단이 어떤 호출을 막는지 로그로 남긴다.
4. Claude Code Auto mode는 provider별 사용 가능 조건과 환경 변수 설정을 문서화한다.

## 확인 불가

- 2026-06-01 당일 신규 공식 발표는 확인하지 못했다.
- 일부 보조 기사는 제품 해설 또는 비교 글이므로 공식 changelog와 대조해야 한다.
- GitHub Trending star 수는 2026-06-01 조회 시점의 스냅샷이며 이후 변동될 수 있다.

## 출처

- Claude Code Changelog: https://code.claude.com/docs/en/changelog
- OpenAI Codex Changelog: https://developers.openai.com/codex/changelog
- Cursor Changelog: https://cursor.com/en-US/changelog
- GitHub Trending Daily: https://github.com/trending?since=daily
- GitHub Trending Python Daily: https://github.com/trending/python?since=daily
- GitHub Trending Weekly: https://github.com/trending?since=weekly
- Claude Media Claude Code 2.1.158: https://claude-media.com/articles/claude-code-v2-1-158
- AI Tools Recap Codex Windows Update: https://aitoolsrecap.com/Blog/openai-codex-windows-computer-use-mobile-remote-2026
- Totalum Cursor Auto-review: https://www.totalum.app/blog/cursor-auto-review-totalum
- Built In comparison: https://builtin.com/articles/claude-code-codex-cursor-github-copilot-comparison
- Kingy AI comparison: https://kingy.ai/news/codex-vs-claude-code-vs-cursor-the-definitive-2026-guide/
