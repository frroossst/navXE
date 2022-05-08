import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
//import './registerServiceWorker'
//import VueQRCodeReader from 'vue-qrcode-reader'
import QrReader from 'vue3-qr-reader';

const app = createApp(App).use(router)
app.use(VueAxios,axios)
app.use(QrReader)
app.provide('axios', app.config.globalProperties.axios)  // provide 'axios'
app.provide('currentPage',0)
app.provide('pagesArray',{0:"home",1:"about",2:"settings"})
app.mount('#app')