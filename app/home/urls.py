from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("schedule/", views.ScheduleView.as_view(), name="schedule"),
    path("volunteers/", views.VolunteersView.as_view(), name="volunteers"),
]
