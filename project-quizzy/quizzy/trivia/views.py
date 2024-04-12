from .forms import TriviaForm, QuestionForm
from .models import Trivia, Question, Choise

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


# Trivia CRUD here.
class TriviaListView(ListView):
    model = Trivia
    paginate_by = 5

class TriviaDetailView(DetailView):
    model = Trivia

class TriviaCreateView(CreateView):
    model = Trivia
    form_class = TriviaForm
    success_url = reverse_lazy('trivia:list')

class TriviaDeleteView(DeleteView):
    model = Trivia
    success_url = reverse_lazy('trivia:list')

class TriviaUpdateView(UpdateView):
    model = Trivia
    form_class = TriviaForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse('trivia:list')                                                                                                                                                 

# Question CRUD here.
class QuestionListView(ListView):
    model = Question

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm

    def get_success_url(self):
        return reverse('trivia:update', args=[self.kwargs['pk_trivia']])

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        kwargs['pk_trivia'] = self.kwargs['pk_trivia']
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('trivia:list')

