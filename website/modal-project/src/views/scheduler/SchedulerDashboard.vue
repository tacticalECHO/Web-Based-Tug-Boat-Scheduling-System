<template>
    <div id="Dashboard">
        <SideBar />
        <div class="pages">
            <router-view />
            <div class="header-style">
                <h2>My Dashboard</h2>
                <MessageButton />
            </div>
            <br>
            <div class="job">
                <input type="file" id="import-task-data"/>
                <label for="import-task-data"><button @click="importTaskData()">Import Task Data</button></label>
                <br><br><br>
                <input type="file" id="import-tugboat-data"/>
                <label for="import-tugboat-data"><button @click="importTugboatData()">Import Tug Boat Data</button></label>
                <br><br><br>
                <button id="schedule" @click="schedule()">Schedule</button>
            </div>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import MessageButton from '@/components/MessageButton.vue'
import axios from 'axios';

export default {
    name: 'Dashboard',
    components: {SideBar, MessageButton},
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
                }).catch(error => {
                    console.error("Error uploading file: ", error);
                });
            };
            input.click();
        },
        importTugboatData(){
            document.getElementById('import-tugboat-data').click();
        }
    }
}
</script>

<style scoped>
#Dashboard {
    font-size: 16px;
}

input {
    display: none;
}
.job button {
    text-align: left;
    box-shadow: 0 2px 3px lightgrey;
    width: 300px;
    border: none;
}
 
button:hover {
    background: lightgrey;
}
</style>
