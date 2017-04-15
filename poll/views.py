from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from .models import Poll, Question, Choice
from django.contrib.auth.models import User

from django.forms import formset_factory
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
    mdict = {'poll': curr_poll}
    mdict.update(csrf(request))
    return render_to_response('poll.html', mdict)


@csrf_protect
def answer(request, poll_id):
    if request.method == 'POST':
        curr_poll = Poll.objects.get(id=poll_id)
        curr_poll.votes += 1
        curr_poll.save()
        selected_list = request.POST.getlist('select')
        for selected in selected_list:
            choice = Choice.objects.get(id=selected)
            choice.votes += 1
            choice.save()
        response = "Thanks for your answers!"
    else:
        response = "Something went wrong!"
    return HttpResponse(response)


def votes(request, poll_id):
    return HttpResponse("Votes for poll %s." % poll_id)
