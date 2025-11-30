from django.urls import path

from app.pages.views import PageDetailView

app_name = "pages"

urlpatterns = [
    path("<slug:slug>/", PageDetailView.as_view(), name="detail"),
]
