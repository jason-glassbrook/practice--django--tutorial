from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):

    fields = [
        "datetime_published",
        "text",
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
