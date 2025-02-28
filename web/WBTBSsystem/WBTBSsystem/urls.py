"""
URL configuration for WBTBSsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from system.views import (
    DeleteScheduleEntriesView,
    DeleteTasksView,
    LoginView,
    ChangePasswordView,
    CaptainViewSet,
    TaskViewSet,
    SchedulerViewSet,
    DeleteSchedulersView,
    DeleteCaptainsView,
    CreateUserView,
    ContainerBoatViewSet,
    BerthViewSet,
    SaveNewTaskView,
    ScheduleEntryViewSet,
    upload_task_data,
    upload_tug_boat_data,
    publish_data,
    download_captain,
    TugBoatViewSet,
    UpdateScheduleEntryView,
    UpdateEntryAndTaskView,
    AutoScheduleView,
    ManualScheduleView,
    UpdateTugBoatView,
    PublishView,
    DeleteTugBoatView,
    TugBoatRescheduleView,
    AutoRescheduleView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/display_captain', CaptainViewSet)
router.register(r'api/display_task', TaskViewSet, basename='task')
router.register(r'api/display_scheduler', SchedulerViewSet)
router.register(r'api/display_berth', BerthViewSet)
router.register(r'api/display_container_boat', ContainerBoatViewSet)
router.register(r'api/display_schedule_entry', ScheduleEntryViewSet, basename='scheduleEntry')
router.register(r'api/display_tugboat', TugBoatViewSet, basename='tugboat')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    #path("system/", include("system.urls")),
    #path("team/", include("system.urls"))
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('api/captains-delete/', DeleteCaptainsView.as_view(), name='delete_captains'),

    path('api/tasks-delete/', DeleteTasksView.as_view(), name='delete_tasks'),
    path('api/scheduleentries-delete/', DeleteScheduleEntriesView.as_view(), name='delete_scheduleentries'),

    path('api/tugboat-delete/', DeleteTugBoatView.as_view(), name='delete_tugboats'),
    path('api/schedulers-delete/', DeleteSchedulersView.as_view(), name='delete_schedulers'),
    path('api/create-user/', CreateUserView.as_view(), name='create_user'),
    path('api/save-newtask/', SaveNewTaskView.as_view(), name='save_newtask'),
    path('api/upload-task-data', upload_task_data, name='upload_task_data'),
    path('api/upload-tug-boat-data', upload_tug_boat_data, name='upload_tug_boat_data'),
    path('api/publish-data', publish_data, name='publish_data'),
    path('api/download-captain', download_captain, name='download_captain'),
    path('api/update-schedule-entry', UpdateScheduleEntryView.as_view(), name='update_schedule_entry'),
    path('api/update-entry-task/', UpdateEntryAndTaskView.as_view(), name="update_entry_task"),
    path('api/auto-schedule', AutoScheduleView.as_view(), name='auto_schedule'),
    path('api/manual-schedule/', ManualScheduleView.as_view(), name='manual_schedule'),
    path('api/update-tugboat/', UpdateTugBoatView.as_view(), name='update_tugboat'),
    path('api/update-publish-time', PublishView.as_view(), name='update-publish-time'),
    path('api/tugboat-reschedule/', TugBoatRescheduleView.as_view(), name='tugboat_reschedule'),
    path('api/auto-reschedule/', AutoRescheduleView.as_view(), name='auto_reschedule'),
    path('', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
