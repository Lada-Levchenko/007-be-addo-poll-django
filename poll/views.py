from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from .models import Poll, Choice, FIELD_TYPE_CHOICES
from django.contrib.auth.models import User


def index(request):
    polls = Poll.objects.all()
    return render(request, "index.html", {'polls': polls})


def registration(request):
    return render(request, "registration/registration_form.html")


def register(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.save()
    return render(request, "registration/registration_complete.html")


@login_required
@csrf_protect
def poll(request, poll_id):
    curr_poll = Poll.objects.get(id=poll_id)
    mdict = {'poll': curr_poll, 'types': FIELD_TYPE_CHOICES}
    mdict.update(csrf(request))
    return render(request, 'poll.html', mdict)


@login_required
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
    return render(request, 'notification.html', response)


def dashboard(request,):
    polls = Poll.objects.all()
    return render(request, 'admin/dashboard.html', {'polls': polls})


def dashboard_poll(request, poll_id):
    curr_poll = Poll.objects.get(id=poll_id)
    polls = Poll.objects.all()
    return render(request, 'admin/dashboard.html', {'curr_poll': curr_poll, 'polls': polls})
