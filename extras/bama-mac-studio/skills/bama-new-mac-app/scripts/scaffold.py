#!/usr/bin/env python3
"""Version-Timestamp: 2026-10-27 07:44:20 AST. Adapted from MIT BAMA scaffold."""
import argparse
import re
import shutil
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Create a fresh BAMA app without Git or installation side effects.')
    parser.add_argument('name')
    parser.add_argument('bundle')
    parser.add_argument('parent', nargs='?', default='.')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Z][A-Za-z0-9]{0,63}', args.name):
        parser.error('AppName must be UpperCamelCase letters and digits, at most 64 characters')
    if not re.fullmatch(r'[A-Za-z][A-Za-z0-9-]*(?:\.[A-Za-z][A-Za-z0-9-]*)+', args.bundle):
        parser.error('bundle id must use reverse-DNS labels, such as com.example.tasks')
    parent = Path(args.parent).expanduser().resolve(strict=True)
    if not parent.is_dir():
        parser.error('parent must be an existing directory')
    dest = parent / args.name
    if dest.exists() or dest.is_symlink():
        parser.error('destination must be new; keep existing work and choose a new destination')
    template = Path(__file__).resolve().parent.parent / 'template'
    # Claim the destination atomically before entering cleanup scope.
    # A concurrent creator must never become this invocation's cleanup target.
    dest.mkdir(mode=0o700)
    owned = dest.lstat()
    try:
        shutil.copytree(template, dest, dirs_exist_ok=True)
        for old, new in [('Sources/__APP_NAME__', f'Sources/{args.name}'), ('Sources/__APP_NAME__Kit', f'Sources/{args.name}Kit'), ('Tests/__APP_NAME__KitTests', f'Tests/{args.name}KitTests')]:
            (dest / old).rename(dest / new)
        for path in dest.rglob('*'):
            if not path.is_file():
                continue
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            path.write_text(text.replace('__APP_NAME__', args.name).replace('__BUNDLE_ID__', args.bundle))
        for path in dest.rglob('*.sh'):
            path.chmod(path.stat().st_mode | 0o111)
    except Exception:
        # Only the fresh destination created by this invocation may be removed.
        try:
            current = dest.lstat()
        except OSError:
            pass
        else:
            if not dest.is_symlink() and (current.st_dev, current.st_ino) == (owned.st_dev, owned.st_ino):
                shutil.rmtree(dest)
        raise
    print(f'created {dest}; no Git, install, signing or launch action performed')
    print(f'next: cd "{dest}" && ./build.sh --no-icon')

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        print(f'scaffold failed: {error}', file=sys.stderr)
        raise SystemExit(1)
