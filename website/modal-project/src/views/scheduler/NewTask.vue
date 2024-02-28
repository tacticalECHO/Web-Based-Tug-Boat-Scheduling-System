<template>
    <div id="NewTask">
        <SideBar />
        <form @submit.prevent="save()">
            <div class="pages">
                <router-view />
                <h2>New Task</h2>
                    <table>
                        <tr>
                            <th><label for="containerBoatId">Container Boat</label></th>
                            <td><input type="text" v-model="containerBoatId" placeholder="Input the ID of Container Boat"></td>
                        </tr>
                        <tr>
                            <th><label for="country">Country</label></th>
                            <td><input type="text" v-model="country" placeholder="Input the Country"></td>
                        </tr>
                        <tr>
                            <th><label for="tonnage">Tonnage</label></th>
                            <td><input type="text" v-model="tonnage" placeholder="Input Tonnage of Ship"></td>
                        </tr>
                        <tr>
                            <th><label for="arrivalTime">Arrival Time</label></th>
                            <td><input type="datetime-local" v-model="arrivalTime" placeholder="Set Arrive Time"></td>
                        </tr>
                        <tr>
                            <th><label for="leaveTime">Leave Time</label></th>
                            <td><input type="datetime-local" v-model="leaveTime" placeholder="Set Leave Time"></td>
                        </tr>
                        <tr>
                            <th><label for="requiredTugBoat">Required Tug Boats</label></th>
                            <td><input type="text" v-model="requiredTugBoat" placeholder="Set number of Tug Boats required"></td>
                        </tr>
                        <tr>
                            <th><label for="action">Action</label></th>
                            <td>
                                <select v-model="action">
                                    <option>Arrival</option>
                                    <option>Departure</option>
                                </select>
                            </td>
                        </tr>
                    </table>
            </div>
            <div class="cancel-save-buttons">
                <button class="grey-border-button" id="cancel" @click="redirect('Exit-NewTask')">Cancel</button>
                <input class="save" type="submit" value="Save">
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
    data() {
        return{
            taskSuccess: false,
            containerBoatSuccess: false,
        }
    },
    mounted() {
        this.$store.dispatch('fetchTasks');
        this.$store.dispatch('fetchContainerBoats');
    },
    methods: {
        async save(){
            try { 
                const response = await axios.post('http://localhost:8000/api/save-containerboat/', {
                containerBoatId: this.containerBoatId,
                arrivalTime: this.arrivalTime,
                leaveTime: this.leaveTime,
                tonnage: this.tonnage,
                country: this.country,
                requiredTugBoat: this.requiredTugBoat,
                containerBoatId: this.containerBoatId,
                action: this.action,
                berthId: this.berthId,
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
                    alert('Add container boat Failed.');
                }
            } catch (error) {
                console.error('Add container boat error:', error);
                alert('Add container boat Error.');
            }
        }
    }
}
</script>

<style scoped>
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

option {
    background: var(--main-button-color);
}
</style>
