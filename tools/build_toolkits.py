"""Build/check integrity for optional two-host toolkit plugins.

Version-Timestamp: 2026-10-27 07:48:54 AST
"""
import argparse
import json
import re
from pathlib import Path

from build_plugin import BuildError, checked_root, digest, output_path, regular_files, replace, sha_lines

NAME = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def toolkit(repo, name, apply=False):
    if not NAME.fullmatch(name):
        raise BuildError('invalid plugin name')
    root = checked_root(checked_root(repo, 'repository') / 'extras' / name, 'toolkit')
    files = regular_files(root)
    manifests = []
    for host in ('.claude-plugin', '.codex-plugin'):
        try:
            data = json.loads(files[host + '/plugin.json'])
        except (KeyError, ValueError) as exc:
            raise BuildError('missing or invalid host manifest') from exc
        if not isinstance(data, dict):
            raise BuildError('host manifest must be an object')
        if data.get('name') != name:
            raise BuildError('host name mismatch')
        if data.get('skills', './skills/') != './skills/':
            raise BuildError('both hosts must load the shared ./skills/ tree')
        manifests.append(data)
    if not manifests[0].get('version') or manifests[0].get('version') != manifests[1].get('version'):
        raise BuildError('host version mismatch')
    if 'LICENSE' not in files:
        raise BuildError('missing upstream LICENSE')
    skills = sorted(path for path in files if re.fullmatch(r'skills/[^/]+/SKILL.md', path))
    all_entries = sorted(path for path in files if path.startswith('skills/') and path.endswith('/SKILL.md'))
    if not skills or all_entries != skills:
        raise BuildError('skills must be nonempty and use one immediate folder per entry')
    for path in skills:
        body = files[path].decode('utf-8')
        frontmatter = body.split('---', 2)
        match = re.search(r'^name:\s*([^\s]+)\s*$', frontmatter[1], re.M) if len(frontmatter) == 3 else None
        if not match or match.group(1) != Path(path).parent.name:
            raise BuildError('skill name differs from folder: ' + path)
    files.pop('PAYLOAD.sha256', None)
    expected = sha_lines(files).encode('utf-8')
    target = output_path(root, 'PAYLOAD.sha256')
    if apply:
        replace(target, expected)
    if not target.is_file() or target.read_bytes() != expected:
        raise BuildError('payload missing or changed: ' + name)
    return {'name': name, 'version': manifests[0]['version'], 'files': len(files),
            'skills': len(skills), 'payload_sha256': digest(expected), 'valid': True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--plugin', action='append', help='Optional companion name; repeatable')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--apply', action='store_true')
    group.add_argument('--check', action='store_true')
    args = parser.parse_args(argv)
    try:
        results = [toolkit(args.repo, name, args.apply) for name in
                   (args.plugin or ['bama-mac-studio', 'rea-toolkit'])]
    except (BuildError, OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({'valid': False, 'error': str(exc)}))
        return 1
    print(json.dumps({'valid': True, 'toolkits': results}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
