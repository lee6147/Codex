# Analysis

## 분석 모드
- 풀 분석 + 설명서형 정리

## 입력 신뢰도
- 보통
- 이유:
  - 스크립트 길이는 길고 내용 밀도도 높다.
  - 그러나 자동 전사 오염이 심하고, 공식 문서가 아니라 인터뷰 발언이다.
  - 따라서 구조와 철학을 이해하는 데는 충분하지만, 설치법/명령어/최신 기능 목록을 확정 문서처럼 믿으면 안 된다.

## 세 줄 요약
- 이 인터뷰에서 OMC와 OMX의 핵심은 "좋은 모델"보다 "좋은 하네스와 운영 프로토콜"이 더 중요하다는 주장이다.
- OMC는 Claude Code 계열에서 학습곡선을 낮추고 유용한 워크플로우를 한 번에 제공하는 풀옵션형 하네스에 가깝다.
- OMX는 장시간 병렬 작업을 팀처럼 굴리기 위한 런타임으로, 인터뷰 -> 프리모템 계획 -> 팀 실행 -> 자동 병합/피드백 루프가 중심이다.

## 핵심 주장
- 좋은 AI 개발 경험은 "모델 선택"보다 "하네스 설계"와 "오케스트레이션"에서 더 많이 갈린다.
- 완전 자동화보다 중요한 것은 종료 조건, 채널 분리, 세션 관리, 행동 교정 같은 운영 규율이다.
- 메모리 시스템은 거대한 특수 DB라기보다 "언제 기록하고, 어떻게 재구조화하고, 언제 다시 읽게 할지"에 대한 프로토콜에 가깝다.
- 에이전트는 스스로 선해지거나 저절로 발전하지 않으며, 외부 환경에 노출되면 이상한 습관도 쉽게 배운다.
- 진짜 팀형 에이전트 시스템은 여러 subagent를 한 번 뿌리는 것이 아니라, 중간중간 소통하고 재할당하며 병합 비용을 줄이는 닫힌 루프를 가져야 한다.

## 새로움 판단
- 부분적으로 새롭다
- 이유:
  - 인터뷰에서 소개된 개별 개념 자체는 완전히 새로운 학술 개념이라기보다 기존 개발 협업 개념의 재조합이다.
  - 하지만 이것을 Claude Code / Codex CLI 위에서 "실전 운영 프로토콜"로 묶고, 인터뷰-프리모템-팀런타임-메모리-라우팅까지 연결한 점은 실무적으로 꽤 강한 차별점이다.

## 직접 볼 가치
- 높음
- 이유:
  - 단순 툴 홍보가 아니라 왜 이런 구조가 필요한지에 대한 운영 철학이 비교적 선명하다.
  - 특히 `완전 자동화 환상`, `메모리 미신`, `subagent 남발`에 대한 반론이 유익하다.
  - 라이브 데모를 보고 싶다면 후반 OMX 데모 구간이 핵심이다.
- 추천 구간:
  - `20:45~28:03`: 메모리 시스템과 "디지털 아기" 비유
  - `36:31~49:06`: OMC/OMX 정의, 학습곡선, 하네스 철학
  - `54:21~1:15:26`: Deep Interview, Ralplan, Team Mode 데모

## 실행 가능성
- 조건부 높음
- 전제조건:
  - CLI 기반 작업에 익숙하거나 최소한 거부감이 없어야 한다.
  - 장시간 세션, 병렬 레인, worktree, branch, merge conflict 개념을 이해해야 효율이 난다.
  - "도구가 다 해준다"가 아니라 "좋은 프로토콜을 심어줘야 한다"는 관점을 받아들여야 한다.

## 데모/증거 유무
- 실제 데모: 있음
- 주장 대비 증거:
  - OMX 데모에서 인터뷰 스킬, 랄플랜, 팀모드, pane, worktree/merge 흐름, 외부 채널 라우팅 개념을 직접 보여 준다.
  - 다만 이는 특정 maintainer 환경의 시연이므로 일반 사용자 환경에서 동일하게 재현되는지는 별도 검증이 필요하다.

