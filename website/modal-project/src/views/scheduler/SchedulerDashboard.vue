<template>
    <div id="TaskManager">
        
        <div class="progress-bar" :class="{ 'progress-bar-active': showProgressBar }"></div>
        <SideBar />
        <div class="pages" @click="toggle">
            <router-view />
            <h2 class="title">Your Dashboard</h2>
            <MessageButton />
            <div class="job buttons-container">
                <button class="btn btn-dark" id="schedule" @click="schedule()">Schedule <font-awesome-icon :icon="['fas', 'calendar-day']" /></button>
                <br><br><br>
                <input type="file" id="import-task-data"/>
                <label for="import-task-data"><button id="import-task" class="btn btn-light" @click="importTaskData()">Import Task Data <font-awesome-icon :icon="['fas', 'file-import']" /></button></label>
                <br><br><br>
                <input type="file" id="import-tugboat-data"/>
                <label for="import-tugboat-data"><button id="import-tugboat" class="btn btn-light" @click="importTugboatData()">Import Tug Boat Data <font-awesome-icon :icon="['fas', 'file-import']" /></button></label>
                <br><br><br>
                <button class="btn btn-light" id="download" @click="download()">Download <font-awesome-icon :icon="['fas', 'download']" /></button>
                <br><br><br>
                <button class="btn btn-outline-dark" id="publish" @click="publish()">Publish <font-awesome-icon :icon="['fas', 'upload']" /></button>
            </div>
            <div class="header-style" id="filter-section">
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
                        <select v-model="workTypeInput">
                            <option value="">All</option>
                            <option>INBOUND</option>
                            <option>OUTBOUND</option>
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
                    <button class="btn btn-light" id="delete" @click= deleteSelected>Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="btn btn-dark" id="add" @click="redirect('NewTask')">Add  + </button>
                </span>
            </div>
            <div v-if="waiting()">No Task Available</div>
            <div v-if="!waiting()" class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th rowspan="2"><input type="checkbox"/></th>
                            <th rowspan="2">No.</th>
                            <th rowspan="2">Planned Time</th>
                            <th rowspan="2">Container Boat</th>
                            <th rowspan="2">Country</th>
                            <th style="text-align: center" colspan="2">Tug Boat</th>
                            <th rowspan="2">Berth</th>
                            <th rowspan="2">Work Type</th>
                            <th style="text-align: center" colspan="2" >Actual Time</th>
                            <th rowspan="2">Status</th>
                            <th rowspan="2">Publish Time</th>
                        </tr>
                        <tr>
                            <th>Need</th>
                            <th>IDs</th>
                            <th>Start</th>
                            <th>End</th>
                        </tr>
                    </thead>
                    <tbody>
