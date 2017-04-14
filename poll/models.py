from django.db import models


FIELD_TYPE_CHOICES = (
    ('0', 'radio button'),
    ('1', 'select'),
    ('2', 'checkbox'),
    ('3', 'multiselect')
)


class Poll(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=FIELD_TYPE_CHOICES)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text


