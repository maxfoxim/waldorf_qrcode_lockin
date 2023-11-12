import datetime

from django.db import models
from django.utils import timezone
import django_tables2 as tables


class Person(models.Model):
    id = models.IntegerField(primary_key=True) # optional
    vorname =  models.CharField(max_length=100, verbose_name="Vorname")
    nachname = models.CharField(max_length=100, verbose_name="Nachname")
    klasse =   models.CharField(max_length=3,   verbose_name="Klasse")
    ankunft =  models.DateTimeField(verbose_name="Ankunft",default=0)
    qr_id  =   models.IntegerField(default=1)

    def __str__(self):
        return (self.id,self.vorname, self.nachname)

class Anwesenheitsliste(models.Model):
    #id =          models.IntegerField(primary_key=True)
    #qr_id  =      models.IntegerField(default=0)
    ankunft          =   models.DateTimeField(verbose_name="Ankunft")
    verlassen        =   models.DateTimeField(verbose_name="Verlassen")
    aufenthaltsdauer =   models.FloatField(verbose_name="Aufenthaltsdauer")

    kommentar        =   models.CharField(max_length=100,   verbose_name="Kommentar")
    qr               =   models.ForeignKey(Person,on_delete=models.CASCADE)

