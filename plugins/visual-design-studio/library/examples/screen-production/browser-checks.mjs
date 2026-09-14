// Version-Timestamp: 2026-09-11 20:25:00 AST
// Dedicated local test browser only. Never connect to a signed-in user profile.
import fs from 'node:fs';
const base='http://127.0.0.1:17658',debug='http://127.0.0.1:17659';
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
  await c('Emulation.setDeviceMetricsOverride',{width,height:900,deviceScaleFactor:1,mobile:false});
  await c('Page.navigate',{url:base});await delay(450);
  await check('loaded '+width,"document.querySelector('#art').complete && document.querySelector('#art').naturalWidth===1920");
  await check('no overflow '+width,'document.documentElement.scrollWidth===innerWidth');
  await shot('wide-'+width);
  await ev("document.querySelector('#next').click()");await delay(100);await check('portrait '+width,"document.querySelector('#art').naturalHeight===1920");await shot('portrait-'+width);
  await ev("document.querySelector('#next').click()");await delay(100);await check('strip '+width,"document.querySelector('#art').naturalHeight===160");await shot('strip-'+width);
 }
 await c('Page.navigate',{url:base});await delay(150);
 await c('Input.dispatchKeyEvent',{type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});await c('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
 await check('keyboard focus',"document.activeElement.id==='play' && getComputedStyle(document.activeElement).outlineStyle!=='none'");await shot('keyboard');
 await c('Input.dispatchKeyEvent',{type:'keyDown',key:'Enter',code:'Enter',text:'\r',windowsVirtualKeyCode:13});await c('Input.dispatchKeyEvent',{type:'keyUp',key:'Enter',code:'Enter',windowsVirtualKeyCode:13});
 await check('keyboard starts',"document.querySelector('#status').textContent.includes('Playing')");
 await delay(8100);await check('timed advance',"document.querySelector('#art').getAttribute('src').includes('portrait')");
 await c('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});await delay(100);
 await check('reduced motion pauses',"document.querySelector('#play').disabled && document.querySelector('#status').textContent.includes('Paused')");
 await ev("document.querySelector('#art').src='missing-fixture.svg'");await delay(200);
 await check('missing asset visible',"!document.querySelector('#error').hidden");await shot('missing');
}finally{
 fs.writeFileSync(output+'/browser-results.json',JSON.stringify({version:version.Browser,results},null,2));
 await call('Target.closeTarget',{targetId});ws.close();
}
console.log(JSON.stringify({passed:results.length,results}));
