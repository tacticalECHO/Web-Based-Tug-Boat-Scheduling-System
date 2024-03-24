<template>
    <div id="Sidebar" @click="closeSidebar()"> 
        <div class="header">
            <img src="../assets/header.jpg" class="header-image">
        </div>
        <div v-if="screen() || sidebarOpened" id="sidebar">
            <h2>Ningbo <br> Harbour</h2>
            <ul>
                <li v-if="isAdmin ||isScheduler" @click="redirect('AdminDashboard')" id="admin-dashboard" class="sidebar-item" :style="{ backgroundColor: adminDashboard }">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    A-Dashboard 
                    <span v-if="adminDashboard != 'none'" class="sidebar-selected">&nbsp;</span>
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('SchedulerDashboard')" id="scheduler-dashboard" class="sidebar-item" :style="{ backgroundColor: schedulerDashboard }">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    S-Dashboard
                    <span v-if="schedulerDashboard != 'none'" class="sidebar-selected">&nbsp;</span>
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('TugBoatList')" id="scheduler-dashboard" class="sidebar-item" :style="{ backgroundColor: tugboat}">
                    <font-awesome-icon :icon="['fas', 'ship']" class="sidebar-icon"/>
                    Tug Boats
                    <span v-if="tugboat != 'none'" class="sidebar-selected">&nbsp;</span>
                </li>
                <li v-if="isCaptain || isScheduler || isAdmin" @click="redirect('CaptainDashboard')" id="captain-dashboard" class="sidebar-item" :style="{ backgroundColor: captainDashboard }">
                    <admin-panel v-if="isCaptain" />
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    C-Dashboard
                    <span v-if="captainDashboard != 'none'" class="sidebar-selected">&nbsp;</span>
                </li>
                <li v-if="isScheduler || isCaptain|| isAdmin" @click="redirect('WorkSchedule')" class="sidebar-item" :style="{ backgroundColor: workSchedule }">
                    <font-awesome-icon :icon="['fas', 'calendar-days']" class="sidebar-icon"/>
                    Work Schedules
                    <span v-if="workSchedule != 'none'" class="sidebar-selected">&nbsp;</span>
                </li>
            </ul>

            <div class="sidebar-bottom-section">
                <ul>
                    <li @click="redirect('Settings')" class="sidebar-item" :style="{ backgroundColor: settings }">
                        <font-awesome-icon :icon="['fas', 'gear']" class="sidebar-icon"/>
                        Settings
                        <span v-if="settings != 'none'" class="sidebar-selected">&nbsp;</span>
                    </li>
                    <li class="sidebar-item" id="profile">
                        <font-awesome-icon :icon="['fas', 'user']" class="sidebar-icon"/>
                        {{profile_name}}
                    </li>
                </ul>
            </div>
        </div>
        <button class="btn btn-outline-dark" @click.stop="openSidebar()" v-if="!screen()" id="open-sidebar"><font-awesome-icon :icon="['fas', 'bars']" size="2x"/></button>
        <!-- <button class="btn btn-outline-dark" @click="closeSidebar()" v-if="sidebarOpened && closeButton()" id="close-sidebar"><font-awesome-icon :icon="['fas', 'backward']" size="2x"/></button> -->
        <footer class="footer fixed-bottom">
            <div class="text-center p-3">
                WEB BASED TUGBOAT SCHEDULING SYSTEM
            </div>
        </footer>
    </div>
    
</template>

<script>
import { mapState } from 'vuex';

