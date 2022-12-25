from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth  
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from pam import authenticate

# Create your views here.

def welcomePage(request):
    return render(request, 'welcome.html')

def login(request):
    return render(request,'loginPage.html')
    
def signup(request):
    # form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    #     return redirect('home')
    # return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username,password=password1,email=email)
        user.save();
        print('user created')
        return redirect('')
    else:
        return render(request, 'signupPage.html')