## 추천 대상
- 실무자 / 팀 리드
- 이유:
  - 이 인터뷰는 단순 코딩 입문보다는 "여러 세션을 조직처럼 굴리는 법"에 관심 있는 사람에게 더 큰 가치가 있다.
  - 초보자도 읽을 수는 있지만, 가장 큰 효용은 장기 태스크, 병렬 작업, 반복되는 이슈 처리에 부딪힌 사람에게 있다.

## 경계할 점
- 인터뷰이는 자신의 도구를 설명하는 입장이므로 성능/철학 설명에는 강한 자기 확신이 섞여 있다.
- "독스 보지 마라", "공식 기능보다 낫다" 같은 표현은 분위기 전달에는 유용하지만 그대로 운영 규칙으로 받아들이면 위험할 수 있다.
- 스타 수, 플러그인 상태, 인증 정책 변화, 최신 기능 지원 여부 같은 것은 시간이 지나면 바뀌므로 transcript만으로 현재 사실로 확정하면 안 된다.
- 이 설명은 설치 매뉴얼이 아니라 개념 설명서에 더 가깝다.

## 바로 실행할 액션
- OMC/OMX를 "AI가 대신 코딩하는 마법도구"가 아니라 "팀 운영 프로토콜이 들어간 하네스"로 이해하라.
- 중요한 작업이라면 `인터뷰 -> 계획 합의 -> 실행`의 3단계를 분리하라.
- 에이전트 메모리는 많이 저장하는 것보다 "언제 정리하고 다시 읽게 할지"를 설계하라.
- 병렬 agent를 돌릴 생각이면 처음부터 merge 비용과 중간 소통 프로토콜을 설계하라.
- 외부 issue/PR/채널을 그대로 학습 재료로 쓰지 말고, 인간이 교정 규칙을 넣는 루프를 반드시 두라.

## 검증 필요 항목
- OMC/OMX의 현재 스타 수, 최신 릴리스 상태
- Claude Code/Codex와의 최신 공식 통합 범위
- transcript에서 언급된 플러그인/인증/오스 정책 변화의 현행 상태
- 팀모드, 메모리 구조, deep-interview, ralplan 명칭과 실제 최신 구현 세부

## 같이 보면 좋은 영상
- Claude Code / Codex 비교 영상
- agent memory / orchestration / workflow design 주제 영상
- worktree, merge conflict, branch strategy 운영 영상
- "AI coding without planning"이 왜 무너지는지 다루는 반례형 영상

## 종합 신뢰도
- 보통
- 이유:
  - 철학과 운영 구조 설명은 설득력이 높다.
  - 하지만 수치, 최신 상태, 설치 세부는 transcript 단독으로 확정하기 어렵다.

## 최종 판단
- 요약만으로 충분하지는 않다. 개념 이해용으로는 이 분석이 충분하지만, 실제 도입 전에는 코드/문서/데모 환경을 따로 확인하는 것이 맞다.

## Subagent Rerun Note
- 이 분석은 이후 실제 `Codex native subagent` 3개를 병렬로 다시 돌려 보강했다.
- 역할 분리:
  - `OMC/OMX 정의와 하네스 철학`
  - `Deep Interview / Ralplan / Team Mode 워크플로우`
  - `메모리 / steering / human oversight`
- 실행 근거:
  - `019db3a4-6297-7942-a1f3-4e646e8bb531` (`Aristotle`): OMC/OMX 정의와 하네스 철학
  - `019db3a4-8421-7a23-a2a6-adfcaf65a221` (`Dewey`): 워크플로우, premortem, Team Mode
  - `019db3a4-b9af-7f13-8980-b94ad32ea2be` (`Bacon`): 메모리, steering, human oversight
- 아래 설명서 본문에는 그 병렬 분석 결과를 통합 반영했다.

