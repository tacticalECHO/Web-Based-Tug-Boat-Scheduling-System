<template>
    <div id="CaptainDashboard">
        <SideBar />
        <div class="pages">
            <div class="header-style">
                <div class="header-style title">
                    <h2>Today Work</h2>
                    <button id="download" @click="download()"><font-awesome-icon :icon="['fas', 'download']" /></button>
                </div>
                <MessageButton />
            </div>
            <br><br><br><br>
            <WorkTable />
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import WorkTable from '@/components/WorkTable.vue'
import MessageButton from '@/components/MessageButton.vue'
import axios from 'axios';


export default {
    name: 'WorkSchedule',
    components: {SideBar, WorkTable, MessageButton},
    methods: {
        download(){
            const captainId = localStorage.getItem('username');
            axios.post('/api/download-captain', { captainId })
            .then(response => {
                console.log(response.data.message);
                alert("Successfully Download!");
            }).catch(error => {
                console.error("error: ", error);
                alert("Failed to download data, check logs for details.");
            });
        },
    }
}
</script>

<style scoped>
#download {
    border: none;
    margin-left: 10px;
    border-radius: 50%;
    height: 35px;
    width: 35px;
    padding: 5px;
}

#download:hover {
    border: 2px solid black;
}
</style>
