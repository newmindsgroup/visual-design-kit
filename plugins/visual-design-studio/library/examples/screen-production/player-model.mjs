// Version-Timestamp: 2026-09-11 20:20:00 AST
export function transition(state,event){
  if(event==='play')return {...state,playing:true};
  if(['pause','hidden','reduced'].includes(event))return {...state,playing:false};
  if(event==='next')return {index:(state.index+1)%3,playing:false};
  if(event==='tick'&&state.playing)return {...state,index:(state.index+1)%3};
  return {...state};
}
