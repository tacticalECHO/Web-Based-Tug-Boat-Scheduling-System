<template>
    <div id="CaptainDashboard">
        <SideBar />
        <div class="pages" @click="toggle">
            <div class="header-style">
                <div class="header-style title">
                    <h2>Today Work</h2>
                    <button id="download" @click="download()"><font-awesome-icon :icon="['fas', 'download']" /></button>
                </div>
                <MessageButton />
            </div>
            <br><br><br><br>
            <div v-if="waiting()">
            <span class="spinner-border spinner-border-sm" role="status"></span>
            &nbsp;Waiting...
        </div>
        <div class="table-container">
            <table v-if="!waiting()" class="table"> 
                <thead>
                    <tr>
                        <th>No.</th>
                        <th>Container Boat</th>
                        <th>Berth</th>
                        <th>Time</th>
                        <th>Captain</th>
                        <th>Work Status</th>
                        <th>Work Type</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(entry,index) in entryList('Incompleted')" :key="index">
                        <td class="number">  <span :id="'entryId' + entry.ScheduleEntryId">{{index+1}}</span> </td>
                        <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                        <td class="berth"> {{entry.TaskId.BerthId}} </td>
                        <td class="time"> {{formatDate(entry.TaskId.startTime)}} &emsp;&emsp; {{formatTime(entry.TaskId.startTime)}} </td>
                        <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId ? tugBoat.CaptainId.CaptainId : 'waiting ').join(",")}} </td>
                        <td @click.stop>
                            <form v-if="showStateForm === entry.ScheduleEntryId">
                                <select @change="edit(entry.ScheduleEntryId)" v-model="state" :id="'state' + entry.ScheduleEntryId" >
                                    <!-- <option>Scheduled</option> -->
                                    <option>Confirmed</option>    
                                    <option>Completed</option>                               
                                </select>
                            </form>
                            <span class="status-container click-hover" @click="selected(entry.ScheduleEntryId, 'state')" v-if="stateInfo != entry.ScheduleEntryId" :style="getStatusStyle(entry.Status, 'Incomplete')">{{entry.Status}}</span> 
                        </td>
                        <td class="work-type"> <span class="type-container" :style="getActionStyle(entry.TaskId.Action, 'Incomplete')">{{entry.TaskId.Action}}</span></td>
                    </tr>

                    <!-- --completed---------------------------------------------------------------------------------------------- -->
                    <tr class="disabled-row" v-for="(entry,index) in entryList('Completed')" :key="index">
                        <td class="number">  <span :id="'taskId' + entry.ScheduleEntryId">{{index+1}}</span> </td>
                        <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                        <td class="berth"> {{entry.TaskId.BerthId}} </td>
                        <td class="time"> {{formatDate(entry.TaskId.startTime)}} &emsp;&emsp; {{formatTime(entry.TaskId.startTime)}} </td>
                        <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId ? tugBoat.CaptainId.CaptainId : 'waiting ').join(",")}} </td>
                        <td>
                            <span class="status-container" @click="selected(entry.ScheduleEntryId, 'state')" :style="getStatusStyle(entry.Status, 'Completed')">{{entry.Status}}</span> 
                        </td>
                        <td class="work-type"> <span class="type-container" :style="getActionStyle(entry.TaskId.Action, 'Completed')">{{entry.TaskId.Action}}</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import MessageButton from '@/components/MessageButton.vue'
import axios from 'axios';
import { mapState } from 'vuex';

export default {
    name: 'CaptainDashboard',
    components: {SideBar, MessageButton},
    mounted(){
        this.$store.dispatch('fetchScheduleEntries');
        this.$store.dispatch('fetchCaptains');
    },
    data() {
        return {
            showStateForm: null,
            stateInfo: null,
            entries: [],
            captains: [],
        }
    },
    computed: {
        ...mapState(['username', 'isCaptain', 'isAdmin', 'isScheduler']),
        captain() {
            return this.username;
        }
    },
    methods: {
        download(){
            const captainId = localStorage.getItem('username');
            axios.post('/api/download-captain', { captainId })
            .then(response => {
                console.log(response.data.message);
                alert("Successfully Download!");
            }).catch(error => {
                console.error("error: ", error);
                alert("Failed to download data, check logs for details.");
            });
        },
        waiting(){
            if(this.entryList('Incompleted').length === 0 && this.entryList('Completed').length === 0){
                return true
            }
            return false
        },
        entryList(state){
            this.entries = this.$store.state.scheduleEntries;
            const isCompleted = state === 'Completed';

            return this.entries.filter((entry) => {
                const byCaptain = entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId ? tugBoat.CaptainId.CaptainId : 'waiting ').includes(this.captain);
                const byCompleted = entry.Status === 'Completed';

                return byCaptain && (isCompleted ? byCompleted : !byCompleted);
            });
        },
        resetNull() {
            this.showStateForm = null;
            this.stateInfo = null;
        },
        selected(id, column) {
            this.resetNull();
            if (column === 'state'){
                this.showStateForm = id;
                this.stateInfo = id;
            }else if (column === 'containerBoatId'){
                this.showContainerBoatIdForm = id;
                this.containerBoatIdInfo = id;
            }
        },
        toggle(event) {
            if (!event.target.closest('form')) {
                this.resetNull();
            }
        },
        async edit(entryId) {
            const newState = this.state;
            const currentTime = new Date().toISOString();
            try {
                const response = await axios.post('/api/update-schedule-entry', { 
                    entryId: entryId,
                    newState: newState,
                    timeStamp: currentTime
                });
                console.log(response.data);
                window.location.reload();
                alert('Update Successfully');
            } catch (error) {
                console.error(error);
                alert('Update Failed');
            }
        }
    }
}
</script>

<style scoped>
#download {
    border: none;
    margin-left: 10px;
    border-radius: 50%;
    height: 35px;
    width: 35px;
    padding: 5px;
}

#download:hover {
    border: 2px solid black;
}
</style>
