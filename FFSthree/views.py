from django.shortcuts import render


def home(request):
    """views the home page"""
    return render(request, 'home.html')


def working(request):
    """under construction dialogue"""
    return render(request,'working.html')
