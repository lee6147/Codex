# Codex — AI Agent 기반 개인 생산성 자동화 워크스페이스

코드를 짜는 레포지토리가 아니다.
AI 코딩 에이전트(OpenAI Codex, Claude Code, Cursor)를 **도구가 아닌 동료**로 활용해서,
정보 수집 · 분석 · 판단을 자동화하는 **운영 체계와 산출물 아카이브**다.

---

## 이 레포가 하는 일

### 1. AI 코딩 도구 트렌드 리포트 자동화

> `Automation/`

Claude Code, Cursor, OpenAI Codex의 최신 동향을 매일 자동으로 조사하고 보고서를 생성한다.

- **공식 업데이트** — 릴리즈 노트, 블로그, 공식 X 계정에서 최근 3일 변경사항 수집
- **GitHub Trending** — AI·개발 생산성 관련 저장소를 선별하고 한국어로 정리
- **기사 수집** — dev.to, Medium, Substack 등에서 실무 시사점 중심으로 요약
- **종합 평가** — 도구별 강점/약점 비교, 추천 사용자 유형, 다음 주 체크포인트까지 포함

산출물은 기본적으로 **`Automation/YYYY-MM-DD/`** 아래에 둔다(프리플라이트 스크립트의 출력 기준 디렉터리가 `Automation/`). HTML 3개 + Obsidian 호환 Markdown 1개다.

```
Automation/2026-04-15/
├── 01_official_tool_updates.html
├── 02_trending_github_repos.html
├── 03_ai_coding_tools_articles.html
└── 04_ai_tools_review.md
```

실행은 Python 스크립트로 프리플라이트 → 스캐폴드 생성 → 리서치 → 검증까지 자동화되어 있다.

### 2. 유튜브 트랜스크립트 에이전트 팀

> `youtube-transcript-team/`

긴 영상을 직접 보지 않고, 에이전트 팀이 스크립트를 분석해서 핵심만 뽑아준다.

| 에이전트 | 역할 |
|---------|------|
| Summary Analyst | 핵심 주장 압축, 실속 없는 부분 분리 |
| Watchworthiness Judge | 시간 투자해서 볼 가치가 있는지 판정 |
| Novelty Detector | 이미 흔한 이야기인지, 새로운 관점이 있는지 구분 |
| Action Curator | 당장 해볼 수 있는 액션만 추출 |
| Practicality Evaluator | 실제 업무 적용 가능성 판정 |
| Fact Checker | 빨리 바뀌는 정보(가격, 정책, 모델명) 검증 표시 |
| Skeptic Reviewer | 과장, 홍보성 주장, 근거 없는 수치 의심 |
| Companion Recommender | 같이 보면 좋은 영상 유형 추천 |

분석 결과는 영상별 폴더에 `intake → analysis → followup` 구조로 저장된다.

```
youtube-transcript-team/analyses/
└── 2026-04-15__chase-ai__seven-levels-of-claude-code-and-rag/
    ├── 00-intake.md
    ├── 01-analysis.md
    ├── 02-followup.md
    └── 03-evaluation.md
```

---

## 레포 구조

```
Codex/
├── README.md
├── AGENTS.md                          # 에이전트 워크스페이스 가이드
├── Automation/
│   ├── codex.md                       # 자동화 실행 계약서
│   ├── YYYY-MM-DD/                    # 날짜별 산출물
│   └── harness/ai-trend-report/
│       ├── skill.md                   # 실행 흐름 정의
│       ├── agents/                    # 병렬 리서치 레인 설계
│       ├── prompts/                   # 자동화 프롬프트 변형 3종
│       ├── references/                # 출력 계약, 출처 정책, 프리플라이트
│       └── scripts/                   # Python 실행 스크립트
└── youtube-transcript-team/
    ├── README.md                      # 에이전트 팀 설계 문서
    ├── prompts/                       # 역할별 프롬프트 8종
    ├── analyses/                      # 영상별 분석 아카이브
    ├── paste-template.md              # 풀 분석 입력 템플릿
    ├── quick-template.md              # 압축 모드 입력 템플릿
    ├── quick-mode.md                  # 압축 모드 시스템 프롬프트
    └── golden-examples.md             # 기준 출력 예시
```

---

## 사용 도구

