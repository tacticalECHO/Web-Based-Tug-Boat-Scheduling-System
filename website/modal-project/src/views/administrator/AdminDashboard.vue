<template>
    <SideBar />
    <div class="pages">
        <div id="AdminDashboard">
            <div class="header-style">
                <h2>Your Dashboard</h2>
                <span>
                    <button class="grey-border-button" id="delete" @click="redirect('')">Delete<span></span></button>
                    &nbsp;
                    <button class="blue-button" id="new-staff" @click="redirect('NewStaff')">New Staff  <span>+</span></button>
                </span>
            </div>
            <table id="captain-info">
                <caption><b>Captain</b></caption>
                <thead>
                    <tr>
                        <th><input type="checkbox" disabled></th>
                        <th>Captain Name</th>
                        <th>Captain ID</th>
                        <th>Tug Boat</th>
                        <th>Captain Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>
                        <td id="captain-name"> {{captainName}} </td>
                        <td id="captain-id"> {{captainId}} </td>
                        <td id="tugboat"> {{tugboat}} </td>
                        <td id="captain-status"> <span  class="status-container">{{captainStatus}}</span> </td>
                    </tr>
                </tbody>
            </table>
            <table id="scheduler-info">
                <caption><b>Scheduler</b></caption>
                <thead>
                    <tr>
                        <th><input type="checkbox" disabled></th>
                        <th>Scheduler Name</th>
                        <th>Scheduler ID</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox" id="myCheckbox" name="myCheckbox"></td>
                        <td id="scheduler-name"> {{schedulerName}} </td>
                        <td id="scheduler-id"> {{schedulerId}} </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <router-view />
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'AdminDashboard',
    components: {SideBar},
    data() {
        return {
            captainName: "Olivia Lim",
            captainId: "56765673",
            tugboat: "ADB0078",
            captainStatus: "Working",

            schedulerName: "Tom Bai",
            schedulerId: "330000234"
        }
    },
}
</script>

<style scoped>
button{
    border-radius: 20px;
}

.header-style{
    padding: 10px;
}

caption {
    text-align: left;
    font-size: 16px;
    margin-bottom: 15px;
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
