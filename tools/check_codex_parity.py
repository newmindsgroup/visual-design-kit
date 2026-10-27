#!/usr/bin/env python3
"""Check that Visual Design Studio works the same way in Codex as in Claude.

Version-Timestamp: 2026-10-23 18:00:00 UTC

Codex loads the plugin's skills through .codex-plugin/plugin.json and reads
maintainer skills from .agents/skills. It does not load the Claude agents in
plugins/visual-design-studio/agents/, so every skill that dispatches one must
also say how to do the work in a single context. This tool checks:

1. manifest   .codex-plugin/plugin.json exists, is valid JSON, has the same
              name as .claude-plugin/plugin.json and a "skills" path that
              resolves to a folder inside the plugin.
2. versions   .codex-plugin/plugin.json, .claude-plugin/plugin.json and the
              root .claude-plugin/marketplace.json (metadata.version and the
              plugin entry) carry one version; .agents/plugins/marketplace.json
              lists the plugin with a source path that exists.
3. skills     every folder under the "skills" path has a SKILL.md whose
              frontmatter has a name equal to the folder and a description.
4. fallback   every Markdown file in a skill that names a plugin agent (the
              file stems in agents/*.md, matched as whole hyphenated words)
              either contains a fallback marker or links to a Markdown file
              that does. A fallback marker is one of:
                - a Markdown heading that contains the word "fallback",
                  for example "## Single-context fallback (claude.ai chat ...)";
                - a line that starts (after any list marker or bold markup)
                  with "Without subagents" or "Single-context fallback".
5. mirror     .claude/skills is an exact copy of .agents/skills (the same
              comparison as tools/sync_agent_skills.py).

Warnings (do not fail the run): a root plugin.json next to .codex-plugin
(Codex does not merge the two files), and a "skills" path other than
"./skills/".

Usage:
    python3 tools/check_codex_parity.py [--repo PATH] [--json]

Exit codes: 0 all checks pass, 1 a check failed, 2 the repository layout
cannot be checked (no plugin folder, or a helper module is missing).
Standard library only; Python 3.9 compatible.
"""

import argparse
import filecmp
import importlib.util
import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
PLUGIN_REL = Path("plugins") / "visual-design-studio"
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s#]+)(?:#[^)\s]*)?(?:\s+\"[^\"]*\")?\)")
HEADING_MARKER = re.compile(r"^\s{0,3}#{1,6}\s.*\bfallback\b", re.IGNORECASE)
LINE_MARKER = re.compile(
    r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*|__)?\s*(?:without subagents|single-context fallback)",
    re.IGNORECASE,
)


class LayoutError(Exception):
    """The repository cannot be checked at all."""


