<template>
    <div id="Sidebar">
        <h2>Ningbo Harbour</h2>
            <ul>
                <li @click="redirect('AdminDashboard')" id="admin-dashboard" class="sidebar-item">
                  <font-awesome-icon :icon="['fat', 'folder']" class="sidebar-icon"/>
                    A-Dashboard
                </li>
                <li @click="redirect('SchedulerDashboard')" id="scheduler-dashboard" class="sidebar-item">
                  <font-awesome-icon :icon="['fat', 'folder']" class="sidebar-icon"/>
                    S-Dashboard
                </li>
                <li @click="redirect('CaptainDashboard')" id="captain-dashboard" class="sidebar-item">
                  <font-awesome-icon :icon="['fat', 'folder']" class="sidebar-icon"/>
                    C-Dashboard
                </li>
                <li @click="redirect('WorkSchedule')" class="sidebar-item">
                    <img src="#.png" alt="" class="sidebar-icon">
                    Work Schedules
                </li>
                <li @click="redirect('TaskManager')" class="sidebar-item">
                    <img src="#.png" alt="" class="sidebar-icon">
                    Task Manager
                </li>
            </ul>

            <div class="sidebar-bottom-section">
                <ul>
                    <li @click="redirect('Settings')" class="sidebar-item">
                        <img src="#.png" alt="" class="sidebar-icon">
                        Settings
                    </li>
                    <li @click="redirect('Profile')" class="sidebar-item">
                        <img src="#.png" alt="" class="sidebar-icon">
                        {{profile_name}}
                    </li>
                </ul>
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'SideBar',
    data() {
        return {
          profile_name: 'Name',
        }
    },
    methods: {
        // redirect(event){
        //     this.$router.push({name: event});
        // }
    }
}
</script>

<style scoped>
#Sidebar {
    text-align: center;
    margin-top: 0px;
    width: 200px;
    position: fixed;
    height: 100%;
    background-color: white;
    color: black;
    border-right: 1px solid grey;
    top: 0;
    left: 0;
    overflow-x: hidden;
    overflow-y: hidden;
    transition: .5s;
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
    margin-top: 170%;
}

.sidebar-icon {
    margin-right: 10px;
    height: 30px;
    width: 50px;
}
</style>
