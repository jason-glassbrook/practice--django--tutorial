from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            "fields": ["datetime_published"],
        }),
        ("Datetime information", {
            "fields": ["text"],
        }),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
