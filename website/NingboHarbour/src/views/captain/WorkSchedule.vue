<template>
    <div id="WorkSchedule">
        <SideBar />
        <div class="pages">
            <h2 class="title">Work Schedules</h2>
            <br><br><br>
            <div class="header-style" >
                <div class ="filter-group">
                    <span class="filter">
                        <label for="containerBoatFilter">Container Boat: </label>
                        <select v-model="containerBoatInput">
                            <option value="">All</option>
                            <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="tugBoatFilter">Tug Boat: </label>
                        <select v-model="tugBoatInput">
                            <option value="">All</option>
                            <option v-for="tugboat in $store.state.tugboats" :key="tugboat.TugBoatId">{{ tugboat.TugBoatId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="berthFilter">Berth: </label>
                        <select v-model="berthInput">
                            <option value="">All</option>
                            <option v-for="berth in $store.state.berths" :key="berth.BerthId">{{ berth.BerthId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="stateFilter">Status: </label>
                        <select v-model="stateInput">
                            <option value="">All</option>
                            <option>Scheduled</option>
                            <option>Confirmed</option>
                            <option>Completed</option>
                        </select>
                    </span>
                </div>
            </div>
            <div v-if="waiting()">
                <span class="spinner-border spinner-border-sm" role="status"></span>
                &nbsp;Waiting...
            </div>
            <div v-if="!waiting()" class="table-container">
                <table class="table">
                    <thead>
                        <tr>
                            <th>No.</th>
                            <th>Container Boat</th>
                            <th>Berth</th>
                            <th>Time
                                <div class="sorting">
                                    <input value="private" name="switch" id="switch" type="checkbox" class="switch" :checked="sort" @change="sorting()">
                                    <label for="switch">
                                        <span class="switch-x-toggletext">
                                            <span class="switch-x-unchecked">Default</span>
                                            <span class="switch-x-checked">Sorted</span>
                                        </span>
                                    </label>
                                </div>
                            </th>
                            <th>Tug Boat</th>
                            <th>Captain</th>
                            <th>Work Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(entry,index) in entryList('Incomplete')" :key="index">
                            <td class="number"> {{index+1}} </td>
                            <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                            <td class="berth"> {{entry.TaskId.BerthId}} </td>
                            <td class="time"> {{formatDate(entry.TaskId.startTime)}} &nbsp; {{formatTime(entry.TaskId.startTime)}} </td>
                            <td class="tugboat"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join("/ ")}} </td>
                            <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId ? tugBoat.CaptainId.CaptainId : 'waiting ').join("/ ")}} </td>
                            <td class="work-status"> 
                                <span class="status-container" :style="getStatusStyle(entry.Status)">{{entry.Status}} </span>
                            </td>
                        </tr>
                        <tr class="disabled-row" v-for="(entry,index) in entryList('Completed')" :key="index">
                            <td class="number"> {{index+1}} </td>
                            <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                            <td class="berth"> {{entry.TaskId.BerthId}} </td>
                            <td class="time"> {{formatDate(entry.TaskId.startTime)}} &nbsp; {{formatTime(entry.TaskId.startTime)}} </td>
                            <td class="tugboat"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join("/")}} </td>
                            <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId ? tugBoat.CaptainId.CaptainId : 'waiting ').join("/")}} </td>
                            <td class="work-status"> 
                                <span class="status-container">{{entry.Status}} </span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import axios from 'axios';

export default {
    name: 'WorkSchedule',
    components: {SideBar},
    mounted(){
        this.$store.dispatch('fetchScheduleEntries', this.sort);
        this.$store.dispatch('fetchTasks', this.sort);
        this.$store.dispatch('fetchContainerBoats');
        this.$store.dispatch('fetchBerths');
        this.$store.dispatch('fetchTugBoats');
    },
    data(){
        return{
            entries: [],
            containerBoatInput: '',
            tugBoatInput: '',
            berthInput: '',
            stateInput: '',
            sort: false,
        }
    },
    methods: {
        sorting(){
            this.sort = !this.sort;
            this.$store.dispatch('fetchScheduleEntries', this.sort);
            this.$store.dispatch('fetchTasks', this.sort);
        },
        waiting(){
            if(this.$store.state.scheduleEntries.length === 0){
                return true
            }
            return false
        },
        checkAll(input) {
            if (input === "All") {
                return '';
            } else {
                return input;
            }
        },
        entryList(state) {
            this.entries = this.$store.state.scheduleEntries;
            this.containerBoatInput = this.checkAll(this.containerBoatInput);
            this.tugBoatInput = this.checkAll(this.tugBoatInput);
            this.berthInput = this.checkAll(this.berthInput);
            this.stateInput = this.checkAll(this.stateInput);

            const isCompleted = state === 'Completed';

            const filtered = this.entries.filter((entry) => {  
                const byContainerBoatId = this.containerBoatInput ? entry.TaskId.ContainerBoatID.ContainerBoatID.toString() === this.containerBoatInput : true;
                const byTugBoatId = this.tugBoatInput ? entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).includes(this.tugBoatInput) : true;
                const byBerthId = this.berthInput ? entry.TaskId.BerthId.toString() === this.berthInput : true;
                const byState = this.stateInput ? entry.Status === this.stateInput : true;
                const byCompleted = entry.Status === 'Completed';

                return byContainerBoatId && byTugBoatId && byBerthId && byState && (isCompleted ? byCompleted : !byCompleted);
            });

            return filtered;
        },
    }
}
</script>

<style scoped>

button{
    border-radius: 10px;
}

.header-style{
    padding: 10px;
}

@media (max-width: 768px) {
    .filter-group {
        justify-content: space-between;
    }

}
</style>
