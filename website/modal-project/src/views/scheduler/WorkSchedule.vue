<template>
    <div id="WorkSchedule">
        <SideBar />
        <div class="pages">
            <h2>Work Schedules</h2>
            <div class="header-style" >
                <button class="grey-border-button" id="filter">Filter Schedules <font-awesome-icon :icon="['fas', 'filter']" /></button>
                <button class="grey-border-button" id="Publish">Publish <font-awesome-icon :icon="['fas', 'upload']" /></button>
            </div>
        </div>
        <WorkTable />
    </div>
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
