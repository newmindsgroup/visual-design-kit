<!-- Version-Timestamp: 2026-10-14 11:06:44 AST -->
<script setup lang="ts">
import {ref,onMounted,watch} from 'vue';import {useMotion,type MotionProps} from '../../lib/useMotion';
const props=defineProps<MotionProps>();const {active,scope}=useMotion(props,{resumeOnVisible:true});const canvas=ref<HTMLCanvasElement>();const status=ref('static');const message=ref('');const visible=ref(true);
let scene:Awaited<ReturnType<typeof import('../../lib/webgl.mjs').createScene>>|undefined;let loading=false,generation=0;
async function sync(){
 if(!active.value){scene?.stop();return;}
 if(scene){if(visible.value)scene.start();return;}
 if(loading||status.value==='error'||scope.disposed||!canvas.value)return;
 loading=true;status.value='loading';const token=++generation;
 try { const {createScene}=await import('../../lib/webgl.mjs');if(scope.disposed||token!==generation||!canvas.value)return;const created=await createScene(canvas.value);if(scope.disposed||token!==generation){created.dispose();return;}scene=created;status.value='ready';if(active.value&&visible.value)scene.start(); }
 catch(error){if(!scope.disposed){status.value='error';message.value=error instanceof Error?error.message:'WebGL could not start.';}}
 finally{loading=false;}
}
onMounted(()=>{if(!canvas.value)return;const resize=new ResizeObserver(()=>scene?.resize());resize.observe(canvas.value);scope.add(()=>resize.disconnect());const observer=new IntersectionObserver(entries=>{visible.value=entries[0].isIntersecting;if(visible.value)void sync();else scene?.stop()});observer.observe(canvas.value);scope.add(()=>observer.disconnect());scope.listen(canvas.value,'webglcontextlost',(event:Event)=>{status.value='error';message.value='Graphics context lost. Replay to create a fresh study.';scene?.dispose();scene=undefined;});scope.add(()=>{generation++;scene?.dispose();scene=undefined;});watch(active,()=>void sync());void sync()});
</script>
<template><figure class="specimen"><div class="webgl-frame" :data-webgl-status="status"><svg v-if="status!=='ready'||!active" viewBox="0 0 400 250" aria-hidden="true"><ellipse cx="200" cy="125" rx="85" ry="60" fill="none" stroke="#657f95" stroke-width="24" transform="rotate(-28 200 125)"/><ellipse cx="200" cy="125" rx="55" ry="80" fill="none" stroke="#97aca3" stroke-width="16" transform="rotate(28 200 125)"/></svg><canvas ref="canvas" aria-hidden="true" :style="{visibility:status==='ready'&&active?'visible':'hidden'}"></canvas></div><figcaption class="component-note" aria-live="polite">{{status==='loading'?'Loading the graphics study…':status==='error'?message:'Original geometry. Graphics load only when you play this study.'}}</figcaption></figure></template>
<style scoped>.webgl-frame{height:250px;position:relative}.webgl-frame svg,.webgl-frame canvas{width:100%;height:100%;position:absolute;inset:0}</style>