def load_tool(name):
    path = TOOLS / f"{name}.py"
    if not path.is_file():
        raise LayoutError(f"helper module missing: tools/{name}.py")
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(f"_parity_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path, errors, repo):
    rel = path.relative_to(repo).as_posix()
    if not path.is_file():
        errors.append(f"{rel}: missing")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{rel}: invalid JSON ({exc})")
        return None


def check_manifest(repo, plugin, errors, warnings):
    """Returns (codex manifest or None, resolved skills dir or None)."""
    codex = read_json(plugin / ".codex-plugin" / "plugin.json", errors, repo)
    claude = read_json(plugin / ".claude-plugin" / "plugin.json", errors, repo)
    if (plugin / "plugin.json").is_file():
        warnings.append(
            f"{(PLUGIN_REL / 'plugin.json').as_posix()} exists next to .codex-plugin/plugin.json; "
            "Codex does not merge the two, so keep them identical or remove one"
        )
    if not isinstance(codex, dict):
        return None, None
    if isinstance(claude, dict) and codex.get("name") != claude.get("name"):
        errors.append(
            f".codex-plugin name {codex.get('name')!r} differs from .claude-plugin name {claude.get('name')!r}"
        )
    skills = codex.get("skills")
    if not isinstance(skills, str) or not skills.strip():
        errors.append('.codex-plugin/plugin.json: "skills" must be a path string such as "./skills/"')
        return codex, None
    if skills not in {"./skills/", "./skills"}:
        warnings.append(f'.codex-plugin/plugin.json: "skills" is {skills!r}; the kit expects "./skills/"')
    target = (plugin / skills).resolve()
    try:
        target.relative_to(plugin.resolve())
    except ValueError:
        errors.append(f'.codex-plugin/plugin.json: "skills" {skills!r} points outside the plugin')
        return codex, None
    if not target.is_dir():
        errors.append(f'.codex-plugin/plugin.json: "skills" {skills!r} is not a folder')
        return codex, None
    return codex, target


def check_versions(repo, plugin, codex, errors):
    claude = read_json(plugin / ".claude-plugin" / "plugin.json", [], repo)
    market = read_json(repo / ".claude-plugin" / "marketplace.json", errors, repo)
    name = (codex or {}).get("name") or (claude or {}).get("name") or PLUGIN_REL.name
    found = {}
    if isinstance(codex, dict):
        found[".codex-plugin/plugin.json"] = codex.get("version")
    if isinstance(claude, dict):
        found[".claude-plugin/plugin.json"] = claude.get("version")
    if isinstance(market, dict):
        found["marketplace metadata.version"] = (market.get("metadata") or {}).get("version")
        entries = [e for e in market.get("plugins", []) if isinstance(e, dict) and e.get("name") == name]
        if not entries:
            errors.append(f".claude-plugin/marketplace.json does not list {name}")
        else:
            found["marketplace plugin entry"] = entries[0].get("version")
    for label, value in found.items():
        if not value:
            errors.append(f"{label}: version is missing")
    values = {v for v in found.values() if v}
    if len(values) > 1:
        errors.append("version mismatch: " + ", ".join(f"{k} {v}" for k, v in found.items()))
    codex_market = read_json(repo / ".agents" / "plugins" / "marketplace.json", errors, repo)
    if isinstance(codex_market, dict):
        entries = [e for e in codex_market.get("plugins", []) if isinstance(e, dict) and e.get("name") == name]
        if not entries:
            errors.append(f".agents/plugins/marketplace.json does not list {name}")
        else:
            source = entries[0].get("source")
            path = source.get("path") if isinstance(source, dict) else source
            if not isinstance(path, str) or not (repo / path).is_dir():
                errors.append(f".agents/plugins/marketplace.json: source path {path!r} does not exist")
    return sorted(values)


def check_skills(repo, skills_dir, parse_frontmatter, errors):
    names = []
    for folder in sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith(".")):
        rel = (folder / "SKILL.md").relative_to(repo).as_posix()
        skill_md = folder / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{rel}: missing")
            continue
        try:
            meta, _ = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if meta.get("name") != folder.name:
            errors.append(f"{rel}: frontmatter name {meta.get('name')!r} must equal the folder {folder.name!r}")
        if not str(meta.get("description") or "").strip():
            errors.append(f"{rel}: frontmatter description is missing")
        names.append(folder.name)
    if not names:
        errors.append(f"{skills_dir.relative_to(repo).as_posix()}: no skill folders")
    return names


def agent_names(plugin):
    folder = plugin / "agents"
    if not folder.is_dir():
        return []
    return sorted(p.stem for p in folder.glob("*.md"))


def has_marker(text):
    return any(HEADING_MARKER.match(line) or LINE_MARKER.match(line) for line in text.splitlines())


