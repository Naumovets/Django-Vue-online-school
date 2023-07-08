import './assets/css/theme.bundle.css'
import './assets/css/theme.rtl.bundle.css'


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
