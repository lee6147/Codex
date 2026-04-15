# 유튜브 스크립트 분석 산출물 평가

이 문서는 동일 폴더의 `00-intake.md`, `01-analysis.md`, `02-followup.md`를 프로젝트 템플릿·quick-mode·golden-examples 기준으로 대조한 검토 결과다.

**기준 문서:** [analyses/README.md](../README.md), [analyses/_template/](../_template/), [quick-mode.md](../../quick-mode.md), [golden-examples.md](../../golden-examples.md), [prompts/orchestrator.md](../../prompts/orchestrator.md).

---

## 종합 판정

**압축(퀵) 모드로서는 목적에 잘 맞고, golden-examples가 말하는 “시간 절약·검증 분리·실행 단위 액션” 기준을 대체로 충족한다.** 다만 [prompts/orchestrator.md](../../prompts/orchestrator.md)에 정의된 **풀 파이프라인 14절 출력**과 비교하면 **의도적으로 얇은 편**이며, 50분 분량에 대한 **구간별 시청 가이드(타임스탬프/챕터별 추천)**는 없다.

---

## 잘된 점

1. **01-analysis와 프로젝트 템플릿 정합**  
   [analyses/_template/01-analysis.md](../_template/01-analysis.md)의 섹션(한줄 결론, 핵심 요약, 직접 볼 가치, 실행 가능성, 검증 필요 주장, 같이 보면 좋은 유형, 최종 판정)이 채워져 있고, [analyses/README.md](../README.md)의 “01만 먼저 채워도 됨” 운용과도 맞다.

2. **quick-mode 정렬**  
   Intake에 “압축 우선 분석”이 명시되어 있고, [quick-mode.md](../../quick-mode.md)가 요구하는 한줄 결론·핵심 요약·시청 가치·실행·검증 필요·연관 영상 유형이 `01-analysis` / `02-followup`에 분배되어 있다.

3. **golden-examples와의 정합**  
   - 수치·연구 인용은 그대로 믿지 않고 [01-analysis.md](./01-analysis.md) “검증 필요 주장”에 분리(Example 2의 Skeptic/Fact 경계와 일치).  
   - 실행 가능성을 **조건부**로 두고 전제를 적음(Example 2의 보수적 판정과 일치).  
   - 최종 판정이 **“필요한 구간만 시청”**으로 단정적이지 않게 결론(Example 1·2의 냉정한 판정 방향과 일치).

4. **메타데이터 정직성**  
   [00-intake.md](./00-intake.md)에서 제목·채널 **추정**, 업로드 날짜 **불명**, 자막/전사 오류 가능성을 밝힘 — orchestrator의 “스크립트에 없는 내용을 사실처럼 넣지 말 것”과 부합.

5. **02-followup의 실행성**  
   “레벨 자가 진단 → CLAUDE.md 슬림화 → Obsidian 실험” 순서는 [golden-examples.md](../../golden-examples.md) Example 1이 말하는 **바로 실험 가능한 액션**에 가깝다. 이전 영상이 없으므로 구체 제목 대신 **유형** 위주 추천 — [quick-mode.md](../../quick-mode.md) 규칙과 일치.

6. **7단계 구조 요약**  
   약 46~50분 분량의 뼈대(레벨 1~7 + 아웃트로)를 한 줄 결론과 불릿 요약으로 압축한 것은 **의사결정 프레임(단순 → 필요 시 상향)**까지 전달하는 데는 충분하다.

---

## 아쉬운 점 / 기대와의 차이

1. **Orchestrator 풀 출력 대비 생략**  
   [orchestrator.md](../../prompts/orchestrator.md)의 별도 항목인 **입력 신뢰도**, **신규성 판정**, **데모/증거 유무**, **추천 대상(초보/실무자/팀 리드)**, **판단 신뢰도**는 파일에 명시되지 않았다. 압축 모드 선택이라면 타당한 생략이나, “풀 팀 가동” 기대와는 불일치할 수 있다.

2. **50분 vs 45:46**  
   Intake 영상 길이는 **45분 46초**로 적혀 있어 사용자가 말한 50분과 소폭 차이 — 메타 출처(영상 페이지 vs 스크립트 헤더)만 정리하면 됨.

3. **템플릿 00-intake와의 형식 차이**  
   [_template/00-intake.md](../_template/00-intake.md)의 `원문 저장 방식`, `transcript 파일 목록`, 코드 블록 내 스크립트는 비어 있거나 대체됨. 대신 README가 허용하는 **“원문 길면 transcript 폴더 분할”**과, intake 본문의 **“전체 원문 중복 저장 안 함”** 설명으로 의도는 드러난다. **재현·감사**를 중시하면 `transcript/`에 분할 저장이 더 낫다.

4. **“필요한 구간만”에 대한 구체성**  
   최종 판정은 있으나, **어느 레벨(또는 몇 분 경량)만 보면 되는지**는 타임스탬프 없이 서술만 되어 있어, 사용자가 바로 스크롤하기엔 한 단계 부족할 수 있다.

---

## 결론

| 관점 | 평가 |
|------|------|
| 폴더 규칙·01/02 채움 | 양호 |
| youtube-transcript / 퀵 모드 취지 | 양호 |
| 스케프틱·실무 액션·시청 판정 | 양호 |
| Orchestrator 풀 리포트 기대 | 부분 미달 가능 |
| 장편 스크립트 대비 깊이(구간 가이드 등) | 보통 — 필요 시 확장 |

**요약:** 에이전트·스킬 팀이 **이 저장소가 정의한 “압축 분석 + 판단 우선” 워크플로**에는 잘 맞춰 작업했다. **전체 오케스트레이터 14절**이나 **구간별 시청 가이드**까지 기대했다면, 그 한 단계는 다음 확장으로 남아 있다.
