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
            <div class="caption">Captain</div>
            <div class="table-container">
                <table id="captain-info" class="table">
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
                            <td id="captain-status"> <span  class="status-container" :style="getStatusStyle(captain.tugboat.CurrentStatus)">{{captain.tugboat ? captain.tugboat.CurrentStatus : 'waiting'}}</span> </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="caption">Scheduler</div>
            <div class="table-container">
                <table id="scheduler-info" class="table">
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

.caption {
    font-weight: bold;
    text-align: left;
    font-size: 16px;
    margin-bottom: 15px;
}

.table td {
    text-align: left;
}

</style>
