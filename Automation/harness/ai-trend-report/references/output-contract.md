# Output Contract

## 기본 출력 폴더

지정된 출력 기준 폴더 아래에 오늘 날짜 이름의 `YYYY-MM-DD` 폴더를 만든다.
별도 지정이 없으면 현재 작업 폴더, 즉 이 워크스페이스 루트를 출력 기준 폴더로 본다.
`scripts/create_report_scaffold.py`를 직접 실행할 때는 넘긴 `base_dir`가 출력 기준 폴더다.

기본 파일:

- `01_official_tool_updates.html`
- `02_trending_github_repos.html`
- `03_ai_coding_tools_articles.html`
- `04_ai_tools_review.md`

## 01 공식 업데이트 보고서

대상:

- Claude Code
- Cursor
- OpenAI Codex, 필요 시 CLI 포함

확인 범위:

- 공식 블로그
- 릴리즈 노트
- 문서 변경 로그
- 공식 X 계정
- 필요 시 공식 GitHub 릴리즈 또는 공지

기간:

- 최근 3일

항목별 필수 정보:

- 도구명
- 기능 또는 업데이트명
- 핵심 설명
- 실사용 관점에서 중요한 이유
- 발표일
- 출처명
- 출처 URL
- 확인 상태: `확인 완료` 또는 `확인 불가`

## 02 트렌딩 GitHub 레포트

기준:

- GitHub Trending Daily 또는 Weekly 스냅샷

선정 규칙:

- 최대 10개
- AI, 코딩, 개발 생산성과 연결되는 저장소만 유지
- 억지로 개수를 채우지 않는다

항목별 필수 정보:

- 순서
- 저장소명
- GitHub URL
- 한국어 설명
- 주요 기능 또는 쓰임새
- Star 수 `조회 시점 기준`
- 지금 주목할 이유
- Claude Code, Cursor, Codex 사용자와의 연결점
- 한줄 총평

## 03 AI 코딩 도구 아티클 요약

대상:

- Claude Code
- Cursor
- OpenAI Codex

우선 출처:

- 공식 블로그
- 신뢰 가능한 기술 블로그
- dev.to
- Medium
- Substack
- 주요 기술 또는 뉴스 매체

기간:

- 최근 2일 우선
- 자료가 부족하면 최근 7일로 확장하고 보고서 상단에 명시

도구별 목표 개수:

- 2개에서 3개

항목별 필수 정보:

- 제목
- 게시일
- 작성자 또는 매체
- 출처 URL
- 3줄에서 5줄 요약
- 2줄에서 3줄 실무 시사점
- 신뢰도 메모: `공식 글`, `실사용 후기`, `비교 리뷰`, `뉴스 기사`, `광고성 강함`

## 04 종합 평가 Markdown

형식:

- Obsidian 호환 Markdown
- 한국어

필수 섹션:

- 개요
- 도구별 평가
- 도구 간 비교
- 추천 사용자 유형
- 이번 주 총평
- 다음 주 체크포인트

도구별 평가 항목:

- 강점
- 약점
- 추천 사용 시나리오
- 피해야 할 사용 시나리오
- 최근 업데이트 반영 관점
- 현재 시점 총평

비교 항목:

- 자동화 및 에이전트 작업 적합성
- 코드 작성 및 수정 능력
- 대규모 저장소 탐색 적합성
- CLI 활용성
- 초보자, 중급자, 고급자 적합성
- 가격 대비 체감 가치, 확인 가능할 때만

필수 링크:

- `[[01_official_tool_updates]]`
- `[[02_trending_github_repos]]`
- `[[03_ai_coding_tools_articles]]`

참고:

- Markdown 안의 위키링크는 확장자 없이 유지한다.
- 실제 HTML 산출물 파일명은 위 목록의 `.html` 파일명을 따른다.
