from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/display_captain', views.CaptainViewSet)
router.register('api/display_task', views.TaskViewSet)

urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('', include(router.urls)),
]