from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.IndexView.as_view(), name='index'),
    path('choices/', views.ChoiceView.as_view(), name='choices'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
