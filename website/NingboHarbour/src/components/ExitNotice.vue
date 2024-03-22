<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Notice</b>
                <span id="notice-info">The change will not be saved if u exit now.</span>
                <br/>
                <span class="notice-buttons">
                    <button class="btn btn-outline-dark" id="exit" @click="exit()">Exit</button>
                    &nbsp; 
                    <button class="btn btn-dark" id="save" @click="cancel()">Cancel</button>
                </span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ExitNotice',
    methods: {
        exit() {
            this.$router.push({ name: this.$store.state.exitPath });
        },
        cancel() {
            this.$router.back();
        }
    }
}
</script>

<style scoped>
</style>
