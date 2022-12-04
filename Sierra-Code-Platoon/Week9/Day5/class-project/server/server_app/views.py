from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

def index(request):
    index_file = open('static/index.html').read()
    return HttpResponse(index_file)

@api_view(["GET","POST"])
def categories(request):
    return JsonResponse({'success': True})

@api_view(["GET","PUT","DELETE"])
def category(request, category_id):
    pass

@api_view(["GET"])
def posts(request):
    pass

@api_view(["GET","PUT"])
def post(request, post_id):
    pass

@api_view(["GET","POST"])
def category_posts(request, category_id):
    pass

@api_view(["GET"])
def post_by_category(request, category_id, post_id):
    pass