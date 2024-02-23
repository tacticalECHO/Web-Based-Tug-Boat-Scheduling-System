<template>
    <SideBar />
    <div class="pages">
        <div id="TaskManager">
            <h2>Today Task</h2>
            <div class="header-style">
                <form><input id="search"></form>
                <span>
                    <button class="blue-border-button" id="delete" @click="redirect('')">Delete<span></span></button>
                    &nbsp;
                    <button class="blue-border-button" id="add" @click="redirect('NewTask')">Add<span></span></button>
                </span>
            </div>
            <table>
                <thead>
                    <tr>
                        <th><input type="checkbox" disabled></th>
                        <th>No.1</th>
                        <th>Container Boat</th>
                        <th>Tonnage</th>
                        <th>Country</th>
                        <th>Arrival Time</th>
                        <th>Leave Time</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>
                        <td id="number"> {{number}} </td>
                        <td id="container-boat"> {{containerBoat}} </td>
                        <td id="berth"> {{tonnage}} </td>
                        <td id="time"> {{country}} </td>
                        <td id="tugboat"> {{arrivalTime}} </td>
                        <td id="captain"> {{leaveTime}} </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'WorkSchedule',
    components: {SideBar},
    data() {
        return {
            number: "1",
            containerBoat: "JHSANG888",
            tonnage: "110928",
            country: "Australia",
            arrivalTime: "08.30",
            leaveTime: "08.30",
        }
    },
}
</script>

<style scoped>

form input {
    padding: 10px;
    border-radius: 20px;
    border: 1px solid lightgrey;
}

button{
    color: black;
    border-radius: 20px;
}

.header-style{
    padding: 10px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    font-size: var(--font-size);
}

th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 10px;
}

th {
    background-color: #f2f2f2;
}
</style>
