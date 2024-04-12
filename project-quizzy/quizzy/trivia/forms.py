from django import forms
from .models import Trivia, Question, Choise

class TriviaForm(forms.ModelForm):
    class Meta:
        model = Trivia
        fields = ['theme', 'type_trivia']
        labels = {'theme':'TEMA', 'type_trivia':'TIPO'}
        help_texts = {'theme':'Ingresa el tema mas interesante'}
        widgets = {
            'theme' : forms.TextInput(attrs={"class": "form-control"}),
            'type_trivia' : forms.Select(attrs={"class": "form-select bg-primary text-light"}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'trivia']
        labels = {'question_text':'Pregunta'}
        help_texts = {'question_text':'Que sea lo mejor'}
        widgets = {
            'question_text':forms.TextInput(attrs={"class": "form-control"}),
            'trivia':forms.TextInput(attrs={"class": "form-control"}),
        }

class TriviaNormalForm(forms.Form):
    IS_ANSWER_CHOICES = [
        ('1', 'Choice 1'),
        ('2', 'Choice 2'),
        ('3', 'Choice 3'),
        ('4', 'Choice 4'),
        ]
    question_text = forms.CharField(help_text='Escribe tu pregunta',label="QUESTION", max_length=150, widget = forms.Textarea(attrs = {'class':'form-control', 'rows':'2'}))
    choise_text_1 = forms.CharField(label="CHOISE 1", max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
    choise_text_2 = forms.CharField(label="CHOISE 2", max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
    choise_text_3 = forms.CharField(label="CHOISE 3", max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
    choise_text_4 = forms.CharField(label="CHOISE 4", max_length=50, widget = forms.TextInput(attrs = {'class':'form-control'}))
    is_answer = forms.ChoiceField(
        help_text='¿Cual es la respuesta correcta?',
        label="CORRECT ANSWER", 
        choices=IS_ANSWER_CHOICES, 
        widget=forms.RadioSelect(attrs = {'class':'btn-check'}))
