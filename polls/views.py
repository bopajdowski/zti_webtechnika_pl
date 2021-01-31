
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    model = Question

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class ChoiceView(generic.ListView):
    model = Choice
    
    def get_queryset(self):
        return Choice.objects.filter(choice_text__istartswith='d')


class DetailView(generic.DetailView):
    model = Question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class AboutView(generic.TemplateView):
    template_name = "polls/about.html"


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
