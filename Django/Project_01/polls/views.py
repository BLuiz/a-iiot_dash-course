from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question

# Arquivos de visualização do site


def index1(request):
    return HttpResponse('Olá, esse é meu primeiro site')


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail1(request, question_id):
    return HttpResponse('Essa é a pergunta de número %s' % question_id)


def results1(request, question_id):
    return HttpResponse('Esses são os resultados da pergunta da pergunta de número %s' % question_id)


def results(request, question_id):
    question = Question(pk=question_id)     # pk: Primary key
    return render(request, 'polls/results.html', {'question': question})


def vote1(request, question_id):
    return HttpResponse('Você está votando na questão de número %s' % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))



