from django.contrib import admin
import nested_admin

from pseudosci.models import Quiz, Question, Choice

# Register your models here.

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 4

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [ChoiceInline]
    extra = 0

class QuizAdmin(nested_admin.NestedModelAdmin):
    """Show helpful fields on the changelist page."""
    list_display = ('title', 'author', 'created', 'modified')
    inlines = [QuestionInline]
    search_fields = ['prompt']

admin.site.register(Quiz, QuizAdmin)
