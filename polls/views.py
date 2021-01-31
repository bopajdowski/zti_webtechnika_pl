
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


def index(request):
    template_name = 'polls/index.html'
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
        'today': timezone.now(),
    }
    return render(request, template_name, context)


def detail(request, question_id):
    template_name = 'polls/detail.html'
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, template_name, context)


def results(request, question_id):
    template_name = 'polls/results.html'
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, template_name, context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        success_url = reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(success_url)