---

# OMC / OMX 설명서

## 1. 한 문장 정의

### OMC
Claude Code 계열 환경에서 "바로 쓸 수 있는 강한 기본기"를 제공하도록 만든 풀옵션형 agent harness다.

### OMX
Codex 중심 환경에서 여러 작업 레인을 팀처럼 지속적으로 굴리기 위한 team runtime이다.

## 2. 왜 이런 도구가 필요한가

이 인터뷰에서 반복해서 강조되는 문제는 단순하다.

- 세션이 많아지면 사람이 컨텍스트를 관리하기 어렵다.
- long-running task를 그냥 한 세션에 몰아넣으면 흐름이 꼬인다.
- subagent를 여러 개 뿌려도 서로 소통하지 않으면 팀이 아니라 "따로 노는 병렬 작업"이 된다.
- 메모리를 아무렇게나 쌓으면 나중에 agent가 이상한 습관을 다시 꺼내 쓴다.
- 구현 전에 생각해야 할 문제를 실행 중간에 뒤늦게 깨닫기 시작하면 프로젝트 전체가 흔들린다.

즉, OMC/OMX는 "모델을 더 똑똑하게 만드는 도구"라기보다,
"사람이 감당해야 할 인지 부하를 줄이도록 운영 프로토콜을 넣은 도구"로 보는 편이 맞다.

## 3. OMC의 핵심 성격

인터뷰 기준으로 OMC는 이런 방향을 가진다.

- Claude Code 위에 얹는 하네스
- 유용하다고 검증된 스킬과 워크플로우를 한 번에 제공
- 사용자가 스킬 이름을 외우지 않아도 되게 함
- 키워드 감지로 적절한 workflow를 자동 invoke
- 기본 설정 파일을 프리셋으로 덮어써 learning curve를 낮춤
- 노트패드, 프로젝트 메모리, MCP 저장 공간을 구조화해서 사용하게 만듦

쉽게 말하면, 인터뷰이는 Claude Code를 "가구 없는 원룸"에 비유하고,
OMC는 그 원룸에 필요한 가구와 동선을 한 번에 넣어 주는 쪽에 가깝다고 설명한다.

### OMC를 이렇게 이해하면 좋다
- 처음부터 세세한 커스텀보다 "검증된 기본 흐름"을 강하게 제공한다.
- 파워 유저에게는 답답할 수 있지만, 많은 사용자에게는 진입 장벽을 낮춘다.
- 핵심은 기능의 양보다 "무슨 상황에서 어떤 스킬을 꺼내야 하는지"를 시스템이 대신 안내하는 데 있다.

## 4. OMX의 핵심 성격

OMX는 인터뷰에서 훨씬 런타임 지향적으로 설명된다.

- leader session이 있다.
- 여러 worker lane이 있다.
- 각 worker는 별도 worktree에서 일한다.
- worker끼리 mailbox/메시지로 상태를 주고받는다.
- 자동 checkpoint, auto-merge, fast-forward, rebase, conflict nudge 같은 운영 루프가 있다.
- leader는 필요할 때 worker에게 재할당을 지시한다.

즉 OMX는 "subagent 한 번 호출하고 끝"이 아니라,
지속적으로 재사용되는 협업 레인이 존재하는 런타임에 가깝다.

### OMX의 진짜 포인트
- 컨텍스트 낭비를 줄인다.
- 병렬 작업의 merge 비용을 줄인다.
- 중간에 막힌 lane을 재할당할 수 있다.
- 팀처럼 소통하기 때문에 "각자 다 하고 나중에 한 번에 합치기"보다 덜 위험하다.

## 4-1. OMC/OMX가 본격 소개되는 구간의 핵심 설명

이 인터뷰에서 OMC/OMX가 본격적으로 소개되는 구간은 대체로 `36:31~49:06`이다.  
강의용으로 설명할 때는 아래 핵심과 부차를 분리해서 보는 편이 좋다.

