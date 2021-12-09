from django.shortcuts import render
from .models import Session

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


def home(request):
    context = {"days": days}
    return render(request, "scheduler/home.html", context)


def about(request):
    context = {"days": days}
    return render(request, "scheduler/about.html", context)


def sessions(request):
    context = {"sessions": Session.objects.all()}
    return render(request, "scheduler/sessions.html", context)


def report_issues(request):
    return render(request, "scheduler/report_issues.html")
