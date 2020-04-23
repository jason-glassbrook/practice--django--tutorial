from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    list_display = [
        "text",
        "datetime_published",
        "was_published_recently",
    ]

    list_filter = [
        "datetime_published",
    ]

    search_fields = [
        "text",
    ]

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
