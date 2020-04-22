import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        datetime_published is in the future.
        """

        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(datetime_published=future_time)
        self.assertIs(future_question.was_published_recently(), False)

        return

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        datetime_published is within 1 day.
        """

        recent_time = timezone.now() - datetime.timedelta(
            hours=23,
            minutes=50,
            seconds=59,
        )
        recent_question = Question(datetime_published=recent_time)
        self.assertIs(recent_question.was_published_recently(), True)

        return

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return True for questions whose
        datetime_published is older than 1 day.
        """

        old_time = timezone.now() - datetime.timedelta(
            days=1,
            seconds=1,
        )
        old_question = Question(datetime_published=old_time)
        self.assertIs(old_question.was_published_recently(), False)

        return
