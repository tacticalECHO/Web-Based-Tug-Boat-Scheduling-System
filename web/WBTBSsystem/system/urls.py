from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("team/", views.detail, name="detail"),
    path("tugboat/", views.TugBoatDetail, name="TugBoatDetail"),
    path("schedule/", views.ScheduleDetail, name="ScheduleDetail"),
    path("captain/", views.CaptainDetail, name="CaptainDetail")
]