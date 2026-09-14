"""Generate offline comparison specimens and check opaque sRGB token pairs."""
# Version-Timestamp: 2026-09-11T19:32:14-04:00
import argparse
import base64
import hashlib
import html
import json
import math
import re
from pathlib import Path
from datetime import datetime

def rgb(value):
    if not isinstance(value,str) or not re.fullmatch(r'#[0-9a-fA-F]{6}',value):
        raise ValueError('Expected opaque six-digit sRGB hex color')
    return [int(value[i:i+2],16)/255 for i in (1,3,5)]

def contrast(a,b):
    def luminance(value):
        v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb(value)]
        return sum(x*y for x,y in zip(v,[.2126,.7152,.0722]))
    x,y=sorted([luminance(a),luminance(b)])
    return (y+.05)/(x+.05)

def audit(data,previous=None):
    pairs=[];seen=set();palettes=set()
    for palette in data['palettes']:
        pid=palette['id']
        if not isinstance(pid,str) or not re.fullmatch(r'[a-z0-9-]+',pid) or pid in palettes:raise ValueError('Invalid or duplicate palette ID')
        palettes.add(pid)
        for value in palette['tokens'].values():rgb(value)
        for pair in palette['pairs']:
            ident=pid+'/'+pair['id']
            if ident in seen:raise ValueError('Duplicate pair ID')
            seen.add(ident)
            try:a,b=[palette['tokens'][pair[k]] for k in ['fg','bg']]
            except KeyError as exc:raise ValueError('Missing pair token') from exc
            minimum=pair['minimum']
            if isinstance(minimum,bool) or not isinstance(minimum,(int,float)) or not math.isfinite(minimum) or not 1<=minimum<=21:raise ValueError('Invalid contrast threshold')
            value=contrast(a,b)
            signature=hashlib.sha256(json.dumps([pair['fg'],pair['bg'],a,b,minimum],separators=(',',':')).encode()).hexdigest()
            pairs.append(dict(id=ident,ratio=value,minimum=minimum,passes=value>=minimum,signature=signature))
    old={x['id']:x['signature'] for x in (previous or {}).get('pairs',[])}
    now={x['id']:x['signature'] for x in pairs}
    changed=sorted(k for k in old.keys()|now.keys() if old.get(k)!=now.get(k)) if previous is not None else []
    return {'Version-Timestamp':datetime.now().astimezone().isoformat(timespec='seconds'),'scope':'Opaque sRGB pair arithmetic only. No font, composition, gradient, alpha, print or accessibility certification.','pairs':pairs,'affected_pairs':changed}

