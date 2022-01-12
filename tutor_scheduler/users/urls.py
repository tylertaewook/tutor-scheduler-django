from django.contrib.auth import views as auth_views
from django.urls import path

from tutor_scheduler.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from . import views as user_views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile, name="profile"),
    # ! seems like ~update/ will replace this path
    # path("edit-profile/", user_views.editprofile, name="editprofile"),
]
