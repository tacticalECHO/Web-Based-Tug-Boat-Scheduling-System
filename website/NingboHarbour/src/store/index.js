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
          id: 1,
          currentRoute: null,
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
        resetNull(state) {
          resetNull(state);
        },
        setTugBoatInfo(state, id) {
          state.tugBoatInfo = id;
        },
        setTimeInfo(state, id) {
          state.timeInfo = id;
        },
        setContainerBoatInfo(state, id) {
          state.containerBoatInfo = id;
        },
        setBerthInfo(state, id) {
          state.berthInfo = id;
        },
        setActionInfo(state, id) {
          state.actionInfo = id;
        },
        setStateInfo(state, id) {
          state.stateInfo = id;
        },
        setCurrentRoute(state, route) {
          state.currentRoute = route;
        },
    },

    actions:{
        fetchCaptains({ commit }) {
            axios.get('/api/display_captain/')
              .then(response => {
                commit('setCaptains', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchTasks({ commit }) {
            axios.get('/api/display_task/')
              .then(response => {
                commit('setTasks', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchSchedulers({ commit }) {
            axios.get('/api/display_scheduler/')
              .then(response => {
                commit('setSchedulers', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchBerths({ commit }) {
            axios.get('/api/display_berth/')
              .then(response => {
                commit('setBerths', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchContainerBoats({ commit }) {
            axios.get('/api/display_container_boat/')
              .then(response => {
                commit('setContainerBoats', response.data);
              })
              .catch(error => console.error(error));
        },
        fetchScheduleEntries({ commit }) {
          axios.get('/api/display_schedule_entry/')
            .then(response => {
              commit('setScheduleEntries', response.data);
            })
            .catch(error => console.error(error));
        },
        fetchTugBoats({ commit }) {
          axios.get('/api/display_tugboat/')
            .then(response => {
              commit('setTugBoats', response.data);
            })
            .catch(error => console.error(error));
        },
        updateCurrentRoute({ commit }, route) {
          commit('setCurrentRoute', route);
        },
    },
});
export default store;