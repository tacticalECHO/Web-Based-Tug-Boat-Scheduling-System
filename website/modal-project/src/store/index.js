import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
    state() {
        return {
          username: '',
          passwordPlaceholder: '******',
          isCaptain: false,
          isAdmin: false,
          isScheduler: false,
          captains: [],
          tasks: [],
          schedulers: []
        };
        
    },
    mutations: {
        setUser(state, { username}) {
            state.username = username;
        },
        setUserRole(state, { isCaptain, isAdmin, isScheduler}) {
            state.isCaptain = isCaptain;
            state.isAdmin = isAdmin;
            state.isScheduler = isScheduler;
        },
        setCaptains(state, captains) {
            state.captains = captains;
        },
        setTask(state, tasks) {
            state.tasks = tasks;
        },
        setSchedulers(state, schedulers) {
            state.schedulers = schedulers;
        }
    },

    actions:{
        fetchCaptains({ commit }) {
            axios.get('http://localhost:8000/api/display_captain/')
              .then(response => {
                commit('setCaptains', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchTasks({ commit }) {
            axios.get('http://localhost:8000/api/display_task/')
              .then(response => {
                commit('setTask', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchSchedulers({ commit }) {
            axios.get('http://localhost:8000/api/display_scheduler/')
              .then(response => {
                commit('setSchedulers', response.data);
              })
              .catch(error => console.error(error));
        }
    }
});
export default store;