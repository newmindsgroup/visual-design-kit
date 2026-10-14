// Version-Timestamp: 2026-10-14 11:06:44 AST
import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';
import tailwind from '@tailwindcss/vite';
export default defineConfig({ integrations: [vue()], vite: { plugins: [tailwind()] }, devToolbar: { enabled: false } });
