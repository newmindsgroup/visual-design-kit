<!-- Version-Timestamp: 2026-10-14 11:06:44 AST -->
<script setup lang="ts">
import {ref,onMounted,watch} from 'vue';import {gsap} from 'gsap';import {useMotion,type MotionProps} from '../../lib/useMotion';
const props=defineProps<MotionProps>();const {active,scope}=useMotion(props);const root=ref<HTMLElement>();let ctx:ReturnType<typeof gsap.context>|undefined;
function sync(){ctx?.revert();if(active.value&&root.value)ctx=gsap.context(()=>{gsap.fromTo('.tile',{y:24,opacity:0},{y:0,opacity:1,duration:.65,ease:'power2.out',stagger:props.variant==='stagger'?.12:0})},root.value);}
onMounted(()=>{sync();scope.add(()=>ctx?.revert());watch(active,sync)});
</script>
<template><div ref="root" class="specimen grid grid-cols-1 sm:grid-cols-3 gap-3"><div v-for="(label,i) in ['Notice','Understand','Act']" :key="label" class="tile fixture min-h-40 flex flex-col justify-between"><span class="eyebrow">0{{i+1}}</span><span>{{label}}</span></div></div></template>
