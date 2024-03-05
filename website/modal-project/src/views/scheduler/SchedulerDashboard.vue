<template>
    <div id="TaskManager">
        <SideBar />
        <div class="pages" @click="toggle">
            <router-view />
            <div class="header-style">
                <h2>My Dashboard</h2>
                <span class="message-container">
                    <button id="message" @click="message()"><font-awesome-icon :icon="['fas', 'bell']" /></button>
                </span>
            </div>
            <div class="job buttons-container">
                <button id="schedule" @click="schedule()">Schedule <font-awesome-icon :icon="['fas', 'calendar-day']" /></button>
                <br><br><br>
                <input type="file" id="import-task-data"/>
                <label for="import-task-data"><button @click="importTaskData()">Import Task Data <font-awesome-icon :icon="['fas', 'file-import']" /></button></label>
                <br><br><br>
                <input type="file" id="import-tugboat-data"/>
                <label for="import-tugboat-data"><button @click="importTugboatData()">Import Tug Boat Data <font-awesome-icon :icon="['fas', 'file-import']" /></button></label>
                <br><br><br>
                <button id="download" @click="download()">Download <font-awesome-icon :icon="['fas', 'download']" /></button>
                <br><br><br>
                <button class="blue-button" id="publish" @click="publish()">Publish <font-awesome-icon :icon="['fas', 'upload']" /></button>
            </div>
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
                        <label for="countryFilter">Country: </label>
                        <select v-model="countryInput">
                            <option value="">All</option>
                            <option v-for="(country, index) in countryList()" :key="index">{{ country }}</option>
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
                        <label for="workTypeFilter">Work Type: </label>
                        <!-- <select v-model="workTypeInput">
                            <option>All</option>
                            <option v-for="task in $store.state.tasks" :key="task.Action">{{ task.Action }}</option>
                        </select> -->
                        <select v-model="workTypeInput">
                            <option value="">All</option>
                            <option>Arrival</option>
                            <option>Departure</option>
                        </select>
                    </span>
                    <span class="filter">
                        <label for="statusFilter">Status: </label>
                        <select v-model="statusInput">
                            <option value="">All</option>
                            <option>Completed</option>
                            <option>Confirmed</option>
                            <option>Scheduled</option>
                            <option>Unscheduled</option>
                        </select>
                    </span>
                </div>
                <span>
                    <button class="blue-border-button" id="delete" @click="redirect('')">Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="blue-border-button" id="add" @click="redirect('NewTask')">Add  + </button>
                </span>
            </div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th rowspan="2"><input type="checkbox"/></th>
                            <th rowspan="2">No.</th>
                            <th rowspan="2">Planned Time</th>
                            <th rowspan="2">Container Boat</th>
                            <th rowspan="2">Country</th>
                            <th rowspan="2">Tug Boat</th>
                            <th rowspan="2">Berth</th>
                            <th rowspan="2">Work Type</th>
                            <th style="text-align: center" colspan="2" >Actual Time</th>
                            <th rowspan="2">Status</th>
                            <th rowspan="2">Publish Time</th>
                        </tr>
                        <tr>
                            <th>Start</th>
                            <th>End</th>
                        </tr>
                    </thead>
                    <tbody>
<!-- --Scheduled / Confirmed--------------------------------------------------------------------------------------------------------- -->
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
                        <!-- <ScheduleEntry /> -->
<!-- --Unscheduled--------------------------------------------------------------------------------------------------------- -->
                        <tr v-for="(task, index) in taskList()" :key="index">
                            <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>

                            <td  @click.stop class="number"> {{index+1}} </td>

                            <td @click.stop>
                                <form v-if="timeInfo === task.TaskId" @submit="edit(task.TaskId)">
                                    <input v-model="time" :id="'time' + task.TaskId" :ref="'time' + task.TaskId" type="datetime-local">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span @click="selected(task.TaskId, 'time')" v-if="timeInfo != task.TaskId">{{formatDate(task.startTime)}}&emsp;&emsp;{{ formatTime(task.startTime) }}</span> 
                            </td>

                            <td @click.stop>
                                <form v-if="containerBoatInfo === task.TaskId" @submit="edit(task.TaskId)">
                                    <select @change="edit(task.TaskId)" v-model="containerBoatId">
                                        <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'containerBoatId')" v-if="containerBoatInfo != task.TaskId">{{task.ContainerBoatID.ContainerBoatID}}</span> 
                            </td>

                            <td  @click.stop class="country">{{task.ContainerBoatID.Country}}</td>

                            <td @click.stop class="disabled-column"></td>

                            <td @click.stop>
                                <form v-if="berthInfo === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="berthId"  :id="'berthId' + task.BerthId">
                                        <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'berthId')" v-if="berthInfo != task.TaskId">{{ task.BerthId}}</span> 
                            </td>

                            <td  @click.stop class="work-type"><span class="status-container" :style="getActionStyle(task.Action)">{{task.Action}}</span></td>

                            <td  @click.stop class="disabled-column">{{}}</td>

                            <td  @click.stop class="disabled-column">{{}}</td>

                            <td  @click.stop class="work-status"> <span class="status-container" :style="getStatusStyle(task.State)">{{task.State}} </span></td>

                            <td  @click.stop class="disabled-column">{{}}</td>

                        </tr>
