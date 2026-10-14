<!-- Version-Timestamp: 2026-10-14 11:06:44 AST -->
<script setup lang="ts">
import {ref,nextTick,useId} from 'vue';import {useMotion,type MotionProps} from '../../lib/useMotion';
const props=defineProps<MotionProps>();const {hydrated,reduced}=useMotion(props);const selected=ref(0);const id=useId();
const names=['Purpose','Timing','Fallback'];const copy=['Movement should have one clear job.','Immediate feedback comes before a long decorative sequence.','The same content must remain available without animation.'];
async function move(event:KeyboardEvent){let next=selected.value;if(event.key==='ArrowRight')next=(next+1)%3;else if(event.key==='ArrowLeft')next=(next+2)%3;else if(event.key==='Home')next=0;else if(event.key==='End')next=2;else return;event.preventDefault();selected.value=next;await nextTick();document.getElementById(`${id}-tab-${next}`)?.focus();}
</script>
<template><div class="specimen" :class="{'reduce':reduced}"><div role="tablist" aria-label="Motion principles" class="demo-row"><button v-for="(name,i) in names" :key="name" role="tab" :id="`${id}-tab-${i}`" :aria-controls="`${id}-panel-${i}`" :aria-selected="selected===i" :tabindex="selected===i?0:-1" :disabled="!hydrated" @click="selected=i" @keydown="move">{{name}}</button></div><div v-for="(text,i) in copy" :key="text" role="tabpanel" :id="`${id}-panel-${i}`" :aria-labelledby="`${id}-tab-${i}`" :hidden="hydrated&&selected!==i" tabindex="0" class="fixture mt-5 panel">{{text}}</div></div></template>
<style scoped>.panel:not([hidden]){animation:panel .25s ease-out}.reduce .panel{animation:none}@keyframes panel{from{opacity:.4;transform:translateY(6px)}to{opacity:1;transform:none}}</style>
