from django.db import models


FIELD_TYPE_CHOICES = (
    ('0', 'radio button'),
    ('1', 'select'),
    ('2', 'checkbox'),
    ('3', 'multiselect')
)


class Choice(models.Model):
    text = models.CharField(max_length=200)


class Question(models.Model):
    text = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice, related_name="question")
    type = models.CharField(max_length=1, choices=FIELD_TYPE_CHOICES)


class Poll(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    questions = models.ManyToManyField(Question, related_name="poll")
    votes = models.IntegerField(default=0)
