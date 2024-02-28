<template>
    <div id="TaskManager">
        <SideBar />
        <div class="pages" @click="toggle">
            <h2>Today Task</h2>
            <div class="header-style">
                <form class="search-form">
                    <input id="search" placeholder="Search...">
                    <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="search-icon" />
                </form>
                <span>
                    <button class="blue-border-button" id="delete" @click="redirect('')">Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="blue-border-button" id="add" @click="redirect('NewTask')">Add  + </button>
                </span>
            </div>
            <table>
                <thead>
                    <tr>
                        <th><input type="checkbox" disabled></th>
                        <th>Task Id</th>
                        <th>Required Tug Boat</th>
                        <th>Start Time</th>
                        <th>End Time</th>
                        <th>Container Boat Id</th>
                        <th>Berth Id</th>
                        <th>Action</th>
                        <th>State</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="task in $store.state.tasks" :key="task.TaskId">
                        <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>
                        <td>
                            <span :id="'taskId' + task.TaskId">{{task.TaskId}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showRequiredTugBoatForm === task.TaskId" @submit.prevent="edit(task.TaskId)">
                                <input :id="'requiredTugBoat' + task.taskId" :ref="'requiredTugBoat' + task.taskId" type="text"  :value="task.ReqauriedTugBoat">
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'requiredTugBoat')" v-if="requiredTugBoatInfo != task.TaskId">{{task.ReqauriedTugBoat}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showStartTimeForm === task.TaskId" @submit.prevent="edit(task.TaskId)">
                                <input :id="'startTime' + task.taskId" :ref="'startTime' + task.taskId" type="text"  :value="task.startTime">
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'startTime')" v-if="startTimeInfo != task.TaskId">{{task.startTime}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showEndTimeForm === task.TaskId">
                                <input :id="'endTime' + task.taskId" :ref="'endTime' + task.taskId" type="text"  :value="task.endTime">
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'endTime')" v-if="endTimeInfo != task.TaskId">{{task.endTime}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showContainerBoatIdForm === task.TaskId">
                                <input :id="'containerBoatId' + task.taskId" :ref="'containerBoatId' + task.taskId" type="text"  :value="task.ContainerBoatID">
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'containerBoatId')" v-if="containerBoatIdInfo != task.TaskId">{{task.ContainerBoatID}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showBerthIdForm === task.TaskId">
                                <select :id="'berthId' + task.taskId"  :value="task.berthId">
                                    <option>Unscheduled</option>
                                    <option>Scheduled</option>
                                </select>
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'berthId')" v-if="berthIdInfo != task.TaskId">{{task.BerthId}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showActionForm === task.TaskId">
                                <select :id="'action' + task.taskId" :value="task.Action">
                                    <option>Arrival</option>
                                    <option>Departure</option>
                                </select>
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'action')" v-if="actionInfo != task.TaskId">{{task.Action}}</span> 
                        </td>
                        <td @click.stop>
                            <form v-if="showStateForm === task.TaskId">
                                <select :id="'state' + task.taskId"  :value="task.State">
                                    <option>Unscheduled</option>
                                    <option>Scheduled</option>
                                </select>
                                <input class="submit-button" type="submit" />
                            </form>
                            <span @click="selected(task.TaskId, 'state')" v-if="stateInfo != task.TaskId">{{task.State}}</span> 
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'WorkSchedule',
    components: {SideBar},
    mounted() {
        this.$store.dispatch('fetchTasks');
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
        }
    },
    methods: {
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
                const response = await axios.post('http://localhost:8000/api/change-password/', {
                username: this.username,
                password: this.password,
                });
                if (response.data.success) {
                    this.$router.push({ name: 'Login' });
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
