import datetime

from tutor_scheduler.scheduler.models import Session


class CreateSession:
    def create(
        user,
        date_posted=datetime.datetime.now(),
        deltadays=0,
        timeblock="A",
        course_name="test",
        course_teacher="test",
        helptype="test",
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
