# AI 코딩 도구 종합 평가 - 2026-06-07

#AI트렌드 #ClaudeCode #Cursor #Codex #개발생산성

> 이 문서는 [[01_official_tool_updates]], [[02_trending_github_repos]], [[03_ai_coding_tools_articles]] 내용을 종합한 Obsidian 호환 리뷰다. 실제 HTML 산출물은 `01_official_tool_updates.html`, `02_trending_github_repos.html`, `03_ai_coding_tools_articles.html`이다.

## 개요

- 공식 업데이트 기준으로는 Claude Code 2.1.166/167/168, Cursor 3.7, OpenAI Codex 0.138.0-alpha 계열 및 Codex 역할별 플러그인/Sites 흐름이 핵심이다.
- 기사 수집은 최근 2일 우선 기준으로는 도구별 물량이 부족해 최근 7일(2026-06-01부터 2026-06-07까지)로 확장했다.
- 이번 주 흐름은 모델 성능보다 agent 운영, 권한, 공유, 검토 피로, UI/voice 피드백, reusable skills/memory에 집중된다.

## 도구별 평가

### Claude Code

**강점**

- 2026-06-06의 2.1.166에서 fallback 모델, deny-rule glob, cross-session messaging 권한 하드닝, thinking 제어, remote/session 안정화가 명확히 확인됐다.
- 2026-06-05의 2.1.165는 세부 공개가 적지만, 2.1.162~2.1.166 흐름 전체가 permission rule, managed settings, background agent, headless 실행 안정화에 집중돼 있다.

**약점**

- 릴리스가 빠르고 세부 기능이 운영 정책과 맞물려 있어 조직 배포에서는 버전 고정과 변경 영향 추적이 필요하다.
- “bug fixes and reliability improvements”만 공개된 릴리스는 세부 영향이 확인 불가다.

**추천 사용 시나리오**

- 복잡한 repo 작업, background/subagent 병렬 작업, 권한 규칙이 중요한 장기 작업에 적합하다.
- CI/headless `claude -p`와 managed settings를 쓰는 팀은 최신 릴리스 전후로 별도 smoke test를 둬야 한다.

**피해야 할 사용 시나리오**

- 조직 권한 정책 없이 auto mode를 넓게 켜고 shell/config 파일 쓰기를 맡기는 방식은 피해야 한다.

**현재 총평**

Claude Code는 agent runtime을 더 오래 안정적으로 돌리기 위한 보안·운영 레이어를 빠르게 보강 중이다.

### Cursor

**강점**

- Cursor 3.7은 Design Mode에서 클릭, 드로잉, voice input, multi-select를 통해 UI 수정 의도를 더 구조화한다.
- Canvas context usage report와 SDK 흐름은 agent가 무엇을 소비했고 어디에 토큰을 쓰는지 검토하는 데 도움이 된다.

**약점**

- shared canvas와 embedded prompt button은 새로운 권한/오용 표면이다.
- Design Mode는 frontend review에는 강하지만, backend side effect나 production merge 안전성은 여전히 CI와 branch protection에 의존한다.

**추천 사용 시나리오**

- UI/대시보드/내부 도구를 agent와 반복 수정하는 팀, 디자인 리뷰가 잦은 frontend 팀에 적합하다.

**피해야 할 사용 시나리오**

- shared canvas 권한, prompt button 검토, branch protection 없이 production-connected 작업을 맡기는 방식은 피해야 한다.

**현재 총평**

Cursor는 “IDE 안 agent”에서 “시각적 리뷰를 agent 지시로 변환하는 도구”로 진화하고 있다.

### OpenAI Codex

**강점**

- OpenAI 공식 발표에 따르면 Codex는 주간 500만 명 이상이 사용하고, 비개발자 지식근로자가 약 20%를 차지한다.
- 역할별 플러그인, 62개 앱, 110개 skills, Sites preview, annotations는 Codex를 코드 작성 밖의 업무 실행기로 확장한다.
- GitHub Releases에서는 2026-06-04부터 2026-06-06까지 0.138.0-alpha 계열 배포가 확인된다.

**약점**

- alpha 릴리스의 세부 변경은 GitHub 페이지 로딩 문제로 일부 확인 불가다.
- 역할별 플러그인과 Sites는 공유, RBAC, app permission, 데이터 출처 관리가 정리되지 않으면 governance 부담이 커진다.

**추천 사용 시나리오**

- 코드 변경과 함께 보고서, 대시보드, prototype, 분석 artifact까지 생성해야 하는 cross-functional 작업에 적합하다.

**피해야 할 사용 시나리오**

- plugin sharing과 Sites 공개 범위를 정하지 않은 상태에서 민감 데이터가 들어간 업무 자동화를 공유하는 방식은 피해야 한다.

