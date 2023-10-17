# tutorial/tables.py
import django_tables2 as tables
from .models import Person,Anwesenheitsliste
from django_tables2 import TemplateColumn

class PersonTable(tables.Table):
    
    anmeldung =    tables.TemplateColumn('<button type="button" class="btn btn-primary" onclick="location.href=\'{% url "zeitspeichernankommen" record.id%}\'" >Anmeldung</button>',verbose_name=("Anmeldung"), orderable=False)
    verlassen =    tables.TemplateColumn('<button type="button" class="btn btn-warning" onclick="location.href=\'{% url "zeitspeichernverlassen" record.id%}\'">Verlassen</button>', verbose_name=("Verlassen"), orderable=False)

    class Meta:
        model = Person
       #managed = True
        template_name = "django_tables2/bootstrap.html"
        attrs =  {"class":"table table-striped"}
        fields = ["id","vorname", "nachname","klasse","ankunft","anmeldung","verlassen"]



class AnwesenheitenTable(tables.Table):
    class Meta:
        model = Anwesenheitsliste
        #attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ["id","qr_id", "ankunft","verlassen","kommentar"]
        #managed = True