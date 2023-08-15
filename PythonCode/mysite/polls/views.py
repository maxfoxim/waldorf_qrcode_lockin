from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person



"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""



class PersonListView(ListView):
    model = Person
    template_name = 'people.html'