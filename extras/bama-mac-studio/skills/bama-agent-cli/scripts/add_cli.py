#!/usr/bin/env python3
"""Version-Timestamp: 2026-10-27 07:44:20 AST. Add app-local agent code only."""
import argparse
import re
import shutil
import sys
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description='Add opt-in app-local CLI/MCP code. No global links or registration.')
    parser.add_argument('app_folder')
    parser.add_argument('cli_name')
    args=parser.parse_args()
    if not re.fullmatch(r'[a-z][a-z0-9-]{0,47}',args.cli_name):
        parser.error('cli name must be lowercase letters, digits and hyphens')
    root=Path(args.app_folder).expanduser().resolve(strict=True)
    apps=[p for p in (root/'Sources').iterdir() if p.is_dir() and (p/'App.swift').is_file()]
    if len(apps)!=1: parser.error('expected exactly one app target with App.swift')
    src=apps[0]; name=src.name
    if (src/'Agent').exists() or (src/'Main.swift').exists(): parser.error('Agent or Main.swift already exists; refusing overwrite')
    app=(src/'App.swift').read_text();content=(src/'ContentView.swift').read_text()
    appnew,count=re.subn(r'^@main\s*\n', '', app, count=1,flags=re.M)
    if count!=1: parser.error('App.swift needs one @main entry to replace')
    if '.task {' not in content: parser.error('ContentView.swift needs the template task lifecycle')
    contentnew=content.replace('.task {','.task {\n            AgentRouter.model = model\n            AgentSocket.listen { AgentRouter.handle($0) }',1)
    template=Path(__file__).resolve().parent.parent/'template'
    files={src/'Agent'/p.name:p.read_text().replace('__APP_NAME__',name).replace('__CLI_NAME__',args.cli_name) for p in (template/'Agent').glob('*.swift')}
    files[src/'Main.swift']=(template/'Main.swift').read_text().replace('__APP_NAME__',name)
    try:
        (src/'Agent').mkdir()
        for path,data in files.items(): path.write_text(data)
        (src/'App.swift').write_text(appnew);(src/'ContentView.swift').write_text(contentnew)
    except Exception:
        (src/'App.swift').write_text(app);(src/'ContentView.swift').write_text(content)
        for path in files:
            if path.is_file(): path.unlink()
        if (src/'Agent').is_dir(): (src/'Agent').rmdir()
        raise
    print(f'added app-local CLI {args.cli_name}; no PATH link or MCP registration changed')
    print('Build the staged app, then enable the local server explicitly with APP_AGENT_ENABLED=1.')
    print('Write commands additionally require APP_AGENT_WRITES=1; same-user processes share this trust boundary.')

if __name__=='__main__':
    try: main()
    except OSError as error:
        print(f'CLI addition failed: {error}',file=sys.stderr);raise SystemExit(1)
