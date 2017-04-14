from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Poll, Question, Choice
from django.contrib.auth.models import User

from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from .forms import QuestionForm


def index(request):
    polls = Poll.objects.all()
    return render(request, "index.html", {'polls': polls})


def registration(request):
    return render(request, "registration/registration_form.html")


def register(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.save()
    return render(request, "registration/registration_complete.html")


@csrf_protect
def poll(request, poll_id):
    curr_poll = Poll.objects.get(id=poll_id)
    QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=0)
    formset = QuestionFormSet(request.POST or None, queryset=curr_poll.questions.all())
    return render_to_response('poll.html', {'formset': formset})


@csrf_protect
def answer(request, poll_id):
    if request.method == 'POST':
        curr_poll = Poll.objects.get(id=poll_id)
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=0)
        formset = QuestionFormSet(request.POST, queryset=curr_poll.questions.all())
        if formset.is_valid():
            curr_poll.votes += 1
            for form in formset.forms:
                choices = form.cleaned_data['model'].choices
                for choice in choices:
                    choice.votes += 1
        response = "Thanks for your answers!"
    else:
        response = "Something went wrong!"
    return HttpResponse(response)


def votes(request, poll_id):
    return HttpResponse("Votes for poll %s." % poll_id)
