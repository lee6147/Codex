#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ANALYSES_ROOT = ROOT / "analyses"
TEMPLATE_DIR = DEFAULT_ANALYSES_ROOT / "_template"
PROMPTS_DIR = ROOT / "prompts"


@dataclass(frozen=True)
class RolePrompt:
    title: str
    path: Path
    when_to_use: str | None = None


@dataclass(frozen=True)
class ModeConfig:
    label: str
    leader_prompt: Path
    core_roles: tuple[RolePrompt, ...]
    optional_roles: tuple[RolePrompt, ...]


MODE_CONFIGS = {
    "full": ModeConfig(
        label="풀 버전",
        leader_prompt=PROMPTS_DIR / "orchestrator.md",
        core_roles=(
            RolePrompt("Summary Analyst", PROMPTS_DIR / "summary-analyst.md"),
            RolePrompt("Practicality Evaluator", PROMPTS_DIR / "practicality-evaluator.md"),
            RolePrompt("Watchworthiness Judge", PROMPTS_DIR / "watchworthiness-judge.md"),
            RolePrompt("Action Curator", PROMPTS_DIR / "action-curator.md"),
        ),
        optional_roles=(
            RolePrompt(
                "Novelty Detector",
                PROMPTS_DIR / "novelty-detector.md",
                "비슷한 영상을 이미 많이 봤거나 중복 제거가 중요할 때",
            ),
            RolePrompt(
                "Fact Checker",
                PROMPTS_DIR / "fact-checker.md",
                "최신 기능, 가격, 정책, 모델명처럼 날짜 민감 요소가 핵심일 때",
            ),
            RolePrompt(
                "Skeptic Reviewer",
                PROMPTS_DIR / "skeptic-reviewer.md",
                "영상이 과장되었거나 판매성이 강해 보일 때",
            ),
            RolePrompt(
                "Companion Recommender",
                PROMPTS_DIR / "companion-recommender.md",
                "이미 본 영상 목록이나 자주 보는 채널 정보가 있을 때",
            ),
        ),
    ),
    "quick": ModeConfig(
        label="압축",
        leader_prompt=ROOT / "quick-mode.md",
        core_roles=(
            RolePrompt("Summary Analyst", PROMPTS_DIR / "summary-analyst.md"),
            RolePrompt("Watchworthiness Judge", PROMPTS_DIR / "watchworthiness-judge.md"),
            RolePrompt("Action Curator", PROMPTS_DIR / "action-curator.md"),
        ),
        optional_roles=(),
    ),
}


def slugify(value: str, fallback: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_only.lower()).strip("-")
    return slug or fallback


