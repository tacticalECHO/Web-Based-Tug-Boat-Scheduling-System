<template>
    <SideBar />
    <div class="pages">
        <div id="ConflictScheduleList">
            <h2>Conflict Schedule List</h2>
            <div class="button-style" >
                <button class="grey-border-button" id="filter">Filter Schedules</button>
                <button class="grey-border-button" id="Publish">Publish</button>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>No.1</th>
                        <th>Container Boat</th>
                        <th>Berth</th>
                        <th>Time</th>
                        <th>Tug Boat</th>
                        <th>Captain</th>
                        <th>Work Status</th>
                        <th>Work Type</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="number"> {{number}} </td>
                        <td class="container-boat"> {{containerBoat}} </td>
                        <td class="berth"> {{berth}} </td>
                        <td class="time"> {{time}} </td>
                        <td class="tugboat"> {{tugBoat}} </td>
                        <td class="captain"> {{captain}} </td>
                        <td class="work-status"> <span class="status-container">{{workStatus}} </span></td>
                        <td class="work-type"> <span class="type-container">{{workType}}</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'ConflictScheduleList',
    components: {SideBar},
    data() {
        return {
            number: "1",
            containerBoat: "JHSANG888",
            berth: "NB02",
            time: "08.30",
            tugBoat: "ADB0078",
            captain: "unknown",
            workStatus: "Completed",
            workType: "In",
        }
    },
}
</script>

<style scoped>

button{
    border-radius: 10px;
}

.button-style{
    display: flex;
    justify-content: space-between;
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
    padding: 15px;
}

th {
    background-color: #f2f2f2;
}

td {
    text-align: center;
}

.status-container{
    background: rgb(254, 219, 46);
    color: white;
    border-radius: 30px;
    padding: 8px;
}

.type-container{
    background: rgb(254, 239, 142);
    color: rgb(154, 126, 0);
    border-radius: 30px;
    padding: 8px;
}
</style>
