<template>
    <SideBar />
    <div class="pages">
        <div id="CaptainDashboard" class="header-style">
            <div class="header-style">
                <h2>Today Work</h2>
                <button id="download">D</button>
            </div>
            <MessageButton />
        </div>
    </div>
    <WorkTable />
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
    height: 30px;
    width: 30px;
}

#download:hover {
    background: lightgrey;
}
</style>
