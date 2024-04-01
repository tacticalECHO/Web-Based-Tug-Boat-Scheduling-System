<!-- Vue file created by Team 10, ©2024 -->
<template>
    <!-- Scheduler Dashboard Page -->
    <div id="TaskManager">
        <div class="progress-bar" :class="{ 'progress-bar-active': showProgressBar }"></div>
        <SideBar />
        <div class="pages" @click="toggle">
            <router-view />
            <h2 class="title">Your Dashboard</h2>
            <MessageButton />
            <!-- Main button features -->
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

            <!-- Filter Group Feature -->
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
                <!-- Add and Delete button -->
                <span class="add-delete">
                    <button type="button" class="delete" id="delete" @click= deleteSelected>
                        <span class="delete__text">Delete &nbsp;</span>
                        <span class="delete__icon"><font-awesome-icon :icon="['fas', 'delete-left']" /></span>
                    </button>
                    &nbsp;
                    <button type="button" class="add" id="add" @click="redirect('NewTask')">
                        <span class="add__text">Add &nbsp;</span>
                        <span class="add__icon"><font-awesome-icon :icon="['fas', 'plus']" /></span>
                    </button>
                </span>
            </div>
            <!-- Display no task available -->
            <div v-if="waiting()">No Task Available</div>

            <!-- Work table container -->
            <div v-if="!waiting()" class="table-container">
                <table class="table">
                    <thead>
                        <tr>
                            <th rowspan="2"><input type="checkbox" disabled/></th>
                            <th rowspan="2">No.</th>
                            <th>Planned Time</th>
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
                            <th>
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
                            <th style="text-align: center">Need</th>
                            <th style="text-align: center">IDs</th>
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

                            <td @click.stop class="planTime">
                                <form v-if="timeInfo === entry.ScheduleEntryId" @submit.prevent="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)">
                                    <input v-model="plannedTime" type="datetime-local">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span class="click-hover time" @click="selected(entry.ScheduleEntryId, 'time')" v-if="timeInfo != entry.ScheduleEntryId">{{formatDate(entry.TaskId.startTime)}}&emsp;&emsp;{{ formatTime(entry.TaskId.startTime) }}</span> 
                            </td>

                            <td @click.stop class="container-boat">
                                <form v-if="containerBoatInfo === entry.ScheduleEntryId" @submit="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)">
                                    <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)" v-model="containerBoatId">
                                        <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                                    </select>
                                </form>
                                <span class="click-hover" @click="selected(entry.ScheduleEntryId, 'containerBoatId')" v-if="containerBoatInfo != entry.ScheduleEntryId">{{entry.TaskId.ContainerBoatID.ContainerBoatID}}</span> 
                            </td>

                            <td class="country">{{entry.TaskId.ContainerBoatID.Country}}</td>
                            
                            <td><span>{{ entry.TaskId.RequiredTugBoat }}</span></td>

                            <td @click.stop class="tugboat">
                                <span v-for="tugBoats in entry.listOfTugBoats.map(tugBoat => tugBoat)" :key="tugBoats">
                                    <span @click="selectAndGetTugBoat(entry.ScheduleEntryId, tugBoats, entry.TaskId.TaskId)" v-if="tugBoatInfo != entry.ScheduleEntryId || tugBoatIndex != tugBoats">
                                        <span class="status-container click-hover" :style="getStatusStyle(tugBoats.CurrentStatus)">{{ tugBoats.TugBoatId }}</span>
                                        &nbsp;
                                    </span>
                                    <form v-if="tugBoatInfo === entry.ScheduleEntryId && tugBoatIndex === tugBoats">
                                        <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId, tugBoats.TugBoatId)" v-model="tugBoat">
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

                            <td @click.stop class="berth">
                                <form v-if="berthInfo === entry.ScheduleEntryId">
                                    <select @change="edit(entry.TaskId.TaskId, entry.ScheduleEntryId)" v-model="berthId">
                                        <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                                    </select>
                                </form>
                                <span class="click-hover" @click="selected(entry.ScheduleEntryId, 'berthId')" v-if="berthInfo != entry.ScheduleEntryId">{{ entry.TaskId.BerthId }}</span> 
                            </td>

                            <td class="work-type"><span class="status-container" :style="getActionStyle(entry.TaskId.Action)">{{entry.TaskId.Action}}</span></td>

                            <td class="start-time">{{ entry.StartTime ? formatTime(entry.StartTime) : 'waiting' }}</td>

                            <td class="end-time">{{ entry.EndTime ? formatTime(entry.EndTime) : 'waiting' }}</td>

                            <td class="work-status"> <span class="status-container" :style="getStatusStyle(entry.Status)">{{entry.Status}} </span></td>

                            <td class="publish-time">{{ entry.PublishTime ? formatTime(entry.PublishTime) : '-' }}</td>
                        </tr>
