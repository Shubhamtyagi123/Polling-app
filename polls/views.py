from django.urls import reverse
from django.http import HttpResponseRedirect,Http404
from django.views import generic
from django.views.generic import ListView, DetailView
from django.template import loader
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

from .models import Choice,Town


"""class Indexview(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Town.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]


class Detailview(generic.DetailView):
    model = Town
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Town.objects.filter(pub_date__lte = timezone.now())

class Resultsview(generic.DetailView):
    model = Town
    template_name = 'polls/results.html'
"""

def index(request):
    latest_question_list = Town.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

    def get_queryset(self):
        return Town.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

def detail(request, question_id):
    try:
        question = Town.objects.get(pk=question_id)
    except Town.DoesNotExist:
        raise Http404("Town does not exist")
    return render(request, 'polls/detail.html', {'question': question})

    def get_queryset(self):
        return Town.objects.filter(pub_date__lte=timezone.now())

def results(request, question_id):

    question = get_object_or_404(Town, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Town, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, '/polls/detail.html', {
            'question': question,
            'error_message': "Choice not slected.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))
# Create your views here.

def final(request):
    return HttpResponseRedirect(reverse('polls/(?P<question_id>[0-9]+)/^/final.html'))