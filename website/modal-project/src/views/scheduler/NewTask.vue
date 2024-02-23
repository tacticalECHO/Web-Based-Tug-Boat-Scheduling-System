<template>
    <SideBar />
    <div class="pages">
        <div id="NewTask">
            <h2>New Task</h2>
            <table>
                <tr>
                    <td><b><label for="container-boat">Container Boat</label></b></td>
                    <td><input type="text" id="container-boat" placeholder="Input the ID of Container Boat"></td>
                </tr>
                <tr>
                    <td><b><label for="country">Country</label></b></td>
                    <td><input type="text" id="country" placeholder="Input the Country"></td>
                </tr>
                <tr>
                    <td><b><label for="tonnage">Tonnage</label></b></td>
                    <td><input type="text" id="tonnage" placeholder="Input Tonnage of Ship"></td>
                </tr>
                <tr>
                    <td><b><label for="arrival-time">Arrival Time</label></b></td>
                    <td><input type="text" id="arrival-time" placeholder="Set Arrive Time"></td>
                </tr>
                <tr>
                    <td><b><label for="leave-time">Leave Time</label></b></td>
                    <td><input type="text" id="leave-time" placeholder="Set Leave Time"></td>
                </tr>
            </table>
        </div>
        <router-view />
    </div>
    
    <div class="cancel-save-buttons">
        <button class="grey-border-button" id="cancel" @click="redirect('Exit-NewTask')">Cancel</button>
        <button class="blue-button" id="save" @click="save()">Save</button>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'NewTask',
    components: {SideBar},
    methods: {
    save(){
        //save pasword
        this.$router.push({name: 'Save-NewTask'});
    }
    }
}
</script>

<style scoped>
table {
    text-align: left;
    font-size: 16;
    margin-bottom: 15px;
}

th, td {
    padding: 10px;
}

input {
    border: none;
    padding: 8px;
    border-radius: 10px;
    border: 1px solid black;
    width: 300px;
}
</style>
