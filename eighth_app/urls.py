# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('model_form_creation', views.model_form_creation)
]