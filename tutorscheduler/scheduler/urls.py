from django.urls import path
from . import views
from .views import (
    SessionListView,
    SessionDetailView,
    SessionCreateView,
    SessionEditView,
    SessionCancelView,
)

urlpatterns = [
    path("", views.home, name="scheduler-home"),
    path("about/", views.about, name="scheduler-about"),
    path("sessions/", SessionListView.as_view(), name="scheduler-sessions"),
    path("sessions/<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
    path("sessions/new/", SessionCreateView.as_view(), name="session-create"),
    path("sessions/<int:pk>/edit", SessionEditView.as_view(), name="session-edit"),
    path(
        "sessions/<int:pk>/cancel", SessionCancelView.as_view(), name="session-cancel"
    ),
    path("issues/", views.report_issues, name="scheduler-issues"),
]

