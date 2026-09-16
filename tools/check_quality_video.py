#!/usr/bin/env python3
# Version-Timestamp: 2026-09-16T18:33:30.738440-04:00
from playwright.sync_api import sync_playwright
from pathlib import Path
import json,hashlib,datetime,argparse
p=argparse.ArgumentParser(description="Observe complete browser playback and sampled decoded-frame branding. Not all-frame or hardware certification.")
p.add_argument('--base-url',required=True);p.add_argument('--video-file',required=True,type=Path);p.add_argument('--report',required=True,type=Path);a=p.parse_args()
if a.report.exists():raise SystemExit('Refusing to overwrite report')
video=a.video_file.resolve(strict=True)
with sync_playwright() as p:
 b=p.chromium.launch()
 page=b.new_page(viewport={"width":1280,"height":720})
 page.goto(a.base_url.rstrip('/')+'/')
 served_sha=page.evaluate("""async()=>{const r=await fetch('exports/tidal-motion.webm');if(!r.ok)throw new Error('video fetch failed');const h=await crypto.subtle.digest('SHA-256',await r.arrayBuffer());return [...new Uint8Array(h)].map(v=>v.toString(16).padStart(2,'0')).join('')}""")
 expected_sha=hashlib.sha256(video.read_bytes()).hexdigest()
 if served_sha!=expected_sha:raise RuntimeError('Served video differs from the supplied local file')
 r=page.evaluate("""async()=>{
 const v=document.createElement('video'); v.src='exports/tidal-motion.webm';v.muted=true;v.playsInline=true; document.body.replaceChildren(v);
 const c=document.createElement('canvas');c.width=1280;c.height=720;const x=c.getContext('2d',{willReadFrequently:true}); let counts=[],frames=0;
 let timer;return await new Promise(async(resolve,reject)=>{
 timer=setTimeout(()=>reject(new Error('playback timeout')),25000);
 v.onerror=()=>reject(new Error('decode failed'));
 function sample(now,m){x.drawImage(v,0,0,1280,720);const d=x.getImageData(64,43,130,66).data;let n=0;for(let i=0;i<d.length;i+=4){if(d[i]>230&&d[i+1]>230&&d[i+2]>230)n++};counts.push(n);frames++;if(!v.ended)v.requestVideoFrameCallback(sample);}
 v.onended=()=>{clearTimeout(timer);resolve({duration:v.duration,width:v.videoWidth,height:v.videoHeight,ended:v.ended,decodedCallbacks:frames,brandPixelsMin:Math.min(...counts),brandPixelsMax:Math.max(...counts)})};
 v.requestVideoFrameCallback(sample);await v.play();
 });} """)
 b.close()
r['served_sha256']=served_sha
r.update({"Version-Timestamp":datetime.datetime.now().astimezone().isoformat(),"sha256":hashlib.sha256(video.read_bytes()).hexdigest(),"scope":"Full clock playback and sampled decoded-frame brand region; no hardware or aesthetic acceptance"})
r['wordmark_region']={'x':64,'y':43,'width':130,'height':66,'channel_threshold_exclusive':230,'minimum_pixels':2000}
r['expected_source_frames']=288
r['callback_limit']='requestVideoFrameCallback may omit frames including the initial frame; callback count is observations, not an all-decoded-frames claim.'
with a.report.open('x') as report: report.write(json.dumps(r,indent=2)+'\n')
print(json.dumps(r));assert r['ended'] and r['duration']==12 and r['brandPixelsMin']>2000
