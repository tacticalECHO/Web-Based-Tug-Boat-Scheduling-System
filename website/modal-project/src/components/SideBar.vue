<template>
    <div id="Sidebar">
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
                <li v-if="isCaptain || isAdmin" @click="redirect('CaptainDashboard')" id="captain-dashboard" class="sidebar-item">
                    <admin-panel v-if="isCaptain" />
                  <font-awesome-icon :icon="['fas', 'display']" class="sidebar-icon"/>
                    C-Dashboard
                </li>
                <li v-if="isScheduler || isAdmin" @click="redirect('WorkSchedule')" class="sidebar-item">
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
    
</template>

<script>
import { mapState } from 'vuex';
// @method_decorator(csrf_exempt, name='dispatch')
// class EditTaskView(View):
//     def post(self, request, *args, **kwargs):
//         data = json.loads(request.body)
//         taskId = data.get('taskId')
//         requiredTugBoat = data.get('requiredTugBoat')
//         startTime = data.get('startTime')
//         endTime = data.get('startTime')
//         containerBoatID = data.get('containerBoatId')
//         action = data.get('action')
//         berthId = data.get('berthId')
//         state = data.get('state')
        
//         try:
//             task = Task.objects.get(TaskId = taskId)
//             task.set_password(new_password)
//             task.save()
//             return JsonResponse({'success': True})
//         except User.DoesNotExist:
//             return JsonResponse({'success': False}, status=401)

export default {
    name: 'SideBar',
    computed: {
        ...mapState(['username', 'isCaptain', 'isAdmin', 'isScheduler']),
        profile_name() {
            return this.username || 'Guest';
        }
    },
    methods: {

        // //control the availibility of sidebar based on screen size
        // openNav(x) {
        //     document.getElementById("Sidebar").style.display="block";
        //     if(x.matches){
        //         document.getElementById("close_button").style.display="none";
        //     }
        //     else{
        //         document.getElementById("close_button").style.display="block";
        //     }
        // },
        // //close the sidebar
        // closeNav() {
        //     document.getElementById("Sidebar").style.display="";
        //     document.getElementById("close_button").style.display="";
        // }
    }
}
</script>

<style scoped>
#Sidebar {
    z-index: 9999;
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
