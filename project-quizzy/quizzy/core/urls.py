from .views import HomePageView, ContactPageView, AboutPageView, GetInfoTrivia
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hola/', GetInfoTrivia),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
]
