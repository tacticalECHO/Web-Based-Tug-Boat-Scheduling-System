<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <button @click="close" class="close-btn">X</button>
                <br/>
                <font-awesome-icon :icon="['fas', 'user-plus']" :size="['2x']"/>
                <br/>
                <div class = "form">
                    <div class="form-group">
                        <b><label for="username">ID</label></b>  
                        <input type="text" id="username" v-model="username" placeholder="Input staff ID" required/>
                    </div>
                    <div class="form-group">
                        <b><label for="name">Name</label></b>
                        <input type="text" id="name" v-model="name" placeholder="Input staff name" required/>
                    </div>
                    <div class = "form-group">
                        <b><label for="position">Position</label></b>
                        &nbsp;   
                        <select id="position" v-model="selectedPosition" required>
                            <option disabled value="" selected>Choose the position</option>
                            <option>Administrator</option>
                            <option>Scheduler</option>
                            <option>Captain</option>
                        </select>
                    </div>
                </div>
                <br>
                <button class="btn btn-dark" id="confirm" @click="confirm()">Confirm</button>
                <br/> 
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'MessageDetails',
    data() {
        return {
        username: '',
        name: '',
        selectedPosition: ''
        };
    },
    methods: {
        close(){
            this.$router.back();
        },
        async confirm() {
            const apiUrl = '/api/create-user/';
            try {
                const response = await axios.post(apiUrl, {
                username: this.username,
                name: this.name,
                position: this.selectedPosition,
                password: '12345678'
            }, {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                alert('User created successfully');
                this.close(); 
            } catch (error) {
                console.error('Failed to create user:', error);
                alert('Failed to create user');
            }
        }
    }
}
</script>

<style scoped>
.backdrop {
    z-index: 1000; 
    position: fixed; 
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5); 
}

.form-group {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
}
.form-group label {
    width: 90px;
    display: inline-block; 
    text-align: right;
    margin-right: 10px; 
}

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

.btn {
    align-self: center;
    width: 130px;
    height: 40px;
    font-size: 13px;
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
