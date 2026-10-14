<!-- Version-Timestamp: 2026-10-14 11:06:44 AST -->
<script setup lang="ts">
import {computed,ref,defineAsyncComponent,defineComponent,h,onMounted,onBeforeUnmount} from 'vue';
import {getEffect} from '../lib/catalog.mjs';
const props=defineProps<{id:string}>(); const effect=getEffect(props.id);const run=ref(0),playing=ref(false),reduced=ref(false),hydrated=ref(false);const systemReduced=ref(false);
const loaders=import.meta.glob('./effects/*.vue');
const ErrorView=defineComponent({setup:()=>()=>h('p',{role:'alert'},'The study could not load. Replay to try again. Its static description remains below.')});
const PendingView=defineComponent({setup:()=>()=>h('p',{role:'status'},'Loading the study…')});
const component=computed(()=>effect?.component?defineAsyncComponent({loader:loaders[`./effects/${effect.component}.vue`] as ()=>Promise<any>,loadingComponent:PendingView,errorComponent:ErrorView,delay:120,timeout:10000}):undefined);
let query:MediaQueryList|undefined;const visibility=()=>{if(document.hidden)playing.value=false;};const read=()=>{systemReduced.value=!!query?.matches;if(systemReduced.value)playing.value=false;};
onMounted(()=>{hydrated.value=true;query=matchMedia('(prefers-reduced-motion: reduce)');read();query.addEventListener('change',read);document.addEventListener('visibilitychange',visibility);});onBeforeUnmount(()=>{query?.removeEventListener('change',read);document.removeEventListener('visibilitychange',visibility);});
function replay(){run.value++;playing.value=true;}function toggleReduced(){reduced.value=!reduced.value;}
</script>
<template><section v-if="effect" class="preview" :data-reduced="reduced||systemReduced"><div class="mb-5 flex flex-wrap items-center gap-3"><button :disabled="!hydrated||systemReduced" @click="replay">{{run===0?'Play study':'Replay study'}}</button><button :disabled="!hydrated" @click="playing=!playing" >{{playing?'Pause motion':'Play motion'}}</button><button :disabled="!hydrated" @click="toggleReduced" :aria-pressed="reduced">Reduced preview</button><span v-if="systemReduced" class="text-sm text-muted">System reduced motion is active.</span></div><div class="stage" ><component v-if="component" :is="component" :key="run" :playing="playing" :reduced="reduced||systemReduced" :variant="effect.variant"/><div v-else class="text-center"><p class="text-3xl tracking-tight">{{effect.name}}</p><p class="component-note">{{effect.status==='implemented'?'Use the navigation below to preview a page transition.':'This technique has a researched recipe; no live component is claimed.'}}</p></div></div></section><p v-else role="alert">Unknown study.</p></template>
