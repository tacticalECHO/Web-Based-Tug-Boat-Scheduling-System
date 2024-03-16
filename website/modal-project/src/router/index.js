import { createRouter, createWebHashHistory } from 'vue-router'
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
import NewTask from '@/views/scheduler/NewTask.vue'
import TugBoatList from '@/views/scheduler/TugBoatList.vue'
import NewTugBoat from '@/views/scheduler/NewTugBoat.vue'
// captain--------------------------------------------------------------------
import CaptainDashboard from '@/views/captain/CaptainDashboard.vue'
import WorkSchedule from '@/views/captain/WorkSchedule.vue'



const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/admin',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAdmin: true },
    children: [
      {
        path: 'add-new-staff',
        name: 'NewStaff',
        component: NewStaff,
      },
    ]
  },
  {
    path: '/captain',
    name: 'CaptainDashboard',
    component: CaptainDashboard,
    meta: { requiresRoles: ['captain'] },
    meta: { requiresCap: true },
    children: [
      {
        path: 'message',
        name: 'CaptainMessage',
        component: Message,
      },
    ]
  },
  {
    path: '/scheduler',
    name: 'SchedulerDashboard',
    component: SchedulerDashboard,
    meta: { requiresSch: true },
    children: [
      {
        path: 'message',
        name: 'SchedulerMessage',
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
    path: '/tugboat-list',
    name: 'TugBoatList',
    component: TugBoatList,
    meta: { requiresSch: true },
    children: [
      {
        path: 'add-new-tugboat',
        name: 'NewTugBoat',
        component: NewTugBoat,
      },
    ]
  },
  {
    path: '/work-schedules',
    name: 'WorkSchedule',
    component: WorkSchedule,
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
    path: '/add-new-task',
    name: 'NewTask',
    component: NewTask,
    meta: { requiresSch: true },
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
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
});

 router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const username = localStorage.getItem('username');
  const roles = JSON.parse(localStorage.getItem('roles'));

  if (isLoggedIn) {
    if (store.state.username !== username) {
        store.commit('setUser', { username });
        store.commit('setUserRole', roles);
    }
  }

  if (!isLoggedIn && to.name !== 'Login') {
    next({ name: 'Login' });
  // } else if (to.meta.requiresAdmin && !roles.isAdmin || to.meta.requiresCap && !roles.isCaptain || to.meta.requiresSch && !roles.isScheduler) {
  //   alert('You do not have permission to view this page.');
  //   next(false);
  } else {
    next();
  }
 });


export default router;