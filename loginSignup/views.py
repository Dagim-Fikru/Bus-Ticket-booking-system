# from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth  
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from pam import authenticate

# Create your views here.

def welcomePage(request):
    return render(request, 'welcome.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'ticket_booking_page.html')
        else:
            messages.info(request, 'incorrect username or password')
            return render(request,'loginPage.html')


        
    else:
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

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'*username taken try another' )
                # print('*username taken')
                return render(request, 'signupPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist try with another' )

                # print('email taken')
                return render(request, 'signupPage.html')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print('user created')
                return render(request, 'loginPage.html')
        # return redirect('')
        else:
            messages.info(request, '*password not match try again ')
            # print('*password not match')
            return render(request, 'signupPage.html')
    else:
        return render(request, 'signupPage.html')
