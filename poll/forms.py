from django.contrib import admin

from .models import Question, Choice
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


class EditLinkToInlineObject(object):

    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label, instance._meta.model_name), args=[instance.pk])
        if instance.pk:
            return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''


class QuestionInline(EditLinkToInlineObject, admin.TabularInline):
    model = Question
    readonly_fields = ('edit_link',)


class PollAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]
