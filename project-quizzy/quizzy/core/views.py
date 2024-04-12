from typing import Any
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render 
from trivia.models import Trivia

class HomePageView(TemplateView):
    template_name = 'core/home.html'

class ContactPageView(TemplateView):
    template_name = 'core/contact.html'

class AboutPageView(TemplateView):
    template_name = 'core/about.html'

def GetInfoTrivia(request):
    return JsonResponse({'context': 'hola'})
