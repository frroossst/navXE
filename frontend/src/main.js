import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
//import './registerServiceWorker'

const app = createApp(App).use(router)
app.use(VueAxios,axios)
app.provide('axios', app.config.globalProperties.axios)  // provide 'axios'
app.mount('#app')