<!-- --Unscheduled--------------------------------------------------------------------------------------------------------- -->
                        <tr v-for="(task, index) in taskList()" :key="index">
                            <td><input type="checkbox" :id="'myCheckbox' + task.TaskId" :name="myCheckbox" v-model="selectedTasks" :value="task.TaskId"></td>

                            <td class="number"> {{index+1}} </td>

                            <td @click.stop class="planTime">
                                <form v-if="timeInfo === task.TaskId" @submit.prevent="edit(task.TaskId)">
                                    <input v-model="plannedTime" type="datetime-local">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span class="click-hover time" @click="selected(task.TaskId, 'time')" v-if="timeInfo != task.TaskId">{{formatDate(task.startTime)}}&emsp;&emsp;{{ formatTime(task.startTime) }}</span> 
                            </td>

                            <td @click.stop class="container-boat">
                                <form v-if="containerBoatInfo === task.TaskId" @submit="edit(task.TaskId)">
                                    <select @change="edit(task.TaskId)" v-model="containerBoatId">
                                        <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                                    </select>
                                </form>
                                <span class="click-hover" @click="selected(task.TaskId, 'containerBoatId')" v-if="containerBoatInfo != task.TaskId">{{task.ContainerBoatID.ContainerBoatID}}</span> 
                            </td>

                            <td class="country">{{task.ContainerBoatID.Country}}</td>

                            <td><span>{{ task.RequiredTugBoat }}</span></td>

                            <td @click.stop class="disabled-column tugboat">
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

                            <td @click.stop class="berth">
                                <form v-if="berthInfo === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="berthId">
                                        <option v-for="berth in $store.state.berths" :key="berth.BerthID">{{ berth.BerthId }}</option>
                                    </select>
                                </form>
                                <span class="click-hover" @click="selected(task.TaskId, 'berthId')" v-if="berthInfo != task.TaskId">{{ task.BerthId }}</span> 
                            </td>

                            <td @click.stop class="work-type task-type">
                                <form v-if="actionInfo === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="action">
                                        <option>INBOUND</option>
                                        <option>OUTBOUND</option>
                                    </select>
                                </form>
                                <span class="status-container click-hover" @click="selected(task.TaskId, 'action')" v-if="actionInfo != task.TaskId" :style="getActionStyle(task.Action)">{{task.Action}}</span>
                            </td>

                            <td class="disabled-column">{{}}</td>

                            <td class="disabled-column">{{}}</td>

                            <td> <span class="status-container work-status" :style="getStatusStyle(task.State)">{{task.State}} </span></td>

                            <td class="disabled-column">{{}}</td>

                        </tr>
