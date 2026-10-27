#!/usr/bin/env python3
"""Version-Timestamp: 2026-10-27 07:44:20 AST. Isolated CLI/MCP contract check."""
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def main():
    if len(sys.argv)!=2: raise ValueError('pass exactly one staged executable path')
    binary=Path(sys.argv[1]).expanduser().resolve(strict=True)
    if not binary.is_file() or not os.access(binary, os.X_OK): raise ValueError('not an executable')
    root=Path(tempfile.mkdtemp(prefix='bama-test-')).resolve();root.chmod(0o700)
    (root/'.bama-test-root').write_text('BAMA isolated test root\n')
    env={**os.environ,'APP_TEST_ROOT':str(root),'APP_STORE':str(root/'test.store'),'APP_AGENT_SOCKET':str(root/'agent.sock'),'APP_AGENT_ENABLED':'1'}
    env.pop('APP_AGENT_WRITES',None)
    stdout=(root/'app.stdout.log').open('w');stderr=(root/'app.stderr.log').open('w')
    process=subprocess.Popen([str(binary)],env=env,stdout=stdout,stderr=stderr)
    results=[]
    def invoke(args,expected=0):
        result=subprocess.run([str(binary),*args],env=env,capture_output=True,text=True,timeout=20)
        results.append({'args':args,'exit':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
        if result.returncode!=expected: raise ValueError(f'{args}: expected {expected}, got {result.returncode}')
        return result.stdout
    try:
        for _ in range(100):
            if (root/'agent.sock').exists(): break
            if process.poll() is not None: raise ValueError('test app exited before socket readiness')
            time.sleep(.1)
        else: raise ValueError('test socket not ready within 10 seconds')
        schema=json.loads(invoke(['help','--json'])); commands=schema['commands']
        if not commands: raise ValueError('no commands')
        invoke(['no-such-command'],2)
        for command in commands:
            if command.get('readOnly') and not command['inputSchema'].get('required'):
                json.loads(invoke([*command['name'].split(),'--json','--no-launch']))
        # A valid write must be denied by the running app's default read-only boundary.
        if any(c['name']=='items add' for c in commands):
            invoke(['items','add','--title','Synthetic check','--json','--no-launch'],1)
        message='\n'.join([json.dumps({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-06-18','capabilities':{},'clientInfo':{'name':'isolated-check','version':'1'}}}),json.dumps({'jsonrpc':'2.0','id':2,'method':'tools/list'})])+'\n'
        mcp=subprocess.run([str(binary),'mcp'],input=message,env=env,capture_output=True,text=True,timeout=20)
        if mcp.returncode: raise ValueError('MCP contract failed')
        replies=[json.loads(line) for line in mcp.stdout.splitlines() if line.strip()]
        tools=next(x['result']['tools'] for x in replies if x.get('id')==2)
        if len(tools)!=len(commands): raise ValueError('MCP command coverage mismatch')
        print('PASS isolated CLI and MCP contract; writes denied by default')
        return 0
    finally:
        process.terminate()
        try: process.wait(timeout=10)
        except subprocess.TimeoutExpired: process.kill();process.wait(timeout=5)
        stdout.close();stderr.close()
        (root/'checks.json').write_text(json.dumps(results,indent=2)+'\n')
        print(f'BAMA_TEST_ROOT={root}; evidence retained; only the owned test process was stopped')

if __name__=='__main__':
    try: raise SystemExit(main())
    except (OSError,ValueError,subprocess.SubprocessError) as error:
        print(f'FAIL CLI check: {error}',file=sys.stderr);raise SystemExit(1)
