<template>
    <div id="Settings">
        <SideBar />
        <div class="pages">
            <router-view />
            <h3>Settings</h3>
                <div class = "form">
                    <b><label for="username">Username  </label></b>
                    &nbsp;  
                    <input type="text" id="username" v-model="username" :placeholder="username" readonly>
                </div>
                <br>
                <div class = "form">
                    <b><label for="password">Password  </label></b>
                    &nbsp;  
                    <input type="password" id="password" v-model="password" placeholder="Enter new password">
                </div>
                <br>
                <div class = "form">
                    <b><label for="passwordReEntered">Re-Enter</label></b>
                    &nbsp; &nbsp; 
                    <input type="password" id="passwordReEntered"  placeholder="Re-enter new password">
                </div>
            </div>
            <div class="cancel-save-buttons">
                <button class="grey-border-button" id="cancel" @click="redirect('Exit-ChangePassword')">Cancel</button>
                <button class="blue-button" id="save" @click="save()">Save</button>
            </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import { mapState } from 'vuex';
import axios from 'axios';

export default {
    name: 'ChangePassword',
    components: {SideBar},
    data(){
        return{
            password: '',
            reenter: '',
        }
    },
    computed: {
        ...mapState([
            'username',
            'passwordPlaceholder' 
        ]),

        comparePassword(){
            
        }

    },
    methods: {
        cancel(){
            this.$router.push({name: 'Exit-ChangePassword'});
        },
        async save() {
            this.password = document.getElementById('password').value;
            this.reenter = document.getElementById('passwordReEntered').value;
            if(this.password === this.reenter){
                try {
                    
                        const response = await axios.post('http://localhost:8000/api/change-password/', {
                        username: this.username,
                        password: this.password,
                        });
                        if (response.data.success) {
                            this.$router.push({ name: 'Login' });
                        } else {
                            alert('Password change failed.');
                        }
                    
                } catch (error) {
                    console.error('Change password error:', error);
                    alert('Password change error.');
                }
            }else {
                alert('Passwords are not similar.');
                document.getElementById('passwordReEntered').style.border = "1px solid red";
            }
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
