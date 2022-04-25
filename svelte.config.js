import preprocess from "svelte-preprocess";
import adapter from "@sveltejs/adapter-auto";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),

    // Override http methods in the Todo forms
    methodOverride: {
      allowed: ["PATCH", "DELETE"],
    },
    vite: {
      server: {
        hmr: {
          port: 8080,
          clientPort: 8082
        }
      }
    }
  },

  preprocess: [
    preprocess({
      postcss: true,
    }),
  ],
};

export default config;
