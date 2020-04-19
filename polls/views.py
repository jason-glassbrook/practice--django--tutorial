from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-datetime_published")[:5]
    output = ", ".join([q.text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
