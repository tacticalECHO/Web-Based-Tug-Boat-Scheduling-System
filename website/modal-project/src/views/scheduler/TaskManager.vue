<template>
    <div id="TaskManager">
        <SideBar />
        <div class="pages" @click="toggle">
            <h2>Today Task</h2>
            <div class="header-style">
                <form class="search-form">
                    <input id="search" v-model="input" placeholder="Search...">
                    <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="search-icon" />
                </form>
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
                            <th><input type="checkbox"></th>
                            <th>Task Id</th>
                            <th>Start Time</th>
                            <th>End Time</th>
                            <th>Container Boat Id</th>
                            <th>Required Tug Boat</th>
                            <th>Berth Id</th>
                            <th>Action</th>
                            <th>State</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="task in taskList()" :key="task.TaskId">
                            <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>
                            <td>
                                <span :id="'taskId' + task.TaskId">{{task.TaskId}}</span>
                            </td>
                            <td @click.stop>
                                <form v-if="showStartTimeForm === task.TaskId" @submit="edit(task.TaskId)">
                                    <input v-model="startTime" :id="'startTime' + task.taskId" :ref="'startTime' + task.taskId" type="datetime-local">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span @click="selected(task.TaskId, 'startTime')" v-if="startTimeInfo != task.TaskId">{{formatDate(task.startTime)}}&emsp;&emsp;{{ formatTime(task.startTime) }}</span> 
                            </td>
                            <td @click.stop>
                                <form v-if="showEndTimeForm === task.TaskId" @submit="edit(task.TaskId)">
                                    <input v-model="endTime" :id="'endTime' + task.taskId" :ref="'endTime' + task.taskId" type="datetime-local">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span @click="selected(task.TaskId, 'endTime')" v-if="endTimeInfo != task.TaskId">{{formatDate(task.endTime)}}&emsp;&emsp;{{ formatTime(task.endTime) }}</span> 
                            </td>
                            <td @click.stop>
                                <form v-if="showContainerBoatIdForm === task.TaskId" @submit="edit(task.TaskId)">
                                    <select @change="edit(task.TaskId)" v-model="containerBoatId">
                                        <option v-for="containerBoat in $store.state.containerBoats" :key="containerBoat.ContainerBoatID">{{ containerBoat.ContainerBoatID }}</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'containerBoatId')" v-if="containerBoatIdInfo != task.TaskId">{{task.ContainerBoatID.ContainerBoatID}}</span> 
                            </td>
                            <td @click.stop>
                                <form v-if="showRequiredTugBoatForm === task.TaskId" @submit="edit(task.TaskId)">
                                    <input v-model="requiredTugBoat" :id="'requiredTugBoat' + task.taskId" :ref="'requiredTugBoat' + task.taskId" type="text">
                                    <input class="submit-button" type="submit" />
                                </form>
                                <span @click="selected(task.TaskId, 'requiredTugBoat')" v-if="requiredTugBoatInfo != task.TaskId">{{task.RequiredTugBoat}}</span> 
                            </td>
                            <td @click.stop>
                                <form v-if="showBerthIdForm === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="berthId"  :id="'berthId' + task.taskId">
                                        <option v-for="berth in $store.state.berths" :key="berth.berthID">{{ berth.berthId }}</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'berthId')" v-if="berthIdInfo != task.TaskId">{{task.BerthId}}</span> 
                            </td>
                            <td @click.stop>
                                <form v-if="showActionForm === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="action" :id="'action' + task.taskId">
                                        <option>Arrival</option>
                                        <option>Departure</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'action')" v-if="actionInfo != task.TaskId">{{task.Action}}</span> 
                            </td>
                            <td @click.stop>
                                <form v-if="showStateForm === task.TaskId">
                                    <select @change="edit(task.TaskId)" v-model="state" :id="'state' + task.taskId" >
                                        <option>Unscheduled</option>
                                        <option>Scheduled</option>
                                    </select>
                                </form>
                                <span @click="selected(task.TaskId, 'state')" v-if="stateInfo != task.TaskId">{{task.State}}</span> 
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
    mounted() {
        this.$store.dispatch('fetchTasks');
        this.$store.dispatch('fetchBerths');
        this.$store.dispatch('fetchContainerBoats');
    },
    data() {
        return {
            showRequiredTugBoatForm: null,
            showStartTimeForm: null,
            showEndTimeForm: null,
            showContainerBoatIdForm: null,
            showActionForm: null,
            showStateForm: null,
            showBerthIdForm: null,
            requiredTugBoatInfo: null,
            startTimeInfo: null,
            endTimeInfo: null,
            containerBoatIdInfo: null,
            berthIdInfo: null,
            actionInfo: null,
            stateInfo: null,
            searchValue: null,
            tasks: [],
            input: '',
        }
    },
    methods: {
        taskList(){
            this.tasks = this.$store.state.tasks;
            const filtered = this.tasks.filter((task) => {
                const byTaskId = task.TaskId.toString().includes(this.input);
                const byContainerBoatId = task.ContainerBoatID.ContainerBoatID.toLowerCase().includes(this.input.toLowerCase());
                const byBerthId = task.BerthId.toString().includes(this.input);
                const byAction = task.Action.toLowerCase().includes(this.input.toLowerCase());

                return byTaskId || byContainerBoatId || byBerthId || byAction;
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
            this.showRequiredTugBoatForm = null;
            this.showStartTimeForm = null;
            this.showEndTimeForm = null;
            this.showContainerBoatIdForm = null;
            this.showBerthIdForm = null;
            this.showActionForm = null;
            this.showStateForm = null;
            this.requiredTugBoatInfo = null;
            this.startTimeInfo = null;
            this.endTimeInfo = null;
            this.containerBoatIdInfo = null;
            this.berthIdInfo = null;
            this.actionInfo = null;
            this.stateInfo = null;

        },
        selected(id, column) {
            this.resetNull();
            if(column === 'requiredTugBoat'){
                this.showRequiredTugBoatForm = id;
                this.requiredTugBoatInfo = id;
                // this.$nextTick(() => {
                //     this.$refs['requiredTugBoat'+id].focus();
                // });
            }else if (column === 'startTime'){
                this.showStartTimeForm = id;
                this.startTimeInfo = id;
            }else if (column === 'endTime'){
                this.showEndTimeForm = id;
                this.endTimeInfo = id;
            }else if (column === 'containerBoatId'){
                this.showContainerBoatIdForm = id;
                this.containerBoatIdInfo = id;
            }else if (column === 'berthId'){
                this.showBerthIdForm = id;
                this.berthIdInfo = id;
            }else if (column === 'action'){
                this.showActionForm = id;
                this.actionInfo = id;
            }else if (column === 'state'){
                this.showStateForm = id;
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
        }
    }
}
</script>

<style scoped>
form {
    margin-right: none;
}
.submit-button {
    display: none;
}

#containerBoatForm {
    width: fit-content;
}

#search {
    padding: 10px;
    border-radius: 20px;
    border: 1px solid lightgrey;
}

.search-form {
    position: relative;
    display: inline-block;
}

.search-icon {
    position: absolute;
    top: 40%;
    right: 10px;
    transform: translateY(-50%);
}

button{
    color: black;
    border-radius: 20px;
}

.header-style{
    padding: 10px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: var(--font-size);
}

th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 10px;
}

th {
    background-color: #f2f2f2;
}
</style>
