from django.test import TestCase
from django.urls import reverse

from ..models import (
    Question,
    Choice,
)
from .tools import (
    create_question,
    past_question_text,
    future_question_text,
    mock_question_repr,
)

################################################################################
#   Question > IndexView
################################################################################


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
        When both past and future questions exist, only the past questions
        are displayed.
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
