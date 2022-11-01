from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

latest_question_list = [
    {
        'id' : 1,
        'question_text': 'whats up',
        'pub_date':'2022-01-04',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
    {
        'id' : 2,
        'question_text': 'whats new',
        'pub_date':'2022-02-09',
        'choices': [
            {
                'id':1,
                'choice_text':'not much',
                'votes': 0,
            },
            {
                'id':2,
                'choice_text':'the sky',
                'votes': 0,
            },
        ]
    },
]

# Create your views here.
def index(request):
    data = { 'latest_question_list': latest_question_list}
    return render(request, 'polls_app/index.html', data)

def detail(request, question_id):
    question = latest_question_list[question_id-1]
    data = {'question': question}
    return render(request, 'polls_app/details.html', data)

def results(request, question_id):
    question = latest_question_list[question_id-1]
    return render(request, 'polls_app/results.html', {'question': question})

def vote(request, question_id):
    question = latest_question_list[question_id-1]
    choice_id = int(request.POST['choice'])
    selected_choice = question['choices'][choice_id -1]
    print(selected_choice)
    selected_choice['votes'] += 1

    return HttpResponseRedirect(f'/{question_id}/results')