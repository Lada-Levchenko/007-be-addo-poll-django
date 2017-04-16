from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from .models import Poll, Question, Choice, FIELD_TYPE_CHOICES
from django.contrib.auth.models import User

from django.shortcuts import render_to_response


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
    mdict = {'poll': curr_poll, 'types': FIELD_TYPE_CHOICES}
    mdict.update(csrf(request))
    return render_to_response('poll.html', mdict)


@csrf_protect
def answer(request, poll_id):
    if request.method == 'POST':
        curr_poll = Poll.objects.get(id=poll_id)
        curr_poll.votes += 1
        curr_poll.save()
        choices = request.POST.getlist('choices')
        for selected in choices:
            choice = Choice.objects.get(id=selected)
            choice.votes += 1
            choice.save()
        response = {
            'notification': "Thank you for your answers!",
            'notification_type': 'success'
        }
    else:
        response = {
            'notification': "Something went wrong! Go back home...",
            'notification_type': 'danger'
        }
    return render_to_response('notification.html', response)


def dashboard(request,):
    polls = Poll.objects.all()
    return render_to_response('admin/dashboard.html', {'polls': polls})


def dashboard_poll(request, poll_id):
    curr_poll = Poll.objects.get(id=poll_id)
    polls = Poll.objects.all()
    return render_to_response('admin/dashboard.html', {'curr_poll': curr_poll, 'polls': polls})
