// Version-Timestamp: 2026-10-20 02:52:00 UTC
import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vite';

const page = (name: string) => fileURLToPath(new URL(name, import.meta.url));

export default defineConfig({
  // Relative asset paths so dist/ works from any static host or sub-path.
  base: './',
  plugins: [react(), tailwindcss()],
  build: {
    target: 'es2022',
    rollupOptions: {
      input: { index: page('./index.html'), billing: page('./billing.html') },
    },
  },
  server: { port: 5173, strictPort: false },
  preview: { port: 4173 },
});