**현재 총평**

Codex는 AI 코딩 도구에서 업무 운영 플랫폼으로 확장 중이며, 개발팀은 기능보다 권한·공유·검토 체계를 먼저 봐야 한다.

## 도구 간 비교

| 항목 | Claude Code | Cursor | OpenAI Codex |
| --- | --- | --- | --- |
| 이번 주 핵심 | runtime 안정성, fallback, 권한 하드닝 | Design Mode, Canvas, SDK agent UX | role plugins, Sites, knowledge-work 확장 |
| 가장 강한 사용처 | repo 단위 장기 agent 작업 | UI/Canvas 중심 반복 수정 | 코드+문서+대시보드 통합 산출물 |
| 운영 리스크 | 빠른 릴리스와 권한 정책 변화 | shared canvas와 prompt button | plugin/Sites 권한과 데이터 공유 |
| 검토 포인트 | version pin, managed settings, headless smoke test | canvas sharing, CI gate, branch protection | RBAC, app permissions, Sites publishing |

## 추천 사용자 유형

- **대규모 코드베이스 자동화 팀**: Claude Code를 우선 검토하되, managed settings와 fallback 정책을 문서화한다.
- **frontend/product engineering 팀**: Cursor 3.7 Design Mode를 staging repo에서 먼저 써보고, shared canvas 권한을 제한한다.
- **분석·문서·prototype까지 묶는 팀**: Codex role plugins와 Sites를 검토하되, workspace 권한과 공유 정책을 먼저 설계한다.
- **로컬 자동화/리서치 팀**: GitHub Trending의 `last30days-skill`, `superpowers`, `mempalace`, `Agent-Reach` 같은 보조 도구를 검토하되 출처 검증과 보안 경계를 별도 유지한다.

## 이번 주 총평

AI 코딩 도구 경쟁은 “누가 더 많은 코드를 쓰는가”에서 “누가 agent workstream을 안전하게 오래 굴리고, 결과물을 검토 가능한 형태로 공유하게 하는가”로 이동하고 있다. Claude Code는 runtime과 권한 안전장치를 강화하고, Cursor는 시각적 피드백을 agent 입력으로 바꾸며, Codex는 coding 밖 지식 작업까지 표면을 넓힌다.

## 주요 트렌드 관찰

1. Agent 운영 보조재가 강하다. GitHub Trending에서 research skill, memory, generative UI, skill framework가 부상했다.
2. Human-in-the-loop의 형태가 바뀐다. code review뿐 아니라 canvas review, voice instruction, context usage report가 중요해진다.
3. 권한과 공유가 핵심 병목이다. plugin sharing, Sites, shared canvas, cross-session messaging은 생산성 기능인 동시에 보안 표면이다.
4. 기사 물량은 최근 2일 기준으로 충분하지 않아, 2026-06-01부터 2026-06-07까지 7일로 확장해 판단했다.

## 다음 주 체크포인트

- Claude Code 2.1.166 이후 fallbackModel과 cross-session 권한 하드닝이 실제 운영 이슈를 줄이는지 확인한다.
- Cursor 3.7 Design Mode가 cloud agents, Auto-review, shared canvas 권한 모델과 어떻게 결합되는지 추적한다.
- OpenAI Codex 0.138.0-alpha 계열이 stable로 올라오며 세부 릴리스 노트를 공개하는지 확인한다.
- Codex Sites와 role-specific plugins의 Enterprise/Edu 기본값, RBAC, plugin sharing 정책 변화를 계속 확인한다.
- GitHub Trending의 agent memory/skills/research 저장소가 실제 coding workflow plugin으로 채택되는지 본다.

## 출처 메모

- Claude Code changelog: https://code.claude.com/docs/en/changelog
- Cursor changelog: https://cursor.com/en-US/changelog
- OpenAI Codex product post: https://openai.com/index/codex-for-every-role-tool-workflow/
- OpenAI knowledge work post: https://openai.com/index/codex-for-knowledge-work/
- OpenAI Enterprise/Edu release notes: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-%CF%83%CE%B7%CE%BC%CE%B5%CE%B9%CF%8E%CF%83%CE%B5%CE%B9%CF%82-%CE%AD%CE%BA%CE%B4%CE%BF%CF%83%CE%B5%CE%B9%CF%82
- OpenAI Codex GitHub releases: https://github.com/openai/codex/releases
- GitHub Trending: https://github.com/trending
- Axios Codex article: https://www.axios.com/2026/06/02/openai-codex-knowledge-workers
- Production AI Institute Cursor assessment: https://www.productionai.institute/insights/cursor-canvas-3-7-psf-assessment-2026
- DevelopersIO Claude Code update article: https://dev.classmethod.jp/en/articles/20260603-cc-updates-v2-1-165/
