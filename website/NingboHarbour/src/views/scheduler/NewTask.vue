<!-- Vue file created by Team 10, ©2024 -->
<template>
    <div id="NewTask">
        <SideBar />
        <form @submit.prevent="save()">
            <div class="pages">
                <router-view />
                <h2 class="title">New Task</h2>
                <br><br><br>
                    <table>
                        <tr>
                            <th><label for="containerBoatId">Container Boat</label></th>
                            <td><input type="text" v-model="containerBoatId" placeholder="Input the ID of Container Boat" required></td>
                        </tr>
                        <tr>
                            <th><label for="country">Country</label></th>
                            <td><input type="text" v-model="country" placeholder="Input the Country" required></td>
                        </tr>
                        <tr>
                            <th><label for="tonnage">Tonnage</label></th>
                            <td><input type="text" v-model="tonnage" placeholder="Input Tonnage of Ship" required></td>
                        </tr>
                        <tr>
                            <th><label for="requiredTugBoat">Total Tugboat Required</label></th>
                            <td><input type="text" v-model="requiredTugBoat" placeholder="Input Number of Tugboats Needed" required></td>
                        </tr>
                        <tr>
                            <th><label for="time">Time</label></th>
                            <td><input type="datetime-local" v-model="time" placeholder="Set time" required></td>
                        </tr>
                        <tr>
                            <th><label for="action">Action</label></th>
                            <td>
                                <select v-model="action" required>
                                    <option>INBOUND</option>
                                    <option>OUTBOUND</option>
                                </select>
                            </td>
                        </tr>
                        <tr>
                            <th><label for="berth">Berth</label></th>
                            <td>
                                <select v-model="berth" required>
                                    <option v-for="berth in $store.state.berths" :key="berth.BerthId">{{ berth.BerthId }}</option>
                                </select>
                            </td>
                        </tr>
                    </table>
            </div>
            <div class="cancel-save-buttons">
                <button class="btn btn-outline-dark" id="cancel" @click="redirect('Exit-NewTask')">Cancel</button>
                <input class="btn btn-dark" type="submit" value="Save">
            </div>
        </form>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import axios from 'axios';

export default {
    name: 'NewTask',
    components: {SideBar},
    mounted() {
        this.$store.dispatch('fetchBerths');
        this.$store.commit('setExitPath', 'SchedulerDashboard');
    },
    methods: {
        async save(){
            try { 
                const response = await axios.post('/api/save-newtask/', {
                containerBoatId: this.containerBoatId,
                time: this.time,
                tonnage: this.tonnage,
                country: this.country,
                requiredTugBoat: this.requiredTugBoat,
                action: this.action,
                berthId: this.berth,
                state: this.state,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                if (response.data.success) {
                    alert('Added successfully');
                    this.$router.push({name: 'Save-NewTask'});
                } else {
                    alert('Add new task Failed.');
                }
            } catch (error) {
                console.error('Add new task error:', error);
                alert('Add new task Error.');
            }
        }
    }
}
</script>

<style scoped>
.btn {
    width: 100px;
}

.btn-outline-dark:hover{
    background-color: lightgray;
}

.btn-dark:hover{
    background-color: darkgray;
}

table {
    font-size: 13px;
    text-align: left;
    margin-bottom: 15px;
}

th, td {
    padding: 10px;
}

.pages input, select {
    font-size: 13px;
    border: none;
    padding: 8px;
    border-radius: 10px;
    border: 1px solid grey;
    width: 300px;
}

td {
    border: none;
}
</style>
