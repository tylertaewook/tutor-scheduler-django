from django.shortcuts import render, redirect
from .models import Session, DayBlock
from datetime import datetime
from .forms import IssuesForm, SessionForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

days = [
    {
        "day": "Monday",
        "onduty": "Mr. Brett Hand",
        "dept": "English",
        "desc": "English/History term papers",
    },
    {
        "day": "Tuesday",
        "onduty": "Ms. Reagan Ridley",
        "dept": "Physics",
        "desc": "Physics Lab reports",
    },
    {
        "day": "Wednesday",
        "onduty": "Dr. Andre Lee",
        "dept": "Chemistry",
        "desc": "Chemistry Lab reports",
    },
    {
        "day": "Thursday",
        "onduty": "Mr. Magic Myc",
        "dept": "English",
        "desc": "English essays",
    },
    {
        "day": "Friday",
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

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }


class SessionEditView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = Session
    fields = ["helptype"]
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


class SessionCancelView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = Session
    success_url = "/profile"
    success_message = "Session was cancelled successfully"
    # FIXME: success message not showing - eh maybe not necessary tho

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
            messages.success(request, f"Successfully reported issue!")
            return redirect("scheduler-home")
    else:  # displays empty form initially
        form = IssuesForm()

    return render(request, "scheduler/report_issues.html", {"form": form})
