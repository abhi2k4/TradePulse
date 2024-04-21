
from django.shortcuts import render,redirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'show_navbar': True,
        'show_footer': True,
    }
    return render(request, 'core/index.html', context)

def crypto(request):
    context = {
        'show_navbar': True,
        'show_footer': True,
    }
    return render(request, 'core/cryptocurrency.html', context)

def news(request):
    context = {
        'show_navbar': True,
        'show_footer': True,
    }
    return render(request, 'core/news.html', context)

def personal(request):
    context = {
        'show_navbar': False,
        'show_footer': False,
    }
    return render(request, 'core/personal.html', context)

def calculator(request):
    context = {
        'show_navbar': True,
        'show_footer': True,
    }
    return render(request, 'core/calculator.html', context)

def watchlist(request):
    context = {
        'show_navbar': True,
        'show_footer': True,
    }
    return render(request, 'core/watchlist.html', context)

def academy(request):
    context = {
        'show_navbar': True,
        'show_footer': False,
    }
    return render(request, 'core/academy.html', context)

def streamlit_view(request):
    context = {
        'show_navbar': True,
        'show_footer': True,
    }    
    return render(request, 'core/forecast.html')

    