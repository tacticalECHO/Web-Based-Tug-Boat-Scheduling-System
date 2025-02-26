import { createApp } from 'vue'
import App from './App.vue'
import './css/root.css'
import './css/popup.css'
import store from './store';
import router from './router'
import { redirect } from './js/methods.js'

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

app.config.globalProperties.created = function () {
  // Check if authentication information exists in localStorage
  const isAuthenticated = localStorage.getItem('authentication') === 'true';
  if (isAuthenticated) {
    const username = localStorage.getItem('username');
    const isCaptain = localStorage.getItem('isCaptain') === 'true';

    // Set authentication information in the store
    store.commit('setAuthentication', true);
    store.commit('setUser', { username });
    store.commit('setUserRole', { isCaptain });
  }
};

export default {
    components: {
      FontAwesomeIcon
    }
  }