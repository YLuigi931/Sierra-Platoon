from django.shortcuts import render
from django.contrib.auth.models import User
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Create your views here.

def index(request):
    """homepage"""
    return render(request, 'index.html')

def signup(request):
    # Create my user

    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    return render(request, 'signup.html')