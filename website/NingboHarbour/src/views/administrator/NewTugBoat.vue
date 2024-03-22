<template>
    <div class="backdrop">
        <div class="container-position">
            <form class="popup-container">
                <button class="close-btn" @click="redirect('TugBoatList')">X</button>
                <br/>
                <div class = "form">
                    <div class="form-group">
                        <b><label for="tugboatId">Tug Boat ID</label></b>  
                        <input type="text" id="tugboatId" v-model="tugboatId" placeholder="Input New Tug Boat ID" required>
                    </div>
                    <div class="form-group">
                        <b><label for="captainId">Captain</label></b>
                        <select v-model="captainId">
                            <option></option>
                            <option v-for="captain in $store.state.captains" :key="captain.CaptainId">{{ captain.CaptainId }} : {{ captain.name }}</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <b><label for="startTime">Working Hours</label></b>
                        <input type="time" id="startTime" v-model="startTime" required>&emsp; to<input type="time" id="endTime" v-model="endTime" required>
                    </div>
                </div>
                <br>
                <button class="btn btn-dark" id="confirm" @click="add()">Add</button>
                <br/> 
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'NewTugBoat',
    mounted(){
        this.$store.dispatch('fetchCaptains');
    },
    methods: {
        async add(){
            try { 
                const response = await axios.post('/api/update-tugboat/', {
                    tugboatId: this.tugboatId,
                    captainId: this.captainId,
                    startTime: this.startTime,
                    endTime: this.endTime,
                });
                if (response.data.success) {
                    alert(response.data.message+'\nNew Tug Boat Added Successfully');
                    
                    setTimeout(() => {
                        this.$store.dispatch('fetchCaptains');
                        this.$router.push({ path: '/tugboat-list' })
                    }, 1000); 
                    // this.$router.back()
                } else {
                    alert('Fail to add tug boat.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('New tug boat Error.');
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

#startTime, #endTime {
    width: 120px;
}

#endTime {
    margin-left: 20px;
}

</style>
