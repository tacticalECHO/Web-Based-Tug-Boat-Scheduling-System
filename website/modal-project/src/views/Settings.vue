<template>
    <SideBar />
    <div class="pages">
        <div id="Settings">
            <h2>Settings</h2>
            <div class = "form">
                <b><label for="username">Username  </label></b>
                &nbsp; 
                <input type="text" id="username" v-model="username" :placeholder="username" readonly>
            </div>
            <div class = "form">
                <b><label for="password">Password  </label></b>
                &nbsp; 
                <input type="password" id="password" v-model="password" :placeholder="passwordPlaceholder" readonly>
                <button class="grey-border-button" @click="change_password()">Change</button>
            </div>
            <button class="blue-button" @click="redirect('Login')">Logout</button>
        </div>
    </div>
    <router-view/>
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

.form button {
    width: 80px;
}

.form button:hover {
    border: 2px solid lightgrey;
}

button {
    width: 250px;
}

input {
    border: none;
}
</style>
