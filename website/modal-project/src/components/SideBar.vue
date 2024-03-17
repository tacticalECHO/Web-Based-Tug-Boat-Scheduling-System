<template>
    <div id="Sidebar"> 
        <div class="header">
            <img src="../assets/header.jpg" class="header-image">
        </div>
        <div v-if="screen() || sidebarOpened" id="sidebar">
            <h2>Ningbo Harbour</h2>
            <ul>
                <li v-if="isAdmin ||isScheduler" @click="redirect('AdminDashboard')" id="admin-dashboard" class="sidebar-item" :style="{ backgroundColor: adminDashboard }">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    A-Dashboard
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('SchedulerDashboard')" id="scheduler-dashboard" class="sidebar-item" :style="{ backgroundColor: schedulerDashboard }">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    S-Dashboard
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('TugBoatList')" id="scheduler-dashboard" class="sidebar-item" :style="{ backgroundColor: tugboat}">
                    <font-awesome-icon :icon="['fas', 'ship']" class="sidebar-icon"/>
                    Tug Boats
                </li>
                <li v-if="isCaptain || isScheduler || isAdmin" @click="redirect('CaptainDashboard')" id="captain-dashboard" class="sidebar-item" :style="{ backgroundColor: captainDashboard }">
                    <admin-panel v-if="isCaptain" />
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    C-Dashboard
                </li>
                <li v-if="isScheduler || isCaptain|| isAdmin" @click="redirect('WorkSchedule')" class="sidebar-item" :style="{ backgroundColor: workSchedule }">
                    <font-awesome-icon :icon="['fas', 'calendar-days']" class="sidebar-icon"/>
                    Work Schedules
                </li>
            </ul>

            <div class="sidebar-bottom-section">
                <ul>
                    <li @click="redirect('Settings')" class="sidebar-item" :style="{ backgroundColor: settings }">
                        <font-awesome-icon :icon="['fas', 'gear']" class="sidebar-icon"/>
                        Settings
                    </li>
                    <li class="sidebar-item">
                        <font-awesome-icon :icon="['fas', 'user']" class="sidebar-icon"/>
                        {{profile_name}}
                    </li>
                </ul>
            </div>
        </div>
        <button class="btn btn-outline-dark" @click="openSidebar()" v-if="!screen()" id="open-sidebar"><font-awesome-icon :icon="['fas', 'forward']" /></button>
        <button class="btn btn-outline-dark" @click="closeSidebar()" v-if="sidebarOpened && closeButton()" id="close-sidebar"><font-awesome-icon :icon="['fas', 'backward']" /></button>
        <footer class="footer fixed-bottom">
            <div class="text-center p-3">
                NINGBO HARBOUR
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
        },
        updateSidebarBackground(path){
            switch(path){
                case 'AdminDashboard':
                case 'NewStaff':
                    this.adminDashboard = 'lightgrey';
                    console.log("Admin: "+path + this.adminDashboard)
                    break;
                case 'CaptainDashboard':
                    this.captainDashboard = 'lightgrey';
                    break;
                case 'SchedulerDashboard':
                case 'NewTask':
                    this.schedulerDashboard = 'lightgrey';
                    break;
                case 'TugBoatList':
                case 'NewTugBoat':
                    this.tugboat = 'lightgrey';
                    console.log("Tugboat: "+path + this.tugboat)
                    break;
                case 'WorkSchedule':
                    this.workSchedule = 'lightgrey';
                    break;
                case 'Settings':
                case 'ChangePassword':
                    this.settings = 'lightgrey';
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
}

#open-sidebar {
    z-index: 9998;
    position: fixed;
    top: 0;
    left: 0;
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
</style>