<!-- --Completed---------------------------------------------------------------------------------------------------------- -->
                        <tr class="disabled-row" v-for="(entry,index) in entryList('Completed')" :key="index">

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

                            <td  @click.stop class="work-type"><span class="status-container">{{entry.TaskId.Action}}</span></td>

                            <td  @click.stop class="start-time">{{entry.startTime}}</td>

                            <td  @click.stop class="end-time">{{entry.endTime}}</td>

                            <td  @click.stop class="work-status"> <span class="status-container">{{entry.Status}} </span></td>

                            <td  @click.stop class="publish-time">{{entry.publishTime}}</td>
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
    mounted() {
        this.$store.dispatch('fetchScheduleEntries');
        this.$store.dispatch('fetchTasks');
        this.$store.dispatch('fetchContainerBoats');
        this.$store.dispatch('fetchBerths');
        this.$store.dispatch('fetchTugBoats');
    },
    data() {
        return {
            tugBoatInfo: null,
            timeInfo: null,
            containerBoatInfo: null,
            berthInfo: null,
            actionInfo: null,
            statusInfo: null,
            searchValue: null,
            entries: [],
            tasks: [],
            containerBoats: [],
            containerBoatInput: '',
            countryInput: '',
            tugBoatInput: '',
            berthInput: '',
            workTypeInput: '',
            statusInput: '',
            // Input: [containerBoatInput, countryInput, tugBoatInput, berthInput, workTypeInput, statusInput]
        }
    },
    methods: {
        schedule() {
            this.$router.push({name: 'AutoReschedule'})
        },
        importTaskData(){
            let input = document.getElementById('import-task-data');
            input.onchange = (e) => {
                const file = e.target.files[0];
                if (!file) {
                    return;
                }
                let formData = new FormData();
                formData.append('task_data', file);
                axios.post('http://localhost:8000/api/upload-task-data', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                    console.log(response.data);
                    alert("Imported success!");
                }).catch(error => {
                    console.error("Error uploading file: ", error);
                    alert("Failed to import, check logs for details.");
                });
            };
            input.click();
        },
        importTugboatData(){
            let input = document.getElementById('import-task-data');
            input.onchange = (e) => {
                const file = e.target.files[0];
                if (!file) {
                    return;
                }
                let formData = new FormData();
                formData.append('tug_boat_data', file);
                axios.post('http://localhost:8000/api/upload-tug-boat-data', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                    console.log(response.data);
                    alert("Imported success!");
                }).catch(error => {
                    console.error("Error uploading file: ", error);
                    alert("Failed to import, check logs for details.");
                });
            };
            input.click();
        },
        download(){
            axios.post('http://localhost:8000/api/publish-data')
            .then(response => {
                console.log(response.data.message);
                alert("Published success!");
            }).catch(error => {
                console.error("error: ", error);
                alert("Failed to publish data, check logs for details.");
            });
        },
        publish(){

        },
        checkAll(input) {
            if (input === "All") {
                return '';
            } else {
                return input;
            }
        },
        formatInput(){
            this.containerBoatInput = this.checkAll(this.containerBoatInput);
            this.countryInput = this.checkAll(this.countryInput);
            this.tugBoatInput = this.checkAll(this.tugBoatInput);
            this.berthInput = this.checkAll(this.berthInput);
            this.workTypeInput = this.checkAll(this.workTypeInput);
            this.statusInput = this.checkAll(this.statusInput);
        },
        countryList(){
            const country = [...new Set(this.$store.state.containerBoats.map(boat => boat.Country))];
            return country;
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
        taskList() {
            this.tasks = this.$store.state.tasks;
            this.formatInput();

            const filtered = this.tasks.filter((task) => {  
                const byCountry = this.countryInput ? task.ContainerBoatID.Country.toString() === this.countryInput : true;
                const byContainerBoatId = this.containerBoatInput ? task.ContainerBoatID.ContainerBoatID.toString() === this.containerBoatInput : true;
                const byTugBoatId = this.tugBoatInput === '';
                const byBerthId = this.berthInput ? task.BerthId.toString() === this.berthInput : true;
                const byWorkType = this.workTypeInput ? task.Action === this.workTypeInput : true;
                const byStatus = this.statusInput ? task.State === this.statusInput : true;
                const unscheduled = task.State === 'Unscheduled';

                return byCountry && byContainerBoatId && byTugBoatId && byBerthId && byWorkType && byStatus && unscheduled;
            });

            return filtered;
        },
        formatTime(event){
            const dateTime = new Date(event);
            const hours = dateTime.getHours().toString().padStart(2, '0');
            const minutes = dateTime.getMinutes().toString().padStart(2, '0');

            return `${hours}:${minutes}`;
        },
        formatDate(event){
            const dateTime = new Date(event);
            const date = dateTime.getDate().toString().padStart(2, '0');
            const month = (dateTime.getMonth()+1).toString().padStart(2, '0');

            return `${date}/${month}`;
        },
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
        async edit(id) {
            try { 
                const response = await axios.post('http://localhost:8000/api/save-task/', {
                taskId: id,
                requiredTugBoat: this.requiredTugBoat,
                startTime: this.startTime,
                endTime: this.endTime,
                containerBoatId: this.containerBoatId,
                action: this.action,
                berthId: this.berthId,
                state: this.state,
                });
                if (response.data.success) {
                    alert('Edit Successfully');
                    window.location.reload();
                    this.resetNull();
                } else {
                    alert('Edit Task Failed.');
                }
            } catch (error) {
                console.error('Edit task error:', error);
                alert('Edit Task Error.');
            }
        },
        getStatusStyle(state){
            let backgroundColor;

            switch (state) {
                case 'Confirmed':
                backgroundColor = 'green';
                break;
                case 'Scheduled':
                backgroundColor = 'rgb(254, 219, 46)';
                break;
                case 'Completed':
                backgroundColor = 'darkgrey';
                break;
                default:
                backgroundColor = 'lightgrey';
            }

            return {
                background: backgroundColor,
            };
        },
        getActionStyle(action){
            let backgroundColor;

            switch (action) {
                case 'Arrival':
                backgroundColor = '#72bedf';
                break;
                default:
                backgroundColor = '#020071';
            }

            return {
                background: backgroundColor,
            };
        }
    }
}
</script>

