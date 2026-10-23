"""Build a fictional static site with server-side publication filtering."""
# Version-Timestamp: 2026-09-11T20:58:31-04:00
import html
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'examples/website-practice'
ART='''<figure><svg viewBox="0 0 500 380" role="img" aria-label="Original schematic illustration of a chair"><g fill="none" stroke="#364d42" stroke-width="12" stroke-linejoin="round"><path d="M150 80H345V215H150Z M130 230H370V265H130Z M145 265L120 350 M355 265L380 350 M180 215V85 M230 215V85 M280 215V85 M330 215V85"/></g></svg><figcaption>ORIGINAL VECTOR STUDY / FICTIONAL WORK</figcaption></figure>'''
def render(records):
 if not isinstance(records,list):raise ValueError('records must be a list')
 output=[]
 for row in records:
  if not isinstance(row,dict) or set(row)!={'status','title','body','image'}:raise ValueError('invalid record fields')
  if row['status'] not in ['draft','published'] or not isinstance(row['image'],bool):raise ValueError('invalid record state')
  for k in ['title','body']:
   if not isinstance(row[k],str) or not row[k].strip() or len(row[k])>5000:raise ValueError('invalid text')
  if row['status']=='draft':continue
  output.append('<article class="story'+('' if row['image'] else ' no-image')+'">'+(ART if row['image'] else '')+'<div><h2>'+html.escape(row['title'])+'</h2><p>'+html.escape(row['body'])+'</p></div></article>')
 return (SOURCE/'template.html').read_text().replace('@@RECORDS@@',''.join(output))

def build(destination):
 destination=Path(destination)
 destination.mkdir(parents=True,exist_ok=False)
 records=[{'status':'published','title':'A familiar chair. A fresh chapter.','body':'This fictional case study explains the design approach without claiming real project results. The image is an original schematic illustration, not a client photograph.','image':True},{'status':'draft','title':'PRIVATE DRAFT SENTINEL','body':'Never included in the public build.','image':False}]
 (destination/'index.html').write_text(render(records))
 records[0]['title']='A thoughtful restoration story with a much longer title that still needs to remain readable on a small screen'
 records[0]['image']=False
 (destination/'long.html').write_text(render(records))
 for name in ['style.css','form.mjs','form-model.mjs']:shutil.copy2(SOURCE/name,destination/name)
 return destination
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('destination',type=Path);args=parser.parse_args()
 try:print(build(args.destination))
 except (ValueError,OSError) as error:parser.exit(1,str(error)+'\n')
