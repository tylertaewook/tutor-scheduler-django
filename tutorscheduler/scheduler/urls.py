from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="scheduler-home"),
    path("about/", views.about, name="scheduler-about"),
    path("sessions/", views.sessions, name="scheduler-sessions"),
    path("issues/", views.report_issues, name="scheduler-issues"),
]