| 도구 | 용도 |
|------|------|
| [OpenAI Codex](https://openai.com/index/codex/) | 자동화 하네스 실행, 웹 리서치, 보고서 생성 |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | 에이전트 팀 오케스트레이션, 분석 실행 |
| [Cursor](https://www.cursor.com/) | 워크스페이스 관리, 프롬프트 설계, 규칙 편집 |
| [oh-my-codex](https://github.com/pinkpixel-dev/oh-my-codex) | Codex 스킬/훅/팀 자동화 확장 |
| [Task Master](https://github.com/task-master-ai/task-master-ai) | 태스크 관리, PRD 파싱, 복잡도 분석 |

---

## 앞으로 활용할 기능들

이 레포는 현재 정보 수집과 분석 자동화에 집중하고 있지만, 아직 활용하지 못한 에이전트 기능이 많다.

아래 항목은 **이 저장소에 이미 구현되어 있는 기능이 아니라**, Claude Code·Cursor·Codex 확장, Task Master, 개인 스킬 등 **외부 도구·워크플로 위에서 단계적으로 붙일 계획**이다.

### 에이전트 오케스트레이션

| 기능 | 설명 | 상태 |
|------|------|------|
| **멀티 에이전트 팀** | Claude Code 네이티브 팀 모드로 N개 에이전트가 공유 태스크 리스트를 동시 처리 | 예정 |
| **Best-of-N 실행** | 같은 태스크를 격리된 워크트리에서 병렬 시도 후 최적 결과 선택 | 예정 |
| **Ultrawork** | 고처리량 병렬 실행 엔진으로 대량 태스크 동시 처리 | 예정 |
| **Ralph 루프** | 태스크 완료까지 자기 참조 루프를 돌며 검증 리뷰어가 품질 체크 | 예정 |
| **Autopilot** | 아이디어에서 동작하는 코드까지 완전 자율 실행 | 예정 |

### 분석 고도화

| 기능 | 설명 | 상태 |
|------|------|------|
| **Deep Interview** | 소크라틱 인터뷰로 모호한 요구사항을 수학적으로 명확화한 뒤 실행 | 예정 |
| **Trace** | 경쟁 가설을 세우고 증거 기반으로 근본 원인을 추적하는 조사 모드 | 예정 |
| **SciOMC** | 병렬 과학자 에이전트로 종합 분석 수행 | 예정 |
| **Research (Task Master)** | AI 기반 리서치로 최신 정보를 태스크에 직접 주입 | 예정 |

### 워크플로우 확장

| 기능 | 설명 | 상태 |
|------|------|------|
| **Tagged Task Lists** | 피처/브랜치/실험별 독립 태스크 컨텍스트 운영 | 예정 |
| **PRD → 태스크 자동 생성** | 요구사항 문서를 파싱해서 구조화된 태스크 리스트 자동 생성 | 예정 |
| **Complexity Analysis** | 태스크 복잡도를 AI가 분석하고 분해 전략을 추천 | 예정 |
| **Obsidian 연동** | 분석 산출물을 Obsidian 볼트에 자동 동기화, 위키링크로 지식 그래프 구축 | 예정 |
| **Hooks** | 에이전트 이벤트(커밋, 태스크 완료 등)에 자동 후처리 스크립트 연결 | 예정 |

### 품질 관리

| 기능 | 설명 | 상태 |
|------|------|------|
| **UltraQA** | 테스트 → 검증 → 수정 → 반복 사이클로 목표 달성까지 순환 | 예정 |
| **AI Slop Cleaner** | AI가 생성한 코드에서 불필요한 부분을 삭제 우선으로 정리 | 예정 |
| **Self-Improve** | 자율 진화형 코드 개선 엔진, 토너먼트 선택 방식 | 예정 |

---

## 철학

- **에이전트는 도구가 아니라 동료다** — 프롬프트 한 줄이 아니라 역할, 규칙, 검증 체계를 설계한다.
- **산출물은 아카이브한다** — 일회성 채팅이 아니라 날짜별·영상별로 구조화해서 쌓는다.
- **자동화는 재현 가능해야 한다** — 프롬프트, 스크립트, 계약서를 분리해 절차와 산출물 형식을 고정하고, 같은 입력에 최대한 가깝게 따라갈 수 있게 한다(LLM 출력은 비결정적일 수 있다).
- **검증 없는 정보는 정보가 아니다** — Fact Checker, Skeptic Reviewer, verify_outputs.py로 항상 걸러낸다.

---

## 시작하기

### AI 트렌드 리포트 생성

```bash
cd Automation
python harness/ai-trend-report/scripts/run_preflight.py --ensure-scaffold
# Codex 또는 Claude Code에서 아래 프롬프트로 실행
# "Read codex.md first. Run the local AI trend report harness preflight,
#  then create today's report set and verify the outputs at the end."
```

### 유튜브 영상 분석

(레포 루트 기준 경로)

1. `youtube-transcript-team/paste-template.md` 형식으로 영상 정보와 스크립트를 준비
2. `youtube-transcript-team/prompts/orchestrator.md`를 리더 프롬프트로 사용
3. 빠른 판단만 필요하면 `youtube-transcript-team/quick-template.md` + `youtube-transcript-team/quick-mode.md` 사용

---

## 저작·이용 안내

개인 생산성 워크스페이스용 자료다. 자유롭게 참고해도 되며, 산출물에 인용한 원문·원본 출처는 각 보고서에 따로 적혀 있다. 별도 SPDX 라이선스는 두지 않았다.