<!-- --Scheduled / Confirmed--------------------------------------------------------------------------------------------------------- -->
                        <tr v-for="(entry,index) in entryList('Incomplete')" :key="index">

                            <td><input type="checkbox" :id="'mycheckbox' + entry.ScheduleEntryId" :name='myCheckbox' v-model="selectedScheduleEntries" :value="entry.TaskId.TaskId"></td>

                            <!-- <td class="number"> {{index+1}} </td> -->
                            <td class="number"> {{entry.ScheduleEntryId}} </td>

                            <td @click.stop>
                                <form v-if="timeInfo === entry.ScheduleEntryId" @submit="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)">
                                    <input v-model="plannedTime" type="datetime-local">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span @click="selected(entry.ScheduleEntryId, 'time')" v-if="timeInfo != entry.ScheduleEntryId">{{formatDate(entry.TaskId.startTime)}}&emsp;&emsp;{{ formatTime(entry.TaskId.startTime) }}</span> 
                            </td>

                            <td @click.stop>
                                <form v-if="containerBoatInfo === entry.ScheduleEntryId" @submit="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)">
                                    <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)" v-model="containerBoatId">
                                        <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                                    </select>
                                </form>
                                <span @click="selected(entry.ScheduleEntryId, 'containerBoatId')" v-if="containerBoatInfo != entry.ScheduleEntryId">{{entry.TaskId.ContainerBoatID.ContainerBoatID}}</span> 
                            </td>

                            <td @click.stop class="country">{{entry.TaskId.ContainerBoatID.Country}}</td>
                            
                            <td @click.stop>
                                <span>{{ entry.TaskId.RequiredTugBoat }}</span>
                            </td>

                            <td @click.stop>
                                <span v-for="tugBoats in entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId)" :key="tugBoats">
                                    <span @click="selectAndGetTugBoat(entry.ScheduleEntryId, tugBoats, entry.TaskId.TaskId)" v-if="tugBoatInfo != entry.ScheduleEntryId || tugBoatIndex != tugBoats">
                                        <span>{{ tugBoats }} / </span>
                                    </span>
                                    <form v-if="tugBoatInfo === entry.ScheduleEntryId && tugBoatIndex === tugBoats">
                                        <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId, tugBoats)" v-model="tugBoat">
                                            <option value=""></option>
                                            <option v-for="tugboat in filteredTugBoats" :key="tugboat.TugBoatId">{{ tugboat.TugBoatId }}</option>
                                        </select>
                                    </form>
                                </span>
                                <span @click="selectAndGetTugBoat(entry.ScheduleEntryId, 'add', entry.TaskId.TaskId)" v-if="tugBoatInfo != entry.ScheduleEntryId || tugBoatIndex != 'add'">
                                    <font-awesome-icon :icon="['fas', 'circle-plus']" id="add-tugboat"/>
                                </span>
                                <form v-if="tugBoatInfo === entry.ScheduleEntryId && tugBoatIndex === 'add'">
                                    <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)" v-model="tugBoat">
                                        <option v-for="tugboat in filteredTugBoats" :key="tugboat.TugBoatId">{{ tugboat.TugBoatId }}</option>
                                    </select>
                                </form>
                            </td>

                            <td @click.stop>
                                <form v-if="berthInfo === entry.ScheduleEntryId">
                                    <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)" v-model="berthId">
                                        <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                                    </select>
                                </form>
                                <span @click="selected(entry.ScheduleEntryId, 'berthId')" v-if="berthInfo != entry.ScheduleEntryId">{{ entry.TaskId.BerthId }}</span> 
                            </td>

                            <td class="work-type"><span class="status-container" :style="getActionStyle(entry.TaskId.Action)">{{entry.TaskId.Action}}</span></td>

                            <td class="start-time">{{ formatTime(entry.StartTime) }}</td>

                            <td class="end-time">{{ formatTime(entry.EndTime) }}</td>

                            <td class="work-status"> <span class="status-container" :style="getStatusStyle(entry.Status)">{{entry.Status}} </span></td>

                            <td class="publish-time">{{formatTime(entry.PublishTime)}}</td>
                        </tr>
<!-- --Unscheduled--------------------------------------------------------------------------------------------------------- -->
                        <tr v-for="(task, index) in taskList()" :key="index">
                            <td><input type="checkbox" :id="'myCheckbox' + task.TaskId" :name="myCheckbox" v-model="selectedTasks" :value="task.TaskId"></td>

                            <td class="number"> {{index+1}} </td>

                            <td @click.stop>
                                <form v-if="timeInfo === task.TaskId" @submit="edit(task.TaskId)">
                                    <input v-model="plannedTime" type="datetime-local">
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

                            <td class="country">{{task.ContainerBoatID.Country}}</td>

                            <td @click.stop>
                                <span>{{ task.RequiredTugBoat }}</span>
                            </td>

                            <td @click.stop class="disabled-column">
                                <span @click="addSelected('task'+task.TaskId, 'tugBoat',task.TaskId)" v-if="tugBoatInfo != 'task'+task.TaskId">
                                    <font-awesome-icon :icon="['fas', 'circle-plus']" id="add-tugboat"/>
                                </span>
                                <form v-if="tugBoatInfo === 'task'+task.TaskId" @submit.prevent="manualSchedule(task.TaskId)">
                                    <select multiple v-model="listOfTugBoat">
                                        <option v-for="tugboat in filteredTugBoats" :key="tugboat.TugBoatId">
                                            <!-- <span :style="getTugBoatStyle(tugboat.TugBoatId)"> -->
                                                {{ tugboat.TugBoatId }}
                                            <!-- </span> -->
                                        </option>
                                    </select>
                                    <button class="submit-button" type="submit"></button>
                                </form>
                            </td>

                            <td @click.stop>
                                <form v-if="berthInfo === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="berthId">
                                        <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'berthId')" v-if="berthInfo != task.TaskId">{{ task.BerthId }}</span> 
                            </td>

                            <td @click.stop class="work-type">
                                <form v-if="actionInfo === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="action">
                                        <option>INBOUND</option>
                                        <option>OUTBOUND</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'action')" v-if="actionInfo != task.TaskId" class="status-container" :style="getActionStyle(task.Action)">{{task.Action}}</span>
                            </td>

                            <td class="disabled-column">{{}}</td>

                            <td class="disabled-column">{{}}</td>

                            <td class="work-status"> <span class="status-container" :style="getStatusStyle(task.State)">{{task.State}} </span></td>

                            <td class="disabled-column">{{}}</td>

                        </tr>
