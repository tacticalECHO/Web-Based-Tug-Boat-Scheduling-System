import { createStore } from 'vuex';

const store = createStore({
    state() {
        return {
          username: '',
          passwordPlaceholder: '******', 
        };
    },
    mutations: {
        setUser(state, { username, password }) {
        state.username = username;
        },
    },
});
export default store;