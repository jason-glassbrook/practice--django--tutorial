from django.test import TestCase

from ..models import (
    Question,
    Choice,
)
from .tools import (
    offset_datetime_now,
)

################################################################################
#   Question
################################################################################


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        `was_published_recently()` should return `False` for questions whose
        `datetime_published` is in the future.
        """

        future_datetime = offset_datetime_now(days=+30)
        future_question = Question(datetime_published=future_datetime)

        self.assertIs(future_question.was_published_recently(), False)

        return

    def test_was_published_recently_with_recent_question(self):
        """
        `was_published_recently()` should return `True` for questions whose
        `datetime_published` is within 1 day.
        """

        recent_datetime = offset_datetime_now(days=-1, seconds=+1)
        recent_question = Question(datetime_published=recent_datetime)

        self.assertIs(recent_question.was_published_recently(), True)

        return

    def test_was_published_recently_with_old_question(self):
        """
        `was_published_recently()` should return `False` for questions whose
        `datetime_published` is older than 1 day.
        """

        old_datetime = offset_datetime_now(days=-1, seconds=-1)
        old_question = Question(datetime_published=old_datetime)

        self.assertIs(old_question.was_published_recently(), False)

        return


################################################################################
