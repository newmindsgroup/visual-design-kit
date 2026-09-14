// Version-Timestamp: 2026-09-11 20:20:00 AST
import {transition} from './player-model.mjs';
const formats=[['wide','Ultrawide'],['portrait','Portrait'],['strip','Shelf strip']];
let state={index:0,playing:false};
const art=document.querySelector('#art'),play=document.querySelector('#play'),status=document.querySelector('#status'),error=document.querySelector('#error');
const motion=matchMedia('(prefers-reduced-motion: reduce)');
function update(event){
 state=transition(state,event);
 const [id,label]=formats[state.index];
 const source=`render-v1/${id}.svg`;
 if(art.getAttribute('src')!==source){error.hidden=true;art.src=source;}
 art.alt=`Rill fictional water campaign in ${label.toLowerCase()} format`;
 play.textContent=state.playing?'Pause sequence':'Play sequence';
 play.disabled=motion.matches;
 status.textContent=`${label} · ${state.playing?'Playing':motion.matches?'Paused for reduced motion':'Paused'}`;
}
play.addEventListener('click',()=>update(state.playing?'pause':'play'));
document.querySelector('#next').addEventListener('click',()=>update('next'));
document.addEventListener('visibilitychange',()=>{if(document.hidden)update('hidden')});
motion.addEventListener('change',()=>update('reduced'));
art.addEventListener('error',()=>{update('pause');error.textContent='This format could not load. Choose another format or verify the local export package.';error.hidden=false});
setInterval(()=>update('tick'),8000);
update(motion.matches?'reduced':'pause');
