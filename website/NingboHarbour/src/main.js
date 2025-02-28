import { createApp } from 'vue'
import App from './App.vue'
import './css/root.css'
import './css/popup.css'
import store from './store'
import router from './router'
import { redirect, formatTime, formatDate, getActionStyle, getStatusStyle, toggle, getCaptainId, getCaptainName, deletionAlert } from './js/methods.js'

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
app.config.globalProperties.formatTime = formatTime
app.config.globalProperties.formatDate = formatDate
app.config.globalProperties.getActionStyle = getActionStyle
app.config.globalProperties.getStatusStyle = getStatusStyle
app.config.globalProperties.toggle = toggle
app.config.globalProperties.getCaptainId = getCaptainId
app.config.globalProperties.getCaptainName = getCaptainName
app.config.globalProperties.deletionAlert = deletionAlert

export default {
    components: {
      FontAwesomeIcon
    }
  }