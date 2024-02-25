<template>
    <div id="CaptainDashboard">
        <SideBar />
        <div class="pages">
            <div class="header-style">
                <div class="header-style">
                    <h2>Today Work</h2>
                    <button id="download"><font-awesome-icon :icon="['fas', 'download']" /></button>
                </div>
                <MessageButton />
            </div>
        </div>
        <WorkTable />
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import WorkTable from '@/components/WorkTable.vue'
import MessageButton from '@/components/MessageButton.vue'


export default {
    name: 'WorkSchedule',
    components: {SideBar, WorkTable, MessageButton},
}
</script>

<style scoped>
#download {
    border: none;
    margin-left: 10px;
    margin-top: 15px;
    border-radius: 50%;
    height: 35px;
    width: 35px;
    padding: 5px;
}

#download:hover {
    border: 1px solid lightgrey;
}
</style>
