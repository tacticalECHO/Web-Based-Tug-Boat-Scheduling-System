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
            this.$router.push({name: 'Message'})
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