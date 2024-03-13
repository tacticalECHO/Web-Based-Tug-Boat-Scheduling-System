<template>
    <div id="Sidebar"> 
        <div v-if="screen() || sidebarOpened" id="sidebar">
            <h2>Ningbo Harbour</h2>
            <ul>
                <li v-if="isAdmin" @click="redirect('AdminDashboard')" id="admin-dashboard" class="sidebar-item">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    A-Dashboard
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('SchedulerDashboard')" id="scheduler-dashboard" class="sidebar-item">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    S-Dashboard
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('TugBoatList')" id="scheduler-dashboard" class="sidebar-item">
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    Tug Boats
                </li>
                <li v-if="isCaptain || isAdmin" @click="redirect('CaptainDashboard')" id="captain-dashboard" class="sidebar-item">
                    <admin-panel v-if="isCaptain" />
                <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    C-Dashboard
                </li>
                <li v-if="isScheduler || isAdmin || isCaptain" @click="redirect('WorkSchedule')" class="sidebar-item">
                    <font-awesome-icon :icon="['fas', 'calendar-days']" class="sidebar-icon"/>
                    Work Schedules
                </li>
            </ul>

            <div class="sidebar-bottom-section">
                <ul>
                    <li @click="redirect('Settings')" class="sidebar-item">
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
        <button class="blue-border-button" @click="openSidebar()" v-if="!screen()" id="open-sidebar"><font-awesome-icon :icon="['fas', 'forward']" /></button>
        <button class="blue-border-button" @click="closeSidebar()" v-if="sidebarOpened && closeButton()" id="close-sidebar"><font-awesome-icon :icon="['fas', 'backward']" /></button>
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
        }
    },
    created() {
        // Update screen size on window resize
        window.addEventListener('resize', this.handleResize);
    },
    destroyed() {
        // Remove the event listener when the component is destroyed
        window.removeEventListener('resize', this.handleResize);
    },
    methods: {
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
#Sidebar {
    top: 0;
    z-index: 9999;
}

#close-sidebar {
    margin-left: 195px;
    padding: 10px;
    cursor: pointer;
    z-index: 99999;
    position: fixed;
}

#open-sidebar {
    z-index: 9998;
    position: fixed;
}

#sidebar {
    z-index: 9999;
    width: 200px;
    background-color: white;
    border-right: 1px solid grey;
    text-align: center;
    margin-top: 0px;
    position: fixed;
    height: 100%;
    color: black;
    top: 0;
    left: 0;
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
