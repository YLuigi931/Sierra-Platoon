from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import json
# debugger tool 1:07:40 W9D5:(2 of 2)
def index(request):
    index_file = open('static/index.html').read()
    return HttpResponse(index_file)

# @api_view(["GET","POST"])
def categories(request):
    list_of_categories = [
        {'id':1, 'title':'Games'},
        {'id':2, 'title':'Hobbies'},
        {'id':3, 'title':'Movies'}
    ]
    if request.method == 'GET':
        print('Category request happened on the back-end')
        return JsonResponse({'categories':list_of_categories})
    
    elif request.method == 'POST':
        print(json.loads(request.body))
        # print(request.data['title'])
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