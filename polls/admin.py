from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            "fields": ["datetime_published"],
        }),
        ("Datetime information", {
            "fields": ["text"],
        }),
    ]

    inlines = [
        ChoiceInline,
    ]


admin.site.register(Question, QuestionAdmin)
