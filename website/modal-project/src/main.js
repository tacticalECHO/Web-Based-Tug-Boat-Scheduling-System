import { createApp } from 'vue'
import App from './App.vue'
import './css/root.css'
import './css/popup.css'
import router from './router'
import { redirect } from './js/methods.js'

//icons---------------------------------------------------------
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const app = createApp(App)
app.use(router)
app.mount('#app')
app.component('font-awesome-icon', FontAwesomeIcon)
app.config.globalProperties.redirect = redirect
