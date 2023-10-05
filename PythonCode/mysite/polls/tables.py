# tutorial/tables.py
import django_tables2 as tables
from .models import Person,Anwesenheitsliste
from django_tables2 import TemplateColumn

class PersonTable(tables.Table):
    
    anmeldung =    tables.TemplateColumn('<a href="{% url "zeitspeichernankommen" record.id%}">Anmeldung</a>',verbose_name=("Anmeldung"), orderable=False)
    verlassen =    tables.TemplateColumn('<a href="{% url "zeitspeichernverlassen" record.id%}">Verlassen</a>', verbose_name=("Verlassen"), orderable=False)

    class Meta:
        model = Person
       #managed = True
        template_name = "django_tables2/bootstrap.html"
        fields = ["id","vorname", "nachname","klasse","anmeldung","verlassen"]



class AnwesenheitenTable(tables.Table):
    class Meta:
        model = Anwesenheitsliste
        #attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ["id","qr_id", "ankunft","verlassen","kommentar"]
        #managed = True