def check_fallback(repo, plugin, skills_dir, agents, errors):
    """Every skill file that names an agent states, or links to, a fallback."""
    if not agents:
        return []
    pattern = re.compile(r"(?<![\w-])(" + "|".join(re.escape(a) for a in agents) + r")(?![\w-])")
    plugin_root = plugin.resolve()
    marker_cache = {}

    def marked(path):
        key = path.resolve()
        if key not in marker_cache:
            try:
                marker_cache[key] = has_marker(key.read_text(encoding="utf-8"))
            except OSError:
                marker_cache[key] = False
        return marker_cache[key]

    covered = []
    for path in sorted(skills_dir.rglob("*.md")):
        if any(part in {"node_modules", "results"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        mentioned = sorted(set(pattern.findall(text)))
        if not mentioned:
            continue
        rel = path.relative_to(repo).as_posix()
        if marked(path):
            covered.append(rel)
            continue
        linked = False
        for target in LINK.findall(text):
            if "://" in target or target.startswith("mailto:") or not target.endswith(".md"):
                continue
            dest = (path.parent / target).resolve()
            try:
                dest.relative_to(plugin_root)
            except ValueError:
                continue
            if dest.is_file() and marked(dest):
                linked = True
                break
        if linked:
            covered.append(rel)
        else:
            errors.append(
                f"{rel}: names plugin agent(s) {', '.join(mentioned)} but has no single-context fallback; "
                'add a "## Single-context fallback" section or a line starting "Without subagents", '
                "or link to a file in the skill that has one"
            )
    return covered


def check_mirror(repo, files_under, errors):
    source, mirror = repo / ".agents" / "skills", repo / ".claude" / "skills"
    src, dst = files_under(source), files_under(mirror)
    if not src:
        errors.append(".agents/skills: no maintainer skills found")
        return
    for rel in sorted(set(src) - set(dst)):
        errors.append(f"missing in .claude/skills: {rel} (run python3 tools/sync_agent_skills.py --apply)")
    for rel in sorted(set(dst) - set(src)):
        errors.append(f"only in .claude/skills (edit .agents/skills instead): {rel}")
    for rel in sorted(set(src) & set(dst)):
        if not filecmp.cmp(str(src[rel]), str(dst[rel]), shallow=False):
            errors.append(f".claude/skills/{rel} differs from .agents/skills (run python3 tools/sync_agent_skills.py --apply)")


def run(repo):
    repo = Path(repo).resolve()
    plugin = repo / PLUGIN_REL
    if not plugin.is_dir():
        raise LayoutError(f"{PLUGIN_REL.as_posix()} not found under {repo}")
    validate_plugin = load_tool("validate_plugin")
    sync = load_tool("sync_agent_skills")

    checks, warnings = {}, []
    manifest_errors = []
    codex, skills_dir = check_manifest(repo, plugin, manifest_errors, warnings)
    checks["manifest"] = manifest_errors

    version_errors = []
    versions = check_versions(repo, plugin, codex, version_errors)
    checks["versions"] = version_errors

    skill_errors, skills, agents, covered = [], [], agent_names(plugin), []
    fallback_errors = []
    if skills_dir is not None:
        skills = check_skills(repo, skills_dir, validate_plugin.parse_frontmatter, skill_errors)
        covered = check_fallback(repo, plugin, skills_dir, agents, fallback_errors)
    else:
        skill_errors.append("skipped: the Codex manifest has no usable skills path")
    checks["skills"] = skill_errors
    checks["fallback"] = fallback_errors

    mirror_errors = []
    check_mirror(repo, sync.files_under, mirror_errors)
    checks["mirror"] = mirror_errors

    errors = [f"[{name}] {msg}" for name, msgs in checks.items() for msg in msgs]
    return {
        "valid": not errors,
        "version": versions[0] if len(versions) == 1 else versions,
        "skills": len(skills),
        "agents": agents,
        "fallback_files": covered,
        "checks": {name: ("pass" if not msgs else "fail") for name, msgs in checks.items()},
        "errors": errors,
        "warnings": warnings,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check Codex parity for Visual Design Studio.")
    parser.add_argument("--repo", default=str(TOOLS.parent), help="repository root (default: this checkout)")
    parser.add_argument("--json", action="store_true", help="print the result as JSON")
    args = parser.parse_args(argv)
    try:
        result = run(args.repo)
    except LayoutError as exc:
        if args.json:
            print(json.dumps({"valid": False, "errors": [str(exc)], "layout": False}))
        else:
            print(f"layout error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for name, state in result["checks"].items():
            print(f"{state.upper():4}  {name}")
        for message in result["errors"]:
            print(f"error: {message}")
        for message in result["warnings"]:
            print(f"warning: {message}")
        print(
            f"{'OK' if result['valid'] else 'FAILED'}: version {result['version']}, {result['skills']} skills, "
            f"{len(result['agents'])} agents, {len(result['fallback_files'])} agent-naming files with a fallback"
        )
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
