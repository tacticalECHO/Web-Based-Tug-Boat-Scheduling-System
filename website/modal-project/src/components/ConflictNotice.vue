<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Notice</b>
                <span>Do you need to reschedule the conflict schedules automatically?</span>
                <br/>
                <span class="notice-buttons">
                    <button class="blue-border-button" id="manual" @click="manual()">Manual</button>
                    &nbsp; 
                    <button class="blue-button" id="reschedule" @click="reschedule()">Reschedule</button>
                </span>  
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ConflictNotice',
    props: [],
    methods: {
        manual(){
            this.$router.push({name: 'ConflictScheduleList'});
        },
        reschedule(){
            this.$router.push({name: 'AutoReschedule'});
        }
    }
}
</script>

<style scoped>
.popup-container {
    width: 400px;
}
</style>
