# Workspace Guidance

이 워크스페이스는 AI 에이전트가 정보 수집·분석·보고서 생성을 자동으로 수행하는 공간이다.
코드 애플리케이션이 아니라 **운영 절차, 프롬프트, 산출물 아카이브**로 구성되어 있다.

---

## 워크스페이스 구조

```
Codex/
├── Automation/          # AI 트렌드 리포트 자동화 하네스
│   ├── codex.md         # 자동화 실행 계약서 (최우선 읽기)
│   ├── YYYY-MM-DD/      # 날짜별 산출물
│   └── harness/         # 실행 흐름, 프롬프트, 스크립트, 참조 문서
└── youtube-transcript-team/
    ├── prompts/         # 역할별 에이전트 프롬프트
    ├── analyses/        # 영상별 분석 결과 아카이브
    └── *.md             # 템플릿, 모드 정의, 골든 예시
```

---

## Git / Worktree 규칙

- `C:\Users\user\Desktop\Codex`가 `main` 브랜치의 기본 워크트리다.
- 대규모 병렬 작업, 위험한 편집, 브랜치 격리 실험에는 별도 워크트리를 생성한다.
- 워크트리마다 다른 브랜치를 사용한다.
- 보조 워크트리가 이미 존재한다고 가정하지 않는다. 먼저 확인한다.
- 사용자 대상 분석 산출물은 별도 요청이 없는 한 메인 워크스페이스에 보관한다.

---

## Automation 규칙

### 실행 순서

에이전트는 자동화 작업을 시작하기 전에 반드시 아래 순서를 따른다.

1. `Automation/codex.md`를 읽는다.
2. `Automation/harness/ai-trend-report/skill.md`를 읽는다.
3. 필요 시 `Automation/harness/ai-trend-report/references/` 아래 문서를 순서대로 읽는다(`preflight.md`, `output-contract.md`, `source-policy.md`).
4. 프리플라이트 실행: `Automation/`을 작업 디렉터리로 두고 `python harness/ai-trend-report/scripts/run_preflight.py --ensure-scaffold`를 실행한다. 레포 루트에서 돌릴 때는 `python Automation/harness/ai-trend-report/scripts/run_preflight.py --ensure-scaffold`로 동일하다.
5. 그 다음에만 리서치와 파일 생성을 시작한다.

### 산출물

- 기본 출력 위치는 `Automation/YYYY-MM-DD/`다(프리플라이트 기본값과 동일).
- HTML 3개 + Markdown 1개를 생성한다.
- HTML은 한국어 단일 파일, 링크 가능한 출처를 포함한다.
- Markdown은 Obsidian 호환으로 작성한다.
- 작업 종료 전에 검증한다. `Automation/`에서 실행할 때: `python harness/ai-trend-report/scripts/verify_outputs.py`. 레포 루트에서 실행할 때는 출력 기준을 넘긴다: `python Automation/harness/ai-trend-report/scripts/verify_outputs.py --output-base-dir Automation`.

### 리서치 원칙

- 확인된 출처만 사용한다.
- 최신 정보는 반드시 실제 조회로 검증한다.
- 추측, 과장, 광고성 표현을 피한다.
- 확인 불가능한 내용은 `확인 불가`로 표시한다.
- 상대 날짜 대신 `YYYY-MM-DD` 형식을 사용한다.

---

## YouTube Transcript Team 규칙

### 분석 저장

- `youtube-transcript-team/analyses/` 아래에 영상별 폴더를 생성한다.
- 폴더 이름: `YYYY-MM-DD__channel__video-slug`
- 기본 파일: `00-intake.md`, `01-analysis.md`, `02-followup.md`
- 원문 스크립트가 길면 `transcript/` 하위 폴더에 파트별로 분할 저장한다.

### 분석 모드

- **풀 분석**: `youtube-transcript-team/paste-template.md` + `youtube-transcript-team/prompts/orchestrator.md` 사용
- **압축 모드**: `youtube-transcript-team/quick-template.md` + `youtube-transcript-team/quick-mode.md` 사용
- 짧은 영상이나 정보 밀도가 낮은 영상은 3인 체제(Summary, Watchworthiness, Action)로 충분하다.

### 에이전트 팀 구성

기본 4인 팀: Summary Analyst, Watchworthiness Judge, Practicality Evaluator, Action Curator

보조 역할 추가 조건:
- 최신 기능/가격/정책이 핵심이면 → Fact Checker
- 자극적이거나 판매성이 강하면 → Skeptic Reviewer
- 중복 제거가 중요하면 → Novelty Detector
- 시리즈형 학습이면 → Companion Recommender

---

## 공통 규칙

- 이 워크스페이스에서는 전역 설정보다 로컬 하네스 파일(`codex.md`, `skill.md`)을 우선한다.
- 새 자동화 유형을 추가할 때는 `Automation/harness/` 아래에 독립 하네스를 만든다.
- 모든 산출물에는 생성 날짜, 출처, 확인 상태를 명시한다.