### 반드시 설명해야 하는 핵심
- OMC는 `Claude Code 위에 얹는 풀옵션 하네스`라는 점
- OMX는 `Codex 중심의 team runtime`이라는 점
- 둘 다 단순 스킬 모음이 아니라 `오케스트레이션과 상태 관리`가 중심이라는 점
- 진짜 차별점은 `모델 자체`보다 `하네스 설계`에 있다는 화자의 주장
- OMC는 `학습곡선 감소`, OMX는 `병렬 협업과 merge 비용 절감` 쪽에 더 무게가 있다는 점

### 같이 설명하면 좋은 부차적 포인트
- OMC는 스킬 이름을 외우지 않아도 되게 하는 프리셋/키워드 감지 UX를 중시한다.
- OMX는 subagent를 한 번 호출하고 끝내는 방식보다, 재사용되는 worker lane을 유지하는 방식을 더 중요하게 본다.
- OMC는 "풀옵션 원룸", OMX는 "협업 사무실"에 비유하면 이해가 쉽다.
- 화자는 공식 제공 도구와 별도 하네스의 관계를 "제조사 기본 세팅 vs 현장 튜닝" 차이로 설명한다.
- 화자는 스킬을 많이 모아 둔 것만으로는 하네스가 아니며, 상태 전이 규칙과 닫힌 루프까지 있어야 하네스라고 본다.
- 인간 역할이 사라지는 것이 아니라, 초기에 더 많이 생각하고 이후에 더 길게 핸드오프하는 방식으로 바뀐다고 본다.

### 강의에서 특히 강조해야 하는 해석
- OMC/OMX는 "AI를 더 똑똑하게 만든다"기보다 "사람이 여러 세션과 agent를 감당 가능하게 만든다"는 쪽이 더 정확하다.
- 따라서 이 도구의 핵심 가치는 `추론 성능 자체`보다 `운영 가능성`, `핸드오프 범위`, `인지 부하 감소`, `협업 프로토콜`에 있다.

### 설명할 때 조심해야 하는 부분
- `국내에서 스타가 가장 많다`, `제로 러닝 커브`, `공식 랄프는 랄프가 아니다` 같은 문장은 화자의 강한 자기 평가와 해석이 섞인 표현이다.
- 따라서 강의에서는 `화자의 주장`, `인터뷰 기준 설명`, `현재 상태는 별도 검증 필요`를 분리해서 말하는 편이 안전하다.

## 5. 인터뷰가 말하는 핵심 철학

## 5-1. 모델보다 하네스
- frontier model 사이 성능 차이가 줄어들수록,
  사용자 체감 품질은 orchestration과 workflow 설계에서 더 많이 갈린다는 주장이다.

## 5-2. planning과 execution을 분리하라
- 인터뷰이는 가장 큰 차별점으로 planning/execution 경계를 강조한다.
- 그냥 "대충 만들어 보고 고치기"는 위험한 종류의 작업에서 재앙이 될 수 있다고 본다.

## 5-3. 프리모템이 핵심이다
- 문제가 터진 뒤 사후 수습하는 postmortem이 아니라,
  구현 전에 어디서 망가질지 따져보는 premortem이 핵심이라고 본다.

## 5-4. 메모리는 저장보다 라이프사이클
- 얼마나 많이 저장하느냐보다
  언제 기록하고, 언제 재구조화하고, 언제 다시 읽히게 하느냐가 중요하다고 본다.

## 5-5. 에이전트는 방치형 자율 생물이 아니다
- 자가 발전이라는 표현을 경계한다.
- 외부 issue나 잘못된 피드백을 계속 먹이면 잘못된 습관도 학습한다.
- 따라서 인간이 steer하고 혼내고 행동 강령을 갱신해야 한다고 본다.

## 6. 추천 워크플로우 해설

인터뷰에서 사실상 표준 루프로 제시된 것은 아래 흐름이다.

