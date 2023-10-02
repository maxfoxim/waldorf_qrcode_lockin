from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable
from django_tables2 import SingleTableView


"""
def index(request):   
    return HttpResponse("Hello, world. You're at the polls index.")                 
"""


class PersonTableView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'