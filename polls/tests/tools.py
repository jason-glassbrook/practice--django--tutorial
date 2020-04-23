import datetime

from django.utils import timezone

from ..models import (
    Question,
    Choice,
)

################################################################################
#   TESTING TOOLS
################################################################################


def offset_datetime(when, **kwargs):

    return when + datetime.timedelta(**kwargs)


def offset_datetime_now(**kwargs):

    return timezone.now() + datetime.timedelta(**kwargs)


def create_question(text, **kwargs):
    """
    Create a question with the given `text` and published with
    the `datetime.timedelta` offset specified by `**kwargs`.
    """

    return Question.objects.create(
        text=text,
        datetime_published=offset_datetime_now(**kwargs),
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


################################################################################
