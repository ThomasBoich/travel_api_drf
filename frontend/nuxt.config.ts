// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: false },
  modules: ['@pinia/nuxt',],
  ssr: true,
  app: {
    head: {
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'author', content: 'https://boich.ru | ARTEM BOYKO' },
      ],
      title: 'КудаУгодно',
      htmlAttrs: {
        lang: 'ru'
      },
      script: [
      ],
      // link: [
      // { rel: 'stylesheet', href: '~/assets/css/main.css' }
      // ],
      // style: [
      //   { children: ':root { color: red }', type: 'text/css' }
      // ],
      noscript: [
        { children: 'JavaScript is required' }
      ]
    }
  },
  css: [
    //'primevue/resources/themes/aura-light-green/theme.css',
    //'primevue/resources/primevue.css',
    //'primeicons/primeicons.css',
    '~/assets/css/main.css',
    // SCSS file in the project
    '~/assets/css/main.scss',
    //'primeflex/primeflex.css',
    //'~/assets/css/tailwind.css'
  ],
})