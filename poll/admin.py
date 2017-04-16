from django.contrib import admin
from .models import Poll, Question, Choice
from .forms import PollAdmin, QuestionAdmin
from .views import dashboard
from django.conf.urls import url

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


def get_admin_urls(urls):
    def get_urls():
        my_urls = [
            url(r'^dashboard/$', admin.site.admin_view(dashboard))
        ]
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
