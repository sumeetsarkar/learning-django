from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last 5 published questions """
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExists):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    choice.votes = F('votes') + 1
    choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
