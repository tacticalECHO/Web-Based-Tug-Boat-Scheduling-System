<template>
    <div id="work-table" class="pages">
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
</template>

<script>

export default {
    name: 'WorkTable',
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
</style>