export default {
    name: 'SideBar',
    computed: {
        ...mapState(['username', 'isCaptain', 'isAdmin', 'isScheduler']),
        profile_name() {
            return this.username || 'Guest';
        }
    },
    data() {
        return {
            screenWidth: window.innerWidth,
            screenHeight: window.innerHeight,
            screenResized: null,
            sidebarOpened: null,
            adminDashboard: '',
            tugboat: '',
            schedulerDashboard: '',
            captainDashboard: '',
            workSchedule: '',
            settings: '',
        }
    },
    mounted(){
        this.updateSidebarBackground(this.$store.state.currentRoute);
    },
    created() {
        // Update screen size on window resize
        window.addEventListener('resize', this.handleResize);
        this.unsubscribe = this.$store.subscribe((mutation, state) => {
            if (mutation.type === 'setCurrentRoute') {
                this.updateSidebarBackground(state.currentRoute);
            }
        });
    },
    destroyed() {
        // Remove the event listener when the component is destroyed
        window.removeEventListener('resize', this.handleResize);
        this.unsubscribe();
    },
    methods: {
        resetNone(){
            this.adminDashboard = 'none';
            this.tugboat = 'none';
            this.schedulerDashboard = 'none';
            this.captainDashboard = 'none';
            this.workSchedule = 'none';
            this.settings = 'none';
        },
        updateSidebarBackground(path){
            let backgroundColor =  'rgb(136, 187, 252, 0.2)';
            this.resetNone();
            switch(path){
                case 'AdminDashboard':
                case 'NewStaff':
                    this.adminDashboard = backgroundColor;
                    break;
                case 'CaptainDashboard':
                    this.captainDashboard = backgroundColor;
                    break;
                case 'SchedulerDashboard':
                case 'NewTask':
                    this.schedulerDashboard = backgroundColor;
                    break;
                case 'TugBoatList':
                case 'NewTugBoat':
                    this.tugboat = backgroundColor;
                    break;
                case 'WorkSchedule':
                    this.workSchedule = backgroundColor;
                    break;
                case 'Settings':
                case 'ChangePassword':
                    this.settings = backgroundColor;
                    break;
            }
            this.$forceUpdate();
        },
        screen(){
            if(this.screenHeight > 380 && this.screenWidth > 820){
                this.sidebarOpened = true;
                return true;
            }
            return false;
        },
        closeButton(){
            if(this.screenHeight <= 380 || this.screenWidth <= 820){
                return true;
            }
        },
        handleResize() {
            // Update screen size on window resize
            this.screenWidth = window.innerWidth;
            this.screenHeight = window.innerHeight;
            if(this.screenHeight <= 380 || this.screenWidth <= 820){
                this.screenResized = true;
                this.sidebarOpened = false;
            }else{
                this.screenResized = false;
            }
        },
        openSidebar() {
            this.sidebarOpened = true;
        },
        closeSidebar() {
            this.sidebarOpened = false;
        }
    }
}
</script>

<style scoped>
.header {
    top: 0;
    z-index: -9999;
    position: absolute;
}

.header-image {
    height: 200px;
    width: 100vw;
    object-fit: cover;
    opacity: 0.8;
    /* filter: brightness(120%) grayscale(20%); */
    -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent);
        mask-image: linear-gradient(to bottom, black 60%, transparent);
}

.footer{
    height: 45px;
    background-color: linear-gradient(to top, transparent, black);
}

.text-center.p-3 {
    letter-spacing: 10px;
    color: lightgrey;
    font-size: 0.8em;
}

#Sidebar {
    z-index: 9999;
}

#close-sidebar {
    margin-left: 200px;
    padding: 10px;
    cursor: pointer;
    z-index: 99999;
    position: fixed;
    top: 0;
    border: none;
}

#open-sidebar {
    z-index: 9998;
    position: fixed;
    top: 0;
    left: 0;
    border: none;
}

#sidebar {
    top: 0;
    padding-top: 2em;
    z-index: 9999;
    width: 200px;
    background-color: white;
    box-shadow: 5px 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    position: fixed;
    height: 100%;
    color: black;
    overflow-x: hidden;
    overflow-y: hidden;
}

#Sidebar h2 {
    color: darkblue;
}

#Sidebar ul {
    list-style-type: none; /* Remove bullets */
    padding: 0;
    margin: 0;
}

#Sidebar li {
    font-size: var(--font-size);
    text-align: left;
    padding: 10px;
    cursor: pointer;
}

#Sidebar li:hover:not(#profile){
    background-color: lightgrey;
}

.sidebar-item {
    display: flex;
    align-items: center;
    padding: 10px;
    cursor: pointer;
}

.sidebar-bottom-section {
    position: absolute;
    bottom: 0; 
    width: 100%; 
}

.sidebar-icon {
    margin-right: 10px;
    height: 30px;
    width: 50px;
}

.sidebar-selected {
    position: absolute;
    border-radius: 5px;
    background-color: rgb(115, 176, 255);
}
</style>
