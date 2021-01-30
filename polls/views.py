
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.utils import timezone

from .models import Question


def index(request):
    template_name = 'polls/index.html'
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, template_name, context)


def detail(request, question_id):
    template_name = 'polls/detail.html'
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'question': question,
    }
    return render(request, template_name, context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
