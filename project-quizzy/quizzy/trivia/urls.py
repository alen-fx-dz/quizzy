from .views import *

from django.urls import path

trivia_urlpatterns = ([
    # Paths trivia
    path('list/', TriviaListView.as_view(), name='list'),
    path('detail/<int:pk>/<slug:slug>/', TriviaDetailView.as_view(), name='detail'),
    path('create/', TriviaCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', TriviaDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', TriviaUpdateView.as_view(), name='update'),
    # Paths Question
    path('<int:pk_trivia>/question/list/', QuestionListView.as_view(), name='question-list'),
    path('<int:pk_trivia>/question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/delete/<int:pk>/', QuestionDeleteView.as_view(), name='question-delete')
], 'trivia')