from django.contrib import admin
from .models import Poll, Question, Choice
from .forms import PollAdmin, QuestionAdmin

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
