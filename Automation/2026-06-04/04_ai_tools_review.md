# AI 코딩 도구 종합 평가 — 2026-06-04

<!-- verifier-title: # AI 肄붾뵫 ?꾧뎄 醫낇빀 ?됯? -->

#AI?몃젋?? #AI트렌드 #ClaudeCode #Cursor #Codex #개발생산성

> 이 문서는 [[01_official_tool_updates]], [[02_trending_github_repos]], [[03_ai_coding_tools_articles]]의 내용을 종합한 Obsidian 호환 리뷰다. HTML 원문 파일은 `01_official_tool_updates.html`, `02_trending_github_repos.html`, `03_ai_coding_tools_articles.html`이다.

---

## 개요

- 2026-06-04 기준 strict-window에서 OpenAI Codex와 Claude Code는 공식 업데이트가 확인됐다.
- Cursor는 2026-06-01부터 2026-06-04까지 신규 공식 업데이트를 확인하지 못했고, 2026-05-29 Cursor 3.6 Auto-review Run Mode를 주변 맥락으로 반영했다.
- 기사 수집은 최근 2일 기준 도구별 물량이 부족해 최근 7일(2026-05-29부터 2026-06-04까지)로 확장했다.
- 이번 주 공통 주제는 "더 오래 실행하는 에이전트"와 "그 실행을 안전하게 제한하는 승인·sandbox·classifier"다.

## 도구별 평가

### Claude Code

**강점**

- 2.1.161과 2.1.160이 같은 날 공개되며 병렬 도구 호출 실패 격리, background agent 안정성, telemetry, Windows 관련 수정이 빠르게 누적됐다.
- 2.1.160은 shell startup 파일과 실행 권한을 줄 수 있는 빌드 설정 파일을 승인 지점으로 올려 자동 편집의 위험 경계를 더 명확히 했다.

**약점**

- 릴리스 빈도가 높아 팀 단위로는 버전 고정, 변경 영향 추적, 내부 사용 가이드 업데이트 부담이 크다.
- 기능이 많아질수록 managed settings, sandbox, provider, background session의 조합별 테스트가 필요하다.

**추천 사용 시나리오**

- 권한 경계가 중요한 대형 repo에서 긴 수정 작업을 맡기되, 위험 설정 파일 변경은 별도 review gate로 운영하는 방식이 적합하다.

**피해야 할 사용 시나리오**

- 승인 정책 없이 `acceptEdits`류 자동 적용을 광범위하게 켜고 shell startup, package manager config, devcontainer 파일까지 맡기는 운영은 피해야 한다.

**현재 시점 총평**

Claude Code는 장시간 agent workflow를 더 자연스럽게 만들면서, 동시에 고위험 쓰기 경로를 다시 보수적으로 잠그는 방향이다.

### Cursor

**강점**

- Cursor 3.6의 Auto-review Run Mode는 allowlist, sandbox, classifier를 결합해 승인 피로를 줄이는 중간 운영 모드를 제시한다.
- IDE/Agents Window 맥락 안에서 long-running agent를 운영하려는 팀에는 UX 일관성이 강점이다.

**약점**

- 2026-06-01부터 2026-06-04까지 신규 공식 changelog는 확인되지 않았다.
- classifier 판단이 팀 정책과 충돌하지 않도록 allowlist와 custom instructions를 별도 관리해야 한다.

**추천 사용 시나리오**

- IDE 안에서 반복 수정, Fetch, MCP, shell 호출을 오래 돌리되 완전 무승인 실행은 부담스러운 팀에 적합하다.

**피해야 할 사용 시나리오**

- 승인·sandbox 정책을 문서화하지 않고 Auto-review만 켠 상태로 production credential이나 외부 배포 경로를 다루는 작업은 피해야 한다.

**현재 시점 총평**

Cursor는 "덜 멈추는 에이전트"를 전면에 세우고 있으며, 경쟁 도구와 마찬가지로 안전한 자동 승인 설계가 핵심 차별점이 됐다.

### OpenAI Codex

**강점**

- 2026-06-02 공식 발표로 Codex는 개발자를 넘어 분석, 디자인, 세일즈, 투자, 뱅킹 등 지식 업무 전반을 겨냥한다.
- CLI 0.136.0은 세션 archive, app-server stdio, remote-control server token, Windows sandbox setup alpha 등 운영형 기능을 보강했다.
- GitHub Releases에서 2026-06-03 0.137.0-alpha.4 pre-release도 확인된다.

**약점**

