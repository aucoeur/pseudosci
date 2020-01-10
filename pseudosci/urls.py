from django.urls import path
from pseudosci.views import IndexView, QuizView, QuizNewView, QuizUpdateView, QuizDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name = 'pseudosci-index'),
    path('quiz/<str:slug>', QuizView.as_view(), name = 'quiz-page'),
    path('quiz/create/', QuizNewView.as_view(), name='quiz-create-page'),
    path('quiz/<str:slug>/update', QuizUpdateView.as_view(), name='quiz-update-page'),
    path('quiz/<str:slug>/delete', QuizDeleteView.as_view(), name='quiz-delete'),
]
