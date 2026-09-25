from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcribe_file, name='home')
]