// Version-Timestamp: 2026-09-11T23:42:59-04:00
import {initial,transition} from './session.mjs';
let state=initial(),timer;
const $=id=>document.getElementById(id);
function schedule(){clearTimeout(timer);if(state.phase==='attract')return;const session=state.session,epoch=state.epoch;const type=state.phase==='warning'?'expire':'warn';timer=setTimeout(()=>send({type,session,epoch}),state.phase==='warning'?15000:45000)}
function draw(){
 $('attract').hidden=state.phase!=='attract';$('active').hidden=state.phase==='attract';$('warning').hidden=state.phase!=='warning';
 $('choice').textContent=state.choices[0]==='chair'?'Chair: a simple upright silhouette.':state.choices[0]==='table'?'Table: a broad horizontal surface.':'Select a form to see its description.';
 $('status').textContent=state.media==='fallback'?'Media is unavailable. The schematic remains visible; you can keep exploring.':'';
 document.querySelector('.art').setAttribute('aria-label',state.choices[0]==='table'?'Original schematic table illustration':'Original schematic chair illustration');
 document.querySelector('.art path').setAttribute('d',state.choices[0]==='table'?'M45 95h210M65 100v115m170-115v115':'M85 130V45h125v85M75 140h145M90 145v70m110-70v70');
 for(const id of ['chair','table'])$(id).setAttribute('aria-pressed',String(state.choices[0]===id));
}
function send(event){const prior=state;state=transition(state,event);if(state===prior)return;draw();schedule();if(state.phase==='attract')$('enter').focus();else if(prior.phase==='attract')$('chair').focus();else if(state.phase==='warning')$('extend').focus();else if(prior.phase==='warning')$('chair').focus()}
$('enter').onclick=()=>send({type:'enter'});$('exit').onclick=()=>send({type:'reset'});$('extend').onclick=()=>send({type:'extend'});
for(const value of ['chair','table'])$(value).onclick=()=>send({type:'select',value});
let mediaRequest=0;
$('fail').onclick=()=>{
 if(state.phase==='attract')return;
 const session=state.session,request=++mediaRequest,probe=new Image();
 $('fail').dataset.result='loading';
 probe.onerror=()=>{if(request!==mediaRequest || session!==state.session)return;$('fail').dataset.result='error';send({type:'media-failed',session})};
 probe.onload=()=>{if(request!==mediaRequest || session!==state.session)return;$('fail').dataset.result='loaded';send({type:'media-ready',session})};
 probe.src=new URL('intentionally-missing-fixture.png',import.meta.url).href;
};$('warn').onclick=()=>send({type:'warn',session:state.session,epoch:state.epoch});
draw();
