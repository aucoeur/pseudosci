from django.shortcuts import render

# Create your views here.

def index(request):
  text = 'I LIKE FOOD IS POTATOE.'
  return render(request, 'pseudosci/index.html', {'text': text})