<!-- Version-Timestamp: 2026-10-14 14:03:25 AST -->
<script setup lang="ts">
import {computed,ref,onMounted,onBeforeUnmount} from 'vue';
import {navigate} from 'astro:transitions/client';
import {Dialog,DialogPanel,DialogTitle,DialogDescription,TransitionRoot,TransitionChild} from '@headlessui/vue';
const props=defineProps<{variant?:string;playing:boolean;reduced:boolean}>();
const drawer=computed(()=>props.variant==='drawer');
const mounted=ref(false),open=ref(false),leavingRoute=ref(false),closeButton=ref<HTMLButtonElement|null>(null),trigger=ref<HTMLButtonElement|null>(null);
let focusFrame=0;
// The browser regression requires final focus after leave, guarded against route teardown.
function restoreFocus(){focusFrame=requestAnimationFrame(()=>{if(mounted.value&&!leavingRoute.value&&!open.value&&trigger.value?.isConnected)trigger.value.focus({preventScroll:true});});}
const quiet=computed(()=>props.reduced||!props.playing||leavingRoute.value);
const close=()=>{open.value=false;};
async function follow(event:MouseEvent){if(event.defaultPrevented)return;const link=event.currentTarget as HTMLAnchorElement;if(link.target&&link.target!=="_self"||link.hasAttribute("download")||link.relList.contains("external")||link.hasAttribute("data-astro-reload")||link.origin!==location.origin)return;if(event.metaKey||event.ctrlKey||event.shiftKey||event.altKey||event.button!==0)return;const href=(event.currentTarget as HTMLAnchorElement).getAttribute("href");if(!href)return;event.preventDefault();try{await navigate(href);}catch{location.assign(href);}}
const beforeSwap=()=>{document.removeEventListener('astro:before-swap',beforeSwap);cancelAnimationFrame(focusFrame);leavingRoute.value=true;open.value=false;mounted.value=false;};
onMounted(()=>{mounted.value=true;document.addEventListener('astro:before-swap',beforeSwap);});
onBeforeUnmount(()=>{document.removeEventListener('astro:before-swap',beforeSwap);cancelAnimationFrame(focusFrame);});
</script>
<template>
 <div class="specimen fixture">
  <p class="eyebrow">{{drawer?'Navigation / everyday':'Project conversation / everyday'}}</p>
  <h2 class="mt-4 text-3xl tracking-tight">{{drawer?'A clear way through.':'Make room for a good idea.'}}</h2>
  <p class="mt-4 text-muted">{{drawer?'A mobile drawer with familiar links and deliberate focus.':'A calm dialog for the next step. This specimen does not submit information.'}}</p>
  <button ref="trigger" data-overlay-trigger class="mt-6" :disabled="!mounted" @click="open=true">{{drawer?'Open navigation':'Open project dialog'}}</button>
  <p class="component-note">Interactive preview requires JavaScript. Pause or reduced preview removes movement while keeping the controls available.</p>
  <a class="mt-4 inline-block text-sm underline" href="/#catalog">Browse all studies</a>
 </div>
 <TransitionRoot v-if="mounted" as="template" :show="open" @after-leave="restoreFocus">
  <Dialog :initial-focus="closeButton" @close="close" class="fixed inset-0 z-50" :data-reduced="quiet">
   <TransitionChild as="template" enter="transition-opacity duration-200 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity duration-150 ease-in" leave-from="opacity-100" leave-to="opacity-0">
    <div data-overlay-backdrop class="fixed inset-0 bg-ink/40" aria-hidden="true" />
   </TransitionChild>
   <div class="fixed inset-0 pointer-events-none flex overflow-y-auto" :class="drawer?'justify-end':'items-center justify-center p-4'">
    <TransitionChild as="template" enter="transition duration-200 ease-out" :enter-from="drawer?'translate-x-full opacity-0':'translate-y-3 opacity-0'" enter-to="translate-x-0 translate-y-0 opacity-100" leave="transition duration-150 ease-in" leave-from="translate-x-0 translate-y-0 opacity-100" :leave-to="drawer?'translate-x-full opacity-0':'translate-y-3 opacity-0'">
     <DialogPanel data-overlay-panel :data-reduced="quiet" class="pointer-events-auto border border-line bg-paper text-ink p-6 sm:p-8" :class="drawer?'w-[min(88vw,420px)] min-h-full':'w-full max-w-lg rounded-sm max-h-[90dvh] overflow-y-auto'">
      <div class="flex items-center justify-between gap-4"><span class="eyebrow">Motion Atlas</span><button ref="closeButton" aria-label="Close panel" @click="close">Close</button></div>
      <DialogTitle class="mt-10 text-4xl tracking-tight">{{drawer?'Find your next study.':'Start with the right question.'}}</DialogTitle>
      <DialogDescription class="mt-4 text-muted">{{drawer?'Explore the library, then choose the motion your project needs.':'What should this website help someone do? Keep that answer at the center of the design.'}}</DialogDescription>
      <nav v-if="drawer" aria-label="Study navigation" class="mt-10 flex flex-col gap-6 text-lg">
       <a href="/#catalog" @click="follow">Browse all studies</a><a href="/effects/reveal/" @click="follow">Content reveals</a><a href="/effects/branded-dialog/" @click="follow">Project dialog</a>
      </nav>
      <div v-else class="mt-8"><p class="border-t border-line pt-6 leading-relaxed">Define the audience, the useful next action and the content that supports it. Then choose a visual direction.</p><button class="mt-8" @click="close">Return to the study</button></div>
      <p class="mt-12 text-sm text-muted">Use Escape or the close button to return.</p>
     </DialogPanel>
    </TransitionChild>
   </div>
  </Dialog>
 </TransitionRoot>
</template>
