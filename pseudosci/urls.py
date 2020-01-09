from django.urls import path
from pseudosci.views import IndexView, QuizView


urlpatterns = [
    path('', IndexView.as_view(), name = 'pseudosci-index'),
    path('quiz/<str:slug>', QuizView.as_view(), name = 'quiz-page')
]
