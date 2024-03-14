<template>
    <div id="TugBoatList" @click="toggle()">
        <SideBar />
        <router-view />
        <div class="pages">
            <h2>Tug Boat List</h2>
            <div class="header-style" >
                <form class="search-form">
                    <input id="search" type="text" v-model="input" placeholder="Search...">
                    <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="search-icon" />
                </form>
                <span>
                    <button class="grey-border-button" id="delete" @click="redirect('')">Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="blue-button" id="add" @click="redirect('NewTugBoat')">Add  + </button>
                </span>
            </div>
            
            <div class="filter-group">
                <label for="statusFilter">Status: </label>
                <input type="checkbox" value="" v-model="allStatus" @change="handleChange('')" selected> All
                <input type="checkbox" value="Free" v-model="freeStatus" @change="handleChange('Free')"> Free
                <input type="checkbox" value="Busy" v-model="busyStatus" @change="handleChange('Busy')"> Busy
                <input type="checkbox" value="Maintenance" v-model="maintenanceStatus" @change="handleChange('Maintenance')"> Maintenance
            </div>

            <div class="table-container">
                <div class="work-table">
                    <table>
                        <thead>
                            <tr>
                                <th style="text-align: center" rowspan="2"><input type="checkbox"/></th>
                                <th rowspan="2">No.</th>
                                <th rowspan="2">Tugboat ID</th>
                                <th colspan="2">Captain</th>
                                <th colspan="2">Working Hours</th>
                                <th rowspan="2">Status</th>
                            </tr>
                            <tr>
                                <th style="text-align: center">ID</th>
                                <th style="text-align: center">Name</th>
                                <th style="text-align: center">Start</th>
                                <th style="text-align: center">End</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(tugboat,index) in tugboatList()" :key="index">
                                <td><input type="checkbox"/></td>
                                <td class="number"> {{ index+1 }} </td>
                                <td>{{ tugboat.TugBoatId }}</td>
                                <td @click.stop>
                                    <form v-if="captainInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <select @change="edit(tugboat.TugBoatId)" v-model="captainId">
                                            <option v-for="captain in $store.state.captains" :key="captain.CaptainId">{{ captain.CaptainId }} : {{ captain.name }}</option>
                                        </select>
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span v-if="captainInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'captain')">{{ getCaptainId(tugboat.TugBoatId) }}</span>
                                </td>
                                <td>{{ getCaptainName(tugboat.TugBoatId) }}</td>
                                <td @click.stop>
                                    <form v-if="startTimeInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <input v-model="startTime" type="time">
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span v-if="startTimeInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'startTime')">{{ tugboat.StartWorkingTime }}</span>
                                </td>
                                <td @click.stop>
                                    <form v-if="endTimeInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <input v-model="endTime" type="time">
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span v-if="endTimeInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'endTime')">{{ tugboat.EndWorkingTime }}</span>
                                </td>
                                <td class="work-status" @click.stop> 
                                    <form v-if="statusInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <select @change="edit(tugboat.TugBoatId)" v-model="status">
                                            <option>Maintenance</option>
                                        </select>
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span v-if="statusInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'status')" class="status-container" :style="getStatusStyle(tugboat.CurrentStatus)">{{tugboat.CurrentStatus}} </span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';
import axios from 'axios';

export default {
    name: 'TugBoatList',
    components: {SideBar},
    mounted(){
        this.$store.dispatch('fetchTugBoats');
        this.$store.dispatch('fetchCaptains');
    },
    data(){
        return{
            tugboats: [],
            input: '',
            allStatus: true,
            freeStatus: null,
            busyStatus: null,
            maintenanceStatus: null,
            chosenStatus: '',
            captainInfo: null,
            startTimeInfo: null,
            endTimeInfo: null,
            statusInfo: null,
        }
    },
    methods: {
        handleChange(state) {
            this.chosenStatus = state;
            if (state === 'Free') {
                this.allStatus = null;
                this.busyStatus = null;
                this.maintenanceStatus = null;
            }else if (state === 'Busy'){
                this.allStatus = null;
                this.freeStatus = null;
                this.maintenanceStatus = null;
            }else if (state === 'Maintenance'){
                this.allStatus = null;
                this.freeStatus = null;
                this.busyStatus = null;
            }else{
                this.freeStatus = null;
                this.busyStatus = null;
                this.maintenanceStatus = null;
            }
        },
        tugboatList() {
            // Fetch tugboats from the store
            this.tugboats = this.$store.state.tugboats;

            // Filter tugboats based on input and chosenStatus
            return this.tugboats.filter((tugboat) => {  
                const byTugBoatId = tugboat.TugBoatId.toLowerCase().includes(this.input.toLowerCase());
                const byCaptainName = tugboat.CaptainId ? tugboat.CaptainId.name.toLowerCase().includes(this.input.toLowerCase()): true;
                const byCaptainId = tugboat.CaptainId ? tugboat.CaptainId.CaptainId.toLowerCase().includes(this.input.toLowerCase()): true;
                const byStatus = this.chosenStatus ? tugboat.CurrentStatus.toLowerCase() === this.chosenStatus.toLowerCase() : true;

                return (byCaptainName || byCaptainId || byTugBoatId) && byStatus;
            });
        },
        getCaptainId(id){
            const tugboat = this.tugboats.find((tugboat) => tugboat.TugBoatId === id);
            return tugboat && tugboat.CaptainId ? tugboat.CaptainId.CaptainId : "-";
        },
        getCaptainName(id){
            const tugboat = this.tugboats.find((tugboat) => tugboat.TugBoatId === id);
            return tugboat && tugboat.CaptainId ? tugboat.CaptainId.name : "-";
        },
        selected(id, type){
            this.resetNull();
            if(type === 'captain'){
                this.captainInfo = id;
            }else if(type === 'startTime'){
                this.startTimeInfo = id;
            }else if(type === 'endTime'){
                this.endTimeInfo = id;
            }else if(type === 'status'){
                this.statusInfo = id
            }
        },
        resetNull(){
            this.captainInfo = null
            this.startTimeInfo = null
            this.endTimeInfo = null
            this.statusInfo = null
        },
        async edit(id){
            try { 
                const response = await axios.post('/api/update-tugboat/', {
                    tugboatId: id,
                    captainId: this.captainId,
                    startTime: this.startTime,
                    endTime: this.endTime,
                    status: this.status,
                });
                if (response.data.success) {
                    alert('Edited Succesfully')
                    window.location.reload();
                    this.resetNull();
                } else {
                    alert('Edit Failed.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert(error);
            }
        }
    }
}
</script>

<style scoped>
button{
    border-radius: 10px;
}

.header-style{
    padding: 10px;
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

</style>