<!-- --Completed---------------------------------------------------------------------------------------------------------- -->
                        <tr class="disabled-row" v-for="(entry,index) in entryList('Completed')" :key="index">
                            <td><input type="checkbox" :id="'myCheckbox' + entry.TaskId" :name="myCheckbox" v-model="selectedTasks" :value="entry.TaskId.TaskId"></td>
                            <td class="number"> {{index+1}} </td>
                            <td class="planTime">{{formatDate(entry.TaskId.startTime)}}&emsp;&emsp;{{ formatTime(entry.TaskId.startTime) }}</td>
                            <td class="container-boat">{{entry.TaskId.ContainerBoatID.ContainerBoatID}}</td>
                            <td class="country">{{entry.TaskId.ContainerBoatID.Country}}</td>
                            <td><span>{{ entry.TaskId.RequiredTugBoat }}</span></td>
                            <td class="tugboat">{{entry.listOfTugBoats.map(tugBoat => tugBoat.TugBoatId).join('/ ')}}</td>
                            <td class="berth">{{ entry.TaskId.BerthId}}</td>
                            <td class="work-type"><span class="status-container">{{entry.TaskId.Action}}</span></td>
                            <td class="start-time">{{entry.startTime}}</td>
                            <td class="end-time">{{entry.endTime}}</td>
                            <td class="work-status"> <span class="status-container">{{entry.Status}} </span></td>
                            <td class="publish-time">{{ entry.PublishTime ? formatTime(entry.PublishTime) : '-' }}</td>
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
        this.$store.dispatch('fetchScheduleEntries', this.sort);
        this.$store.dispatch('fetchTasks', this.sort);
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
            sort: false,
        }
    },
    methods: {
        reload(){ // refetch data from database
            this.$store.dispatch('fetchScheduleEntries', this.sort);
            this.$store.dispatch('fetchTasks', this.sort);
            this.$store.dispatch('fetchContainerBoats');
            this.$store.dispatch('fetchBerths');
            this.$store.dispatch('fetchTugBoats');
        },
        sorting(){ // fetch sorted/ default schedule entry and task
            this.sort = !this.sort;
            this.$store.dispatch('fetchScheduleEntries', this.sort);
            this.$store.dispatch('fetchTasks', this.sort);
        },
        async reschedule(entryId, tugboatId){ // reschedule remaining tasks
            this.showProgressBar = true;
            try {
                const response = await axios.post('/api/auto-reschedule/', {
                    entryId: entryId,
                    tugboatId: tugboatId,
                });
                console.log(response.data.success)
                if(response.data.success){ // if reschedule success
                    console.log('success')
                    setTimeout(() => { // hide progress bar and reload page
                        this.showProgressBar = false;
                        window.location.reload();
                        alert("Reschedule operation successful!");
                    }, 2000);
                }else { // if reschedule failed
                    alert('Failed to reschedule');
                }
            } catch (error) { // if api failed
                console.error("Error during reschedule operation: ", error);
                alert("Reschedule operation failed, check logs for details.");
            }
        },
        async deleteSelected() { // delete selected tasks/ schedule entries
            if(this.deletionAlert()){
                let isScheduleEntry = false;
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
                    isScheduleEntry = true;
                    console.log("schedule entry");
                    await fetch(`/api/scheduleentries-delete/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ ids: this.selectedScheduleEntries })
                    });
                }

                if(isScheduleEntry){ // prompts for rescheduling if deleted ones is schedule entry
                    console.log("reschedule");
                    if (confirm('Deleted successfully. \nReschedule remaning schedule?')){
                        this.reschedule();
                    }
                }else{
                    alert('Deleted successfully');
                }

                this.reload();
            }
            // reset selected entries to null
            this.selectedTasks = [];
            this.selectedScheduleEntries = [];
        },
        waiting(){ // return availability of tasks/ schedule entry
            if(this.$store.state.scheduleEntries.length === 0 && this.$store.state.tasks.length === 0){
                return true
            }
            return false
        },
        async schedule() { // schedule unscheduled tasks
            this.showProgressBar = true;
            try {
                const response = await axios.post('/api/auto-schedule', {});
                console.log(response.data);
            } catch (error) {
                console.error("Error during schedule operation: ", error);
                alert("Schedule operation failed, check logs for details.");
            }
            setTimeout(() => { // hide progress bar and reload page
                this.showProgressBar = false;
                alert("Schedule operation successful!");
                window.location.reload();
            }, 2000);
        },
        importTaskData(){ // get task data excel sheet from local computer
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
        importTugboatData(){ // get tugboat data excel sheet from local computer
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
        download(){ // download task/schedule entry
            axios.post('/api/publish-data')
            .then(response => {
                console.log(response.data.message);
                alert("Successfully Download!");
            }).catch(error => {
                console.error("error: ", error);
                alert("Failed to publish data, check logs for details.");
            });
        },
        async publish(){ // add publish time to schedule entry
            const currentTime = new Date().toISOString();
            try {
                const response = await axios.post('/api/update-publish-time', { 
                    timeStamp: currentTime
                });
                console.log(response.data);
                
                alert('Publish Successfully');
                this.reload();
            } catch (error) {
                console.error(error);
                alert('Publish Successfully');
            }
        },
        countryList(){ // return all country available in tasks
            const country = [...new Set(this.$store.state.containerBoats.map(boat => boat.Country))];
            return country;
        },
        entryList(state) { // return entry list according to filter
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
        taskList() { // return task list according to filter
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
        changeTugboatList(taskId) { // return available tugboats
            this.getTugboatList(taskId)
                .then(data => {
                    this.filteredTugBoats = data;
                })
                .catch(error => {
                    console.error(error);
                });
            return this.filteredTugBoats
        },
        async getTugboatList(taskId) { // get available tugboats from database
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
        resetNull() { // reset information to null
            this.tugBoatInfo = null;
            this.tugBoatIndex = null;
            this.timeInfo = null;
            this.containerBoatInfo = null;
            this.berthInfo = null;
            this.actionInfo = null;
            this.plannedTime = null;
            this.containerBoatId = null;
            this.tugBoat = null;
            this.berthId = null;
            this.action = null;
        },
        tugBoatSelected(id, index){
            this.resetNull();
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
        async edit(taskId, entryId, tugBoat) { // post data to edit data in database
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
                    if(response.data.tugboatConflict){
                        if (confirm('Tug Boat '+ this.tugBoat + ' is conflicted.\n Confirm Auto Reschedule?')){
                            this.reschedule(entryId, this.tugBoat);
                        }else{
                            alert('Please Edit Manually');
                        }
                    }else if(response.data.timeConflict){
                        this.autoRescheduleTugboats(response.data.tugboat, response.data.total, entryId, taskId);
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
        async autoRescheduleTugboats(tugboatList, total, entryId, taskId){ // auto reschedule data upon confirmation
            const auto = confirm('Conlict Notice: \n\nTugboat(s): '+ tugboatList + " are not available \n\nAuto Reschedule?")
            if(auto){
                try{
                    const confirmResponse = await axios.post('/api/tugboat-reschedule/',{
                        total: total,
                        entryId: entryId,
                        taskId: taskId
                    });
                    if (confirmResponse.data.success){
                        if(confirmResponse.data.insufficient){
                            alert('Insufficient tugboat');
                        }else{
                            alert('Auto Reschedule Successful');
                        }
                    }else {
                        alert('Failed to Auto Reschedule. Please add new tugboat manually.');
                    }
                } catch (error) {
                    alert('Auto Reschedule Error. Please add new tugboat manually.');
                }
            }else{
                alert('Tugboat(s): '+ tugboatList +" is removed from entry.")
            }
        },
        async manualSchedule(taskId){ // manual adding tug boats to tasks
            try { 
                const response = await axios.post('/api/manual-schedule/', {
                    taskId: taskId,
                    tugBoatList: this.listOfTugBoat,
                });
                if (response.data.success) {
                    if(response.data.conflict){
                        alert("Conflicted (Tugboat : Entry):\n" + response.data.conflictList + '\nRescheduling...');
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
        selectAndGetTugBoat(entryId, tugboats, taskId){
            this.tugBoatSelected(entryId, tugboats)
            this.changeTugboatList(taskId)
        },
        addSelected(task, tugboat, taskId){
            this.selected(task, tugboat);
            this.changeTugboatList(taskId)
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

.job button{
    width: 160px;
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
    color: rgb(233, 232, 232);
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
    animation: progressBarAnimation 3s linear forwards;
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

    .job button {
        width: fit-content;
    }

    /* .filter {
        flex-basis: calc(50% - 20px);
    } */
}

#filter-section{
    margin-top: 1em;
}

#schedule {
    height: 50px;
    font-size: var(--font-size);
    color: white;
    width: 200px;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgb(15, 15, 15);
    border: none;
    font-weight: bold;
    font-size: 0.9em;
    gap: 8px;
    cursor: pointer;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.103);
    position: relative;
    overflow: hidden;
    transition-duration: .3s;
}

#schedule::before {
    width: 0;
    height: 0;
    position: absolute;
    content: "";
    background-color: var(--blue-color);
    border-radius: 50%;
    transition-duration: .4s;
    mix-blend-mode: hard-light;
}

#schedule:hover::before {
    transition-duration: .4s;
    width: 100%;
    height: 100%;
    /* transform: translate(100%, -50%); */
    border-radius: 0;
}

</style>