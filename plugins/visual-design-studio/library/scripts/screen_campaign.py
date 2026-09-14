"""Deterministic, offline SVG campaign fixture builder. No player deployment."""
# Version-Timestamp: 2026-09-11 20:20:00 AST
import argparse
import datetime
import hashlib
import html
import json
import re
import shutil
from pathlib import Path

SIZES = {'wide': (1920,480), 'portrait':(1080,1920), 'strip':(1920,160)}

def validate(data):
    if not isinstance(data,dict):raise ValueError('campaign must be an object')
    expected={'Version-Timestamp','id','brand','headline','subtitle','background','foreground','accent','variants'}
    if set(data)!=expected:raise ValueError('missing or unknown campaign fields')
    if not isinstance(data['id'],str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,47}',data['id']):raise ValueError('invalid id')
    for key,limit in [('brand',12),('subtitle',65)]:
        value=data[key]
        if not isinstance(value,str) or not value.strip() or len(value)>limit or any(ord(c)<32 for c in value):raise ValueError(f'invalid {key}')
    lines=data['headline']
    if not isinstance(lines,list) or not 1<=len(lines)<=2 or any(not isinstance(s,str) or not s.strip() or len(s)>22 or any(ord(c)<32 for c in s) for s in lines):raise ValueError('headline requires one or two short, explicit lines')
    for key in ['background','foreground','accent']:
        if not isinstance(data[key],str) or not re.fullmatch(r'#[0-9A-Fa-f]{6}',data[key]):raise ValueError(f'invalid {key}')
    variants=data['variants']
    if not isinstance(variants,list) or not variants or any(not isinstance(v,str) or v not in SIZES for v in variants) or len(set(variants))!=len(variants):raise ValueError('invalid variants')
    try:
        dt=datetime.datetime.fromisoformat(data['Version-Timestamp'])
        if dt.tzinfo is None:raise ValueError()
    except (ValueError,TypeError):raise ValueError('timestamp requires timezone') from None

def svg(data,kind):
    w,h=SIZES[kind];bg,fg,ac=[data[k] for k in ['background','foreground','accent']]
    esc=html.escape
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">',f'<title id="title">{esc(data["brand"])} fictional screen study, {kind}</title>',f'<!-- Version-Timestamp: {esc(data["Version-Timestamp"])} -->',f'<rect width="{w}" height="{h}" fill="{bg}"/>']
    def text(x,y,size,value,font='Arial, sans-serif',color=fg,spacing=0):
        parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" letter-spacing="{spacing}">{esc(value)}</text>')
    if kind=='strip':
        text(55,105,64,data['brand'],spacing=5)
        parts.append(f'<path d="M420 34V126" stroke="{ac}"/>')
        text(485,102,58,' '.join(data['headline']),font='Georgia, serif')
        text(1435,95,20,'FICTIONAL / STILL WATER',color=ac)
    else:
        portrait=kind=='portrait';x=70 if portrait else 80
        text(x,110 if portrait else 90,34,data['brand'],spacing=7)
        top=285 if portrait else 207;fs=100 if portrait else 94
        for i,line in enumerate(data['headline']):text(x,top+i*(fs+5),fs,line,font='Georgia, serif')
        text(x,540 if portrait else 403,18,data['subtitle'],spacing=2)
        # Original schematic product illustration, not a real product photograph.
        px,py,scale=(390,760,2.4) if portrait else (1390,52,0.93)
        parts.append(f'<g transform="translate({px} {py}) scale({scale})"><rect x="25" y="0" width="110" height="34" rx="8" fill="{ac}"/><path d="M30 34H130V80Q160 100 160 130V342Q160 372 130 372H30Q0 372 0 342V130Q0 100 30 80Z" fill="{fg}"/><path d="M12 146H148V283H12Z" fill="{ac}"/>')
        text(29,207,28,data['brand'],color=bg,spacing=2)
        text(29,244,10,'STILL WATER',color=bg,spacing=1)
        parts.append('</g>')
        if portrait:
            text(70,1790,18,'ORIGINAL VECTOR STUDY',color=ac,spacing=2)
            parts.append(f'<path d="M70 1830H1010" stroke="{ac}"/>')
        else:parts.append(f'<circle cx="1790" cy="92" r="20" fill="{ac}"/>')
    return '\n'.join(parts+['</svg>'])+'\n'

def build(data,destination):
    validate(data);destination=Path(destination)
    if destination.exists() or destination.is_symlink():raise ValueError('destination exists; choose a new version directory')
    outputs={kind+'.svg':svg(data,kind).encode() for kind in data['variants']}
    outputs['campaign.json']=(json.dumps(data,indent=2,ensure_ascii=False)+'\n').encode()
    manifest={'Version-Timestamp':data['Version-Timestamp'],'id':data['id'],'status':'candidate','files':{name:hashlib.sha256(payload).hexdigest() for name,payload in outputs.items()}}
    # Exclusive directory creation prevents overwriting a previous or concurrent build.
    try:destination.mkdir(parents=True,exist_ok=False)
    except FileExistsError:raise ValueError('destination exists') from None
    try:
        for name,payload in outputs.items():(destination/name).write_bytes(payload)
        (destination/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    except BaseException:
        shutil.rmtree(destination)
        raise
    return manifest

def verify(destination):
    p=Path(destination);errors=[]
    if p.is_symlink():return ['symlink destination rejected']
    try:
        mf=p/'manifest.json'
        if mf.is_symlink():return ['symlink manifest rejected']
        manifest=json.loads(mf.read_text())
        files=manifest['files']
        if not isinstance(files,dict) or not files:return ['invalid files manifest']
        source=p/'campaign.json'
        if source.is_symlink():return ['unsafe campaign source']
        campaign=json.loads(source.read_text());validate(campaign)
        expected={'campaign.json'}|{v+'.svg' for v in campaign['variants']}
        if set(files)!=expected:errors.append('manifest does not match campaign variants')
        if manifest.get('id')!=campaign['id'] or manifest.get('Version-Timestamp')!=campaign['Version-Timestamp'] or manifest.get('status')!='candidate':errors.append('manifest metadata mismatch')
        for name,digest in files.items():
            if name not in {'campaign.json','wide.svg','portrait.svg','strip.svg'} or not isinstance(digest,str) or not re.fullmatch('[a-f0-9]{64}',digest):
                errors.append('invalid manifest entry');continue
            f=p/name
            if f.is_symlink() or not f.is_file():errors.append(f'missing or unsafe {name}');continue
            if hashlib.sha256(f.read_bytes()).hexdigest()!=digest:errors.append(f'hash mismatch {name}')
        for f in p.iterdir():
            if f.name not in files and f.name!='manifest.json':errors.append(f'unexpected {f.name}')
    except (OSError,ValueError,KeyError,TypeError):errors.append('unreadable or malformed manifest')
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    b=sub.add_parser('build');b.add_argument('source',type=Path);b.add_argument('destination',type=Path)
    v=sub.add_parser('verify');v.add_argument('destination',type=Path)
    args=parser.parse_args()
    try:
        if args.action=='build':result=build(json.loads(args.source.read_text()),args.destination);print(json.dumps({'built':str(args.destination),'status':result['status']}));return 0
        errors=verify(args.destination);print(json.dumps({'valid':not errors,'errors':errors}));return bool(errors)
    except (OSError,ValueError) as exc:print(json.dumps({'valid':False,'error':str(exc)}));return 1
if __name__=='__main__':raise SystemExit(main())
