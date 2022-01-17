from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Tutor Scheduler."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("firstname"), blank=True, max_length=255)  # type: ignore
    last_name = CharField(_("lastname"), blank=True, max_length=255)  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Teacher(models.Model):
    WEEKDAY_CHOICES = (
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
    )

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)
    assigned_day = models.CharField(
        max_length=10, choices=WEEKDAY_CHOICES, default="MONDAY"
    )

    def __str__(self):
        return self.assigned_day

    def get_name(self):
        return self.teacher.first_name + " " + self.teacher.last_name
