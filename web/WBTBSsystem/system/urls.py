from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/display_captain', views.CaptainViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("team/", views.detail, name="detail"),
    path("tugboat/", views.TugBoatDetail, name="TugBoatDetail"),
    path("schedule/", views.ScheduleDetail, name="ScheduleDetail"),
    path("captain/", views.CaptainDetail, name="CaptainDetail"),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('', include(router.urls)),
]