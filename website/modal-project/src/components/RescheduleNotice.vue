<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Notice</b>
                <span>Do you need to auto change this task's schedule?</span>
                <br/>
                <span class="notice-buttons">
                    <button class="blue-border-button" id="no" @click="no()">No</button>
                    &nbsp; 
                    <button class="blue-button" id="manualReschedule" @click="change()">Change</button>
                </span>  
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'RescheduleNotice',
    props: [],
    methods: {
        no(){
            this.$router.push({name: 'ManualReschedule'});
        },
        change(){
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
