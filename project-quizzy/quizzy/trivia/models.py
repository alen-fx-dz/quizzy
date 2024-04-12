from django.db import models

# Create your models here.
class Trivia(models.Model):
    class TypeTrivia(models.TextChoices):
        NORMAL = 'NO'
        TIME_OUT = 'TO'
        YES_NO = 'YN'

    theme = models.CharField(max_length=15)
    type_trivia = models.CharField(choices=TypeTrivia, default=TypeTrivia.NORMAL, max_length=2)
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

class Question(models.Model):
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE)
    question_text = models.CharField(verbose_name="Pregunta", max_length=30)

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=10)
    is_correct = models.BooleanField(default=False)
