from datetime import date

# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Session(models.Model):

    TIMEBLOCK_CHOICES = (
        ("A", "8:00-8:20"),
        ("B", "8:20-8:40"),
        ("C", "8:40-9:00"),
        ("D", "9:00-9:20"),
        ("E", "9:20-9:40"),
        ("F", "9:40-10:00"),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    timeblock = models.CharField(max_length=10, choices=TIMEBLOCK_CHOICES, default="A")

    course_name = models.CharField(max_length=30, default="")
    course_teacher = models.CharField(max_length=30, default="")
    helptype = models.CharField(max_length=50, default="")

    # @property
    def is_upcoming(self):
        return date.today() <= self.date

    is_upcoming.admin_order_field = "date"
    is_upcoming.boolean = True
    is_upcoming.short_description = "Session in the future?"

    @property
    def get_weekday(self):
        return self.date.strftime("%A")

    def __str__(self) -> str:
        return f"{self.student.username}: {self.date} ({self.timeblock})"

    def get_absolute_url(self):
        # returns a complete url string and let view handle the redirect
        return reverse("session-detail", kwargs={"pk": self.pk})


# REF: READ https://docs.djangoproject.com/en/4.0/topics/db/models/
class DayBlock(models.Model):
    date = models.DateField(default=timezone.now)
    # onduty = models.OneToOneField(Teacher, on_delete=models.CASCADE, default="")
    # allBlocks = Session.objects.filter(date=date)
    # blockA = allBlocks.filter(timeblo)
    # blockB = models.OneToOneField(Teacher, on_delete=models.CASCADE, default='')
    # blockC = models.OneToOneField(Teacher, on_delete=models.CASCADE, default='')
    # blockD = models.OneToOneField(Teacher, on_delete=models.CASCADE, default='')
    # blockE = models.OneToOneField(Teacher, on_delete=models.CASCADE, default='')
    # blockF = models.OneToOneField(Teacher, on_delete=models.CASCADE, default='')


class Issue(models.Model):
    email = models.EmailField()
    issue = models.TextField()
    user_agent = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    # dunder STR
    def __str__(self):
        return self.email
