import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: './', // Crucial: ensures assets load with relative paths
  build: {
    outDir: 'dist',
  }
})