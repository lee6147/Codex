# Scripts

## `connect_analysis.py`

분석용 템플릿, 역할 프롬프트, 분석 폴더 생성을 한 번에 연결해 주는 로컬 CLI다.

### 새 분석 폴더 만들기

```powershell
python scripts/connect_analysis.py new `
  --title "Claude Code vs Codex" `
  --channel "Example Channel" `
  --mode full
```

필요하면 긴 원문용 `transcript/` 폴더도 같이 만들 수 있다.

```powershell
python scripts/connect_analysis.py new `
  --title "Long Transcript Demo" `
  --channel "Example Channel" `
  --mode quick `
  --transcript-parts 3
```

생성 결과:

- `00-intake.md`
- `01-analysis.md`
- `02-followup.md`
- `03-prompt-bundle.md`
- 필요 시 `transcript/transcript-part-XX.md`

### intake 수정 후 번들만 다시 만들기

```powershell
python scripts/connect_analysis.py bundle `
  analyses\2026-04-16__example-channel__claude-code-vs-codex `
  --mode full
```

`03-prompt-bundle.md`에는 현재 intake와 선택한 리더 프롬프트, 역할 프롬프트가 함께 들어간다.
