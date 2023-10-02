# tutorial/tables.py
import django_tables2 as tables
from .models import Person
from django_tables2 import TemplateColumn

class PersonTable(tables.Table):

    #edit = tables.TemplateColumn('<a href='{% url "edit_my_model_instance" record.id %}'>Edit</a>', verbose_name=u'Edit', )    
    edit =    tables.TemplateColumn('<button type="submit">Anmelden</button>', verbose_name=("Anmeldung"), orderable=False)
    editzwo = tables.TemplateColumn('<a href="{% url "zeitspeichern" record.id%}">Verlassen</a>', verbose_name=("Verlassen"), orderable=False)
    #editzwo = tables.TemplateColumn('<a href="https://www.web.de"  type="submit">Verlassen</a>', verbose_name=("Verlassen"), orderable=False)

    class Meta:
        model = Person
        #attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ["id","vorname", "nachname","klasse","edit","editzwo"]
        #Angekommen = TemplateColumn(template_name='mysite/training_update_column.html')
