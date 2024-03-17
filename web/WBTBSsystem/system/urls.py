from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

router = DefaultRouter()
router.register(r'api/display_captain', views.CaptainViewSet)
router.register(r'api/display_task', views.TaskViewSet, basename='task')
router.register(r'api/display_scheduler', views.SchedulerViewSet)
router.register(r'api/display_berth', views.BerthViewSet)
router.register(r'api/display_container_boat', views.ContainerBoatViewSet)
router.register(r'api/display_schedule_entry', views.ScheduleEntryViewSet, basename='scheduleEntry')
router.register(r'api/display_tugboat', views.TugBoatViewSet, basename='tugboat')

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change_password'),

    path('api/tasks-delete/', views.DeleteTasksView.as_view(), name='delete_tasks'),
    path('api/scheduleentries-delete/', views.DeleteScheduleEntriesView.as_view(), name='delete_scheduleentries'),

    path('api/captains-delete/', views.DeleteCaptainsView.as_view(), name='delete_captains'),
    path('api/schedulers-delete/', views.DeleteSchedulersView.as_view(), name='delete_schedulers'),
    path('api/tugboat-delete/', views.DeleteTugBoatView.as_view(), name='delete_tugboats'),
    path('api/create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('api/save-newtask/', views.SaveNewTaskView.as_view(), name='save_newtask'),
    path('api/upload-task-data', views.upload_task_data, name='upload_task_data'),
    path('api/upload-tug-boat-data', views.upload_tug_boat_data, name='upload_tug_boat_data'),
    path('api/publish-data', views.publish_data, name='publish_data'),
    path('api/download-captain', views.download_captain, name='download_captain'),
    path('api/update-schedule-entry', views.UpdateScheduleEntryView.as_view(), name='update_schedule_entry'),
    path('api/manual-schedule/', views.ManualScheduleView.as_view(), name='manual_schedule'),
    path('api/update-tugboat/', views.UpdateTugBoatView.as_view(), name='update_tugboat'),
    path('api/api/update-publish-time', views.PublishView.as_view(), name='update-publish-time'),
    path('', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)