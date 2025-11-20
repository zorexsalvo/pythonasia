from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("code-of-conduct/", views.CodeOfConductView.as_view(), name="code-of-conduct"),
    path("partnership/", views.PartnershipView.as_view(), name="partnership"),
    path("travel-info/", views.TravelInfoView.as_view(), name="travel-info"),
    path("aid-scholarships/", views.AidScholarshipsView.as_view(), name="aid-scholarships"),
]