def render(data):
    report=audit(data);esc=lambda value:html.escape(str(value),quote=True)
    title=esc(data['title']);text=esc(data['text'])
    fonts=data.get('fonts',[{'label':'Serif','family':'Georgia, serif'},{'label':'Sans serif','family':'Arial, sans-serif'},{'label':'Monospace','family':'monospace'}])
    for font in fonts:
        if not re.fullmatch(r'[A-Za-z0-9 ,_-]+',font['family']):raise ValueError('Unsafe font family; use installed family names only')
    specimens=''.join(f'<article class="font" style="font-family:{esc(family)}"><p class="label">{esc(name)}</p><h2 data-wrap>{text}</h2><p data-wrap>Compare the options before you decide. Choose a clear direction, then refine the details.</p><p>Il1 O0 rn m · $1,234.56 · ¿Qué opción prefieres?</p><p class="note">System-family specimen. Exact font identity requires separate verification.</p></article>' for family,name in [(f['family'],f['label']) for f in fonts])
    boards=[]
    for palette in data['palettes']:
        pair=palette['pairs'][0] if palette['pairs'] else None
        if pair:
            fg,bg=[palette['tokens'][pair[k]] for k in ['fg','bg']]
            swatches=''.join(f'<li><span class="swatch" style="background:{value}"></span>{esc(key)} <code>{value}</code></li>' for key,value in palette['tokens'].items())
            boards.append(f'<article><div class="application" style="color:{fg};background:{bg}"><p class="label">{esc(palette["id"])}</p><h2 data-wrap>{text}</h2><p data-wrap>Same message. Different color relationships.</p></div><ul>{swatches}</ul></article>')
    rows=''.join(f'<tr><th scope="row">{esc(x["id"])}</th><td>{x["ratio"]:.2f}:1</td><td>{x["minimum"]}:1</td><td>{"Pass" if x["passes"] else "Revise"}</td></tr>' for x in report['pairs'])
    logo_sheet=''
    if data.get('logo_data'):
        uri=data['logo_data']
        if not re.fullmatch(r'data:image/(?:svg\+xml|png|jpeg);base64,[A-Za-z0-9+/=]+',uri):raise ValueError('Expected embedded image data')
        cells=''.join(f'<article style="background:{bg};padding:20px"><p style="color:{fg}">{size}px, unchanged source</p><img alt="Supplied logo at {size} pixels" src="{uri}" width="{size}"></article>' for bg,fg in [('#ffffff','#202722'),('#202722','#ffffff')] for size in [16,32,64,128])
        logo_sheet=f'<section><h2>Logo stress sheet</h2><p>Same supplied source at four sizes and two backgrounds. No unauthorized recoloring or simplification.</p><div class="grid">{cells}</div></section>'
    return f'''<!doctype html>
<!-- Version-Timestamp: {report['Version-Timestamp']} -->
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#f4f1e9;color:#202722;font:17px/1.6 system-ui,sans-serif}}main{{max-width:1200px;margin:auto;padding:clamp(20px,4vw,64px)}}h1{{font:clamp(2rem,5vw,4rem)/1.12 Georgia,serif;max-width:18ch;text-wrap:balance}}h2{{font-size:clamp(1.5rem,3vw,2.2rem);line-height:1.2;text-wrap:balance}}p{{text-wrap:pretty}}.intro{{max-width:65ch}}section{{margin:60px 0}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:24px}}article{{border-top:1px solid #747970;padding-top:16px;min-width:0}}.serif{{font-family:Georgia,serif}}.sans{{font-family:Arial,sans-serif}}.mono{{font-family:monospace}}.label{{font:12px/1.5 system-ui,sans-serif;text-transform:uppercase;letter-spacing:.1em}}.note{{font:13px/1.5 system-ui,sans-serif}}.application{{padding:24px;min-height:240px}}ul{{list-style:none;padding:0}}.swatch{{display:inline-block;width:22px;height:22px;border:1px solid #777;vertical-align:middle;margin-right:10px}}table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{text-align:left;padding:8px;border-bottom:1px solid #aaa;overflow-wrap:anywhere}}.mark{{width:100%;height:120px}}code{{font-size:12px}}@media print{{body{{background:white}}section{{break-inside:avoid}}}}
</style><main><p class="label">Design craft / synthetic comparison</p><h1>{title}</h1><p class="intro">An inspection workspace for typography, color and optical balance. These examples demonstrate comparisons, not an approved brand or tested audience response.</p>
<section><h2>One message, three type treatments</h2><div class="grid">{specimens}</div></section>
<section><h2>Color in a composition</h2><div class="grid">{''.join(boards)}</div></section>
<section><h2>Optical balance study</h2><div class="grid"><article><svg class="mark" viewBox="0 0 280 120" role="img" aria-label="Circle and triangle with equal geometric bounds"><circle cx="70" cy="60" r="35" fill="#202722"/><path d="M180 25 L215 95 L145 95 Z" fill="#202722"/></svg><p>Equal bounds. Notice how shape and negative space affect apparent weight.</p></article><article><svg class="mark" viewBox="0 0 280 120" role="img" aria-label="Proposed larger triangle for optical comparison"><circle cx="70" cy="60" r="35" fill="#202722"/><path d="M180 17 L220 97 L140 97 Z" fill="#202722"/></svg><p>Proposed optical adjustment. Compare at small sizes before choosing; larger is not automatically better.</p></article></div></section>
{logo_sheet}<section><h2>Declared color pairs</h2><p class="note">Numeric results apply only to these opaque sRGB colors and declared thresholds.</p><table><thead><tr><th>Pair</th><th>Ratio</th><th>Target</th><th>Result</th></tr></thead><tbody>{rows}</tbody></table></section>
<p class="note">Version-Timestamp: {report['Version-Timestamp']}</p></main></html>'''

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--previous',type=Path);p.add_argument('--report',type=Path,required=True);p.add_argument('--html',type=Path);p.add_argument('--logo',type=Path);args=p.parse_args()
    try:
        if args.html and args.html.resolve()==args.report.resolve():raise ValueError('Report and HTML outputs must differ')
        for output in [args.report,args.html]:
            if output and (output.exists() or output.resolve()==args.input.resolve()):raise ValueError('Output exists; choose a new versioned path')
        data=json.loads(args.input.read_text());prior=json.loads(args.previous.read_text()) if args.previous else None
        if args.logo:
            mime={'.svg':'svg+xml','.png':'png','.jpg':'jpeg','.jpeg':'jpeg'}.get(args.logo.suffix.lower())
            if not mime:raise ValueError('Logo must be SVG, PNG or JPEG')
            if args.logo.stat().st_size>5_000_000:raise ValueError('Logo exceeds 5 MB limit')
            data['logo_data']='data:image/'+mime+';base64,'+base64.b64encode(args.logo.read_bytes()).decode('ascii')
        result=audit(data,prior);page=render(data) if args.html else None
        with args.report.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
        if args.html:
            with args.html.open('x') as f:f.write(page)
    except (OSError,ValueError,KeyError,TypeError,IndexError) as exc:p.exit(1,f'Craft check failed: {exc}\n')
if __name__=='__main__':main()
