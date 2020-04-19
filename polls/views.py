from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):

    latest_question_list = Question.objects.order_by("-datetime_published")[:5]

    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)


def detail(request, question_id):

    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")

    context = {
        "question": question,
    }

    return render(request, "polls/detail.html", context)


def results(request, question_id):

    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):

    return HttpResponse(f"You're voting on question {question_id}.")