<style scoped>
.disabled-row {
    background: rgb(233, 232, 232);
    color: darkgrey;
}

.disabled-row .status-container {
    /* background: darkgrey; */
    /* color: white; */
    background: rgb(233, 232, 232);
    color: darkgrey;
}
.disabled-column {
    background: rgb(233, 232, 232);
}

#Dashboard {
    font-size: 16px;
}
.buttons-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
}
#schedule {
    background-color: #409BBF;
    color: white;
    font-weight: bold;
    border-radius: 5px;
}
#publish {
    background-color: #8BC7DF;
    width: 90px;
    margin-left: auto;
}
.job input {
    display: none;
}
.job button:not(#publish) {
    text-align: left;
    box-shadow: 0 2px 3px lightgrey;
    margin-right: 10px;
    border: none;
}
.job button:not(#publish):not(#schedule) {
    background-color: #C5E6F3;
}
 
.job button:hover {
    background: lightgrey;
}

.filter-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 10px;
}
.filter{
    display: flex;
    /* flex-direction: column; */
    font-size: var(--font-size);
    border: 2px solid grey;
    border-radius: 5px;
    padding: 5px;
    margin-right: 5px;
}

.filter select{
    border: none;
}

form {
    margin-right: none;
}
.submit-button {
    display: none;
}

#containerBoatForm {
    width: fit-content;
}

button{
    color: black;
    border-radius: 20px;
}

.header-style{
    padding: 10px;
}

@media (max-width: 768px) {
    .filter-group {
        justify-content: space-between;
    }

    /* .filter {
        flex-basis: calc(50% - 20px);
    } */
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: var(--font-size);
}

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
</style>
