<template>
    <tr v-for="(entry,index) in entryList('Incomplete')" :key="index">

        <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>

        <td  @click.stop class="number"> {{index+1}} </td>

        <td @click.stop>
            <form v-if="timeInfo === entry.ScheduleEntryId" @submit="edit(entry.ScheduleEntryId)">
                <input v-model="time" :id="'time' + entry.ScheduleEntryId" :ref="'time' + entry.ScheduleEntryId" type="datetime-local">
                <input class="submit-button" type="submit" />
            </form>
            <span @click="selected(entry.ScheduleEntryId, 'time')" v-if="timeInfo != entry.ScheduleEntryId">{{formatDate(entry.TaskId.startTime)}}&emsp;&emsp;{{ formatTime(entry.TaskId.startTime) }}</span> 
        </td>

        <td @click.stop>
            <form v-if="containerBoatInfo === entry.ScheduleEntryId" @submit="edit(entry.ScheduleEntryId)">
                <select @change="edit(entry.ScheduleEntryId)" v-model="containerBoatId">
                    <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                </select>
            </form>
            <span @click="selected(entry.ScheduleEntryId, 'containerBoatId')" v-if="containerBoatInfo != entry.ScheduleEntryId">{{entry.TaskId.ContainerBoatID.ContainerBoatID}}</span> 
        </td>

        <td  @click.stop class="country">{{entry.TaskId.ContainerBoatID.Country}}</td>

        <td @click.stop>
            <form v-if="tugBoatInfo === entry.ScheduleEntryId" @submit="edit(entry.ScheduleEntryId)">
                <input v-model="tugBoat" :id="'tugBoat' + entry.ScheduleEntryId" :ref="'tugBoat' + entry.ScheduleEntryId" type="text">
                <input class="submit-button" type="submit" />
            </form>
            <span @click="selected(entry.ScheduleEntryId, 'tugBoat')" v-if="tugBoatInfo != entry.ScheduleEntryId">{{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join(', ')}}</span> 
        </td>

        <td @click.stop>
            <form v-if="berthInfo === entry.ScheduleEntryId">
                <select @change="edit(entry.ScheduleEntryId)" v-model="berthId"  :id="'berthId' + entry.TaskId.BerthId">
                    <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                </select>
            </form>
            <span @click="selected(entry.ScheduleEntryId, 'berthId')" v-if="berthInfo != entry.ScheduleEntryId">{{ entry.TaskId.BerthId}}</span> 
        </td>

        <td  @click.stop class="work-type"><span class="status-container" :style="getActionStyle(entry.TaskId.Action)">{{entry.TaskId.Action}}</span></td>

        <td  @click.stop class="start-time">{{entry.startTime}}</td>

        <td  @click.stop class="end-time">{{entry.endTime}}</td>

        <td  @click.stop class="work-status"> <span class="status-container" :style="getStatusStyle(entry.Status)">{{entry.Status}} </span></td>

        <td  @click.stop class="publish-time">{{entry.publishTime}}</td>
        </tr>
</template>

<script>

export default{
    name: 'ScheduleEntry',
    props: [],
    mounted() {
        this.$store.dispatch('fetchScheduleEntries');
        this.$store.dispatch('fetchTasks');
        this.$store.dispatch('fetchContainerBoats');
        this.$store.dispatch('fetchBerths');
        this.$store.dispatch('fetchTugBoats');
    },
    methods: {
        resetNull() {
            this.tugBoatInfo = null;
            this.timeInfo = null;
            this.containerBoatInfo = null;
            this.berthInfo = null;
            this.actionInfo = null;
            this.stateInfo = null;

        },
        selected(id, column) {
            this.resetNull();
            if(column === 'requiredTugBoat'){
                this.tugBoatInfo = id;
                // this.$nextTick(() => {
                //     this.$refs['requiredTugBoat'+id].focus();
                // });
            }else if (column === 'time'){
                this.timeInfo = id;
            }else if (column === 'containerBoatId'){
                this.containerBoatInfo = id;
            }else if (column === 'berthId'){
                this.berthInfo = id;
            }else if (column === 'action'){
                this.actionInfo = id;
            }else if (column === 'state'){
                this.stateInfo = id;
            }
        },
        toggle(event) {
            if (!event.target.closest('form')) {
                this.resetNull();
            }
        },
        entryList(state) {
            this.entries = this.$store.state.scheduleEntries;
            const isCompleted = state === 'Completed';
            this.formatInput();

            return this.entries.filter((entry) => {
                const byCountry = !this.countryInput || entry.TaskId.ContainerBoatID.Country.toString() === this.countryInput;
                const byContainerBoatId = !this.containerBoatInput || entry.TaskId.ContainerBoatID.ContainerBoatID.toString() === this.containerBoatInput;
                const byTugBoatId = !this.tugBoatInput || entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).includes(this.tugBoatInput);
                const byBerthId = !this.berthInput || entry.TaskId.BerthId.toString() === this.berthInput;
                const byWorkType = !this.workTypeInput || entry.TaskId.Action === this.workTypeInput;
                const byStatus = !this.statusInput || entry.Status === this.statusInput;
                const byCompleted = entry.Status === 'Completed';

                return byCountry && byContainerBoatId && byTugBoatId && byBerthId && byWorkType && byStatus && (isCompleted ? byCompleted : !byCompleted);
            });
        },
    }
}
</script>
