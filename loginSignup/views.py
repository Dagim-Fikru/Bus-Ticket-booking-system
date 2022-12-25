from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth  
from django.http import HttpResponse

# Create your views here.

def welcomePage(request):
    return render(request, 'welcome.html')

def login(request):
    return render(request,'loginPage.html')
    
def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username,password=password1,email=email)
        user.save()
        print('user created')
        return redirect('home')
    else:
        return render(request, 'signupPage.html')
