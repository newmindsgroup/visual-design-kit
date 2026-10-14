// Version-Timestamp: 2026-10-14 11:06:44 AST
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue';
import { createScope } from './runtime.mjs';
export interface MotionProps { reduced?: boolean; playing?: boolean; variant?: string }
export function useMotion(props: MotionProps, options: {resumeOnVisible?:boolean} = {}) {
 const hydrated = ref(false), systemReduced = ref(false), hidden = ref(false);
 const scope = createScope(); const stopped=ref(false), interrupted=ref(false);
 const reduced = computed(() => !!props.reduced || systemReduced.value);
 const active = computed(() => hydrated.value && !stopped.value && !interrupted.value && !!props.playing && !reduced.value && !hidden.value);
 onMounted(() => {
  hydrated.value = true;
  const query = window.matchMedia('(prefers-reduced-motion: reduce)');
  const update = () => { systemReduced.value = query.matches; hidden.value = document.hidden; if(hidden.value && !options.resumeOnVisible)interrupted.value=true; };
  update(); watch(()=>props.playing, value=>{if(value&&!document.hidden)interrupted.value=false;}); scope.listen(query, 'change', update); scope.listen(document,'visibilitychange',update);
  scope.listen(document, 'astro:before-swap', () => { stopped.value=true; scope.dispose(); });
 });
 onBeforeUnmount(() => { scope.dispose(); });
 return { hydrated, reduced, active, scope };
}
