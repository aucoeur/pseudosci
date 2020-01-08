from django.urls import path
from pseudosci import views
from pseudosci.views import QuizListView


urlpatterns = [
    path('', views.index, name = 'pseudosci-index'),
    path('list/', QuizListView.as_view(), name = 'quiz-list-view'),
]
