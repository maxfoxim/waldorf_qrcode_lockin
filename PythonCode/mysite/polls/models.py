import datetime

from django.db import models
from django.utils import timezone
import django_tables2 as tables


class Person(models.Model):
    vorname =  models.CharField(max_length=100, verbose_name="Vorname")
    nachname = models.CharField(max_length=100, verbose_name="Nachname")
    klasse =   models.CharField(max_length=2,   verbose_name="Klasse")
    qr_id  =   models.IntegerField(default=0,primary_key=True)

class Anwesenheitsliste(models.Model):
    qr_id  =      models.IntegerField(default=0)
    ankunft   =   models.DateTimeField(verbose_name="Ankunft")
    verlassen =   models.DateTimeField(verbose_name="Verlassen")
    kommentar =   models.CharField(max_length=100,   verbose_name="Kommentar")



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
