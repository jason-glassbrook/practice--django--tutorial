from django.db import models


class Question(models.Model):
    text = models.CharField(
        "the text of the question",
        max_length=200,
    )
    datetime_published = models.DateTimeField(
        "the datetime when the question was published",
    )
