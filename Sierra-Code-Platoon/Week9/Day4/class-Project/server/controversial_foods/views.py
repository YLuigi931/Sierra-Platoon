from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

def index(request):
    """
    Home Page
    """
    print('index')
    homePage = open('static/index.html').read()
    return HttpResponse(homePage)

# @api_view['GET']
# def whoAmI(request):
#     # get user from database
#     user = {}
#     return JsonResponse(data=user)
