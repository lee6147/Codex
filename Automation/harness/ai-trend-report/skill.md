# AI Trend Report Harness

이 문서는 이 워크스페이스 전용 로컬 실행 하네스다.
자동화 또는 에이전트는 `codex.md`를 먼저 읽은 뒤 이 문서를 기준으로 작업을 수행한다.

## 빠른 실행 순서

1. 현재 작업 폴더 기준으로 가장 가까운 `codex.md`를 이미 읽었는지 확인한다.
2. `references/preflight.md`를 읽는다.
3. `references/output-contract.md`를 읽는다.
4. `references/source-policy.md`를 읽는다.
5. `scripts/run_preflight.py --ensure-scaffold`를 우선 실행한다.
6. 웹 리서치를 수행한다.
7. HTML 3개를 먼저 작성한다.
8. 마지막에 `04_ai_tools_review.md`를 작성한다.
9. `scripts/verify_outputs.py`로 산출물을 검증한다.

## 기본 워크플로

기본 조사 순서는 아래와 같다.

1. Claude Code, Cursor, OpenAI Codex의 최근 3일 공식 업데이트를 수집한다.
2. GitHub Trending Daily 또는 Weekly 스냅샷에서 AI 및 개발 생산성 관련 저장소를 고른다.
3. 각 도구 관련 아티클을 최근 2일 우선으로 수집하고, 부족하면 최근 7일로 넓힌다.
4. HTML 보고서 3개를 작성한다.
5. Markdown 종합 평가 파일을 작성한다.

## 로컬 병렬화

필요하면 `agents/research-lanes.md`의 세 레인으로 나눠서 조사한다.
단, 최종 파일 통합과 종합 평가는 단일 메인 흐름에서 수행한다.

## 자동화 프롬프트

용도에 따라 프롬프트를 나눠 쓴다.

- 최소형: `prompts/minimal-prompt.txt`
- 권장형: `prompts/automation-prompt.txt`
- 안전형: `prompts/safe-prompt.txt`

최소형은 가장 짧은 시작 문구만 담고, 권장형은 기본 예외 규칙까지 포함한다.
자료가 부족할 때의 확장 규칙이나 출력 위치 변경 같은 예외만 추가로 붙인다.

## 실행 스크립트

- `scripts/run_preflight.py`: 로컬 하네스 파일 존재 여부 점검, 날짜 폴더 확인, 필요 시 스캐폴드 생성
- `scripts/create_report_scaffold.py`: 날짜 폴더와 기본 파일 생성
- `scripts/verify_outputs.py`: 생성된 보고서의 기본 형식과 플레이스홀더 잔존 여부 검증
