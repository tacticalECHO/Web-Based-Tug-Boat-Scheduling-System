from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/display_captain', views.CaptainViewSet)
router.register(r'api/display_task', views.TaskViewSet)
router.register(r'api/display_scheduler', views.SchedulerViewSet)
router.register(r'api/display_berth', views.BerthViewSet)
router.register(r'api/display_container_boat', views.ContainerBoatViewSet)

urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('api/captains-delete/', views.DeleteCaptainsView.as_view(), name='delete_captains'),
    path('api/schedulers-delete/', views.DeleteSchedulersView.as_view(), name='delete_schedulers'),
    path('api/create-user/', views.CreateUserView.as_view(), name='create_user'),
    path('api/save-task/', views.SaveTaskView.as_view(), name='save_task'),
    path('api/save-containerboat/', views.SaveContainerBoatView.as_view(), name='save_container_boat'),
    path('', include(router.urls)),
]