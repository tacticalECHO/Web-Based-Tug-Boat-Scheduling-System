<!-- Vue file created by Team 10, ©2024 -->
<template>
    <div id="TugBoatList" @click="toggle()">
        <SideBar />
        <router-view />
        <div class="pages">
            <h2 class="title">Tug Boat List</h2>
            <div class="search-form">
                <label for="search">
                    <input required="" autocomplete="off" placeholder="Search ... " id="search"  v-model="input" type="text">
                    <div class="icon">
                        <svg stroke-width="2" stroke="currentColor" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="swap-on">
                            <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" stroke-linejoin="round" stroke-linecap="round"></path>
                        </svg>
                        <svg stroke-width="2" stroke="currentColor" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="swap-off">
                            <path d="M10 19l-7-7m0 0l7-7m-7 7h18" stroke-linejoin="round" stroke-linecap="round"></path>
                        </svg>
                    </div>
                    <button type="reset" class="close-btn" @click="input=''">
                        <svg viewBox="0 0 20 20" class="h-5 w-5" xmlns="http://www.w3.org/2000/svg">
                            <path clip-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" fill-rule="evenodd"></path>
                        </svg>
                    </button>
                </label>
            </div>
            <br><br>
            <div class="header-style">
                <div class="filter-group">
                    <span>Status: </span>
                    <span class="btn-group" role="group" aria-label="Vertical radio toggle button group">
                        <input type="radio" class="btn-check" name="vbtn-radio" id="All" autocomplete="off" value="" v-model="allStatus" @change="handleChange('')" checked>
                        <label class="btn btn-outline-dark filter-btn" for="All">All</label>
                        
                        <input type="radio" class="btn-check" name="vbtn-radio" id="Free" autocomplete="off" value="Free" v-model="freeStatus" @change="handleChange('Free')">
                        <label class="btn btn-outline-dark filter-btn" for="Free">Free</label>
                        
                        <input type="radio" class="btn-check" name="vbtn-radio" id="Busy" autocomplete="off" value="Busy" v-model="busyStatus" @change="handleChange('Busy')">
                        <label class="btn btn-outline-dark filter-btn" for="Busy">Busy</label>
                        
                        <input type="radio" class="btn-check" name="vbtn-radio" id="Maintenance" autocomplete="off" value="Maintenance" v-model="maintenanceStatus" @change="handleChange('Maintenance')">
                        <label class="btn btn-outline-dark filter-btn" for="Maintenance">Maintenance</label>
                    </span>
                </div>
                <span class="add-delete">
                    <button type="button" class="delete" id="delete" @click= deleteSelected>
                        <span class="delete__text">Delete &nbsp;</span>
                        <span class="delete__icon"><font-awesome-icon :icon="['fas', 'delete-left']" /></span>
                    </button>
                    &nbsp;
                    <button type="button" class="add" id="add" @click="redirect('NewTugBoat')">
                        <span class="add__text">Add &nbsp;</span>
                        <span class="add__icon"><font-awesome-icon :icon="['fas', 'plus']" /></span>
                    </button>
                </span>
                    <!-- <button class="btn btn-light" id="delete" @click= "deleteSelected()">Delete  <font-awesome-icon :icon="['fas', 'delete-left']" /></button>
                    &nbsp;
                    <button class="btn btn-dark" id="add" @click="redirect('NewTugBoat')">Add  + </button> -->
            </div>
            <div class="table-container">
                <div class="work-table">
                    <table class="table">
                        <thead>
                            <tr>
                                <th style="text-align: center" rowspan="2"><input type="checkbox" disabled/></th>
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
                                <td><input type="checkbox" v-model="selectedTugboat" :value="tugboat.TugBoatId"/></td>
                                <td class="number"> {{ index+1 }} </td>
                                <td>{{ tugboat.TugBoatId }}</td>
                                <td @click.stop>
                                    <form v-if="captainInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <select @change="edit(tugboat.TugBoatId)" v-model="captainId">
                                            <option value=""></option>
                                            <option v-for="captain in $store.state.captains" :key="captain.CaptainId">{{ captain.CaptainId }} : {{ captain.name }}</option>
                                        </select>
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span class="click-hover" v-if="captainInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'captain')">{{ getCaptainId(tugboat.TugBoatId) }}</span>
                                </td>
                                <td>{{ getCaptainName(tugboat.TugBoatId) }}</td>
                                <td @click.stop>
                                    <form v-if="startTimeInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <input v-model="startTime" type="time">
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span class="click-hover" v-if="startTimeInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'startTime')">{{ tugboat.StartWorkingTime }}</span>
                                </td>
                                <td @click.stop>
                                    <form v-if="endTimeInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <input v-model="endTime" type="time">
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span class="click-hover" v-if="endTimeInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'endTime')">{{ tugboat.EndWorkingTime }}</span>
                                </td>
                                <td class="work-status" @click.stop> 
                                    <form v-if="statusInfo === tugboat.TugBoatId" @submit="edit(tugboat.TugBoatId)">
                                        <select @change="edit(tugboat.TugBoatId)" v-model="status">
                                            <option>{{ tugboatStatus(tugboat.CurrentStatus) }}</option>
                                        </select>
                                        <input class="submit-button" type="submit" />
                                    </form>
                                    <span v-if="statusInfo != tugboat.TugBoatId" @click="selected(tugboat.TugBoatId, 'status')" class="status-container click-hover" :style="getStatusStyle(tugboat.CurrentStatus)">{{tugboat.CurrentStatus}} </span>
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
            tugboatStatus: null,
            selectedTugboat: [],
        }
    },
    methods: {
        async deleteSelected() {
            if(this.deletionAlert()){
                if (this.selectedTugboat.length > 0) {
                    await fetch(`/api/tugboat-delete/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ ids: this.selectedTugboat })
                    });
                }
                alert('Deleted successfully');
                this.$store.dispatch('fetchTugBoats');
                this.$store.dispatch('fetchCaptains');
            }
            this.selectedTugboat = [];
        },
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
                const byStatus = this.chosenStatus ? tugboat.CurrentStatus.toLowerCase() === this.chosenStatus.toLowerCase() : true;

                if (this.input) {
                    const byCaptainName = tugboat.CaptainId ? tugboat.CaptainId.name.toLowerCase().includes(this.input.toLowerCase()) : false;
                    const byCaptainId = tugboat.CaptainId ? tugboat.CaptainId.CaptainId.toLowerCase().includes(this.input.toLowerCase()) : false;

                    return (byCaptainName || byCaptainId || byTugBoatId) && byStatus;
                } else {
                    return byTugBoatId && byStatus;
                }
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
        },
        tugboatStatus(status){
            if(status === 'Maintenance'){
                return 'Free';
            }else{
                return 'Maintenance';
            }
        }
    }
}
</script>

<style scoped>
.header-style{
    padding: 10px;
}

.filter-btn {
    width: 90px;
}
/* This section of CSS for search includes styles referenced from [https://uiverse.io/satyamchaudharydev/slippery-parrot-22] All credit for the referenced styles goes to the original authors.  */
.search-form {
    position: relative;
    display: inline-block;
    font-size: var(--font-size);
    --input-bg: #FFf;
    --padding: 1.5em;
    --rotate: 80deg;
    --gap: 2em;
    --icon-change-color: #15A986;
    --height: 40px;
    width: 250px;
    padding-inline-end: 1em;
    background: var(--input-bg);
    position: relative;
    border-radius: 20px;
}

.search-form label {
    display: flex;
    align-items: center;
    width: 100%;
    height: var(--height);
}

.search-form input {
    width: 100%;
    padding-inline-start: calc(var(--padding) + var(--gap));
    outline: none;
    background: none;
    border: 0;
}

.search-form svg {
    color: #111;
    transition: 0.3s cubic-bezier(.4,0,.2,1);
    position: absolute;
    height: 15px;
    }

.icon {
    position: absolute;
    left: var(--padding);
    transition: 0.3s cubic-bezier(.4,0,.2,1);
    display: flex;
    justify-content: center;
    align-items: center;
}

.swap-off {
    transform: rotate(-80deg);
    opacity: 0;
    visibility: hidden;
}

.close-btn {
    background: none;
    border: none;
    right: calc(var(--padding) - var(--gap));
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #111;
    padding: 0.1em;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    transition: 0.3s;
    opacity: 0;
    transform: scale(0);
    visibility: hidden;
}

.search-form input:focus ~ .icon {
    transform: rotate(var(--rotate)) scale(1.3);
}

.search-form input:focus ~ .icon .swap-off {
    opacity: 1;
    transform: rotate(-80deg);
    visibility: visible;
    color: var(--icon-change-color);
}

.search-form input:focus ~ .icon .swap-on {
    opacity: 0;
    visibility: visible;
}

.search-form input:valid ~ .icon {
    transform: scale(1.3) rotate(var(--rotate))
}

.search-form input:valid ~ .icon .swap-off {
    opacity: 1;
    visibility: visible;
    color: var(--icon-change-color);
}

.search-form input:valid ~ .icon .swap-on {
    opacity: 0;
    visibility: visible;
}

.search-form input:valid ~ .close-btn {
    opacity: 1;
    visibility: visible;
    transform: scale(1);
    transition: 0s;
}

.pageName{
    padding-left: 50px;
}
</style>