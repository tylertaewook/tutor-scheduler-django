from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from tutor_scheduler.scheduler.models import Session

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # TODO: get user object
    # user = request.user
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context[
            "user_group"
        ] = "Student"  # "Teacher" if user.groups.filter(name="teacher") else "Student",
        context[
            "user_sessions"
        ] = Session.objects.all()  # Session.objects.filter(student=user)
        context["teacher_sessions"] = Session.objects.all()
        return context


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


# @login_required
# def profile(request):
#     user = request.user
#     context = {
#         "user_group": "Teacher" if user.groups.filter(name="teacher") else "Student",
#         "user_sessions": Session.objects.filter(student=user),
#         "teacher": "",
#         "teacher_sessions": Session.objects.all(),
#     }
#     return render(request, "users/profile.html", context)
