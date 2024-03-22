<template>
    <div id="Settings">
        <SideBar />
        <div class="pages">
            <router-view/>
            <h2 class="title">Settings</h2>
            <br><br><br><br>
            <div class = "form">
                <b><label for="username">Username  </label></b>
                &nbsp; 
                <input type="text" id="username" v-model="username" :placeholder="username" readonly>
            </div>
            <div class = "form">
                <span class="password-style">
                    <b><label for="password">Password  </label></b>
                    &nbsp; 
                    <input type="password" id="password" v-model="password" :placeholder="passwordPlaceholder" readonly>
                    <button class="change-pwd" @click="change_password()">
                        <div class="change-sign"><font-awesome-icon :icon="['fas', 'pen-to-square']" /></div>
                        <div class="change-text">Change</div>
                    </button>
                </span>
                <!-- <button class="btn btn-dark" @click="change_password()">Change</button> -->
            </div>
            <button class="btn btn-light" @click="redirect('Login')">Logout</button>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'Settings',
    components: {SideBar},
    computed: {
        ...mapState([
            'username',
            'passwordPlaceholder' 
        ]),

    },
    methods: {
        change_password(){
            this.$router.push({name: 'ChangePassword'});
        },
        logout(){
            this.$router.push({name: 'Login'});
        }
    }
}
</script>

<style scoped>
.form {
    font-size: var(--font-size);
    margin-bottom: 15px;
}

button {
    width: 250px;
}

input {
    border: none;
}

.change-pwd {
    font-size: var(--font-size);
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition-duration: .3s;
    background-color: black;
}

.change-sign {
    font-size: 1.5em;
    width: 100%;
    transition-duration: .3s;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.change-text {
    position: absolute;
    right: 0%;
    width: 0%;
    opacity: 0;
    color: white;
    font-size: 1.2em;
    font-weight: 600;
    transition-duration: .3s;
}

.change-pwd:hover {
    width: 125px;
    border-radius: 10px;
    transition-duration: .3s;
}

.change-pwd:hover .change-sign {
    width: 30%;
    transition-duration: .3s;
    padding-left: 20px;
}

.change-pwd:hover .change-text {
    opacity: 1;
    width: 70%;
    transition-duration: .3s;
    padding-right: 10px;
}

.change-pwd:active {
    transform: translate(2px ,2px);
}

.password-style {
  display: flex;
  align-items: center;
}

.password-style input {
  margin-right: 10px;
  margin-left: 10px;
}

</style>
