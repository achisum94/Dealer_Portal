from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')



def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def app_entry(request):
    return render(request, 'accounts/application.html')


def profile(request):
    return render(request, 'accounts/profile.html')

def profile_App(request):
    return render(request, 'accounts/profile_App.html')

# queues
def approved(request):
    return HttpResponse('approved')

def declined(request):
    return HttpResponse('declined')

def payment_calls(request):
    return HttpResponse('payment_calls')

def booked(request):
    return HttpResponse('booked')