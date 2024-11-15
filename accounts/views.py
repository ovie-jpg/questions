from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid details')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')