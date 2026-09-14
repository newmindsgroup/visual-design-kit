// Version-Timestamp: 2026-09-11T23:42:59-04:00
// Pure fictional state model. No network, storage, user data or timers.
export function initial(){return {phase:'attract',session:0,epoch:0,choices:[],media:'idle'}}
export function transition(s,e){
 if(e.type==='enter' && s.phase==='attract')return {...s,phase:'active',session:s.session+1,epoch:s.epoch+1,media:'loading'};
 if(e.type==='reset')return {...initial(),session:s.session+1,epoch:s.epoch+1};
 if(e.type==='select' && s.phase==='active' && ['chair','table'].includes(e.value))return {...s,choices:[e.value]};
 if(e.type==='warn' && s.phase==='active' && e.session===s.session && e.epoch===s.epoch)return {...s,phase:'warning'};
 if(e.type==='extend' && s.phase==='warning')return {...s,phase:'active',epoch:s.epoch+1};
 if(e.type==='expire' && s.phase==='warning' && e.session===s.session && e.epoch===s.epoch)return {...initial(),session:s.session+1,epoch:s.epoch+1};
 if(['media-ready','media-failed'].includes(e.type) && e.session===s.session && ['active','warning'].includes(s.phase))return {...s,media:e.type==='media-ready'?'ready':'fallback'};
 return s;
}
