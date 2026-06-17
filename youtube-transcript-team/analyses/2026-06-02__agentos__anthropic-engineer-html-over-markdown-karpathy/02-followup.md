# Follow-up

## 바로 해볼 실험
- 기존 긴 Markdown 산출물 하나를 골라 같은 입력으로 HTML 버전을 다시 생성한다.
- 비교 기준은 `읽은 시간`, `놓친 위험 발견 여부`, `다음 액션으로 옮기는 속도`, `git/보존 비용` 네 가지로 둔다.
- HTML이 더 낫다면 다음부터는 복잡한 계획/리뷰/리서치에만 HTML을 요청하고, 짧은 기록은 Markdown으로 남긴다.

## 추천 프롬프트
```text
이 내용을 Markdown 보고서가 아니라 한 파일짜리 HTML artifact로 만들어줘.
탭 구조, 위험도 색상, 비교표, 근거/미확인 주장 구분, copy prompt 버튼을 포함해줘.
민감 정보가 있으면 별도 섹션으로 표시하고 외부 공유 금지 문구를 넣어줘.
```

```text
이 PR을 reviewer가 빠르게 판단할 수 있는 HTML 대시보드로 설명해줘.
파일별 변경 의도, 위험도, 테스트 공백, 확인 질문, 승인 전 체크리스트를 포함해줘.
```

## 검증할 외부 출처
- 영상이 인용한 Anthropic/Claude Code 엔지니어 원문 글.
- Karpathy가 HTML output에 대해 언급한 실제 트윗/게시물.
- Claude Code에서 HTML artifact 생성 시 토큰 사용량, 보안 경계, 파일 접근 범위.

## 같이 보면 좋은 영상 유형
- Claude Code/Codex artifact 생성 기본 데모
- PR review automation 실전 데모
- MCP로 Linear/Slack/GitHub 데이터를 읽어 시각화하는 사례
- HTML artifact 보안, local file handling, secret redaction 관련 설명

## 남은 리스크
- 이 분석은 YouTube 자동 자막 기반이다. 원문 블로그와 트윗을 확인하지 않았으므로 인용 사실은 검증 전 상태다.
- 영상 화면을 직접 검토하지 않았으므로 실제 예시 UI의 품질, 코드 완성도, 사용성은 판단하지 않았다.
- HTML-first workflow는 산출물 검토율을 높일 수 있지만, 장기 지식관리와 감사 추적에는 Markdown/structured source를 함께 남기는 편이 안전하다.
