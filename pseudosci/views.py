from django.shortcuts import render
from django.views.generic.list import ListView

from pseudosci.models import Quiz
# Create your views here.

def index(request):
  text = 'I LIKE FOOD IS POTATOE.'
  return render(request, 'pseudosci/index.html', {'text': text})

class QuizListView(ListView):
  """Renders list of all quizzes"""
  model = Quiz

  def get(self, request):
    """GET list of quizzes"""
    quizzes = self.get_queryset().all().order_by('-created')
    return render(request, 'pseudosci/list.html', { 'quizzes': quizzes})