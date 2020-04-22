from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Choice, Question


class IndexView(ListView):

    template_name = "polls/index.html"

    def get_queryset(self):
        """
        Return the 5 most-recently published questions,
        not including those scheduled to be published in the future.
        """

        return Question.objects.filter(
            datetime_published__lte=timezone.now(),
        ).order_by("-datetime_published")[:5]


class DetailView(DetailView):

    model = Question
    template_name = "polls/detail.html"


class ResultsView(DetailView):

    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        # Display the voting form again...

        context = {
            "question": question,
            "error_message": "You didn't select a choice.",
        }

        return render(request, "polls/detail.html", context)

    else:
        selected_choice.vote_count = F("vote_count") + 1
        selected_choice.save()

        # NOTE:
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted multiple times if a user hits the back button.

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
