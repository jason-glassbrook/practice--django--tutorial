from django.contrib import admin
from django.urls import reverse

from .models import Question, Choice


class PollsAdminSite(admin.AdminSite):

    name = "polls-admin-site"
    site_url = "/polls/"
    site_title = "Polls Admin Site"
    site_header = "Polls Administration"


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


polls_admin_site = PollsAdminSite()
polls_admin_site.register(Question, QuestionAdmin)
