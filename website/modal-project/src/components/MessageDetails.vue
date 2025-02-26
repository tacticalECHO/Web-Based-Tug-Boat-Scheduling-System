<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <button @click="close">X</button>
                <br/>
                <table>
                    <tr>
                        <th>Captain</th>
                        <td>Yibai Yuan</td>
                    </tr>
                    <tr>
                        <th>Container Boat</th>
                        <td>JHSANG9865</td>
                    </tr>
                    <tr>
                        <th>Country</th>
                        <td>Singapore</td>
                    </tr>
                    <tr>
                        <th>Tonnage</th>
                        <td>109978</td>
                    </tr>
                    <tr>
                        <th>Berth</th>
                        <td>NB02</td>
                    </tr>
                    <tr>
                        <th>Time</th>
                        <td>08:30</td>
                    </tr>
                    <tr>
                        <th>Tug Boat</th>
                        <td>ADB0078</td>
                    </tr>
                    <tr>
                        <th>Work Status</th>
                        <td>Incompleted</td>
                    </tr>
                    <tr>
                        <th>Work Type</th>
                        <td>In</td>
                    </tr>
                </table>
                <button class="blue-button" id="manualReschedule" @click="edit()">Edit Schedule</button>
                <br/> 
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'MessageDetails',
    props: [],
    methods: {
        close(){
            this.$router.back();
        },
        edit(){
            this.$router.push({name: 'ManualReschedule'});
        }
    }
}
</script>

<style scoped>
button {
    width: 30px;
    height: 30px;
    border: none;
    font-size: 15px;
}

.blue-button {
    align-self: flex-end;
    width: 130px;
    height: 40px;
    font-size: 13px;
}

.popup-container {
    width: 700px;
    height: 430px;
}

.container-position {
    margin-top: 120px;
}

table {
    margin-left: 30px;
    border-collapse: collapse;
    border-spacing: 0;
}

tr, td {
    border: none;
    padding: 10px;
}

th {
    width: 200px;
}

</style>
