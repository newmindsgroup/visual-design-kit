<!-- Version-Timestamp: 2026-10-14 11:06:44 AST -->
<script setup lang="ts">
import {ref} from 'vue'; import {useMotion, type MotionProps} from '../../lib/useMotion';
const props=defineProps<MotionProps>(); const {hydrated,reduced}=useMotion(props); const saved=ref(false);
</script>
<template><div class="specimen text-center"><button :disabled="!hydrated" @click="saved=!saved" :aria-pressed="saved" class="group transition-transform duration-200 motion-reduce:transform-none" :class="{'hover:-translate-y-1 active:scale-95':!reduced}"><span class="label" :class="{underlined:variant==='underline'}">{{saved?'Added to collection':'Add to collection'}}</span><span aria-hidden="true" class="ml-5 inline-block transition-transform group-hover:translate-x-1">{{saved?'✓':'↗'}}</span></button><p class="component-note" aria-live="polite">{{saved?'Selection recorded locally.':'Hover, focus, then activate.'}}</p></div></template>


<style scoped>.label.underlined{position:relative}.label.underlined::after{content:"";position:absolute;height:1px;left:0;right:0;bottom:-4px;background:currentColor;transform:scaleX(0);transform-origin:left;transition:transform .2s}.group:hover .underlined::after,.group:focus-visible .underlined::after{transform:scaleX(1)}</style>
