<!-- Vue file created by Team 10, ©2024 -->
<template>
    <div id="AdminDashboard">
        <SideBar />
        <div class="pages">
            <router-view />
            <h2 class="title">Your Dashboard</h2>
            <div class="header-style">
                <span></span>
                <!-- add and delete button  -->
                <span class="add-delete">
                    <button type="button" class="delete" id="delete" @click= deleteSelected>
                        <span class="delete__text">Delete &nbsp;</span>
                        <span class="delete__icon"><font-awesome-icon :icon="['fas', 'delete-left']" /></span>
                    </button>
                    &nbsp;
                    <button type="button" class="add" id="new-staff" @click="redirect('NewStaff')">
                        <span class="add__text">New &nbsp;</span>
                        <span class="add__icon"><font-awesome-icon :icon="['fas', 'plus']" /></span>
                    </button>
                </span>
            </div>
            <!-- section for displaying captain  -->
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
                            <td id="captain-status">
                                <span class="status-container" :style="captain.tugboat ? getStatusStyle(captain.tugboat.CurrentStatus) : {}">
                                    {{ captain.tugboat ? captain.tugboat.CurrentStatus : 'waiting' }}
                                </span>
                            </td>

                        </tr>
                    </tbody>
                </table>
            </div>
            <!-- section for displaying scheduler  -->
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
        async deleteSelected() { // post data to delete selected user
            if(this.deletionAlert()){
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

                alert('Deleted successfully');

                this.$store.dispatch('fetchCaptains');
                this.$store.dispatch('fetchSchedulers');
            }
            this.selectedCaptains = [];
            this.selectedSchedulers = [];
        }
  },
}
</script>

<style scoped>

.header-style{
    padding: 10px;
}

.caption {
    font-weight: bold;
    text-align: left;
    font-size: 16px;
    margin-bottom: 15px;
}

.table td, .table th{
    text-align: left;
}

.table-container {
    max-height: 20em;
}

</style>
