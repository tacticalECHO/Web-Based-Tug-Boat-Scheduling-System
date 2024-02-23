<template>
    <SideBar />
    <div class="pages">
        <div id="Dashboard">
            <div class="header-style">
                <h2>My Dashboard</h2>
                <MessageButton />
            </div>
            <br>
            <div class="job">
                <button id="import-task-data">Import Task Data</button>
                <br><br><br>
                <button id="import-tugboat-data">Import Tug Boat Data</button>
                <br><br><br>
                <button id="schedule" @click="schedule()">Schedule</button>
            </div>
        </div>
        <router-view />
    </div>
    
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import MessageButton from '@/components/MessageButton.vue'

export default {
    name: 'Dashboard',
    components: {SideBar, MessageButton},
    methods: {
        schedule() {
            this.$router.push({name: 'AutoReschedule'})
        }
    }
}
</script>

<style scoped>
#Dashboard {
    font-size: 16px;
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
