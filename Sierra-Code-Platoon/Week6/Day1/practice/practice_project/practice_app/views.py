from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . models import Students
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    # # play with this code block
    # student = Students(first_name ='johnny', last_name ='irwin', email = 'irwin@Gmail')
    # student.save()
    # # it adds to the database
    # return render(request, 'index.html')
    
    # this code block will view the objects 
    # students = Students.objects.all()
    # print(students[1].first_name)
    # return render(request, 'index.html', {'students': students})

    #student will be deleted
    # student_to_be_deleted = Students.objects.get(id=2)
    # print(student_to_be_deleted)
    # student_to_be_deleted.delete()
    
    students = Students.objects.all()
    
    return render(request, 'index.html', {'students': students})

@csrf_exempt
def add_student(request):
    print(request.method)
    # check for post (this is the reciever)
    if request.method == 'POST':
        print('recieved')
        # when we recieve the request we can parse the data and take the data in body
        body = json.loads(request.body)
        print(body)
        
        # parse the body data to make the student object
        new_student = Students(first_name = body['first'], last_name = body['last'], email = body['email'])
        # adds to the database
        new_student.save()
        # this will give an error if new_student is added here flat due to its a object with parts
        # try json.loads(new_student)
        # another solution would be making a dictionry and appending 
        # look up jamgo serializer
    return JsonResponse({'new_student': new_student.first_name})
    