#!/usr/bin/env python3
"""Mirror maintainer skills from .agents/skills (canonical) to .claude/skills.

Version-Timestamp: 2026-10-23 13:05:00 AST

Codex discovers repository skills in .agents/skills; Claude Code discovers
them in .claude/skills. The canonical copy lives in .agents/skills. This
tool writes an exact byte copy to .claude/skills so both tools load the same
instructions without symlinks (which need extra rights on Windows).

Usage:
    python3 tools/sync_agent_skills.py           # check only (default)
    python3 tools/sync_agent_skills.py --apply   # rewrite the mirror

Exit codes: 0 in sync, 1 drift found (check mode), 2 bad layout.
Standard library only; Python 3.9 compatible.
"""

import argparse
import filecmp
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".agents" / "skills"
MIRROR = ROOT / ".claude" / "skills"
IGNORED = {"__pycache__", ".DS_Store"}


def files_under(base):
    out = {}
    if not base.is_dir():
        return out
    for path in sorted(base.rglob("*")):
        if any(part in IGNORED for part in path.relative_to(base).parts):
            continue
        if path.is_file():
            out[path.relative_to(base).as_posix()] = path
    return out


def drift():
    src, dst = files_under(SOURCE), files_under(MIRROR)
    missing = sorted(set(src) - set(dst))
    extra = sorted(set(dst) - set(src))
    changed = sorted(
        rel for rel in set(src) & set(dst)
        if not filecmp.cmp(str(src[rel]), str(dst[rel]), shallow=False)
    )
    return missing, extra, changed


def apply():
    if MIRROR.exists():
        shutil.rmtree(str(MIRROR))
    for rel, path in files_under(SOURCE).items():
        target = MIRROR / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(path), str(target))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="rewrite .claude/skills from .agents/skills")
    args = parser.parse_args(argv)

    if not files_under(SOURCE):
        print(json.dumps({"valid": False, "errors": ["no skills found in .agents/skills"]}))
        return 2
    if args.apply:
        apply()
    missing, extra, changed = drift()
    errors = (
        ["missing in .claude/skills: " + rel for rel in missing]
        + ["only in .claude/skills (edit .agents/skills instead): " + rel for rel in extra]
        + ["differs from .agents/skills: " + rel for rel in changed]
    )
    print(json.dumps({"applied": args.apply, "valid": not errors, "errors": errors}))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
