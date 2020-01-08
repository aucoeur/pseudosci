from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Quiz(models.Model):
    title = models.CharField('Title', max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.CharField(max_length=120, blank=True, editable=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Quiz")
        verbose_name_plural = ("Quizzes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/what-are-you). """
        path_components = {'slug': self.slug}
        return reverse('quiz-page', kwargs={path_components})
    
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Quiz, self).save(*args, **kwargs)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    prompt = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.prompt

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

