from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Choice

# def index(request):
#     return HttpResponse("""<h1> Hello hafiz keep going<h1>""")

# Create your views here.


def index(request):
    # order by the date by descending order and specifyig how many we want which is 5
    questions_list= Question.objects.order_by('-pub_date')[:5]
    context={'question_list':questions_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})



def result(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question':question})

def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"you should select a choice"
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

    return render(request, 'polls/result.html', {'question':question})
