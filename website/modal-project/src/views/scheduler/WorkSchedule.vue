<template>
    <div id="WorkSchedule">
        <SideBar />
        <div class="pages">
            <h2>Work Schedules</h2>
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
            <div  class="display-data">
                <div class="work-table">
                    <table>
                        <thead>
                            <tr>
                                <th>No.</th>
                                <th>Container Boat</th>
                                <th>Berth</th>
                                <th>Time</th>
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
                                <td class="time"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.EndWorkingTime).join("/ ")}} </td>
                                <td class="tugboat"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join("/ ")}} </td>
                                <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId.CaptainId).join("/ ")}} </td>
                                <td class="work-status"> 
                                    <span class="status-container" :style="getStatusStyle(entry.Status)">{{entry.Status}} </span>
                                </td>
                            </tr>
                            <tr class="disabled-row" v-for="(entry,index) in entryList('Completed')" :key="index">
                                <td class="number"> {{index+1}} </td>
                                <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                                <td class="berth"> {{entry.TaskId.BerthId}} </td>
                                <td class="time"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.EndWorkingTime).join("/")}} </td>
                                <td class="tugboat"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join("/")}} </td>
                                <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId.CaptainId).join("/")}} </td>
                                <td class="work-status"> 
                                    <span class="status-container">{{entry.Status}} </span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
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
        this.$store.dispatch('fetchScheduleEntries');
        this.$store.dispatch('fetchTasks');
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
        }
    },
    methods: {
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
                const byState = this.stateInput ? entry.State === this.stateInput : true;
                const byCompleted = entry.Status === 'Completed';

                return byContainerBoatId && byTugBoatId && byBerthId && byState && (isCompleted ? byCompleted : !byCompleted);
            });

            return filtered;
        },
    }
}
</script>

<style scoped>
.filter-group {
    padding: 10px;
}

.filter{
    font-size: var(--font-size);
    border: 2px solid grey;
    border-radius: 10px;
    padding: 10px;
    margin-right: 5px;
}

.filter select{
    border: none;
}

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
