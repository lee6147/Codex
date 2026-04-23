# Codex Automation Contract

이 워크스페이스는 Codex 자동화 전용 로컬 하네스다.
자동화는 실제 작업을 시작하기 전에 반드시 이 파일을 먼저 읽고, 아래 순서대로 로컬 규칙을 적용한다.

## 필수 시작 순서

1. 현재 작업 폴더에서 가장 가까운 `codex.md`를 읽는다.
2. `harness/ai-trend-report/skill.md`를 읽는다.
3. 필요 시 아래 참고 문서를 순서대로 읽는다.
   - `harness/ai-trend-report/references/preflight.md`
   - `harness/ai-trend-report/references/output-contract.md`
   - `harness/ai-trend-report/references/presentation-style.md`
   - `harness/ai-trend-report/references/source-policy.md`
4. 가능하면 `harness/ai-trend-report/scripts/run_preflight.py --ensure-scaffold`를 먼저 실행한다.
5. 그 다음에만 계획, 웹 리서치, 파일 생성을 시작한다.

## 기본 목적

이 워크스페이스의 기본 자동화 목적은 AI 코딩 도구 및 개발 생산성 트렌드를 조사하고, 날짜별 보고서를 생성하는 것이다.

기본 대상:

- Claude Code
- Cursor
- OpenAI Codex
- AI 개발 생산성과 직접 연결되는 GitHub Trending 및 관련 기사

## 로컬 하네스 규칙

- 이 워크스페이스에서는 전역 skill 대신 로컬 하네스 파일을 기준으로 동작한다.
- 긴 규칙을 자동화 프롬프트에 반복해서 쓰지 말고, 이 파일과 `harness/ai-trend-report/` 아래 문서를 기준으로 실행한다.
- 자동화 프롬프트에는 날짜 범위, 예외, 출력 위치 같은 가변 조건만 남긴다.
- 날짜 폴더와 기본 파일 스캐폴드는 `harness/ai-trend-report/scripts/create_report_scaffold.py`를 사용한다.
- 시작 전 점검은 `harness/ai-trend-report/scripts/run_preflight.py`를 사용한다.
- 종료 전 검증은 `harness/ai-trend-report/scripts/verify_outputs.py`를 사용한다.

## 문서 역할

- `codex.md`: 시작 순서, 로컬 하네스 우선순위, 최종 보고 방식의 기준 문서
- `harness/ai-trend-report/skill.md`: 실행 흐름과 프롬프트 사용 방식
- `harness/ai-trend-report/references/output-contract.md`: 산출물 형식과 파일별 필수 항목
- `harness/ai-trend-report/references/presentation-style.md`: 화면 구성, 정보 밀도, 스캔 가능성 기준
- `harness/ai-trend-report/references/source-policy.md`: 출처, 검증, 기간 확장 규칙

문서 간 표현이 다를 때는 위 역할에 따라 해석한다.

## 리서치 규칙

- 확인된 출처만 사용한다.
- 최신 정보, 최근 업데이트, 가격, 정책, 릴리즈 정보는 반드시 실제 조회로 검증한다.
- 공식 출처가 있으면 공식 출처를 우선한다.
- 추측, 과장, 광고성 표현을 피한다.
- 확인이 불가능한 내용은 `확인 불가`로 표시한다.
- 상대 날짜 표현 대신 실제 날짜를 `YYYY-MM-DD` 형식으로 적는다.
- 같은 사건을 여러 출처가 반복 보도하면 가장 정보량이 높은 대표 출처 위주로 정리한다.

## 기본 산출물 계약

별도 지시가 없으면 오늘 날짜 기준 `YYYY-MM-DD` 폴더를 만들고 아래 파일을 생성한다.

- `01_official_tool_updates.html`
- `02_trending_github_repos.html`
- `03_ai_coding_tools_articles.html`
- `04_ai_tools_review.md`

세 HTML 파일은 모두 한국어 단일 파일 문서로 작성하고, 링크 가능한 출처를 포함한다.
Markdown 파일은 Obsidian 호환으로 작성한다.
형식만 맞추는 평면적인 표 문서보다, 요약 박스, 카드형 섹션, 배지, 분명한 헤더 구조를 우선한다.

## 병렬 작업

필요하면 다음 세 레인으로 병렬화할 수 있다.

- 공식 업데이트 조사
- GitHub Trending 조사
- 기사 수집 및 요약

세 레인의 책임 분리는 `harness/ai-trend-report/agents/research-lanes.md`를 따른다.
최종 통합과 종합 평가는 메인 실행 흐름에서 수행한다.

## 권장 자동화 프롬프트

자동화 설정에는 아래 문구를 기본형으로 사용한다.
더 짧거나 더 보수적인 문구가 필요하면 `harness/ai-trend-report/prompts/` 아래 변형을 사용한다.

`Read codex.md first. Run the local AI trend report harness preflight in this workspace, then create today's report set and verify the outputs at the end. Follow the local presentation-style guide so the reports are easy to scan: strong header, top summary box, card-style sections, and readable Markdown. If article volume is low, widen article search to 7 days and state that clearly.`

## 최종 보고 방식

작업이 끝나면 최소한 아래를 분명히 남긴다.

- 생성한 폴더 경로
- 생성한 파일 목록
- 확인 불가 항목
- 자료 부족 또는 기간 확장 여부

가능하면 최종 보고 전에 `harness/ai-trend-report/scripts/verify_outputs.py`를 실행해 결과를 확인한다.

