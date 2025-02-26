import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
    state() {
        return {
            isAuthenticated: false,
            username: '',
            passwordPlaceholder: '******',
            isCaptain: false,
            captains: []
        };
        
    },
    mutations: {
        setUser(state, { username}) {
            state.username = username;
        },
        setUserRole(state, { isCaptain }) {
            state.isCaptain = isCaptain;
        },
        setCaptains(state, captains) {
            state.captains = captains;
        }
    },

    actions:{
        fetchCaptains({ commit }) {
            axios.get('http://localhost:8000/api/display_captain/')
              .then(response => {
                commit('setCaptains', response.data);
              })
              .catch(error => console.error(error));
        }
    }
});
export default store;