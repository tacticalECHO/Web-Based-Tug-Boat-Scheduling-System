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
from system.views import LoginView, ChangePasswordView, CaptainViewSet, SchedulerViewSet, DeleteSchedulersView, DeleteCaptainsView, CreateUserView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api/display_captain', CaptainViewSet)
router.register(r'api/display_scheduler', SchedulerViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("system/", include("system.urls")),
    #path("team/", include("system.urls"))
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('api/captains-delete/', DeleteCaptainsView.as_view(), name='delete_captains'),
    path('api/schedulers-delete/', DeleteSchedulersView.as_view(), name='delete_schedulers'),
    path('api/create-user/', CreateUserView.as_view(), name='create_user'),
    path('', include(router.urls)),
]
