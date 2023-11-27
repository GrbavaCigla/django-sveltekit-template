import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';

export default defineConfig({
	plugins: [sveltekit()],
	envDir: '../',
	server: {
		proxy: {
			'/api': 'http://127.0.0.1:8000/'
		}
	},
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});
