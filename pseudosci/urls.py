from django.urls import path
from pseudosci import views

urlpatterns = [
    path('', views.index, name = 'pseudosci-index'),
]
