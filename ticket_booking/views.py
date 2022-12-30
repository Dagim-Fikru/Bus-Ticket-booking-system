from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth  
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from pam import authenticate

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request, 'loginPage.html')
