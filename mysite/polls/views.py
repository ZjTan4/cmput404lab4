from .models import Choice, Question
from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, request, response
from django.urls import reverse
from django.views import generic

def index(request):
    # Question 3
    #return HttpResponse("Hello World. You are now at the polls index. ")
    # Question 7
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # Question 6
    #return HttpResponse("You are looking at the question {}".format(question_id))
    # Question 7
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # Question 6
    #response = "You are looking at the results of question {}"
    #return HttpResponse(response.format(question_id))
    # Question 8
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    # Question 6
    #return HttpResponse("You are voting on the question {}".format(question_id))
    # Question 8
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice. ",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return response.HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

# Question 8
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'