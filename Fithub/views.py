from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def join(request):
    return render(request, 'join.html')

def timetable(request):
    return render(request, 'timetable.html')
def base(request):
    return render(request, 'base.html')

def base(request):
    return render(request, 'base.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('Loged in Successfully')
            return redirect('/')
        else:
            print('Invalid Credentials')
            messages.info(request, 'Invalid Credentials')
            return redirect('/')

    else:
        return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstName = request.POST['firstName']
        password = request.POST['password']

        newuser = User.objects.create_user(username=username, email=email, first_name=firstName, password=password)
        newuser.save()
        print('User Created Successfully')
        return redirect('/')
    else:
        return redirect('/')

def LogOut(request):
    auth.logout(request)
    return redirect('/')




