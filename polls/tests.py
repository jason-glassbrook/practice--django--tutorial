import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

########################################
#   TOOLS
########################################


def create_question(text, **kwargs):
    """
    Create a question with the given `text` and published with
    the `datetime.timedelta` offset specified by `**kwargs`.
    """

    datetime_published = timezone.now() + datetime.timedelta(**kwargs)

    return Question.objects.create(
        text=text,
        datetime_published=datetime_published,
    )


def tag_text(base_text, tag=None):

    if tag is not None:
        return f"{base_text} [{tag}]"

    else:
        return base_text


def past_question_text(tag=None):

    return tag_text("When is the past?", tag)


def future_question_text(tag=None):

    return tag_text("When is the future?", tag)


def mock_question_repr(text):

    return f"<Question: {text}>"


########################################
#   Question > Model
########################################


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        `was_published_recently()` should return `False` for questions whose
        `datetime_published` is in the future.
        """

        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(datetime_published=future_time)

        self.assertIs(future_question.was_published_recently(), False)

        return

    def test_was_published_recently_with_recent_question(self):
        """
        `was_published_recently()` should return `True` for questions whose
        `datetime_published` is within 1 day.
        """

        recent_time = timezone.now() - datetime.timedelta(days=1, seconds=-1)
        recent_question = Question(datetime_published=recent_time)

        self.assertIs(recent_question.was_published_recently(), True)

        return

    def test_was_published_recently_with_old_question(self):
        """
        `was_published_recently()` should return `False` for questions whose
        `datetime_published` is older than 1 day.
        """

        old_time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(datetime_published=old_time)

        self.assertIs(old_question.was_published_recently(), False)

        return


########################################
#   Question > IndexView
########################################


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["question_list"],
            [],
        )
        self.assertContains(response, "No polls are available.")

        return

    def test_past_questions(self):
        """
        Questions with `datetime_published` in the past are displayed.
        """

        create_question(text=past_question_text(), days=-30)

        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["question_list"],
            [mock_question_repr(past_question_text())],
        )

        return

    def test_future_questions(self):
        """
        Questions with `datetime_published` in the future aren't displayed.
        """

        create_question(text=future_question_text(), days=+30)

        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["question_list"],
            [],
        )
        self.assertContains(response, "No polls are available.")

        return

    def test_future_question_and_past_question(self):
        """
        When both past and future questions exist, only the past questions are displayed.
        """

        create_question(text=past_question_text(), days=-30)
        create_question(text=future_question_text(), days=+30)

        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(
            response.context["question_list"],
            [mock_question_repr(past_question_text())],
        )

        return

    def test_multiple_past_questions(self):
        """
        The questions index page can display multiple questions.
        """

        n_past_questions = 4

        for i in range(n_past_questions):
            create_question(text=past_question_text(i), days=(-30 - i))

        response = self.client.get(reverse("polls:index"))

        print(response.context["question_list"])

        self.assertQuerysetEqual(
            response.context["question_list"],
            [
                mock_question_repr(past_question_text(i))
                for i in range(n_past_questions)
            ],
        )

        return

        return
