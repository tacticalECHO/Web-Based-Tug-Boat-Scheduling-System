<template>
    <div id="TaskManager">
        <SideBar />
        <div class="pages" @click="toggle">
            <h2>Today Task</h2>
            <div class="header-style">
                <form class="search-form">
                    <input id="search" placeholder="Search...">
                    <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="search-icon" />
                </form>
                <span>
                    <button class="blue-border-button" id="delete" @click="redirect('')">Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="blue-border-button" id="add" @click="redirect('NewTask')">Add  + </button>
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
                        <td @click.stop> 
                            <form>
                                <input id="containerBoatForm" v-if="showContainerBoatForm" type="text" :value="containerBoat">
                            </form>
                            <span v-if="containerBoatInfo" @click="clickContainerBoat()" id="containerBoatInfo">{{containerBoat}}</span> 
                        </td>
                        <td @click.stop>
                            <form>
                                <input id="tonnageForm" v-if="showTonnageForm" type="text"  :value="tonnage">
                            </form>
                            <span v-if="tonnageInfo" @click="clickTonnage()" id="tonnageInfo">{{tonnage}}</span> 
                        </td>
                        <td @click.stop>
                            <form>
                                <input id="countryForm" v-if="showCountryForm" type="text"  :value="country">
                            </form>
                            <span v-if="countryInfo" @click="clickCountry()" id="countryInfo">{{country}}</span> 
                        </td>
                        <td @click.stop>
                            <form>
                                <input id="arrivalTimeForm" v-if="showArrivalTimeForm" type="text"  :value="arrivalTime">
                            </form>
                            <span v-if="arrivalTimeInfo" @click="clickArrivalTime()" id="arrivalTimeInfo">{{arrivalTime}}</span> 
                        </td>
                        <td @click.stop>
                            <form>
                                <input id="leaveTimeForm" v-if="showLeaveTimeForm" type="text"  :value="leaveTime">
                            </form>
                            <span v-if="leaveTimeInfo" @click="clickLeaveTime()" id="leaveTimeInfo">{{leaveTime}}</span> 
                        </td>
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
            showContainerBoatForm: false,
            containerBoatInfo: true,
            showTonnageForm: false,
            tonnageInfo: true,
            showCountryForm: false,
            countryInfo: true,
            showArrivalTimeForm: false,
            arrivalTimeInfo: true,
            showLeaveTimeForm: false,
            leaveTimeInfo: true,
            number: "1",
            containerBoat: "JHSANG888",
            tonnage: "110928",
            country: "Australia",
            arrivalTime: "08.30",
            leaveTime: "08.30",
        }
    },
    methods: {
        clickContainerBoat(){
            this.showContainerBoatForm = true;
            this.containerBoatInfo = false;
            this.showTonnageForm = false;
            //others
            this.tonnageInfo = true;
            this.showCountryForm = false;
            this.countryInfo = true;
            this.showArrivalTimeForm = false;
            this.arrivalTimeInfo = true;
            this.showLeaveTimeForm = false;
            this.leaveTimeInfo = true;
        },
        clickTonnage(){
            this.showTonnageForm = true;
            this.tonnageInfo = false;
            //others
            this.showContainerBoatForm = false;
            this.containerBoatInfo = true;
            this.showCountryForm = false;
            this.countryInfo = true;
            this.showArrivalTimeForm = false;
            this.arrivalTimeInfo = true;
            this.showLeaveTimeForm = false;
            this.leaveTimeInfo = true;
        },
        clickCountry(){
            this.showCountryForm = true;
            this.countryInfo = false;
            //others
            this.showTonnageForm = false;
            this.tonnageInfo = true;
            this.showContainerBoatForm = false;
            this.containerBoatInfo = true;
            this.showArrivalTimeForm = false;
            this.arrivalTimeInfo = true;
            this.showLeaveTimeForm = false;
            this.leaveTimeInfo = true;
    },
        clickArrivalTime(){
            this.showArrivalTimeForm = true;
            this.arrivalTimeInfo = false;
            //others
            this.showTonnageForm = false;
            this.tonnageInfo = true;
            this.showCountryForm = false;
            this.countryInfo = true;
            this.showContainerBoatForm = false;
            this.containerBoatInfo = true;
            this.showLeaveTimeForm = false;
            this.leaveTimeInfo = true;
        },
        clickLeaveTime(){
            this.showLeaveTimeForm = true;
            this.leaveTimeInfo = false;
            //others
            this.showTonnageForm = false;
            this.tonnageInfo = true;
            this.showCountryForm = false;
            this.countryInfo = true;
            this.showArrivalTimeForm = false;
            this.arrivalTimeInfo = true;
            this.showContainerBoatForm = false;
            this.containerBoatInfo = true;
        },
        toggle(event) {
            if (!event.target.closest('form')) {
                this.showContainerBoatForm = false;
                this.containerBoatInfo = true;
                this.showTonnageForm = false;
                this.tonnageInfo = true;
                this.showCountryForm = false;
                this.countryInfo = true;
                this.showArrivalTimeForm = false;
                this.arrivalTimeInfo = true;
                this.showLeaveTimeForm = false;
                this.leaveTimeInfo = true;
            }
        },
    }
}
</script>

<style scoped>
#containerBoatForm {
    width: fit-content;
}

#search {
    padding: 10px;
    border-radius: 20px;
    border: 1px solid lightgrey;
}

.search-form {
    position: relative;
    display: inline-block;
}

.search-icon {
    position: absolute;
    top: 40%;
    right: 10px;
    transform: translateY(-50%);
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
