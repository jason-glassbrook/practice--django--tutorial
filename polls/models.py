from django.db import models


class Question(models.Model):

    text = models.CharField(
        "the text of the question",
        max_length=200,
    )

    datetime_published = models.DateTimeField(
        "the datetime when the question was published",
    )

    def __str__(self):
        return self.text


class Choice(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    text = models.CharField(
        "the text of the choice",
        max_length=200,
    )

    vote_count = models.IntegerField(
        "the number of votes for the choice",
        default=0,
    )

    def __str__(self):
        return self.text
