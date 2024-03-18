<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Notice</b>
                <span>Do you need to auto-schedule this task's?</span>
                <br/>
                <span class="notice-buttons">
                    <button class="btn btn-outline-dark" id="no" @click="no()">No</button>
                    &nbsp;  
                    <button type="button" class="btn btn-dark" id="manualReschedule" @click="change()">Change</button>
                </span>  
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'RescheduleNotice',
    props: [],
    methods: {
        no(){
            this.$router.push({name: 'SchedulerDashboard'});
        },
        async change(){
            try {
                const response = await axios.post('/api/auto-schedule', {"schedule":1});
                //console.log(response.data);
                
            } catch (error) {
                console.error("Error during schedule operation: ", error);
                alert("Schedule operation failed, check logs for details.");
            }
            // setTimeout(() => {
            //     // this.showProgressBar = false;
            //     alert("Schedule operation successful!");
            // }, 2000);
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