### 1단계. Deep Interview
- 요구사항이 모호하지 않을 때까지 질문한다.
- 다만 코드/환경에서 바로 알 수 있는 것은 먼저 찾아본다.
- 목적: 사람의 머릿속에 흩어진 요구와 숨은 조건을 먼저 구조화

### 2단계. Ralplan
- planner / critic / architect가 합의할 때까지 계획을 다듬는다.
- 목적: 인터뷰 과정에서 생긴 모순, 누락, 위험 경로를 미리 잡기

### 3단계. Ralph / Team Mode 실행
- 합의된 계획을 바탕으로 실제 구현을 밀어붙인다.
- 목적: 중간에 사람이 계속 개입하지 않도록 핸드오프 가능한 상태 만들기

### 4단계. 마지막 사용자 검증
- 최종적으로 사람 입장에서 실제 사용 감각을 확인한다.

이 흐름의 핵심은 "중간 개입을 줄이는 것"이다.
인터뷰이는 중간에 자꾸 프롬프트를 끼워 넣으면 프로젝트가 쉽게 맛이 간다고 본다.
마음에 안 들면 새 인터뷰로 다시 따는 편이 낫다는 것이다.

## 7. 메모리 시스템 설명

이 인터뷰에서 말하는 메모리는 화려한 vector DB 이야기와 다르다.

### 핵심 구성
- 루트 레벨 메모리 맵
- 파트/폴더별 메모리
- learnings 같은 교훈 저장소
- 주기적인 리팩터링/중복 제거 루프

### 중요한 아이디어
- 메모리는 단순 저장소가 아니라 "행동 교정 기록"이다.
- 실패 사례와 혼난 사례를 다시 읽게 만들어 같은 실수를 줄인다.
- 하지만 외부 환경의 이상한 노이즈를 그대로 먹이면 잘못된 방향으로 굳어질 수 있다.

### 실무적으로 읽는 법
- 좋은 메모리는 "모든 것을 저장한 메모리"가 아니다.
- 좋은 메모리는 "다음번 행동이 달라지게 만드는 메모리"다.

## 8. OMC와 OMX의 차이

## OMC에 더 가까운 경우
- Claude Code 환경을 이미 쓰고 있다.
- 여러 스킬과 가이드를 한 번에 깔아서 빠르게 쓰고 싶다.
- 낮은 학습곡선이 중요하다.
- "풀옵션 패키지"처럼 바로 usable한 상태를 원한다.

## OMX에 더 가까운 경우
- Codex 중심으로 장시간 병렬 작업을 굴리고 싶다.
- 여러 worker lane을 재사용하고 싶다.
- worktree, merge, branch 전략이 중요하다.
- 팀처럼 소통하는 runtime이 필요하다.

## 둘을 함께 관통하는 공통점
- 단순 프롬프트 모음이 아니다.
- 상태 관리와 오케스트레이션이 중심이다.
- 완전 자동화보다 "잘 설계된 자동화"를 지향한다.

## 8-1. 실제 subagent 재분석에서 다시 강조된 차이
- OMC는 `Claude Code 위에 얹는 풀옵션 하네스`라는 성격이 더 강하게 반복 확인됐다.
- OMX는 `Codex 중심 team runtime`이라는 점이 더 선명하게 재확인됐다.
- OMC 쪽은 "스킬 이름을 몰라도 자동으로 workflow를 유도하는 UX"가 중요하고,
  OMX 쪽은 "지속적으로 소통하고 merge 비용을 줄이는 협업 런타임"이 중요하다는 점이 병렬 분석에서도 일치했다.

## 8-2. 하네스가 모델보다 중요하다는 논지
- 병렬 분석 결과를 합치면, 화자의 주장은 단순히 "모델 차이가 줄었다"가 아니다.
- 더 정확히는:
  - 오케스트레이션
  - 메모리 lifecycle
  - 세션 분리
  - 종료 조건
  - 프리모템
  - 라우팅
  - 팀 협업 프로토콜
  같은 하네스 요소가 실제 생산성 차이를 만든다는 쪽에 가깝다.

