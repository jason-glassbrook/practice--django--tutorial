import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):

    text = models.CharField(
        "question's text",
        max_length=200,
    )

    datetime_published = models.DateTimeField("question's datetime when published")

    def __str__(self):
        return self.text

    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.datetime_published <= now

    was_published_recently.short_description = "published recently?"
    was_published_recently.admin_order_field = "datetime_published"
    was_published_recently.boolean = True


class Choice(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    text = models.CharField(
        "choice's text",
        max_length=200,
    )

    vote_count = models.IntegerField(
        "choice's vote count",
        default=0,
    )

    def __str__(self):
        return self.text
