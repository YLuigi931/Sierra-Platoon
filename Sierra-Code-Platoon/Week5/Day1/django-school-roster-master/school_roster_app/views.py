from django.shortcuts import render
from .models import Student, School
# from django.http import HttpResponse
import json

my_school = School("Django School")

def index(request):
    my_data = {"school_name": my_school.name}
    return render(request, 'pages/index.html', my_data)

def list_staff(request):
    my_data = {"school_staffs_list": my_school.staff}
    return render(request, 'pages/staffs.html', my_data)

def staff_detail(request, employee_id):
    pass # implement

def list_students(request):
    my_data = {"school_student_list": my_school.students}
    return render(request, 'pages/students.html', my_data)

def student_detail(request, student_id):
    pass # implement


# print(my_school.name)