def resolve_workspace_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return (ROOT / path).resolve()


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_utf8(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_intake(
    *,
    title: str,
    channel: str,
    length: str,
    uploaded: str,
    level: str,
    transcript_parts: int,
) -> str:
    transcript_storage = "intake 본문에 직접 저장"
    transcript_lines = "- 없음"
    transcript_block = "여기에 스크립트 붙여 넣기"

    if transcript_parts > 0:
        transcript_storage = "transcript 폴더로 분할 저장"
        transcript_lines = "\n".join(
            f"- transcript/transcript-part-{index:02d}.md"
            for index in range(1, transcript_parts + 1)
        )
        transcript_block = "원문은 transcript/ 하위 파일 참조"

    return f"""# Intake

## 영상 정보
- 제목: {title}
- 채널명: {channel}
- 영상 길이: {length}
- 업로드 날짜: {uploaded}

## 내가 궁금한 것
- 

## 내 수준
- {level}

## 이전에 본 영상
- 

## 자주 보는 채널
- 

## 스크립트 완전성
- 전체 / 일부 / 자동 자막 가능성 있음

## 원문 저장 방식
- {transcript_storage}

## transcript 파일 목록
{transcript_lines}

## 스크립트

```text
{transcript_block}
```
"""


def customize_analysis_template(mode_label: str) -> str:
    template = read_utf8(TEMPLATE_DIR / "01-analysis.md")
    return template.replace("- 압축 / 풀 버전", f"- {mode_label}", 1)


def build_role_section(title: str, prompt_text: str, when_to_use: str | None = None) -> str:
    lines = [f"### {title}"]
    if when_to_use:
        lines.append(f"- 포함 추천 조건: {when_to_use}")
    lines.append("```md")
    lines.append(prompt_text.rstrip())
    lines.append("```")
    return "\n".join(lines)


def render_bundle(mode: str, analysis_dir: Path, intake_text: str) -> str:
    config = MODE_CONFIGS[mode]
    leader_prompt = read_utf8(config.leader_prompt).rstrip()

    core_sections = "\n\n".join(
        build_role_section(role.title, read_utf8(role.path))
        for role in config.core_roles
    )

    optional_sections = ""
    if config.optional_roles:
        optional_sections = "\n\n## 조건부 추가 역할 프롬프트\n\n" + "\n\n".join(
            build_role_section(
                role.title,
                read_utf8(role.path),
                when_to_use=role.when_to_use,
            )
            for role in config.optional_roles
        )

    return f"""# Prompt Bundle

## 분석 폴더
- {analysis_dir}

## 분석 모드
- {config.label}

## 사용 순서
1. `00-intake.md`를 먼저 채운다.
2. 이 파일의 `리더 프롬프트`와 `현재 intake`를 새 대화에 그대로 넣는다.
3. 역할 분리가 필요하면 아래 역할 프롬프트를 추가로 붙인다.
4. 결과를 `01-analysis.md`, 후속 액션을 `02-followup.md`에 정리한다.
5. intake를 수정했다면 이 번들을 다시 생성한다.

## 리더 프롬프트

```md
{leader_prompt}
```

## 현재 intake

```md
{intake_text.rstrip()}
```

## 기본 역할 프롬프트

{core_sections}{optional_sections}

## 결과 저장 위치
- `01-analysis.md`
- `02-followup.md`
"""


def create_transcript_parts(analysis_dir: Path, transcript_parts: int) -> None:
    if transcript_parts <= 0:
        return

    transcript_dir = analysis_dir / "transcript"
    transcript_dir.mkdir(parents=True, exist_ok=True)

    for index in range(1, transcript_parts + 1):
        transcript_file = transcript_dir / f"transcript-part-{index:02d}.md"
        if transcript_file.exists():
            continue
        write_utf8(
            transcript_file,
            f"# Transcript Part {index:02d}\n\n```text\n여기에 스크립트 파트 {index:02d}를 붙여 넣기\n```\n",
        )


def scaffold_analysis(args: argparse.Namespace) -> int:
    config = MODE_CONFIGS[args.mode]
    analyses_root = resolve_workspace_path(args.output_root)
    analyses_root.mkdir(parents=True, exist_ok=True)

    channel_slug = args.channel_slug or slugify(args.channel, "unknown-channel")
    video_slug = args.video_slug or slugify(args.title, "video")
    folder_name = f"{args.date}__{channel_slug}__{video_slug}"
    analysis_dir = analyses_root / folder_name

    if analysis_dir.exists() and not args.force:
        print(f"error: already exists: {analysis_dir}", file=sys.stderr)
        return 1

    analysis_dir.mkdir(parents=True, exist_ok=True)

    intake_text = render_intake(
        title=args.title,
        channel=args.channel,
        length=args.length,
        uploaded=args.uploaded,
        level=args.level,
        transcript_parts=args.transcript_parts,
    )
    write_utf8(analysis_dir / "00-intake.md", intake_text)
    write_utf8(analysis_dir / "01-analysis.md", customize_analysis_template(config.label))
    write_utf8(analysis_dir / "02-followup.md", read_utf8(TEMPLATE_DIR / "02-followup.md"))
    create_transcript_parts(analysis_dir, args.transcript_parts)
    write_utf8(
        analysis_dir / "03-prompt-bundle.md",
        render_bundle(args.mode, analysis_dir, intake_text),
    )

    print(f"created: {analysis_dir}")
    print(f"bundle:  {analysis_dir / '03-prompt-bundle.md'}")
    return 0


def rebuild_bundle(args: argparse.Namespace) -> int:
    analysis_dir = resolve_workspace_path(args.analysis_dir)
    intake_path = analysis_dir / "00-intake.md"

    if not intake_path.exists():
        print(f"error: missing intake file: {intake_path}", file=sys.stderr)
        return 1

    intake_text = read_utf8(intake_path)
    bundle_path = analysis_dir / "03-prompt-bundle.md"
    write_utf8(bundle_path, render_bundle(args.mode, analysis_dir, intake_text))

    print(f"bundle: {bundle_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scaffold YouTube transcript analyses and connect prompts into a ready bundle.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser(
        "new",
        help="Create an analysis folder with intake, output templates, and a prompt bundle.",
    )
    new_parser.add_argument("--title", required=True, help="Video title shown inside intake.")
    new_parser.add_argument(
        "--channel",
        default="unknown-channel",
        help="Channel name shown inside intake.",
    )
    new_parser.add_argument(
        "--mode",
        choices=tuple(MODE_CONFIGS.keys()),
        default="full",
        help="Bundle mode to generate.",
    )
    new_parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Folder date prefix in YYYY-MM-DD format.",
    )
    new_parser.add_argument(
        "--length",
        default="",
        help="Video duration to prefill inside intake.",
    )
    new_parser.add_argument(
        "--uploaded",
        default="",
        help="Upload date to prefill inside intake.",
    )
    new_parser.add_argument(
        "--level",
        default="초보 / 실무자 / 팀 리드",
        help="Reader level to prefill inside intake.",
    )
    new_parser.add_argument(
        "--transcript-parts",
        type=int,
        default=0,
        help="Create transcript part files instead of storing the script inline.",
    )
    new_parser.add_argument(
        "--channel-slug",
        help="ASCII-safe slug for the folder name. Falls back to a generated slug.",
    )
    new_parser.add_argument(
        "--video-slug",
        help="ASCII-safe video slug for the folder name. Falls back to a generated slug.",
    )
    new_parser.add_argument(
        "--output-root",
        default=str(DEFAULT_ANALYSES_ROOT),
        help="Where analysis folders should be created.",
    )
    new_parser.add_argument(
        "--force",
        action="store_true",
        help="Reuse the target folder if it already exists.",
    )
    new_parser.set_defaults(handler=scaffold_analysis)

    bundle_parser = subparsers.add_parser(
        "bundle",
        help="Regenerate the prompt bundle from an existing analysis folder.",
    )
    bundle_parser.add_argument("analysis_dir", help="Existing analysis directory.")
    bundle_parser.add_argument(
        "--mode",
        choices=tuple(MODE_CONFIGS.keys()),
        required=True,
        help="Bundle mode to generate.",
    )
    bundle_parser.set_defaults(handler=rebuild_bundle)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
