<template>
    <SideBar />
    <div class="pages">
        <div id="WorkSchedule">
            <h2>Work Schedules</h2>
            <div class="header-style" >
                <button class="grey-border-button" id="filter">Filter Schedules</button>
                <button class="grey-border-button" id="Publish">Publish</button>
            </div>
        </div>
    </div>
    <WorkTable />
</template>

<script>
import SideBar from '@/components/SideBar.vue'
import WorkTable from '@/components/WorkTable.vue'

export default {
    name: 'WorkSchedule',
    components: {SideBar, WorkTable},
}
</script>

<style scoped>

button{
    border-radius: 10px;
}

.header-style{
    padding: 10px;
}
</style>
