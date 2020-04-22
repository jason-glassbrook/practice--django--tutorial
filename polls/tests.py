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
