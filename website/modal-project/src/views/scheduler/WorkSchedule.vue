<template>
    <div id="WorkSchedule">
        <SideBar />
        <div class="pages">
            <h2>Work Schedules</h2>
            <div class="header-style" >
                <button class="grey-border-button" id="filter">Filter Schedules <font-awesome-icon :icon="['fas', 'filter']" /></button>
                <button class="grey-border-button" id="Publish">Publish <font-awesome-icon :icon="['fas', 'upload']" /></button>
            </div>
            <div class="work-table">
                <table>
                    <thead>
                        <tr>
                            <th>No.1</th>
                            <th>Container Boat</th>
                            <th>Berth</th>
                            <th>Start Time</th>
                            <th>End Time</th>
                            <th>Tug Boat</th>
                            <th>Captain</th>
                            <th>Work Status</th>
                            <th>Work Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="entry in entryList()" :key="entry.ScheduleEntryId">
                            <td class="number"> {{entry.ScheduleEntryId}} </td>
                            <td class="container-boat"> {{entry.TaskId.ContainerBoatID.ContainerBoatID}} </td>
                            <td class="berth"> {{entry.TaskId.BerthId}} </td>
                            <td class="time"> {{entry.listOfTugBoats.StartWorkingTime}} </td>
                            <td class="tugboat"> {{entry.listOfTugBoats.EndWorkingTime}} </td>
                            <td class="captain"> {{entry.listOfTugBoats.CaptainId}} </td>
                            <td class="work-status"> <span class="status-container">{{entry.listOfTugBoats.CurrentStatus}} </span></td>
                            <td class="work-type"> <span class="type-container">{{entry.State}}</span></td>
                        </tr>
                    </tbody>
                </table>
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
    },
    data(){
        return{
            entries: [],
            input: '',
        }
    },
    methods: {
        entryList(){
            return this.entries = this.$store.state.entries

            // this.entries = this.$store.state.entries
            // const filtered = this.tasks.filter((entry) => {
            //     const byEntryId = entry.ScheduleEntryId.toString().includes(this.input);
            //     const byContainerBoatId = entry.TaskId.ContainerBoatID.toLowerCase().includes(this.input.toLowerCase());
            //     const byBerthId = entry.TaskId.BerthId.toString().includes(this.input);
            //     const byState = entry.State.toLowerCase().includes(this.input.toLowerCase());

            //     return byTaskId || byContainerBoatId || byBerthId || byAction;
            // });
        }
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
</style>
