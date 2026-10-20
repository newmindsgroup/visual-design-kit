"""Validate Visual Design Studio packaging for Claude Code, claude.ai, Claude Desktop and Codex.

Version-Timestamp: 2026-10-20 02:05:00 UTC

Checks:
- manifests exist and versions agree (.claude-plugin, .codex-plugin, both marketplaces)
- registered skills: claude.ai-compatible frontmatter, name rules, description budget, body length,
  catalog coverage line with real catalog IDs
- every relative Markdown link in the plugin resolves
- no top-level bin/ directory (claude.ai and Cowork refuse plugins that have one)

Usage: python3 tools/validate_plugin.py [--repo PATH] [--json]
Standard library only.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
DESCRIPTION_LIMIT = 1024
DESCRIPTION_TARGET = 600
LISTING_WARN = 9000
BODY_LIMIT = 500
SKIP_DIRS = {"node_modules", "dist", ".astro", "qa-output", "results", "test-results", "playwright-report"}
CONTINUITY_SKILL = "design-project-start"


def parse_frontmatter(text):
    """Parse the small YAML subset used in SKILL.md frontmatter. Returns (dict, body)."""
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    lines = text[4:end].split("\n")
    data, index = {}, 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if line.startswith((" ", "\t")):
            raise ValueError(f"unexpected indentation: {line!r}")
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value in {">", ">-", "|", "|-"}:
            block = []
            index += 1
            while index < len(lines) and (lines[index].startswith("  ") or not lines[index].strip()):
                block.append(lines[index].strip())
                index += 1
            joiner = " " if value.startswith(">") else "\n"
            data[key] = joiner.join(part for part in block if part).strip()
            continue
        if value == "":
            nested = {}
            index += 1
            while index < len(lines) and lines[index].startswith("  "):
                sub_key, _, sub_value = lines[index].strip().partition(":")
                nested[sub_key.strip()] = sub_value.strip().strip('"').strip("'")
                index += 1
            data[key] = nested
            continue
        data[key] = value.strip('"').strip("'")
        index += 1
    return data, text[end + 5:]


def links_in(text):
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for match in LINK.finditer(line):
            yield match.group(1)


def check_links(path, errors, root):
    for target in links_in(path.read_text(encoding="utf-8")):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        if not (path.parent / clean).exists():
            errors.append(f"{path.relative_to(root)}: broken link {target}")


def load_json(path, errors, root):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(root)}: {exc}")
        return None


def validate(repo):
    repo = repo.resolve()
    plugin = repo / "plugins" / "visual-design-studio"
    errors, warnings, info = [], [], {}

    claude = load_json(plugin / ".claude-plugin" / "plugin.json", errors, repo)
    codex = load_json(plugin / ".codex-plugin" / "plugin.json", errors, repo)
    market = load_json(repo / ".claude-plugin" / "marketplace.json", errors, repo)
    codex_market = load_json(repo / ".agents" / "plugins" / "marketplace.json", errors, repo)
    if claude and codex:
        if claude.get("name") != codex.get("name"):
            errors.append("plugin names differ between .claude-plugin and .codex-plugin")
        if claude.get("version") != codex.get("version"):
            errors.append(f"version mismatch: .claude-plugin {claude.get('version')} vs .codex-plugin {codex.get('version')}")
        info["version"] = claude.get("version")
    if market and claude:
        entries = {entry.get("name"): entry for entry in market.get("plugins", [])}
        entry = entries.get(claude.get("name"))
        if not entry:
            errors.append("root .claude-plugin/marketplace.json does not list visual-design-studio")
        else:
            if entry.get("version") not in (None, claude.get("version")):
                errors.append(f"marketplace entry version {entry.get('version')} != plugin version {claude.get('version')}")
            source = entry.get("source")
            if isinstance(source, str) and not (repo / source).is_dir():
                errors.append(f"marketplace source {source} does not exist")
        if market.get("metadata", {}).get("version") not in (None, claude.get("version")):
            errors.append("marketplace metadata.version does not match the plugin version")
        for name, entry in entries.items():
            source = entry.get("source")
            if isinstance(source, str) and not (repo / source / ".claude-plugin" / "plugin.json").is_file():
                errors.append(f"marketplace plugin {name} has no .claude-plugin/plugin.json at {source}")
    if codex_market and codex:
        names = {entry.get("name") for entry in codex_market.get("plugins", [])}
        if codex.get("name") not in names:
            errors.append(".agents/plugins/marketplace.json does not list the Codex plugin")

    if (plugin / "bin").exists():
        errors.append("plugins/visual-design-studio/bin exists; claude.ai chat and Cowork refuse plugins with bin/")

    catalog = load_json(plugin / "library" / "capabilities.json", errors, repo) or {"capabilities": []}
    catalog_ids = {item["id"] for item in catalog.get("capabilities", [])}

    skills_dir = plugin / "skills"
    listing = 0
    skill_names = []
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        folder = skill_md.parent.name
        rel = skill_md.relative_to(repo)
        try:
            meta, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        skill_names.append(folder)
        extra = set(meta) - ALLOWED_KEYS
        if extra:
            errors.append(f"{rel}: frontmatter keys not accepted by claude.ai uploads: {sorted(extra)}")
        name = meta.get("name", "")
        if name != folder:
            errors.append(f"{rel}: name '{name}' must equal folder '{folder}'")
        if not NAME.match(name) or len(name) > 64:
            errors.append(f"{rel}: name must be lowercase letters, digits and single hyphens, max 64 chars")
        if "claude" in name or "anthropic" in name:
            errors.append(f"{rel}: name must not contain 'claude' or 'anthropic'")
        description = meta.get("description", "")
        if not description:
            errors.append(f"{rel}: description is required")
        elif len(description) > DESCRIPTION_LIMIT:
            errors.append(f"{rel}: description is {len(description)} chars; limit {DESCRIPTION_LIMIT}")
        elif len(description) > DESCRIPTION_TARGET and folder != CONTINUITY_SKILL:
            warnings.append(f"{rel}: description is {len(description)} chars; target {DESCRIPTION_TARGET}")
        listing += len(name) + len(description)
        metadata = meta.get("metadata", {})
        if folder != CONTINUITY_SKILL and not (isinstance(metadata, dict) and metadata.get("version-timestamp")):
            errors.append(f"{rel}: metadata.version-timestamp is required")
        body_lines = len(body.splitlines())
        if body_lines > BODY_LIMIT:
            errors.append(f"{rel}: body is {body_lines} lines; keep SKILL.md under {BODY_LIMIT} and move depth to references/")
        if folder != CONTINUITY_SKILL:
            match = re.search(r"^Catalog IDs covered:\s*(.+)$", body, re.MULTILINE)
            if not match:
                errors.append(f"{rel}: missing 'Catalog IDs covered:' line")
            else:
                ids = [item.strip().rstrip(".") for item in match.group(1).split(",") if item.strip()]
                unknown = [item for item in ids if item not in catalog_ids]
                if unknown:
                    errors.append(f"{rel}: unknown catalog IDs {unknown}")
    for md in sorted(plugin.rglob("*.md")):
        if not any(part in SKIP_DIRS for part in md.relative_to(plugin).parts):
            check_links(md, errors, repo)
    info["skills"] = skill_names
    info["listing_chars"] = listing
    if listing > LISTING_WARN:
        warnings.append(f"skill listing is {listing} chars of names and descriptions; keep it under {LISTING_WARN}")
    return errors, warnings, info


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    errors, warnings, info = validate(args.repo)
    if args.json:
        print(json.dumps({"valid": not errors, "errors": errors, "warnings": warnings, **info}, indent=2))
    else:
        for line in errors:
            print(f"ERROR {line}")
        for line in warnings:
            print(f"WARN  {line}")
        status = "valid" if not errors else f"{len(errors)} error(s)"
        print(f"{status}: {len(info.get('skills', []))} registered skills, listing {info.get('listing_chars', 0)} chars, version {info.get('version')}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
