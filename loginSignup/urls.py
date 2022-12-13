from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcomePage, name='home')
]