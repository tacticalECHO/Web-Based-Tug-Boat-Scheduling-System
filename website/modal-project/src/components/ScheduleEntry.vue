<template>
    <tr v-for="(entry,index) in entryList(entryType)" :key="index" :style="disabled(entryType)">

        <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>

        <td  @click.stop class="number"> {{index+1}} </td>

        <td @click.stop>
            <form v-if="timeInfo === entry.ScheduleEntryId" @submit="edit(entry.ScheduleEntryId)">
                <input v-model="time" :id="'time' + entry.ScheduleEntryId" :ref="'time' + entry.ScheduleEntryId" type="datetime-local">
                <input class="submit-button" type="submit" />
            </form>
            <span @click="$store.selected(entry.ScheduleEntryId, 'time')" v-if="timeInfo != entry.ScheduleEntryId">{{formatDate(entry.TaskId.startTime)}}&emsp;&emsp;{{ formatTime(entry.TaskId.startTime) }}</span> 
        </td>

        <td @click.stop>
            <form v-if="containerBoatInfo === entry.ScheduleEntryId" @submit="edit(entry.ScheduleEntryId)">
                <select @change="edit(entry.ScheduleEntryId)" v-model="containerBoatId">
                    <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                </select>
            </form>
            <span @click="$store.selected(entry.ScheduleEntryId, 'containerBoatId')" v-if="containerBoatInfo != entry.ScheduleEntryId">{{entry.TaskId.ContainerBoatID.ContainerBoatID}}</span> 
        </td>

        <td  @click.stop class="country">{{entry.TaskId.ContainerBoatID.Country}}</td>

        <td @click.stop>
            <form v-if="tugBoatInfo === entry.ScheduleEntryId" @submit="edit(entry.ScheduleEntryId)">
                <input v-model="tugBoat" :id="'tugBoat' + entry.ScheduleEntryId" :ref="'tugBoat' + entry.ScheduleEntryId" type="text">
                <input class="submit-button" type="submit" />
            </form>
            <span @click="$store.selected(entry.ScheduleEntryId, 'tugBoat')" v-if="tugBoatInfo != entry.ScheduleEntryId">{{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join(', ')}}</span> 
        </td>

        <td @click.stop>
            <form v-if="berthInfo === entry.ScheduleEntryId">
                <select @change="edit(entry.ScheduleEntryId)" v-model="berthId"  :id="'berthId' + entry.TaskId.BerthId">
                    <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                </select>
            </form>
            <span @click="$store.selected(entry.ScheduleEntryId, 'berthId')" v-if="berthInfo != entry.ScheduleEntryId">{{ entry.TaskId.BerthId}}</span> 
        </td>

        <td  @click.stop class="work-type"><span class="status-container" :style="getActionStyle(entry.TaskId.Action, entryType)">{{entry.TaskId.Action}}</span></td>

        <td  @click.stop class="start-time">{{entry.startTime}}</td>

        <td  @click.stop class="end-time">{{entry.endTime}}</td>

        <td  @click.stop class="work-status"> <span class="status-container" :style="getStatusStyle(entry.Status, entryType)">{{entry.Status}} </span></td>

        <td  @click.stop class="publish-time">{{entry.publishTime}}</td>
        </tr>
</template>

<script>

export default{
    name: 'ScheduleEntry',
    props: {
        entryType: String,
        entryList: Function,
    },
    mounted(){
        this.$store.dispatch('resetNull');
        this.$store.dispatch('selected');
        this.$store.dispatch('toggle');
    },
    data(){
        return{
            tugBoatInfo: null,
            timeInfo: null,
            containerBoatInfo: null,
            berthInfo: null,
            actionInfo: null,
            statusInfo: null,
        }
    },
    methods: {
        disabled(type){
            let backgroundColor;

            switch (type) {
                case 'Completed':
                backgroundColor = 'rgb(233, 232, 232)';
                break;
                default:
                backgroundColor = 'white';
            }

            return {
                background: backgroundColor,
            };
        },
        // resetNull() {
        //     this.tugBoatInfo = null;
        //     this.timeInfo = null;
        //     this.containerBoatInfo = null;
        //     this.berthInfo = null;
        //     this.actionInfo = null;
        //     this.stateInfo = null;
        // },
        // selected(id, column) {
        //     this.resetNull();
        //     if(column === 'tugBoat'){
        //         this.tugBoatInfo = id;
        //     }else if (column === 'time'){
        //         this.timeInfo = id;
        //     }else if (column === 'containerBoatId'){
        //         this.containerBoatInfo = id;
        //     }else if (column === 'berthId'){
        //         this.berthInfo = id;
        //     }else if (column === 'action'){
        //         this.actionInfo = id;
        //     }else if (column === 'state'){
        //         this.stateInfo = id;
        //     }
        // },
        // toggle(event) {
        //     if (!event.target.closest('form')) {
        //         this.resetNull();
        //     }
        // },
    }
}
</script>

<style scoped>
th {
    text-align: left;
}

td {
    text-align: center;
}

th, td {
    border: 1px solid #dddddd;
    padding: 10px;
}

th {
    background-color: #f2f2f2;
}

form {
    margin-right: none;
}
.submit-button {
    display: none;
}
</style>
