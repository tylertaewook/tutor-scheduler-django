from django import forms
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)

TIME_BLOCK = (
    ("A", "8:00-8:20"),
    ("B", "8:20-8:40"),
    ("C", "8:40-9:00"),
    ("D", "9:00-9:20"),
    ("E", "9:20-9:40"),
    ("F", "9:40-10:00"),
)


class Session(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    date = models.DateField(default=datetime.now)
    timeblock = models.CharField(max_length=1, choices=TIME_BLOCK)

    helptype = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    expertise = models.CharField(max_length=100)
    assigned_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.name


class Issue(models.Model):
    email = models.EmailField()
    issue = models.TextField()
    user_agent = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    # dunder STR
    def __str__(self):
        return self.email
