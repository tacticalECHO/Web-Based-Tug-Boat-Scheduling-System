<!-- Vue file created by Team 10, ©2024 -->
<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Scheduling</b>
                <span>It needs some times to schedule the task, please wait.</span>
                <br/>
                <div v-if="!showButton" class="progress-bar">
                    <div class="progress" :style="{ width: progressWidth }"></div>
                </div>
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
    data() {
        return {
            showButton: false,
            progressWidth: '0%',
        }
    },
    methods: {
        schedule(){
            this.$router.push({name: 'SchedulerDashboard'});
            alert("Schedule operation successful!");
        }
    },
    mounted() {
        const interval = 20;
        const totalTime = 2000;
        let progress = 0;
        
        const progressInterval = setInterval(() => {
            progress += interval;
            this.progressWidth = `${(progress / totalTime) * 100}%`;
            
            if (progress >= totalTime) {
                clearInterval(progressInterval);
                this.showButton = true;
            }
        }, interval);
    }
}
</script>

<style scoped>
.progress-bar {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 5px;
    margin-bottom: 10px;
}

.progress {
    height: 10px;
    background-color: #445f9e;
    border-radius: 5px;
    transition: width 0.2s ease;
}
</style>
