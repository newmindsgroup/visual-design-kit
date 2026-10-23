// Version-Timestamp: 2026-09-11T20:58:31-04:00
// Dedicated local test browser only. Never connect to a signed-in user profile.
import fs from 'node:fs';
const base='http://127.0.0.1:17660',debug='http://127.0.0.1:17661';
const output=process.env.EVIDENCE_DIR;
if(!output)throw Error('Set EVIDENCE_DIR to a local evidence directory');
fs.mkdirSync(output,{recursive:true});
const version=await(await fetch(debug+'/json/version')).json();
const ws=new WebSocket(version.webSocketDebuggerUrl);await new Promise((r,j)=>{ws.onopen=r;ws.onerror=j});
let id=0;const waiting=new Map(),results=[];
ws.onmessage=e=>{const m=JSON.parse(e.data);const p=waiting.get(m.id);if(p){waiting.delete(m.id);clearTimeout(p.timer);m.error?p.reject(Error(m.error.message)):p.resolve(m.result)}};
function call(method,params={},sessionId){return new Promise((resolve,reject)=>{const n=++id;const timer=setTimeout(()=>{waiting.delete(n);reject(Error('timeout '+method))},10000);waiting.set(n,{resolve,reject,timer});ws.send(JSON.stringify({id:n,method,params,...(sessionId?{sessionId}:{})}))});}
const {targetId}=await call('Target.createTarget',{url:'about:blank'});
const {sessionId}=await call('Target.attachToTarget',{targetId,flatten:true});
const c=(m,p={})=>call(m,p,sessionId);
async function ev(expression){const r=await c('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(r.exceptionDetails.text);return r.result.value;}
const delay=ms=>new Promise(r=>setTimeout(r,ms));
async function check(name,expr){const pass=await ev(expr);results.push({name,pass:pass===true});if(pass!==true)throw Error('FAIL '+name);}
async function shot(name){const x=await c('Page.captureScreenshot',{format:'png'});fs.writeFileSync(output+'/'+name+'.png',Buffer.from(x.data,'base64'));}
try{
 await c('Page.enable');
 for(const width of [1280,390]){
  await c('Emulation.setDeviceMetricsOverride',{width,height:950,deviceScaleFactor:1,mobile:false});
  for(const page of ['index.html','long.html']){
   await c('Page.navigate',{url:base+'/'+page});await delay(200);
   await check('no overflow '+width+' '+page,'document.documentElement.scrollWidth===innerWidth');
   await check('no draft '+page,"!document.documentElement.outerHTML.includes('PRIVATE DRAFT SENTINEL')");
   if(page==='long.html')await check('no image frame',"document.querySelectorAll('figure').length===0");
   await shot(page+'-'+width);
  }
 }
 await c('Page.navigate',{url:base});await delay(200);
 await c('Input.dispatchKeyEvent',{type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});await c('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
 await check('skip link reachable',"document.activeElement.className==='skip'");
 await ev("document.querySelector('#service').value='Everyday repair';document.querySelector('#outcome').value='lost';document.querySelector('#demo-form').requestSubmit()");
 await check('submitting disabled',"document.querySelector('#send').disabled");await delay(400);
 await check('unknown blocks retry',"document.querySelector('#send').disabled && document.querySelector('#status').textContent.includes('cannot confirm')");
 await ev("document.querySelector('#demo-form').requestSubmit()");await delay(400);
 await check('repeat stays unknown',"document.querySelector('#status').textContent.includes('cannot confirm')");
 await ev("document.querySelector('#inquiry').scrollIntoView()");await shot('unknown-mobile');
 await ev("document.querySelector('#reconcile').click()");
 await check('reconciliation unlocks',"!document.querySelector('#send').disabled");
 await ev("document.querySelector('#outcome').value='received';document.querySelector('#demo-form').requestSubmit()");await delay(400);
 await check('receipt is honest',"document.querySelector('#send').disabled && document.querySelector('#status').textContent.includes('No real request')");
 const response=await fetch(base+'/template.html');results.push({name:'source not served',pass:response.status===404});if(response.status!==404)throw Error('source served');
 await c('Emulation.setScriptExecutionDisabled',{value:true});await c('Page.navigate',{url:base});await delay(200);
 await c('Emulation.setScriptExecutionDisabled',{value:false});
 await check('no JS stays safe',"document.querySelector('h1').textContent.includes('Good things') && document.querySelector('#send').disabled");
}finally{
 fs.writeFileSync(output+'/browser-results.json',JSON.stringify({version:version.Browser,results},null,2));
 await call('Target.closeTarget',{targetId});ws.close();
}
console.log(JSON.stringify({passed:results.length,results}));
