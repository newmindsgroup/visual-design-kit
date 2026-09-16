#!/usr/bin/env python3
# Version-Timestamp: 2026-09-16T18:27:08.062526-04:00
"""Render original fictional HTML specimens and a silent WebM from explicit frame times."""
import argparse,json,subprocess,io,hashlib,datetime
from PIL import Image
from pathlib import Path
from playwright.sync_api import sync_playwright

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--base-url',required=True);p.add_argument('--output',required=True,type=Path);p.add_argument('--ffmpeg',required=True);mode=p.add_mutually_exclusive_group();mode.add_argument('--video-only',action='store_true');mode.add_argument('--pdf-only',action='store_true');a=p.parse_args();a.output.mkdir(parents=True,exist_ok=False)
 # A new directory is required, so no export, frame, log or record can be overwritten.
 for name in (['tidal-motion.webm'] if a.video_only else ['tidal-motion.webm','form.pdf','tidal.pdf']):
  if (a.output/name).exists():raise SystemExit('Refusing existing export: '+name)
 with sync_playwright() as tool:
  browser=tool.chromium.launch();page=browser.new_page(viewport={'width':1440,'height':1000})
  for brand in ([] if a.video_only else ['form','tidal']):
   page.goto(a.base_url.rstrip('/')+'/specimen.html?brand='+brand);page.evaluate('document.fonts.ready')
   page.emulate_media(media='print');page.set_viewport_size({'width':1360,'height':1000})
   page.add_style_tag(content='@media print{.hero{break-inside:avoid}.details{break-inside:avoid}}')
   content_height=page.locator('footer').evaluate('(e)=>Math.ceil(e.getBoundingClientRect().bottom)')
   page_height=max(content_height+120,1120 if brand=='tidal' else 960)
   page.add_style_tag(content=f'@page{{size:1440px {page_height}px;margin:40px}}')
   page.pdf(path=str(a.output/(brand+'.pdf')),print_background=True,prefer_css_page_size=True,tagged=True,outline=True)
  if a.pdf_only:
   browser.close();return
  page.emulate_media(media='screen')
  page.set_viewport_size({'width':1280,'height':720});page.goto(a.base_url.rstrip('/')+'/motion.html?export=1');page.evaluate('document.fonts.ready');page.evaluate('window.motionReady')
  duration=12;fps=24;frames=duration*fps;wordmark_counts=[];log=(a.output/'encoding.log').open('w')
  command=[a.ffmpeg,'-f','image2pipe','-c:v','mjpeg','-r',str(fps),'-i','pipe:0','-c:v','libvpx','-b:v','4M','-an',str(a.output/'tidal-motion.webm')]
  proc=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=log,stderr=log)
  try:
   for n in range(frames):
    page.evaluate('(t) => new Promise(resolve => { window.setMotionTime(t); requestAnimationFrame(() => requestAnimationFrame(resolve)); })',n/fps)
    image_bytes=page.screenshot(type='jpeg',quality=95)
    im=Image.open(io.BytesIO(image_bytes)).convert('RGB')
    count=sum(1 for y in range(43,108) for x in range(64,193) if min(im.getpixel((x,y)))>200)
    wordmark_counts.append(count)
    if count<2000:raise RuntimeError('Wordmark disappeared at source frame '+str(n))
    proc.stdin.write(image_bytes)
    if n in [0,60,72,120,180,192,216,274,287]:page.screenshot(path=str(a.output/f'frame-{n:03}.png'))
   proc.stdin.close();code=proc.wait(timeout=60)
   if code:raise RuntimeError('Encoding failed; inspect encoding.log')
  finally:
   if proc.poll() is None:proc.kill()
   log.close();browser.close()
  (a.output/'render-record.json').write_text(json.dumps({'Version-Timestamp':datetime.datetime.now().astimezone().isoformat(),'video_sha256':hashlib.sha256((a.output/'tidal-motion.webm').read_bytes()).hexdigest(),'wordmark_region':{'x':64,'y':43,'width':129,'height':65,'channel_threshold_exclusive':200,'minimum_pixels':2000},'frames':frames,'fps':fps,'seconds':duration,'size':[1280,720],'source':'motion.html + motion.js + timeline.json','audio':False,'source_wordmark_pixels_min':min(wordmark_counts),'source_wordmark_pixels_max':max(wordmark_counts),'method':'Chromium frame render, JPEG95 input, VP8 WebM; desktop playback and device acceptance separate'},indent=2)+'\n')
if __name__=='__main__':main()
