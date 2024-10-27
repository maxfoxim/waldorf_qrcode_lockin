from django.contrib import admin

from .models import *

#@admin.register(Person)
class PersonView(admin.ModelAdmin):
    list_display = ('vorname', 'nachname', 'klasse', 'ankunft')

admin.site.register(Anwesenheitsliste)
admin.site.register(Person,PersonView)