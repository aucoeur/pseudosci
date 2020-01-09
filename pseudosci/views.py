from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from pseudosci.models import Quiz
# Create your views here.

class IndexView(ListView):
  model = Quiz
  template_name = 'pseudosci/list.html'

  def get(self, request):
    """GET list of quizzes"""
    quizzes = self.get_queryset().all().order_by('-created')
    return render(request, 'pseudosci/index.html', { 'quizzes': quizzes})

class QuizView(DetailView):
  """ Renders a specific quiz based on its slug."""
  model = Quiz

  def get(self, request, slug):
    """ Returns a specific wiki page by slug. """
    quiz = self.get_queryset().get(slug__iexact=slug)
    return render(request, 'pseudosci/quiz.html', {'quiz': quiz})