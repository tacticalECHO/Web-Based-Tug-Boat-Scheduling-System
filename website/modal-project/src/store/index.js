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
          schedulers: [],
          berths: [],
          containerBoats: [],
          scheduleEntries: [],
          tugboats: [],
          exitPath: 'Settings',
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
        setTasks(state, tasks) {
            state.tasks = tasks;
        },
        setSchedulers(state, schedulers) {
            state.schedulers = schedulers;
        },
        setBerths(state, berths) {
            state.berths = berths;
        },
        setContainerBoats(state, containerBoats) {
            state.containerBoats = containerBoats;
        },
        setScheduleEntries(state, scheduleEntries) {
          state.scheduleEntries = scheduleEntries;
        },
        setTugBoats(state, tugboats) {
          state.tugboats = tugboats;
        },
        setExitPath(state, path) {
          state.exitPath = path;
        },
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
                commit('setTasks', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchSchedulers({ commit }) {
            axios.get('http://localhost:8000/api/display_scheduler/')
              .then(response => {
                commit('setSchedulers', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchBerths({ commit }) {
            axios.get('http://localhost:8000/api/display_berth/')
              .then(response => {
                commit('setBerths', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchContainerBoats({ commit }) {
            axios.get('http://localhost:8000/api/display_container_boat/')
              .then(response => {
                commit('setContainerBoats', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchScheduleEntries({ commit }) {
          axios.get('http://localhost:8000/api/display_schedule_entry/')
            .then(response => {
              commit('setScheduleEntries', response.data);
            })
            .catch(error => console.error(error));
        },
        fetchTugBoats({ commit }) {
          axios.get('http://localhost:8000/api/display_tugboat/')
            .then(response => {
              commit('setTugBoats', response.data);
            })
            .catch(error => console.error(error));
        }
    }
});
export default store;