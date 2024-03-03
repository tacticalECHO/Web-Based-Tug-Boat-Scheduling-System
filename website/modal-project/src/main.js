import { createApp } from 'vue'
import App from './App.vue'
import './css/root.css'
import './css/popup.css'
import store from './store';
import router from './router'
import { redirect } from './js/methods.js'
// import VueNotifications from 'vue-notifications'

//icons---------------------------------------------------------
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas)


const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
app.component('font-awesome-icon', FontAwesomeIcon)
app.config.globalProperties.redirect = redirect

export default {
    components: {
      FontAwesomeIcon
    }
  }