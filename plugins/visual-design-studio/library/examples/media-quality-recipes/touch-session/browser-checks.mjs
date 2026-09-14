// Version-Timestamp: 2026-09-11T23:42:59-04:00
// Dedicated local test browser only. Never connect to a signed-in user profile.
import fs from 'node:fs';
const base='http://127.0.0.1:17662',debug='http://127.0.0.1:17661';
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
 await c('Page.enable');await c('Network.enable');await c('Network.setCacheDisabled',{cacheDisabled:true});
 for(const width of [1280,390]){
 await c('Emulation.setDeviceMetricsOverride',{width,height:950,deviceScaleFactor:1,mobile:false});
 await c('Page.navigate',{url:base});await delay(200);
 await check('attract '+width,"!document.querySelector('#attract').hidden");await shot('attract-'+width);
 await ev("document.querySelector('#enter').click()");
 await check('entry focus '+width,"document.activeElement.id==='chair'");
 await ev("document.querySelector('#table').click()");
 await check('table '+width,"document.querySelector('#choice').textContent.startsWith('Table:') && document.querySelector('.art').getAttribute('aria-label').includes('table')");
 await ev("document.querySelector('#fail').click()");
 await delay(250);await check('actual failed image '+width,"document.querySelector('#fail').dataset.result==='error'");await check('fallback '+width,"document.querySelector('#status').textContent.includes('unavailable') && !document.querySelector('#active').hidden");await shot('active-'+width);
 await ev("document.querySelector('#warn').click()");await check('warning focus '+width,"document.activeElement.id==='extend'");await shot('warning-'+width);
 await ev("document.querySelector('#extend').click()");await check('extension retains '+width,"document.querySelector('#choice').textContent.startsWith('Table:') && document.querySelector('#warning').hidden");
 await ev("document.querySelector('#exit').click();document.querySelector('#enter').click()");await check('cleared '+width,"document.querySelector('#choice').textContent.startsWith('Select')");
 await check('no overflow '+width,'document.documentElement.scrollWidth===innerWidth');
 }
}finally{
 fs.writeFileSync(output+'/browser-results.json',JSON.stringify({version:version.Browser,results},null,2));
 await call('Target.closeTarget',{targetId});ws.close();
}
console.log(JSON.stringify({passed:results.length,results}));