## 8-3. OMC/OMX 설명에서 부차적이지만 놓치면 아쉬운 부분
- OMC/OMX 소개는 기술 구조만이 아니라 "왜 이런 튜닝을 공식 제공자가 직접 안 하느냐"에 대한 답도 포함한다.
- 화자는 모델 프로바이더는 토큰 비용과 안정성을 우선하지만, 하네스 제작자는 인지 부하 감소와 결과물 품질을 위해 더 공격적인 튜닝을 할 수 있다고 본다.
- 이 관점은 OMC/OMX를 단순 플러그인이나 스킬 꾸러미로 오해하지 않게 해 준다.
- 또 OMC는 상대적으로 사용자 경험과 접근성을, OMX는 팀형 실행과 병합 운영을 더 강하게 밀고 있다는 대비도 강의에서 유용하다.

## 9. 이 인터뷰가 특히 잘 짚는 오해

### 오해 1. 메모리 시스템이 있으면 agent가 저절로 똑똑해진다
- 아니다. 잘못된 것을 배울 수도 있다.

### 오해 2. subagent를 여러 개 띄우면 곧 팀이다
- 아니다. 서로 소통하고 재할당되고 병합 비용을 줄여야 팀이다.

### 오해 3. planning은 느리고 execution이 진짜 일이다
- 이 인터뷰는 반대로 planning이 execution 품질을 결정한다고 본다.

### 오해 4. AI가 다 해주니 인간 개입은 없어질 것이다
- 이 인터뷰는 인간 개입이 "직접 구현"에서 "디렉팅과 교정"으로 이동한다고 본다.

## 9-1. 워크플로우 관점에서 본 핵심 차별점
- 실제 subagent 재분석에서도 가장 강하게 겹친 포인트는 `Deep Interview -> Ralplan -> Team Mode` 흐름이었다.
- 화자는 작업을 바로 실행하지 않고:
  - 모호성 제거
  - 합의된 계획 수립
  - 팀 실행
  순으로 넘기는 구조를 핵심으로 본다.
- 여기서 premortem은 "구현 전에 실패 경로를 최대한 논증한다"는 뜻이고,
  planning과 execution을 강하게 분리하는 것이 OMC/OMX 철학의 중심 축으로 재확인됐다.
- 또 team mode의 가치는 단순 병렬성이 아니라 `worktree`, `auto-commit`, `fast-forward`, `rebase`, `conflict nudge`, `message telemetry`를 묶어
  병합 비용과 컨텍스트 낭비를 줄이는 데 있다는 점도 병렬 분석에서 일치했다.

## 9-2. 메모리와 human steering에 대한 해석
- 메모리는 거대한 특수 런타임이라기보다, 무엇을 언제 기록하고 언제 재구조화하고 다시 읽게 할지에 대한 운영 프로토콜이라는 해석이 재확인됐다.
- `learnings`는 단순 로그가 아니라, 실패와 교훈을 더 영속적인 행동 규칙으로 다듬는 층에 가깝다.
- 화자의 "디지털 아기" 비유도 핵심인데, 이는 agent가 저절로 좋아지는 존재가 아니라
  외부 오염을 막고 행동 강령을 계속 고쳐 줘야 핸드오프 범위가 넓어지는 대상이라는 뜻으로 읽는 편이 맞다.
- 따라서 이 transcript에서 자동화는 인간 제거가 아니라 감독 방식의 변화다.

## 10. 초보자가 이해해야 할 핵심 문장

- OMC는 "Claude Code를 더 잘 굴리게 만드는 운영 패키지"다.
- OMX는 "Codex를 팀처럼 굴리게 만드는 런타임"이다.
- 메모리는 많이 저장하는 기술이 아니라, 실수를 덜 반복하게 만드는 운영 규칙이다.
- 자동화의 핵심은 agent를 방치하는 것이 아니라, 좋은 종료 조건과 행동 규칙을 심는 것이다.
- 병렬화의 핵심은 많이 돌리는 것이 아니라, 합쳐질 수 있게 돌리는 것이다.