<!-- --Completed---------------------------------------------------------------------------------------------------------- -->
                        <tr class="disabled-row" v-for="(entry,index) in entryList('Completed')" :key="index">
                            <td><input type="checkbox" :id="'myCheckbox' + entry.TaskId" :name="myCheckbox" v-model="selectedTasks" :value="entry.TaskId.TaskId"></td>
                            <td class="number"> {{index+1}} </td>
                            <td>{{formatDate(entry.TaskId.startTime)}}&emsp;&emsp;{{ formatTime(entry.TaskId.startTime) }}</td>
                            <td>{{entry.TaskId.ContainerBoatID.ContainerBoatID}}</td>
                            <td class="country">{{entry.TaskId.ContainerBoatID.Country}}</td>
                            <td @click.stop><span>{{ entry.TaskId.RequiredTugBoat }}</span></td>
                            <td>{{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join('/ ')}}</td>
                            <td>{{ entry.TaskId.BerthId}}</td>
                            <td class="work-type"><span class="status-container">{{entry.TaskId.Action}}</span></td>
                            <td class="start-time">{{entry.startTime}}</td>
                            <td class="end-time">{{entry.endTime}}</td>
                            <td class="work-status"> <span class="status-container">{{entry.Status}} </span></td>
                            <td class="publish-time">{{entry.publishTime}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import MessageButton from '@/components/MessageButton.vue';
import axios from 'axios';

export default {
    name: 'WorkSchedule',
    components: {SideBar, MessageButton},
    mounted() {
        this.$store.dispatch('fetchScheduleEntries');
        this.$store.dispatch('fetchTasks');
        this.$store.dispatch('fetchContainerBoats');
        this.$store.dispatch('fetchBerths');
        this.$store.dispatch('fetchTugBoats');
    },
    data() {
        return {
            taskId: null,
            tugBoatIndex: null,
            tugBoatInfo: null,
            timeInfo: null,
            containerBoatInfo: null,
            berthInfo: null,
            actionInfo: null,
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
            selectedTasks: [],
            selectedScheduleEntries: [],
            showProgressBar: false,
            filteredTugBoats: [],
        }
    },
    methods: {
        async deleteSelected() {
            if (this.selectedTasks.length > 0) {
                await fetch(`/api/tasks-delete/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ ids: this.selectedTasks })
                });
            }

            if (this.selectedScheduleEntries.length > 0) {
                await fetch(`/api/scheduleentries-delete/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ ids: this.selectedScheduleEntries })
                });
            }

            this.$store.dispatch('fetchTasks');
            this.$store.dispatch('fetchScheduleEntries');

            this.selectedTasks = [];
            this.selectedScheduleEntries = [];
        },
        waiting(){
            if(this.$store.state.scheduleEntries.length === 0 && this.$store.state.tasks.length === 0){
                return true
            }
            return false
        },
        async schedule() {
            this.showProgressBar = true;
            try {
                const response = await axios.post('/api/auto-schedule', {});
                console.log(response.data);
                
            } catch (error) {
                console.error("Error during schedule operation: ", error);
                alert("Schedule operation failed, check logs for details.");
            }
            setTimeout(() => {
                this.showProgressBar = false;
                alert("Schedule operation successful!");
            }, 2000);
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
                axios.post('/api/upload-task-data', formData, {
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
            let input = document.getElementById('import-tugboat-data');
            input.onchange = (e) => {
                const file = e.target.files[0];
                if (!file) {
                    return;
                }
                let formData = new FormData();
                formData.append('tugboat_data', file);
                axios.post('/api/upload-tug-boat-data', formData, {
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
            axios.post('/api/publish-data')
            .then(response => {
                console.log(response.data.message);
                alert("Published success!");
            }).catch(error => {
                console.error("error: ", error);
                alert("Failed to publish data, check logs for details.");
            });
        },
        async publish(){
            const currentTime = new Date().toISOString();
            try {
                const response = await axios.post('/api/update-publish-time', { 
                    timeStamp: currentTime
                });
                console.log(response.data);
                alert('Publish Successfully');
            } catch (error) {
                console.error(error);
                alert('Publish Successfully');
            }
        },
        countryList(){
            const country = [...new Set(this.$store.state.containerBoats.map(boat => boat.Country))];
            return country;
        },
        entryList(state) {
            this.entries = this.$store.state.scheduleEntries;
            const isCompleted = state === 'Completed';

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

            return this.tasks.filter((task) => {  
                const byCountry = this.countryInput ? task.ContainerBoatID.Country.toString() === this.countryInput : true;
                const byContainerBoatId = this.containerBoatInput ? task.ContainerBoatID.ContainerBoatID.toString() === this.containerBoatInput : true;
                const byTugBoatId = this.tugBoatInput === '';
                const byBerthId = this.berthInput ? task.BerthId.toString() === this.berthInput : true;
                const byWorkType = this.workTypeInput ? task.Action === this.workTypeInput : true;
                const byStatus = this.statusInput ? task.State === this.statusInput : true;
                const unscheduled = task.State === 'Unscheduled';

                return byCountry && byContainerBoatId && byTugBoatId && byBerthId && byWorkType && byStatus && unscheduled;
            });
        },
        changeTugboatList(taskId) {
            this.getTugboatList(taskId)
                .then(data => {
                    this.filteredTugBoats = data;
                })
                .catch(error => {
                    console.error(error);
                });
            return this.filteredTugBoats
        },
        async getTugboatList(taskId) {
            try {
                const response = await axios.get('/api/display_tugboat/', {
                    params: {
                        taskId: taskId
                    }
                });
                if(response.data){
                    return response.data;
                }else{
                    alert('Failed to Fetch Available Tug Boats');
                    return [];
                }
            } catch (error) {
                console.error(error);
                alert('Error Fetching Available Tug Boats');
            }
        },
        resetNull() {
            this.tugBoatInfo = null;
            this.tugBoatIndex = null;
            this.timeInfo = null;
            this.containerBoatInfo = null;
            this.berthInfo = null;
            this.actionInfo = null;
        },
        tugBoatSelected(id, index){
            this.resetNull;
            this.tugBoatInfo = id;
            this.tugBoatIndex = index;
        },
        selected(id, column) {
            this.resetNull();
            if (column === 'tugBoat'){
                this.tugBoatInfo = id;
            }else if (column === 'time'){
                this.timeInfo = id;
            }else if (column === 'containerBoatId'){
                this.containerBoatInfo = id;
            }else if (column === 'berthId'){
                this.berthInfo = id;
            }else if (column === 'action'){
                this.actionInfo = id;
            }
        },
        async edit(taskId, entryId, tugBoat) {
            try { 
                const response = await axios.post('/api/update-entry-task/', {
                    entryId: entryId,
                    taskId: taskId,
                    plannedTime: this.plannedTime,
                    containerBoatId: this.containerBoatId,
                    removeTugBoatId: tugBoat,
                    newTugBoatId: this.tugBoat,
                    berthId: this.berthId,
                    action: this.action,
                });
                if (response.data.success) {
                    if(response.data.conflict){
                        alert('There are conflicted entries. Rescheduling...');
                    }else{
                        alert('Edit Successfully');
                    }
                    this.reload();
                    this.resetNull();
                } else {
                    alert('Edit Task Failed.');
                }
            } catch (error) {
                console.error('Edit task error:', error);
                alert('Edit Task Error.');
            }
        },
        async manualSchedule(taskId){
            try { 
                const response = await axios.post('/api/manual-schedule/', {
                    taskId: taskId,
                    tugBoatList: this.listOfTugBoat,
                });
                if (response.data.success) {
                    if(response.data.conflict){
                        alert('There are conflicted entries. Rescheduling...');
                    }else{
                        alert('Manual Scheduling Successful');
                    }
                    this.reload();
                    this.resetNull();
                } else {
                    alert('Manual Schedulling Failed.');
                }
            } catch (error) {
                console.error('Error during manual schedulling:', error);
                alert('Manual Schedulling Error.');
            }
        },
        // async getTugBoatStyle(tugBoatId){
        //     // const tugBoat = entry.listOfTugBoats.find(tug => tug.TugBoatId === tugBoatId);
        //     try { 
        //         const response = await axios.post('/api/tugboat-availability', {
        //             tugboatId: tugBoatId,
        //         });
        //         if (response.data.success) {
        //             console.log("get tugboat availability success")

        //             //set color according to state
        //             let backgroundColor;

        //             switch (response.data.message) {
        //                 case true:
        //                     backgroundColor = 'green';
        //                     break;
        //                 default:
        //                     backgroundColor = 'red';
        //             }
        //             return{
        //                 backgroundColor: backgroundColor,
        //                 color: 'white',
        //                 padding: '5px',
        //                 'border-radius': '10px',
        //             }
        //         } else {
        //             console.log("failed")
        //         }
        //     } catch (error) {
        //         console.error('Get tugboat availability error: ', error);
        //     }
        // },
        selectAndGetTugBoat(entryId, tugboats, taskId){
            this.tugBoatSelected(entryId, tugboats)
            this.changeTugboatList(taskId)
        },
        addSelected(task, tugboat, taskId){
            this.selected(task, tugboat);
            this.changeTugboatList(taskId)
        },
        reload(){
            this.$store.dispatch('fetchScheduleEntries');
            this.$store.dispatch('fetchTasks');
            this.$store.dispatch('fetchContainerBoats');
            this.$store.dispatch('fetchBerths');
            this.$store.dispatch('fetchTugBoats');
        },
    }
}
</script>

<style scoped>
#import-task, #import-tugboat, #download{
    border: none;
    height: 48px;
    padding-left: 10px;
    padding-right: 10px;
    font-size: var(--font-size);
    margin-left: 5px;
}

#schedule{
    height: 50px;
    font-size: var(--font-size);
    background: black;
    color: white;
    font-weight: bold;
    width: 200px;
    text-align: center;
}

#schedule:hover{
    background: white;
    color: black;
    font-size: 1em;
    transition: font-size 0.5s;
}

#publish {
    width: 90px;
    margin-left: auto;
    background: white;
    border-radius: 5px;
    font-size: var(--font-size);
}

#publish:hover{
    background: black;
    color: white;
}

.job input {
    display: none;
}

#add-tugboat {
    /* color: var(--main-button-color); */
    color: grey;
    font-size: 1.5em;
}
#add-tugboat:hover{
    color: lightgrey;
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

.progress-bar {
  width: 100%;
  height: 4px;
  background-color: #409BBF;
  position: fixed;
  top: 0;
  left: 0;
  visibility: hidden;
}

.progress-bar-active {
  width: 100%;
  visibility: visible;
  animation: progressBarAnimation 2s linear forwards;
}

@keyframes progressBarAnimation {
  from { width: 0; }
  to { width: 100%; }
}

form {
    margin-right: none;
}

#containerBoatForm {
    width: fit-content;
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

#filter-section{
    margin-top: 1em;
}
</style>
