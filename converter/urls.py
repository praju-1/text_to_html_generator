# converter/urls.py

from django.urls import path
from converter import views

urlpatterns = [
    path('', views.text_input, name='text_input'),
]
