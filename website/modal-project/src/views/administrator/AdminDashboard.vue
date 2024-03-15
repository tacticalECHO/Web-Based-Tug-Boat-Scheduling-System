<template>
    <div id="AdminDashboard">
        <SideBar />
        <div class="pages">
            <router-view />
            <h2 class="title">Your Dashboard</h2>
            <div class="header-style">
                <span></span>
                <span>
                    <button class="btn btn-light" id="delete" @click= deleteSelected>Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="btn btn-dark" id="new-staff" @click="redirect('NewStaff')">New Staff  <span>+</span></button>
                </span>
            </div>
            <table id="captain-info">
                <caption><b>Captain</b></caption>
                <thead>
                    <tr>
                        <th><input type="checkbox" disabled></th>
                        <th>Captain Name</th>
                        <th>Captain ID</th>
                        <th>Tug Boat</th>
                        <th>Tug Boat Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="captain in $store.state.captains" :key="captain.CaptainId">
                        <td><input type="checkbox" :id="'checkbox' + captain.CaptainId" :name="'checkbox' + captain.name" v-model="selectedCaptains" :value="captain.CaptainId"></td>
                        <td id="captain-name"> {{captain.name}} </td>
                        <td id="captain-id"> {{captain.CaptainId}} </td>
                        <td id="tugboat"> {{captain.tugboat ? captain.tugboat.TugBoatId : 'waiting'}} </td>
                        <td id="captain-status"> <span  class="status-container">{{captain.tugboat ? captain.tugboat.CurrentStatus : 'waiting'}}</span> </td>
                    </tr>
                </tbody>
            </table>
            <table id="scheduler-info">
                <caption><b>Scheduler</b></caption>
                <thead>
                    <tr>
                        <th><input type="checkbox" disabled></th>
                        <th>Scheduler Name</th>
                        <th>Scheduler ID</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="scheduler in $store.state.schedulers" :key="scheduler.SchedulerId">
                        <td><input type="checkbox" :id="'checkbox' + scheduler.SchedulerId" :name="'checkbox' + scheduler.name" v-model="selectedSchedulers" :value="scheduler.SchedulerId"></td>
                        <td id="scheduler-name"> {{scheduler.name}} </td>
                        <td id="scheduler-id"> {{scheduler.SchedulerId}} </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'AdminDashboard',
    components: {SideBar},
    data() {
        return {
            selectedCaptains: [],
            selectedSchedulers: [],
        };
    },
    mounted() {
        this.$store.dispatch('fetchCaptains');
        this.$store.dispatch('fetchSchedulers');
    },
    methods: {
        async deleteSelected() {
            if (this.selectedCaptains.length > 0) {
                await fetch(`http://127.0.0.1:8000/api/captains-delete/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ ids: this.selectedCaptains })
                });
            }

            if (this.selectedSchedulers.length > 0) {
                await fetch(`http://127.0.0.1:8000/api/schedulers-delete/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ ids: this.selectedSchedulers })
                });
            }

            this.$store.dispatch('fetchCaptains');
            this.$store.dispatch('fetchSchedulers');
            
            this.selectedCaptains = [];
            this.selectedSchedulers = [];
        }
  },
}
</script>

<style scoped>
button{
    border-radius: 20px;
}

.header-style{
    padding: 10px;
}

caption {
    text-align: left;
    font-size: 16px;
    margin-bottom: 15px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: var(--font-size);
}

th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 10px;
}

th {
    background-color: #f2f2f2;
}
</style>
