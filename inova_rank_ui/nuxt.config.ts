// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "nuxt-tiptap-editor"],
  tiptap: {
    prefix: 'Tiptap',
  },
  compatibilityDate: "2024-11-03"
})