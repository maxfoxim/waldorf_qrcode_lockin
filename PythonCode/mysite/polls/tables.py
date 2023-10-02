# tutorial/tables.py
import django_tables2 as tables
from .models import Person
from django_tables2 import TemplateColumn

class PersonTable(tables.Table):

    #edit = tables.TemplateColumn('<a href='{% url "edit_my_model_instance" record.id %}'>Edit</a>', verbose_name=u'Edit', )    
    edit =    tables.TemplateColumn(template_name="training_update_column.html", verbose_name=("Anmeldung"), orderable=False)
    editzwo = tables.TemplateColumn(template_name="training_update_column.html", verbose_name=("Abmeldung"), orderable=False)

    class Meta:
        model = Person
        #attrs = {'class': 'table table-sm'}
        template_name = "django_tables2/bootstrap.html"
        fields = ["vorname", "nachname","klasse","edit","editzwo"]
        #Angekommen = TemplateColumn(template_name='mysite/training_update_column.html')
