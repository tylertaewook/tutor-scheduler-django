# import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import IssuesForm, SessionForm
from .models import Session

days = [
    {
        "day": "Monday",
        "date": "2022-01-10",
        "onduty": "Mr. Brett Hand",
        "dept": "English",
        "desc": "English/History term papers",
    },
    {
        "day": "Tuesday",
        "date": "2022-01-11",
        "onduty": "Ms. Reagan Ridley",
        "dept": "Physics",
        "desc": "Physics Lab reports",
    },
    {
        "day": "Wednesday",
        "date": "2022-01-12",
        "onduty": "Dr. Andre Lee",
        "dept": "Chemistry",
        "desc": "Chemistry Lab reports",
    },
    {
        "day": "Thursday",
        "date": "2022-01-13",
        "onduty": "Mr. Magic Myc",
        "dept": "English",
        "desc": "English essays",
    },
    {
        "day": "Friday",
        "date": "2022-01-14",
        "onduty": "Mr. Glenn Dolphman",
        "dept": "History",
        "desc": "History essays",
    },
]


class SessionListView(ListView):
    model = Session
    template_name = "scheduler/sessions.html"  # <app>/<model>_<view_type>.html
    context_object_name = "sessions"
    ordering = ["-date"]


# saving code by following conventions
class SessionDetailView(DetailView):
    model = Session


# note: mixins should come before CreateView
class SessionCreateView(LoginRequiredMixin, CreateView):
    # model = Session
    # fields = ["date", "timeblock", "course_name", "course_teacher", "helptype"]
    form_class = SessionForm
    template_name = "scheduler/session_form.html"
    success_url = "/profile"

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }

    # def get_form_kwargs(self, *args, **kwargs):  # forms.py def clean()
    #     kwargs = super(SessionCreateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs["user"] = self.request.user
    #     return kwargs


class SessionEditView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = Session
    fields = ["course_name", "course_teacher", "helptype"]
    success_url = "/profile"
    success_message = "Session was updated successfully"

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        session = self.get_object()
        if self.request.user == session.student:
            return True
        return False


class SessionCancelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Session
    success_url = "/profile"

    def test_func(self):
        session = self.get_object()
        if self.request.user == session.student:
            return True
        return False


def home(request):
    context = {"days": days}
    return render(request, "scheduler/home.html", context)


def about(request):
    return render(request, "scheduler/about.html")


def sessions(request):
    context = {"sessions": Session.objects.all()}
    return render(request, "scheduler/sessions.html", context)


def report_issues(request):
    if request.method == "POST":
        form = IssuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully reported issue!")
            return redirect("scheduler-home")
    else:  # displays empty form initially
        form = IssuesForm()

    return render(request, "scheduler/report_issues.html", {"form": form})
