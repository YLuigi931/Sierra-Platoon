from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Home Page
    """
    return HttpResponse('<div> Hello world <div>')
