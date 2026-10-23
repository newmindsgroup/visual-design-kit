// Version-Timestamp: 2026-09-11T20:58:31-04:00
export function next(state,event){
 if((state==='idle'||state==='rejected')&&event==='submit')return 'submitting';
 if(state==='submitting'&&event==='lost')return 'unknown';
 if(state==='submitting'&&event==='rejected')return 'rejected';
 if((state==='submitting'||state==='unknown')&&event==='received')return 'received';
 if(state==='unknown'&&event==='not-received')return 'idle';
 return state;
}
