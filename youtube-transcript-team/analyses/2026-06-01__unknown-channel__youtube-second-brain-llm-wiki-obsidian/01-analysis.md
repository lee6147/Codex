# Analysis

## 입력 신뢰도
- 보통
- 이유: 챕터와 시간 정보가 있고 데모 흐름은 충분히 복원된다. 다만 자동 자막 오탈자, 도구명 표기 흔들림, 화면 맥락 부재 때문에 세부 기능 평가는 보수적으로 봐야 한다.

## 세 줄 요약
- 이 구간은 YouTube 대본과 슬라이드를 원천 자료로 삼아 `LLM Wiki` 스타일의 세컨드 브레인을 만드는 데모다.
- Obsidian은 지식 그래프를 보는 인터페이스이고, 실제 처리 엔진은 Claude Code와 에이전트 워크플로다.
- 핵심 메시지는 RAG를 완전히 대체한다는 주장보다, 원본을 보존하고 위키/인덱스/스키마를 반복 갱신하는 캐싱형 지식 하네스를 만들자는 데 있다.

## 핵심 주장
- 지식 자료는 GitHub나 로컬 폴더에 원본으로 보존하고, 별도 processed/wiki 계층에서 핵심만 추출해야 한다.
- LLM Wiki는 `raw source -> distilled wiki -> schema/index` 구조로 누적되는 산출물이다.
- Obsidian 그래프는 전체 주제와 연결을 둘러보기 좋지만, 깊은 질의응답은 에이전트에게 위키를 읽혀 수행하는 쪽이 낫다.
- RAG는 chunking, embedding, semantic search로 관련 문서를 찾아 프롬프트에 넣는 방식이고, LLM Wiki는 사람이 읽기 좋은 중간 지식층을 유지하는 방식에 가깝다.
- 검색/필터만으로는 정보가 많을 때 한계가 있으므로 에이전트 질의와 함께 써야 한다.

## 하네스 엔지니어링 관점
- 좋은 하네스는 모델에게 모든 원문을 매번 다시 읽히는 대신, 반복 가능한 처리 흐름과 검증 가능한 중간 산출물을 제공한다.
- 이 데모의 하네스는 `ingest -> distill -> link -> index -> query -> update` 루프다.
- 원본, 위키, 인덱스가 분리되어야 실패했을 때 되돌리거나 다시 생성하기 쉽다.
- Obsidian은 하네스의 사용자 인터페이스에 가깝고, Claude Code는 작업을 수행하는 실행 계층이다.

## 직접 볼 가치
- 보통
- 이유: 구조 요약은 텍스트만으로 이해 가능하지만, Obsidian 그래프와 Claude Code 병렬 에이전트 작업 화면은 직접 보면 감이 빨리 온다.
- 추천 구간: 38:32-46:58은 LLM Wiki 구조와 RAG 차이, 56:48-1:03:52는 실제 질의와 한계 정리가 핵심이다.

## 실행 가능성
- 조건부
- 전제조건: YouTube 대본/슬라이드 같은 원천 자료, markdown 파일 구조, Obsidian 또는 유사 파일 브라우저, Claude Code/Codex 같은 에이전트 실행 환경이 필요하다.

## 주의점
- `RAG가 필요 없다`는 식으로 단정하면 위험하다. 이 데모는 개인/팀 지식 정리에는 유용하지만, 대규모 검색 품질이나 권한 제어가 중요한 서비스에는 별도 검색 계층이 필요할 수 있다.
- Obsidian 그래프가 예쁘다고 해서 곧바로 좋은 질의응답 시스템이 되는 것은 아니다.
- 자막만으로는 실제 생성된 위키 품질, 링크 정확도, 재현 가능성은 확인할 수 없다.

## 바로 실행할 것
- 원본 자료 폴더와 processed/wiki 폴더를 분리한다.
- 새 자료를 넣는 ingest 규칙을 문서화한다.
- 위키 노트에는 출처, 핵심 개념, 관련 노트, 다시 확인할 질문을 같은 형식으로 넣는다.
- Obsidian 그래프는 탐색용으로 쓰고, 실제 답변은 에이전트가 wiki/index를 읽게 한다.

## 검증 필요 항목
- LLM Wiki 방식이 본인 자료 규모에서 RAG보다 충분히 나은지.
- 병렬 에이전트 11개가 만든 노트의 중복, 누락, 잘못된 연결 비율.
- Obsidian에서 필요한 그래프 필터를 CLI나 자동화로 실제 제어할 수 있는지.

## 영어 학습용 버전
- Core English summary: This segment shows a workflow for turning YouTube transcripts and slides into a personal second brain. Obsidian is the visual workspace, while Claude Code does the heavy processing. The important idea is not just "make a graph," but build a repeatable knowledge harness.
- Easy explanation: A knowledge harness is a system that helps an AI use your files in a reliable way. It keeps raw sources, cleaned notes, and indexes separate.
- Useful expressions: `raw source`, `distilled wiki`, `knowledge graph`, `query workflow`, `source of truth`.
- Grammar note: `Obsidian is the interface, while Claude Code is the engine` uses `while` to compare two different roles.

