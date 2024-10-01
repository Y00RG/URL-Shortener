from django.urls import path
from .views import url_shortener

urlpatterns = [
    path('', url_shortener, name='url_shortener'),
]
