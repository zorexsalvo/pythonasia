from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("code-of-conduct/", views.CodeOfConductView.as_view(), name="code-of-conduct"),
    path("partnership/", views.PartnershipView.as_view(), name="partnership"),
    path("travel-info/", views.TravelInfoView.as_view(), name="travel-info"),
    path("aid-scholarships/", views.AidScholarshipsView.as_view(), name="aid-scholarships"),
    path("covid-policy/", views.CovidPolicyView.as_view(), name="covid-policy"),
    path("data-privacy/", views.DataPrivacyView.as_view(), name="data-privacy"),
    path("everyone-who-can-pays/", views.EveryoneWhoCanPaysView.as_view(), name="everyone-who-can-pays"),
    path("patron-acknowledgment/", views.PatronAcknowledgmentView.as_view(), name="patron-acknowledgment"),
    path("schedule/", views.ScheduleView.as_view(), name="schedule"),
    path("volunteers/", views.VolunteersView.as_view(), name="volunteers"),
]
