<!-- Version-Timestamp: 2026-10-14 11:06:44 AST -->
<script setup lang="ts">
import {ref,onMounted,watch} from 'vue';import {gsap} from 'gsap';import {useMotion,type MotionProps} from '../../lib/useMotion';import {clamp} from '../../lib/runtime.mjs';
const props=defineProps<MotionProps>();const {active,scope}=useMotion(props);const target=ref<HTMLElement>();let tween:gsap.core.Tween|undefined;const fine=ref(false);
function reset(){tween?.kill();if(target.value)gsap.set(target.value,{clearProps:'transform,background'});}
function move(e:PointerEvent){if(!active.value||!fine.value||!target.value)return;const b=target.value.getBoundingClientRect(),x=clamp((e.clientX-b.left)/b.width,0,1)-.5,y=clamp((e.clientY-b.top)/b.height,0,1)-.5;tween?.kill();if(props.variant==='spotlight'){target.value.style.background=`radial-gradient(circle at ${(x+.5)*100}% ${(y+.5)*100}%,#b4c8bc,#e9ede9)`;return;}tween=gsap.to(target.value,props.variant==='magnetic'?{x:x*18,y:y*18,duration:.25}:{rotationX:-y*12,rotationY:x*12,transformPerspective:700,duration:.25});}
onMounted(()=>{const q=window.matchMedia('(hover: hover) and (pointer: fine)');const update=()=>{fine.value=q.matches;if(!fine.value)reset();};update();scope.listen(q,'change',update);scope.add(reset);watch(active,v=>{if(!v)reset()})});
</script>
<template><div class="specimen text-center p-5"><div ref="target" tabindex="0" role="group" aria-label="Decorative pointer study" class="fixture w-full min-h-48 text-2xl" @pointermove="move" @pointerleave="reset" @blur="reset" @focus="reset">{{variant==='magnetic'?'Stay in reach.':variant==='spotlight'?'Find your focus.':'A little perspective.'}}</div><p class="component-note">A decorative enhancement. The card can be focused for inspection; it is not an action button.</p></div></template>
