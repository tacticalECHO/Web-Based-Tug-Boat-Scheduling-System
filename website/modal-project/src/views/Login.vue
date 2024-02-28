<template>
    <div id = "Login">
        <div class = "login-container">
            <h1>Ningbo Harbour</h1>
            <div v-if = "showError" class = "invalid-login">
                <p>Invalid username or password, please log in again</p>
            </div>
            <!-- <form> -->
                <div class = "form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" v-model="username" placeholder="Input your ID">
                </div>
                <div class = "form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" v-model="password" placeholder="Input your password">
                </div>
                <button class="blue-button" @click="login()">Login</button>
            <!-- </form> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
name: 'Login',
data() {
  return {
    username: '',
    password: '',
    showError: false,
  };
},
methods: {
  async login() {
    try {
      const response = await axios.post('http://localhost:8000/api/login/', {
        username: this.username,
        password: this.password,
      });
      // The backend response contains { success: true } on successful login
      if (response.data.success) {
          this.showError = false;
          this.$store.commit('setUser', { username: this.username });
          this.$store.commit('setUserRole', { isCaptain: response.data.is_captain, isAdmin: response.data.is_staff
                                                ,isScheduler: response.data.is_scheduler});
          this.$router.push({ name: 'Settings' });
      } else {
        this.showError = true; // Show error if login failed
      }
    } catch (error) {
      console.error('Login error:', error);
      this.showError = true; 
      document.getElementById('username').style.border = "1px solid red";
      document.getElementById('password').style.border = "1px solid red";
    }
  },
},
};
</script>

<style scoped>
body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
  background-color: #f4f4f4;
}

.login-container {
  margin: auto;
  margin-top: 10%;
  width: 500px;
  background-color: #fff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-container h1{
  color: var(--headings-color);
  font-weight: 900;
  font-size: 45px;
}

.invalid-login{
  width: var(--login-width-size);
  border-radius: 4px;
  border: 2px solid red;
  background-color: rgba(255,0,0,0.2);
  padding-left: 5px;
  padding-right: 5px;
  text-align: center;
  margin-bottom: 15px;
  color: red;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-size: 14px;
  margin-bottom: 5px;
}

input {
  width: var(--login-width-size);
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
}

button {
  width: var(--login-width-size);
  font-size: 16px;
}

</style>
