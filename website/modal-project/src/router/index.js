import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
// components-----------------------------------------------------------------
import ExitNotice from '@/components/ExitNotice.vue'
import RescheduleNotice from '@/components/RescheduleNotice.vue'
import ConflictNotice from '@/components/ConflictNotice.vue'
import AutoReschedule from '@/components/AutoReschedule.vue'
import Message from '@/components/Message.vue'
import MessageDetails from '@/components/MessageDetails.vue'
// general--------------------------------------------------------------------
import Login from '@/views/Login.vue'
import Settings from '@/views/Settings.vue'
import ChangePassword from '@/views/ChangePassword.vue'
// admin----------------------------------------------------------------------
import AdminDashboard from '@/views/administrator/AdminDashboard.vue'
import NewStaff from '@/views/administrator/NewStaff.vue'
// scheduler------------------------------------------------------------------
import SchedulerDashboard from '@/views/scheduler/SchedulerDashboard.vue'
import WorkSchedule from '@/views/scheduler/WorkSchedule.vue'
import TaskManager from '@/views/scheduler/TaskManager.vue'
import NewTask from '@/views/scheduler/NewTask.vue'
import ManualReschedule from '@/views/scheduler/ManualReschedule.vue'
import ConflictScheduleList from '@/views/scheduler/ConflictScheduleList.vue'
// captain--------------------------------------------------------------------
import CaptainDashboard from '@/views/captain/CaptainDashboard.vue'



const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/dashboard',
    name: 'AdminDashboard',
    component: AdminDashboard,
    children: [
      {
        path: 'add-new-staff',
        name: 'NewStaff',
        component: NewStaff,
      },
    ]
  },
  {
    path: '/dashboard',
    name: 'CaptainDashboard',
    component: CaptainDashboard,
  },
  {
    path: '/dashboard',
    name: 'SchedulerDashboard',
    component: SchedulerDashboard,
    children: [
      {
        path: 'message',
        name: 'Message',
        component: Message,
      },
      {
        path: 'message-details', //can change to id later
        name: 'MessageDetails',
        component: MessageDetails,
      },
      {
        path: 'auto-reschedule',
        name: 'AutoReschedule',
        component: AutoReschedule,
      },
    ]
  },
  {
    path: '/manual-reschedule',
    name: 'ManualReschedule',
    component: ManualReschedule,
    children: [
      {
        path: 'notice',
        name: 'Exit-ManualReschedule',
        component: ExitNotice,
      },
      {
        path: 'notice',
        name: 'Save-ManualReschedule',
        component: ConflictNotice,
      }
    ]
  },
  {
    path: '/work-schedules',
    name: 'WorkSchedule',
    component: WorkSchedule,
  },
  {
    path: '/conflict-schedule-list',
    name: 'ConflictScheduleList',
    component: ConflictScheduleList,
  },
  {
    path: '/task-manager',
    name: 'TaskManager',
    component: TaskManager,
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings,
  },
  {
    path: '/settings/change-password',
    name: 'ChangePassword',
    component: ChangePassword,
    children: [
      {
        path: 'notice',
        name: 'Exit-ChangePassword',
        component: ExitNotice,
      }
    ]
  },
  {
    path: '/task-manager/add-new-task',
    name: 'NewTask',
    component: NewTask,
    children: [
      {
        path: 'notice',
        name: 'Exit-NewTask',
        component: ExitNotice,
      },
      {
        path: 'notice',
        name: 'Save-NewTask',
        component: RescheduleNotice,
      }]
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = store.state.username !== '';

//   if (!isLoggedIn && to.name !== 'Login') {
//     next({ name: 'Login' });
//   } else {
//     next();
//   }
// });


export default router;