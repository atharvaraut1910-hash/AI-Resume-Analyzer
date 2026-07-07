from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload_resume, name="upload"),
    path("history/", views.history, name="history"),

    path(
        "download/<int:id>/",
        views.download_report,
        name="download_report",
    ),
]