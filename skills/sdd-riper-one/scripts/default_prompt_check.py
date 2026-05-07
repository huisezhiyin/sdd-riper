#!/usr/bin/env python3
"""Check and optionally install minimal SDD-RIPER default prompt routing."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PROMPT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    ".cursorrules",
]


def has_route(text: str, route: str) -> bool:
    if route == "sdd-riper-one":
        patterns = [
            r"(?:Use|使用|默认使用)[^\n]*`?sdd-riper-one`?(?!-light)",
            r"`sdd-riper-one`\s*(?:负责|是|:|：)",
        ]
        return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)
    patterns = [
        r"(?:Use|使用|默认使用)[^\n]*`?sdd-riper-one-light`?",
        r"`sdd-riper-one-light`\s*(?:负责|是|:|：)",
        r"日常[^\n]*sdd-riper-one-light",
    ]
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def prompt_section(mode: str) -> str:
    if mode == "light":
        return """## AI Coding Harness

- 日常中等及以上 coding 任务默认使用 `sdd-riper-one-light`。
- light 默认用户已拆好任务；agent 只做目标复述、最小 spec/micro-spec、checkpoint、validation、handoff。
- 任务明显过大、边界不清、高风险或需要 codemap/context/频繁阻塞时，建议切到 `sdd-riper-one`。
- 不要裸改：中等以上任务执行前先说明目标、边界、下一步、风险和验证方式。
- 完成必须由测试、日志、运行结果或人工确认等证据证明。
- 不提交本地记忆、trace、SQLite/Milvus、密钥或机器私有路径。
"""
    return """## AI Coding Harness

- 复杂、高风险、陌生代码库、需求不清、需要交接/审计的任务，使用 `sdd-riper-one`。
- 日常已拆好的中低风险任务，使用 `sdd-riper-one-light`。
- `sdd-riper-one` 负责澄清最终目标、生成/引用 codemap/context、拆分最小混沌单元、维护完整 spec、阶段门禁和重度留痕。
- `sdd-riper-one-light` 负责目标复述、最小 spec/micro-spec、checkpoint、validation、进度汇报和中度留痕。
- 中等以上任务不要裸改；执行前必须有目标、边界、风险、验证方式和 checkpoint。
- 高风险或不可逆操作必须先暂停并等待用户确认。
- 完成必须由测试、日志、运行结果或人工确认等证据证明。
- 不提交本地记忆、trace、SQLite/Milvus、密钥或机器私有路径。
"""


def scan(root: Path, mode: str) -> dict:
    files = []
    any_required = False
    any_visible = False

    for rel in PROMPT_FILES:
        path = root / rel
        exists = path.exists()
        any_visible = any_visible or exists
        text = path.read_text(encoding="utf-8", errors="ignore") if exists else ""
        has_light = has_route(text, "sdd-riper-one-light")
        has_one = has_route(text, "sdd-riper-one")
        if mode == "light":
            has_required = has_light
        else:
            has_required = has_light and has_one
        any_required = any_required or has_required
        files.append(
            {
                "path": rel,
                "exists": exists,
                "has_sdd_riper_one": has_one,
                "has_sdd_riper_one_light": has_light,
                "has_required_route": has_required,
            }
        )

    existing = [f["path"] for f in files if f["exists"]]
    target = existing[0] if existing else "AGENTS.md"
    action = "none" if any_required else "ask_user"
    return {
        "root": str(root),
        "mode": mode,
        "checked": files,
        "system_prompt_visible": False,
        "system_prompt_note": "Only project-visible prompt files can be checked by this script.",
        "has_required_route": any_required,
        "has_any_prompt_file": any_visible,
        "recommended_target": target,
        "recommended_action": action,
        "section": prompt_section(mode),
    }


def apply_section(root: Path, target: str, mode: str, force: bool = False) -> dict:
    path = root / target
    path.parent.mkdir(parents=True, exist_ok=True)
    section = prompt_section(mode).rstrip() + "\n"
    if path.exists():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not force and "## AI Coding Harness" in text and (
            has_route(text, "sdd-riper-one-light")
            if mode == "light"
            else has_route(text, "sdd-riper-one-light") and has_route(text, "sdd-riper-one")
        ):
            return {"changed": False, "target": target, "reason": "required route already exists"}
        sep = "" if text.endswith("\n") else "\n"
        path.write_text(text + sep + "\n" + section, encoding="utf-8")
        return {"changed": True, "target": target, "reason": "appended section"}
    path.write_text("# Project Agent Instructions\n\n" + section, encoding="utf-8")
    return {"changed": True, "target": target, "reason": "created file"}


def markdown_report(result: dict) -> str:
    lines = [
        "# Default Prompt Check",
        "",
        f"- Root: `{result['root']}`",
        f"- Mode: `{result['mode']}`",
        f"- Required route found: `{result['has_required_route']}`",
        f"- Recommended target: `{result['recommended_target']}`",
        f"- Recommended action: `{result['recommended_action']}`",
        "- System prompt: not visible to this script; ask the user if system-level rules need syncing.",
        "",
        "## Files",
    ]
    for item in result["checked"]:
        lines.append(
            f"- `{item['path']}`: exists={item['exists']}, "
            f"one={item['has_sdd_riper_one']}, light={item['has_sdd_riper_one_light']}"
        )
    if not result["has_required_route"]:
        lines.extend(
            [
                "",
                "## Suggested Minimal Section",
                "",
                "```markdown",
                result["section"].rstrip(),
                "```",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root to scan")
    parser.add_argument("--mode", choices=["light", "one", "both"], default="one")
    parser.add_argument("--apply", action="store_true", help="Write the minimal prompt section after user approval")
    parser.add_argument("--target", help="Target prompt file, e.g. AGENTS.md")
    parser.add_argument("--force", action="store_true", help="Append even if a harness section exists")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    mode = "one" if args.mode == "both" else args.mode
    result = scan(root, mode)
    if args.apply:
        target = args.target or result["recommended_target"]
        result["apply_result"] = apply_section(root, target, mode, force=args.force)
        result = scan(root, mode) | {"apply_result": result["apply_result"]}

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(markdown_report(result))
        if args.apply and "apply_result" in result:
            print("\n## Apply Result")
            print(json.dumps(result["apply_result"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
