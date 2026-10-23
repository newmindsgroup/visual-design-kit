// Version-Timestamp: 2026-09-11T20:58:31-04:00
import {next} from './form-model.mjs';
let state='idle';const form=document.querySelector('#demo-form'),send=document.querySelector('#send'),status=document.querySelector('#status'),reconcile=document.querySelector('#reconcile');
const copy={idle:'Ready. This simulation sends nothing.',submitting:'Simulating submission…',received:'Simulated receipt confirmed. No real request was sent.',unknown:'We cannot confirm whether it arrived. Repeating the request is disabled until its status is verified.',rejected:'The simulated request was rejected. You can correct the selection and try again.'};
function show(event){state=next(state,event);send.disabled=!['idle','rejected'].includes(state);reconcile.hidden=state!=='unknown';status.textContent=copy[state];}
form.addEventListener('submit',event=>{event.preventDefault();if(!['idle','rejected'].includes(state))return;show('submit');const result=document.querySelector('#outcome').value;setTimeout(()=>show(result),300)});
reconcile.addEventListener('click',()=>show('not-received'));show('ready');
