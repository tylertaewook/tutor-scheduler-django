import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

from .models import Session


class SessionModelTests(TestCase):
    def setUp(self):
        self.password = "mypassword"
        self.my_user = User.objects.create_user(
            "myuser2", "user@test.com", self.password
        )

    def test_is_upcoming_with_future_date(self):
        """
        is_upcoming() returns True for sessions scheduled in the future
        """
        # self.user = User.objects.create_user(username="testuser", password="12345")
        # self.client.login(username=my_user.username, password=password)

        deltadays = 5
        future_session = create_session(user=self.my_user, deltadays=deltadays)
        self.assertIs(future_session.is_upcoming(), True)

    def test_is_upcoming_with_past_date(self):
        """
        is_upcoming() returns False for sessions scheduled in the past
        """
        deltadays = -5
        past_session = create_session(user=self.my_user, deltadays=deltadays)
        self.assertIs(past_session.is_upcoming(), False)


def create_session(
    user,
    date_posted=timezone.now(),
    deltadays=0,
    timeblock="A",
    course_name="",
    course_teacher="",
    helptype="",
):
    """
    Create a session with the given parameters and scheduled to the
    given number of `days` offset to now (negative for sessions scheduled for
    the past, positive for sessions that have future schedule date).
    """
    date = datetime.datetime.now().date() + datetime.timedelta(days=deltadays)
    return Session.objects.create(
        student=user,
        date_posted=date_posted,
        date=date,
        timeblock=timeblock,
        course_name=course_name,
        course_teacher=course_teacher,
        helptype=helptype,
    )
