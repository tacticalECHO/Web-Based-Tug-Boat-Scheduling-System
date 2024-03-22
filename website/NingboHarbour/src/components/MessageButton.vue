<template>
    <span class="message-container">
        <button id="message" @click="message()"><font-awesome-icon :icon="['fas', 'bell']" /></button>
    </span>
</template>

<script>

export default {
    name: 'MessageButton',
    methods: {
        message(){
        if (this.$store.state.isCaptain) {
            this.$router.push({ name: 'CaptainMessage' });
        } else if (this.$store.state.isScheduler) {
            this.$router.push({ name: 'SchedulerMessage' });
        } else {
            alert('Unauthorized or undefined role');
        }
        }
    }
}
</script>

<style scoped>
.message-container {
    margin-top: 10px;
}

#message {
    background: white;
    border-radius: 50%;
    height: 40px;
    width: 40px;
    border: 1px solid lightgrey;
}

#message:hover{
    background: lightgrey;
}

</style>