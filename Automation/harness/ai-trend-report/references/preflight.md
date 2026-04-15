# Preflight

실제 조사와 작성 전에 아래를 확인한다.

## 읽기 순서

1. 워크스페이스 루트의 `codex.md`
2. `harness/ai-trend-report/skill.md`
3. 이 폴더의 `output-contract.md`
4. 이 폴더의 `source-policy.md`

## 작업 폴더 원칙

- 현재 자동화의 작업 폴더를 기준으로 가장 가까운 `codex.md`를 우선한다.
- 이 워크스페이스에서는 로컬 하네스 문서를 전역 skill보다 우선한다.

## 시작 전 확인

- 오늘 날짜 기준 출력 폴더가 이미 있는지 확인한다.
- 가능하면 `scripts/run_preflight.py --ensure-scaffold`를 먼저 실행한다.
- 없으면 `scripts/create_report_scaffold.py`로 생성한다.
- 최신성이 중요한 정보는 브라우징으로 검증한다.
