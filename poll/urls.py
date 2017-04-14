from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^register/$', views.register, name='register'),
    # ex: /5/
    url(r'^(?P<poll_id>[0-9]+)/$', views.poll, name='poll'),
    # ex: /5/answer
    url(r'^(?P<poll_id>[0-9]+)/answer$', views.answer, name='answer'),
    # ex: /5/vote/
    url(r'^(?P<question_id>[0-9]+)/votes/$', views.votes, name='votes'),
]