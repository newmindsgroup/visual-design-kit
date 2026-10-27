#!/usr/bin/env python3
"""Version-Timestamp: 2026-10-27 07:44:20 AST. Staged build, optional explicit install."""
import argparse
import datetime
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(command):
    subprocess.run(command, check=True)


def main():
    parser = argparse.ArgumentParser(description='Build a staged app. Install and signing are explicit options.')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--no-icon', action='store_true', help='Compile without the optional Icon Composer output')
    parser.add_argument('--sign-identity', help='Explicit codesign identity; use - for ad hoc')
    parser.add_argument('--install', action='store_true', help='Install to ~/Applications, preserving a backup')
    parser.add_argument('--open', action='store_true', help='Open the staged or explicitly installed app; never quit another copy')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    name = '__APP_NAME__'
    configuration = 'debug' if args.debug else 'release'
    stage = root / '.build' / 'bama-stage'
    scratch = root / '.build' / 'bama-products'
    stage.mkdir(parents=True, exist_ok=True)
    if (root / 'Icon/AppIcon.icon').exists() and not args.no_icon:
        result = subprocess.run(['xcrun', '--find', 'actool'], capture_output=True, text=True)
        if result.returncode:
            parser.error('Icon Composer compilation requires full Xcode actool. Use --no-icon for a staged code build.')
        run(['zsh', str(root / 'tools/make_icon.sh')])
    run(['swift', 'build', '-c', configuration, '--package-path', str(root), '--scratch-path', str(scratch)])
    location = subprocess.check_output(['swift', 'build', '-c', configuration, '--package-path', str(root), '--scratch-path', str(scratch), '--show-bin-path'], text=True).strip()
    binary = Path(location) / name
    if not binary.is_file() or not os.access(binary, os.X_OK):
        raise RuntimeError('swift build returned without an executable product')
    work = Path(tempfile.mkdtemp(prefix='bundle-', dir=stage))
    app = work / f'{name}.app'
    contents = app / 'Contents'
    try:
        (contents / 'MacOS').mkdir(parents=True)
        (contents / 'Resources').mkdir()
        shutil.copy2(binary, contents / 'MacOS' / name)
        info = plistlib.loads((root / 'Info.plist.in').read_bytes().replace(b'__BUILD__', datetime.datetime.now().strftime('%Y%m%d%H%M').encode()))
        if args.no_icon:
            info.pop('CFBundleIconName', None)
            info.pop('CFBundleIconFile', None)
        (contents / 'Info.plist').write_bytes(plistlib.dumps(info))
        if not args.no_icon:
            for file in ('Assets.car', 'AppIcon.icns'):
                source = root / 'Resources' / file
                if not source.is_file():
                    raise RuntimeError(f'icon compilation produced no {file}')
                shutil.copy2(source, contents / 'Resources' / file)
        if args.sign_identity:
            run(['codesign', '--force', '--sign', args.sign_identity, str(app)])
            run(['codesign', '--verify', '--strict', str(app)])
        print(f'STAGED_APP={app}')
        print(f'STAGED_BINARY={contents / "MacOS" / name}')
        print(f'SIGNING={args.sign_identity or "unsigned"}')
        if args.install:
            applications = Path.home() / 'Applications'
            applications.mkdir(exist_ok=True)
            target = applications / f'{name}.app'
            if target.is_symlink():
                raise RuntimeError('refusing to replace a symlink at the installation path')
            staging = Path(tempfile.mkdtemp(prefix=f'.bama-{name}-', dir=applications))
            new = staging / target.name
            shutil.copytree(app, new)
            backup = None
            try:
                if target.exists():
                    backup = staging / f'{name}.previous.app'
                    target.rename(backup)
                new.rename(target)
            except Exception:
                if backup and backup.exists() and not target.exists():
                    backup.rename(target)
                raise
            print(f'INSTALLED_APP={target}')
            if backup:
                print(f'PRESERVED_BACKUP={backup}')
            app = target
        if args.open:
            run(['open', str(app)])
    except Exception:
        # Keep successful build/log evidence and any install backup for recovery.
        print(f'build artifacts preserved at {work}', file=sys.stderr)
        raise

if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f'build failed: {error}', file=sys.stderr)
        raise SystemExit(1)