## 11. 실전 도입 전에 꼭 확인할 것

- 이 transcript는 개념 설명서로는 좋지만 설치 가이드로는 부족하다.
- 현재 프로젝트의 공식 README, 코드 구조, 실제 명령어, 최신 환경 변수는 별도 확인이 필요하다.
- 특히 팀모드처럼 환경 의존성이 있는 기능은 "데모가 보였다"와 "내 환경에서 재현된다"를 구분해야 한다.

## 12. 결론

이 인터뷰를 기반으로 보면 OMC/OMX의 본질은 "AI가 스스로 다 해주는 미래"가 아니다.
오히려 반대다. 사람의 혼란을 줄이고, 작업을 팀처럼 나누고, 계획과 실행을 분리하고,
메모리와 피드백으로 행동을 교정하는 "운영 시스템"에 가깝다.

그래서 이 도구들을 이해할 때는
`무슨 모델이냐`보다
`어떤 프로토콜이 심어져 있느냐`
를 먼저 봐야 한다.

## 영어 학습 버전

### Core English Summary
- The speaker argues that the real advantage of tools like OMC and OMX is not just the model itself, but the workflow harness around the model.
- OMC is presented as a full-package layer on top of Claude Code that lowers the learning curve and invokes useful workflows automatically.
- OMX is described as a team runtime where multiple workers keep talking to each other, reuse work lanes, and reduce merge costs.
- A key idea in the interview is that planning should come before execution, especially for complex or risky tasks.
- The speaker also says that agent memory is not magic intelligence, but a structured way to record lessons and guide future behavior.

### In Easier English
- The main point is simple: a smart model is not enough.
- You also need a good system around it.
- OMC tries to make the system easy to use.
- OMX tries to make many agents work like a real team.
- The speaker says agents should be trained and guided, not left alone. (혼자 방치하면 안 된다는 뜻)

### Analogy
- Think of OMC as a furnished apartment and OMX as a team office with desks, mailboxes, and managers.
- The base model is like the building itself, but the real daily productivity comes from how the space is organized.

### Difficult Expressions
- `learning curve`: how hard something is to learn. Use it when talking about onboarding. Example: `OMC tries to reduce the learning curve for new users.`
- `orchestration`: coordinating many parts so they work together. Use it for multi-agent or workflow systems. Example: `The tool focuses on orchestration rather than raw model power.`
- `closed loop`: a system that watches its own progress and reacts inside the same process. Example: `Team mode is designed as a closed loop.`
- `merge cost`: the effort needed to combine parallel work safely. Example: `OMX tries to reduce merge cost between workers.`
- `steer`: to guide something in the right direction. Use it for human guidance over AI behavior. Example: `Humans still need to steer the agents.`

### Grammar Notes
- Present simple:
  - Used for general truths and stable descriptions.
  - Example: `OMX reduces merge cost.` / `Good planning matters.`
- Passive voice:
  - Useful when the focus is on the process, not the actor.
  - Example: `Useful workflows are automatically invoked.`
  - Extra example: `The issue was routed to the correct channel.`
- `not A, but B` contrast:
  - This structure is common when correcting a misunderstanding.
  - Example: `The goal is not raw automation, but better orchestration.`
  - Extra example: `Memory is not magic intelligence, but a behavior guide.`

### Daily English Expressions
- `That is the real bottleneck.`
  - Nuance: the most important blocking point.
  - Example: `The model is good enough. The workflow is the real bottleneck.`
- `I would not trust that blindly.`
  - Nuance: polite warning not to accept something too easily.
  - Example: `The demo looked impressive, but I would not trust that blindly without testing it myself.`
- `You need guardrails for that.`
  - Nuance: rules or limits are needed to keep something safe.
  - Example: `If you want long-running agents, you need guardrails for that.`