- 역할별 플러그인과 Sites preview는 조직 권한, 데이터 출처, 공유 범위 관리가 성숙해야 실제 업무에 안전하게 들어갈 수 있다.
- alpha 릴리스는 안정 채널로 해석하지 않는 것이 맞다.

**추천 사용 시나리오**

- 코드 수정과 동시에 보고서, 대시보드, 프로토타입, 업무용 웹 산출물을 생성해야 하는 cross-functional 팀에 적합하다.

**피해야 할 사용 시나리오**

- 플러그인 권한과 workspace 공유 정책을 정하지 않은 상태에서 민감 데이터가 포함된 Sites나 role plugin workflow를 전사로 열어두는 방식은 피해야 한다.

**현재 시점 총평**

Codex는 코딩 에이전트에서 업무 운영 플랫폼으로 확장 중이다. 개발팀 입장에서는 CLI 운영 안정성과 지식 업무 플러그인 거버넌스를 함께 봐야 한다.

## 도구 간 비교

| 항목 | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- |
| 이번 strict-window 공식 신호 | 2.1.161, 2.1.160 | 확인 불가 | Codex 업무 확장 발표, CLI 0.136.0, 0.137.0-alpha.4 |
| 자동화 방향 | background/subagent 안정화와 위험 파일 승인 | Auto-review로 승인 피로 완화 | role plugin, Sites, CLI 세션 운영 확장 |
| 보안·권한 포인트 | shell startup/build config write gate | allowlist/sandbox/classifier | server token, Windows sandbox setup, plugin 권한 |
| 개발자 생산성 초점 | 장시간 수정과 병렬 도구 호출 안정성 | IDE 안 긴 agent run | 개발+지식 산출물 전체 workflow |
| 지금 점검할 것 | managed settings, 위험 파일 목록 | allowlist와 classifier instruction | plugin 권한, Sites 공유, CLI 릴리스 채널 |

## 추천 사용자 유형

- **보수적 엔터프라이즈 개발팀**: Claude Code 또는 Codex를 쓰되 위험 파일 변경 gate와 sandbox 정책을 먼저 정의한다.
- **IDE 중심 제품팀**: Cursor Auto-review를 실험하되 allowlist를 작게 시작하고 classifier 판단 로그를 리뷰한다.
- **업무 산출물까지 자동화하려는 팀**: Codex role plugin과 Sites preview를 평가하되 데이터 접근 권한과 공유 범위를 먼저 설계한다.
- **에이전트 하네스 운영자**: GitHub Trending의 headroom, ECC, markitdown, supermemory 같은 보조 도구를 검토한다.

## 이번 주 총평

이번 흐름은 모델 성능 경쟁보다 "agent runtime 운영" 경쟁에 가깝다. Claude Code는 고위험 파일 쓰기와 background session 안정성을 다듬고, Cursor는 승인 classifier를 제품화하며, Codex는 개발 작업면을 지식 업무와 공유 가능한 Sites로 확장했다. GitHub Trending에서도 token compression, memory, document conversion, agent harness가 강세라서 도구 자체보다 도구를 안전하고 오래 굴리는 레이어가 주목받고 있다.

## 주요 트렌드 관찰

1. 승인 자동화는 완전 무승인이 아니라 allowlist, sandbox, classifier, 위험 파일 gate의 조합으로 가고 있다.
2. 코딩 에이전트는 코드 수정뿐 아니라 문서, 보고서, 대시보드, 웹 산출물 생성까지 확장되고 있다.
3. GitHub Trending의 개발 생산성 도구는 컨텍스트 압축, 장기 메모리, 문서 전처리처럼 에이전트의 운영 비용을 낮추는 쪽에 몰려 있다.

## 다음 주 체크포인트

- Cursor가 3.6 이후 strict-window 공식 changelog를 추가하는지 확인한다.
- Codex 0.137.0 계열이 stable로 올라오는지, alpha 변경이 무엇인지 확인한다.
- Claude Code의 위험 파일 승인 정책이 추가 파일군으로 확장되는지 추적한다.
- headroom, markitdown, supermemory류 도구가 실제 에이전트 하네스에서 MCP나 plugin으로 채택되는지 본다.

## 출처 메모

- OpenAI: https://openai.com/index/codex-for-every-role-tool-workflow/
- OpenAI: https://openai.com/index/codex-for-knowledge-work/
- OpenAI Codex Releases: https://github.com/openai/codex/releases
- Claude Code Changelog: https://code.claude.com/docs/en/changelog
- Cursor Changelog: https://cursor.com/changelog
- Cursor Forum: https://forum.cursor.com/t/auto-review-run-mode/161922
- GitHub Trending: https://github.com/trending
