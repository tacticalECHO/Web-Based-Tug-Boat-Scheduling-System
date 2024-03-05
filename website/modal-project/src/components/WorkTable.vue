<template>
    <div id="work-table" class="pages">
        <table>
            <thead>
                <tr>
                    <th>No.1</th>
                    <th>Container Boat</th>
                    <th>Berth</th>
                    <th>Time</th>
                    <th>Captain</th>
                    <th>Work Status</th>
                    <th>Work Type</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="task in taskList()" :key="task.TaskId">
                    <td class="number">  <span :id="'taskId' + task.TaskId">{{task.TaskId}}</span> </td>
                    <td class="container-boat"> {{task.ContainerBoatID.ContainerBoatID}} </td>
                    <td class="berth"> {{task.BerthId}} </td>
                    <td class="time"> {{task.startTime}} </td>
                    <td class="captain"> {{task.captain}} </td>
                    <td @click.stop>
                        <form v-if="showStateForm === task.TaskId">
                            <select @change="edit(task.TaskId)" v-model="state" :id="'state' + task.taskId" >
                                <option>Unscheduled</option>
                                <option>Scheduled</option>     
                                <option>Done</option>                               
                            </select>
                        </form>
                        <span class="status-container" @click="selected(task.TaskId, 'state')" v-if="stateInfo != task.TaskId">{{task.State}}</span> 
                    </td>
                    <td class="work-type"> <span class="type-container">{{task.Action}}</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'WorkTable',
    mounted(){
        this.$store.dispatch('fetchTasks');
    },
    data() {
        return {
            showStateForm: null,
            stateInfo: null,
            showContainerBoatIdForm: null,
            containerBoatIdInfo: null,
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
        resetNull() {
            this.showStateForm = null;
            this.stateInfo = null;
            this.showContainerBoatIdForm = null;
            this.containerBoatIdInfo = null;
        },
        selected(id, column) {
            this.resetNull();
            if (column === 'state'){
                this.showStateForm = id;
                this.stateInfo = id;
            }else if (column === 'containerBoatId'){
                this.showContainerBoatIdForm = id;
                this.containerBoatIdInfo = id;
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
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: var(--font-size);
}

th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 15px;
}

th {
    background-color: #f2f2f2;
}

td {
    text-align: center;
}
</style>