<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Scheduling</b>
                <span>It needs some times to schedule the task, please wait.</span>
                <br/>
                <span class="notice-buttons">
                    <button class="btn btn-dark" id="schedule" @click="schedule()">Schedule in backstage</button>
                </span>  
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'AutoReschedule',
    methods: {
        schedule(){
            this.$router.push({name: 'SchedulerDashboard'});
        }
    }
}
</script>

<style scoped>
</style>
