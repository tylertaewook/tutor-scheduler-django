import datetime

import pytest

from tutor_scheduler.scheduler.tests.factories import SessionFactory

pytestmark = pytest.mark.django_db


class TestSessionModel:
    def test_is_upcoming_with_future_date(self):
        """
        is_upcoming() returns True for sessions scheduled in the future
        """
        deltadays = 5
        future_session = SessionFactory(
            date=datetime.date.today() + datetime.timedelta(days=deltadays)
        )
        assert future_session.is_upcoming()

    def test_is_upcoming_with_past_date(self):
        """
        is_upcoming() returns False for sessions scheduled in the past
        """
        deltadays = -5
        past_session = SessionFactory(
            date=datetime.date.today() + datetime.timedelta(days=deltadays)
        )
        assert not past_session.is_upcoming()

    def test_get_weekday(self):
        weekday_session = SessionFactory()
        assert weekday_session.get_weekday == datetime.date.today().strftime("%A")

    def test_get_absolute_url(self):
        url_session = SessionFactory()
        assert url_session.get_absolute_url() == f"/sessions/{url_session.pk}/"
