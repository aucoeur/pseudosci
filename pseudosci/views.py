from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from pseudosci.models import Quiz
from pseudosci.forms import QuizForm

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

class QuizNewView(CreateView):
  """ Renders a page to create a new quiz"""
  template_name = 'pseudosci/quiz_new.html'
  form_class = QuizForm
  success_url = '' 

  def get(self, request):
    form = QuizForm()
    return render(request, 'pseudosci/quiz_new.html', {'form': form})

  def post(self, request):
    if request.method == 'POST':
      form = QuizForm(data=request.POST)
      if form.is_valid():
        quiz = form.save()
        return HttpResponseRedirect(reverse_lazy('quiz-page', args = [quiz.slug]))
      return render(request, 'pseudosci/quiz_new.html', {'form': form})


class QuizUpdateView(UpdateView):
  ''' Renders an Edit Quiz Form'''
  model = Quiz
  template_name = 'pseudosci/quiz_edit.html'
  form_class = QuizForm
  
  def get_success_url(self):
      return reverse('quiz-page', kwargs={
          'slug': self.object.slug,
      })

class QuizDeleteView(DeleteView):
  '''Renders a Delete thing'''
  model = Quiz
  success_url = reverse_lazy('pseudosci-index')

  # def get(self, *args, **kwargs):
  #     """
  #     This has been overriden because by default
  #     DeleteView doesn't work with GET requests
  #     """
  #     return self.delete(*args, **kwargs)
