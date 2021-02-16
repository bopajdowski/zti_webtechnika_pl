import datetime
from pprint import pprint

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

from rest_framework import routers, serializers, viewsets

from .serializers import QuestionSerializer


class IndexView(generic.ListView):
    model = Question
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['list_zmiennych'] = [None, 'b', 'c']
        context['for_example'] = {
            'Bartek': 'czerwony',
            'Aga': 2,
            'test': 'fdsfs',
        }
        context['cities'] = [
            {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
            {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
            {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
            {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
            {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
            {'name': 'Mumbai2', 'population': '18,000,000', 'country': 'India'},
        ]
        context['text'] = "i'm using Django <strong>test</strong>"
        context['liczba'] = 34.2345
        context['old_date'] = timezone.now() - datetime.timedelta(days=50)
        context['yesno_example'] = False

        return context


class ChoiceView(generic.ListView):
    model = Choice

    def get_queryset(self):
        return Choice.objects.filter(choice_text__istartswith='d')


class DetailView(generic.DetailView):
    model = Question
    slug_field = 'slug'


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


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
