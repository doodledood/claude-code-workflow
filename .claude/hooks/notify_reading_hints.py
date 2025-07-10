#!/usr/bin/env python
"""
PostToolUse hook

• Triggered after a TodoWrite call succeeds
• Looks at payload.tool_response.newTodos[*] now marked 'in_progress'
• For every Read* directive emits a non-blocking reminder (stderr, exit 2)
"""

import json, os, re, sys

# ---------------------------------------------------------------- helpers ----
DOC_PATHS = {
    "ReadClaude"   : "CLAUDE.md",
    "ReadArchDocs" : "docs/codebase/architecture/",
    "ReadTestDocs" : "docs/codebase/quality_testing/",
    "ReadDataDocs" : "docs/codebase/data_domain/",
}

TEMPLATE_FOR_FILE = (
    "⚠️  You **MUST** read {path} in full before you proceed with this todo."
)

TEMPLATE_FOR_DIR = (
    "⚠️  You **MUST** read the relevant files in the directory {path} in before you proceed with this todo. Read only the relevant files unless you need to read the entire directory. Always read them in full."
)

def build_message(directive: str) -> str:
    """Return the full reminder line for one directive."""
    path = DOC_PATHS.get(directive)
    if not path:  # unknown ReadXDocs → generic fallback
        name = directive[4:-4] or "the relevant"
        path = f"the {name.lower()} docs"
    
    if os.path.isdir(path):
        return TEMPLATE_FOR_DIR.format(path=path)
    else:
        return TEMPLATE_FOR_FILE.format(path=path)

def collect_messages(todos: list) -> list[str]:
    """Collect reminder lines for all in-progress todos."""
    lines: list[str] = []
    for t in todos:
        if (t.get("status") or "").lower().replace("-", "_") != "in_progress":
            continue
        for block in re.findall(r"\[[^\]]+]", t.get("content", "")):
            for directive in (d.strip() for d in block[1:-1].split(",")):
                if directive.startswith("Skip"):
                    continue
                if directive.startswith("Read"):
                    lines.append(build_message(directive))
    # deduplicate while preserving order
    return list(dict.fromkeys(lines))

# ------------------------------------------------------------------ main -----
payload = json.load(sys.stdin)

if payload.get("tool_name") != "TodoWrite":
    sys.exit(0)

todos = (
    payload.get("tool_response", {}).get("newTodos")
    or payload.get("tool_input", {}).get("todos")
    or []
)
if not isinstance(todos, list):
    sys.exit(0)

reminders = collect_messages(todos)
if reminders:
    context = (
        "Because the current todo item includes reading directives, "
        "you must complete the following before proceeding:\n"
    )
    print(context + "\n".join(reminders), file=sys.stderr)
    sys.exit(2)                 # non-blocking notice to Claude

sys.exit(0)