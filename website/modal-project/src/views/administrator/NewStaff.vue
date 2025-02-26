<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <button @click="close">X</button>
                <br/>
                <div class = "form">
                    <b><label for="username">Username  </label></b>  
                    <input type="text" id="username" v-model="username" placeholder="Input username/staff ID">
                </div>
                <br>
                <div class = "form">
                    <b><label for="position">Position  </label></b>
                    &nbsp;   
                    <select id="position">
                        <option disabled selected hidden>Choose the position</option>
                        <option>Administrator</option>
                        <option>Scheduler</option>
                        <option>Captain</option>
                    </select>
                </div>
                <button class="blue-button" id="confirm" @click="confirm()">Confirm</button>
                <br/> 
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'MessageDetails',
    props: [],
    methods: {
        close(){
            this.$router.back();
        },
        confirm(){
            this.$router.back();
        }
    }
}
</script>

<style scoped>
.form {
    font-size: var(--font-size);
    margin-bottom: 15px;
    align-self: center;
}

button {
    width: 30px;
    height: 30px;
    border: none;
    font-size: 15px;
}

.blue-button {
    align-self: center;
    width: 130px;
    height: 40px;
    font-size: 13px;
    margin-top: 20px;
}

.popup-container {
    width: 500px;
}

.container-position {
    margin-top: 200px;
}

input, select {
    margin-left: 30px;
    border: 1px solid grey;
    border-radius: 5px;
    padding: 5px;
    width: 300px;
}

</style>
