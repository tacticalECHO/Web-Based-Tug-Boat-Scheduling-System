<template>
    <router-view />
    <SideBar />
    <div class="pages">
        <div id="Settings">
            <h3>Settings</h3>
            <div class = "form">
                <b><label for="username">Username  </label></b>
                &nbsp;  
                <input type="text" id="username" v-model="username" :placeholder="{ Name }" readonly>
            </div>
            <br>
            <div class = "form">
                <b><label for="password">Password  </label></b>
                &nbsp;  
                <input type="password" id="password" v-model="password" placeholder="Enter new password">
            </div>
        </div>
    </div>
    <div class="cancel-save-buttons">
        <button class="grey-border-button" id="cancel" @click="redirect('Exit-ChangePassword')">Cancel</button>
        <button class="blue-button" id="save" @click="save()">Save</button>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'ChangePassword',
    components: {SideBar},
    props: ['Name'],
    methods: {
        save(){
            //save pasword
            this.$router.back();
        }
    }
}
</script>

<style scoped>
.form {
    font-size: var(--font-size);
    margin-bottom: 15px;
}

#cancel {
    background: none;
    color: black;
}

#cancel:hover {
    background: lightgrey;
}

.settings-buttons {
    position: absolute;
    bottom: 50px;
    right: 10px;
}

input {
    border: none;
}
</style>
