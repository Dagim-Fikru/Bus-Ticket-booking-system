from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcomePage, name='home'),
    path('loginPage/',views.loginPage, name='login')
]