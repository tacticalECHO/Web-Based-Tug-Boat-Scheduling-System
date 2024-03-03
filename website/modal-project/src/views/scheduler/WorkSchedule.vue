<template>
    <div id="WorkSchedule">
        <SideBar />
        <div class="pages" @click="toggle">
            <h2>Work Schedules</h2>
            <div class="header-style" >
                <div class ="filter-group">
                    <span class="filter">
                        <label for="containerBoatFilter">Container Boat: </label>
                        <select v-model="containerBoatFilter" @change="containerBoatInput = containerBoatFilter">
                            <option>All</option>
                            <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="tugBoatFilter">Tug Boat: </label>
                        <select v-model="tugBoatFilter" @change="tugBoatInput = tugBoatFilter">
                            <option>All</option>
                            <option v-for="tugboat in $store.state.tugboats" :key="tugboat.TugBoatId">{{ tugboat.TugBoatId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="berthFilter">Berth: </label>
                        <select v-model="berthFilter">
                            <option>All</option>
                            <option v-for="berth in $store.state.berths" :key="berth.BerthId">{{ berth.BerthId }}</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="stateFilter">State: </label>
                        <select v-model="stateFilter" @change="stateInput = stateFilter">
                            <option>All</option>
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
                            <tr v-for="entry in entryList()" :key="entry.ScheduleEntryId">
                                <td class="number"> {{entry.ScheduleEntryId}} </td>
                                <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                                <td class="berth"> {{entry.TaskId.BerthId}} </td>
                                <td class="time"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.EndWorkingTime).join("/")}} </td>
                                <td class="tugboat"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join("/")}} </td>
                                <td class="captain"> {{entry.listOfTugBoats.map(tugBoat => tugBoat.CaptainId.CaptainId).join("/")}} </td>
                                <td class="work-status" @click.stop> 
                                    <span v-if="stateInfo != entry.ScheduleEntryId" @click="stateInfo = entry.ScheduleEntryId" class="status-container">{{entry.State}} </span>
                                    <form v-if="stateInfo === entry.ScheduleEntryId">
                                        <select @change="edit(entry.ScheduleEntryId)" v-model="state">
                                            <option>{{ displayState(entry.State) }}</option>
                                        </select>
                                    </form>
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
            stateInfo: null,
        }
    },
    methods: {
        // async edit(id){
        //     const state = this.state;
        //     const tugBoatState = null;
        //     if(this.state === "Start Job"){
        //         state = "Confirmed";
        //         tugBoatState = "Busy";
        //     }else if(this.state === "Complete Job"){
        //         state = "Completed";
        //         tugBoatState = "Free";
        //     }
        //     try { 
        //         const response = await axios.post('http://localhost:8000/api/save-task/', {
        //         scheduleEntryId: id,
        //         state: state,
        //         tugBoatState: tugBoatState,
        //         });
        //         if (response.data.success) {
        //             alert('Updated Successfully - ' + state);
        //             window.location.reload();
        //             stateInfo = null;
        //         } else {
        //             alert('Updated Failed.');
        //         }
        //     } catch (error) {
        //         console.error('Updated error:', error);
        //         alert('Updated Error.');
        //     }
        // },
        toggle(event){
            if (!event.target.closest('form')) {
                this.stateInfo = null;
            }
        },
        displayState(state){
            if(state === "Scheduled"){
                return "Start Job";
            }else if(state === "Confirmed"){
                return "Complete Job";
            }
            return "";
        },
        checkAll(input) {
            if (input === "All") {
                return '';
            } else {
                return input;
            }
        },
        entryList() {
            this.entries = this.$store.state.scheduleEntries;
            this.containerBoatInput = this.checkAll(this.containerBoatInput);
            this.tugBoatInput = this.checkAll(this.tugBoatInput);
            this.berthInput = this.checkAll(this.berthInput);
            this.stateInput = this.checkAll(this.stateInput);

            const filtered = this.entries.filter((entry) => {  
                const byContainerBoatId = this.containerBoatInput ? entry.TaskId.ContainerBoatID.ContainerBoatID.toString() === this.containerBoatInput : true;
                const byTugBoatId = this.tugBoatInput ? entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).includes(this.tugBoatInput) : true;
                const byBerthId = this.berthInput ? entry.TaskId.BerthId.toString() === this.berthInput : true;
                const byState = this.stateInput ? entry.State === this.stateInput : true;

                return byContainerBoatId && byTugBoatId && byBerthId && byState;
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
