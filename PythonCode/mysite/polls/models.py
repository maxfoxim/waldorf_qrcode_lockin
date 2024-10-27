import datetime

from django.db import models
from django.utils import timezone
import django_tables2 as tables


class Person(models.Model):
    id       = models.AutoField(primary_key=True)
    vorname =  models.CharField(max_length=100, verbose_name="Vorname")
    nachname = models.CharField(max_length=100, verbose_name="Nachname")
    klasse =   models.CharField(max_length=5,   verbose_name="Klasse")
    ankunft =  models.DateTimeField(verbose_name="Ankunft",default=0, null=True,blank=True)

    def __str__(self):
        return (self.vorname)

class Anwesenheitsliste(models.Model):
    login_id         =   models.AutoField(primary_key=True)
    ankunft          =   models.DateTimeField(verbose_name="Ankunft")
    verlassen        =   models.DateTimeField(verbose_name="Verlassen",null=True)
    aufenthaltsdauer =   models.FloatField(verbose_name="Aufenthaltsdauer",null=True)
    kommentar        =   models.CharField(max_length=100,   verbose_name="Kommentar",null=True)
    person_id        =   models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.person_id))