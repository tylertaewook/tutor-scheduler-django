from django.urls import path, register_converter
from datetime import datetime
from . import views
from .views import (
    SessionListView,
    SessionDetailView,
    SessionCreateView,
    SessionEditView,
    SessionCancelView,
)


class DateConverter:
    regex = "\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value


register_converter(DateConverter, "yyyy")

urlpatterns = [
    path("", views.home, name="scheduler-home"),
    path("about/", views.about, name="scheduler-about"),
    path("sessions/", SessionListView.as_view(), name="scheduler-sessions"),
    path("sessions/<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
    path("sessions/new/", SessionCreateView.as_view(), name="session-create"),
    path(
        "sessions/new/<yyyy:date>/",
        SessionCreateView.as_view(),
        name="session-create-date",
    ),
    path(
        "sessions/new/<yyyy:date>/<str:timeblock>",
        SessionCreateView.as_view(),
        name="session-create-spec",
    ),
    path("sessions/<int:pk>/edit", SessionEditView.as_view(), name="session-edit"),
    path(
        "sessions/<int:pk>/cancel", SessionCancelView.as_view(), name="session-cancel"
    ),
    path("issues/", views.report_issues, name="scheduler-issues"),
]

