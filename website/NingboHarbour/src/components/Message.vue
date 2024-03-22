<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <button class="close-button" @click="close">X</button>
                <div class="info-text">
                    <strongg> ALL UPDATE </strongg><br>
                    If you have any other questions, please call the Ningbo Harbour General Scheduling Office at: <br>
                    <strong>(0574) XXXX-XXXX</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Message',
    props: [],
    methods: {
        close(){
            if (this.$store.state.isCaptain) {
            this.$router.push({ name: 'CaptainDashboard' });
            } else if (this.$store.state.isAdmin) {
                this.$router.push({ name: 'AdminDashboard' });
            } else if (this.$store.state.isScheduler) {
                this.$router.push({ name: 'SchedulerDashboard' });
            } else {
                this.$router.push({ name: 'Settings' });
            }
        }
    }
}
</script>

<style scoped>
.close-button {
    position: absolute;
    top: 10px;
    left: 10px;
    width: 30px;
    height: 30px;
    border: none;
    font-size: 15px;
    cursor: pointer;
    background: transparent;
    z-index: 10;
}

.popup-container {
    position: relative;
    height: 330px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.container-position {
    margin-top: 120px;
}

.info-text {
    margin: 20px;
    font-size: 18px;
    line-height: 1.6;
}

.info-text strongg {
    font-size: 22px;
    color: #f0736f;
    padding: 5px;
    border: 2px solid #f26f6a;
    margin-bottom: 15px; 
    display: inline-block; 
    border-radius: 5px; 
    background-color: #ffd2d2; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
</style>
