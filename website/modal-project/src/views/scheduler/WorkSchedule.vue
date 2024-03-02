<template>
    <div id="WorkSchedule">
        <SideBar />
        <div class="pages">
            <h2>Work Schedules</h2>
            <div class="header-style" >
                <div class ="filter-group">
                    <span class="filter">
                        <label for="entryFilter">Entry: </label>
                        <select v-model="entryFilter" @change="entryInput = entryFilter">
                            <option></option>
                            <option v-for="entry in $store.state.scheduleEntries" :key="entry.ScheduleEntryId">{{ entry.ScheduleEntryId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="taskFilter">Task: </label>
                        <select v-model="taskFilter" @change="taskInput = taskFilter">
                            <option></option>
                            <option v-for="task in $store.state.tasks" :key="task.TaskId">{{ task.TaskId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="containerBoatFilter">Container Boat: </label>
                        <select v-model="containerBoatFilter" @change="containerBoatInput = containerBoatFilter">
                            <option></option>
                            <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="tugBoatFilter">Tug Boat: </label>
                        <select v-model="tugBoatFilter" @change="tugBoatInput = tugBoatFilter">
                            <option></option>
                            <option v-for="tugboat in $store.state.tugboats" :key="tugboat.TugBoatId">{{ tugboat.TugBoatId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="berthFilter">Berth: </label>
                        <select v-model="berthFilter">
                            <option></option>
                            <option v-for="berth in $store.state.berths" :key="berth.BerthId">{{ berth.BerthId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="stateFilter">State: </label>
                        <select v-model="stateFilter" @change="stateInput = stateFilter">
                            <option></option>
                            <option>Completed</option>
                            <option>Scheduled</option>
                        </select>
                    </span>
                </div>
                <button class="blue-button" id="Publish">Publish <font-awesome-icon :icon="['fas', 'upload']" /></button>
            </div>
            <div class="table-container">
                <div class="work-table">
                    <table>
                        <thead>
                            <tr>
                                <th>No.</th>
                                <th>Container Boat</th>
                                <th>Berth</th>
                                <th>Start Time</th>
                                <th>End Time</th>
                                <th>Tug Boat</th>
                                <th>Captain</th>
                                <th>Work Status</th>
                                <th>State</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="entry in entryList()" :key="entry.ScheduleEntryId">
                                <td class="number"> {{entry.ScheduleEntryId}} </td>
                                <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                                <td class="berth"> {{entry.TaskId.BerthId}} </td>
                                <td class="time"> {{entry.listOfTugBoats.StartWorkingTime}} </td>
                                <td class="time"> {{entry.listOfTugBoats.EndWorkingTime}} </td>
                                <td class="tugboat"> {{entry.listOfTugBoats.TugBoatId}} </td>
                                <td class="captain"> {{entry.listOfTugBoats.CaptainId}} </td>
                                <td class="work-status"> <span class="status-container">{{entry.listOfTugBoats.CurrentStatus}} </span></td>
                                <td class="work-type"> <span class="type-container">{{entry.State}}</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'

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
            tasks: [],
            entryInput: '',
            taskInput: '',
            containerBoatInput: '',
            tugBoatInput: '',
            berthInput: '',
            stateInput: '',
        }
    },
    methods: {
        entryList() {
            this.entries = this.$store.state.scheduleEntries;

            const filtered = this.entries.filter((entry) => {  
                const byEntryId = this.entryInput ? entry.ScheduleEntryId.toString() === this.entryInput : true;
                const byTaskId = this.taskInput ? entry.TaskId.toString() === this.taskInput : true;
                const byContainerBoatId = this.containerBoatInput ? entry.TaskId.ContainerBoatID.ContainerBoatID.toString() === this.containerBoatInput : true;
                const byTugBoatId = this.tugBoatInput ? entry.TugBoatId === this.tugBoatInput : true;
                const byBerthId = this.berthInput ? entry.TaskId.BerthId.toString() === this.berthInput : true;
                const byState = this.stateInput ? entry.State === this.stateInput : true;

                return byEntryId && byTaskId && byContainerBoatId && byTugBoatId && byBerthId && byState;
            });

            return filtered;
        }
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
</style>
