<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <b>Notice</b>
                <span id="notice-info">The change will not be saved if u exit now.</span>
                <br/>
                <span class="notice-buttons">
                    <button class="blue-border-button" id="exit" @click="exit()">Exit</button>
                    &nbsp; 
                    <button class="blue-button" id="save" @click="cancel()">Cancel</button>
                </span>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ExitNotice',
    // data() {
    //     return {
    //         path: '',
    //     }
    // },
    // mounted() {
    //     this.path = this.$route.query.path;
    // },
    // computed: {
    //     info () {
    //         if (this.path === 'add-new-task'){
    //             return this.info = 'The change will not be saved if u exit now.';
    //         }else if (this.path === 'change-password'){
    //             return this.info = 'Hello';
    //         }
    //     }
    // },
    methods: {
        exit(){
            this.$router.back();
        },
        cancel(){
            //save password here
            this.$router.back();
        }
    }
}
</script>

<style scoped>
</style>
