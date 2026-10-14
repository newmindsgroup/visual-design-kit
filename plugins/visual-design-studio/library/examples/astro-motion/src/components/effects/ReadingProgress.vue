<!-- Version-Timestamp: 2026-10-14 11:31:19 AST -->
<script setup lang="ts">
import {ref,onMounted} from 'vue';import {useMotion,type MotionProps} from '../../lib/useMotion';import {progress} from '../../lib/runtime.mjs';const props=defineProps<MotionProps>();const {scope}=useMotion(props);const root=ref<HTMLElement>();const amount=ref(0);
function update(){if(root.value)amount.value=progress(root.value.scrollTop,root.value.scrollHeight,root.value.clientHeight);}
onMounted(()=>{if(root.value)scope.listen(root.value,'scroll',update,{passive:true});update()});
</script>
<template><div class="specimen"><div class="mb-3 flex justify-between text-sm"><span>Scroll inside this study</span><output>{{Math.round(amount*100)}}%</output></div><div class="track"><div :style="{width:`${amount*100}%`}"></div></div><div ref="root" class="scroller" tabindex="0" role="region" aria-label="Scrollable motion study"><div class="content"><p class="fixture">Your place in the story.</p><p class="fixture">Read at your own pace.</p><p class="fixture">The complete idea remains readable.</p></div></div><p class="component-note">Keyboard: focus the study and use Page Down or arrow keys.</p></div></template>
<style scoped>.scroller{height:275px;overflow:auto;border:1px solid #d8ddda;background:#f6f7f5}.content{min-height:650px;padding:20px;display:flex;flex-direction:column;justify-content:space-between}.track{height:2px;background:#d8ddda;margin-bottom:12px}.track>div{height:2px;background:#171a1d}</style>
