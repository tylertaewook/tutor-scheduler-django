from django import forms
from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Teacher

# REF: READ https://docs.djangoproject.com/en/4.0/topics/db/models/
class DayBlock(models.Model):
    date = models.DateField(default=timezone.now)


# TODO: experiment with this instead
class Session(models.Model):

    TIMEBLOCK_CHOICES = (
        ("A", "8:00-8:20"),
        ("B", "8:20-8:40"),
        ("C", "8:40-9:00"),
        ("D", "9:00-9:20"),
        ("E", "9:20-9:40"),
        ("F", "9:40-10:00"),
    )

    WEEKDAY_CHOICES = (
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    weekday = models.CharField(max_length=10, choices=WEEKDAY_CHOICES, default="MONDAY")
    timeblock = models.CharField(max_length=10, choices=TIMEBLOCK_CHOICES, default="A")
    helptype = models.CharField(max_length=50)
    # TODO: whether to include these fields or not?
    # course_name = models.CharField(max_length=30)
    # course_teacher = models.CharField(max_length=30)

    @property
    def is_upcoming(self):
        return date.today() <= self.date

    @property
    def get_weekday(self):
        return self.date.strftime("%A")

    def __str__(self) -> str:
        return f"{self.student.username}: {self.date} ({self.timeblock})"

    def get_absolute_url(self):
        # returns a complete url string and let view handle the redirect
        return reverse("session-detail", kwargs={"pk": self.pk})


class Issue(models.Model):
    email = models.EmailField()
    issue = models.TextField()
    user_agent = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    # dunder STR
    def __str__(self):
        return self.email
