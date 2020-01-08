from django import forms
from pseudosci.models import Quiz

class QuizForm(forms.ModelForm):
    """ Render and process form based on Quiz model"""
    class Meta:
        model = Quiz
        fields = '__all__'