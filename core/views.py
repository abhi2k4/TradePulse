from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'core/index.html')

def crypto(request):
    return render(request, 'core/cryptocurrency.html')

def news(request):
    return render(request, 'core/news.html')

def watchlist(request):
    return render(request, 'core/watchlist.html')

def login(request):
    return render(request, 'core/login.html')
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            user = User(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            messages.success(request, 'Your account has been created, you can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')