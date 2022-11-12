from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice

# Create your views here.

def home(request):
    # to grab the data make sure to initialize in a dictionary
    data = {}
    # followed by getting the contents via ORM queries
    questions = Question.objects.order_by('-pub_date')
    # pass the data in as a list and make a name in dictionary so
    # html file can reference it
    data['latest_question_list'] = questions
    # or
    # data = {'latest_question_list' : questions}
    
    # pattern here every time you render
    # render(request, {point out the html file}, {if data exist somewhere})
    # if html file doesn't exist make one in templates folder
    return render(request, 'index.html', data)

def detail(request, question_id):
    
    question = Question.objects.get(id = question_id)
    # return HttpResponse(f"You're looking at question {question_id}.")
    data = {'question':question}
    return render(request, 'details.html', data)

def results(request, question_id):
    question = Question.objects.get(id = question_id)
    return render(request, 'results.html', {'question':question})

def vote(request, question_id):
    
    question = Question.objects.get(id = question_id)
   
    # print(choice_id)
    
    try:
        # make sure to add all the parameters within try or except will fail
        choice_id= request.POST['choice']
        selected_choice = question.choice_set.get(id = choice_id)
    except(KeyError, Choice.DoesNotExist):
        # when handeling error message that uses render, make sure to mention that to the html file
        # since this is rendering the detail page, it needs the question model
        data = {'question':question,
                'error_message': 'you forgot to select a choice'
                
                }
        return render(request, 'details.html', data)
        
    selected_choice.votes+=1
    selected_choice.save()
    
    # return HttpResponse(f"You're voting on question {question_id}.")
    # you don't want to render on a Post. You have to use the redirect
    
    return HttpResponseRedirect(f"/polls/{question_id}/results")

def all_results(request):
    
    data ={}
    questions = Question.objects.all()
    data = {'questions_list': questions}
    
    return render(request, 'all_results.html', data)