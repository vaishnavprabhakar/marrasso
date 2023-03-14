from django.shortcuts import render, redirect
from django.contrib import messages
from . models import CustomUser
from django.db import *
from django.contrib.auth import logout
from django.contrib import *
from django.core import *
# from django.contrib.sessions
from django.contrib.auth.decorators import login_required
# from PIL import Image

# Create your views here.

# @login_required(redirect_field_name='login')
def home(request):
    return render(request, 'home.html')




def logout(request):
    messages.info(request, 'You have been Logged Out')
    request.session.flush()
    return redirect('login')

def sign(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['name']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            user = CustomUser.objects.create(
                email=email, username=username, password=password1)
            user.save()
        else:
            messages.info(request, 'Password Missmatch...')
    return render(request, 'sign-in.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.filter(email= email).first()

        print(user)
        
        if user is not None:
            if password ==  user.password:
                messages.success(request, 'Successfuly Logged in to Your account')
                return redirect('home') #Replace 'home' with the name of your desired URL pattern
        else:
            messages.info(request, 'Credentials Not Found. You must create an account here.')
            return redirect('sign') # Handle invalid login credentials
        return render(request, 'log.html')
    return render(request, 'log.html')
