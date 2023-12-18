"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls.views import * 


urlpatterns = [
    #path("polls/", include("polls.urls")),
    path("hauptseite/",hauptseite,name="hauptseite"),
    path("schuelerliste/", PersonTableView.as_view(),name="schuelerliste"),
    path("admin/", admin.site.urls),
    path("zeitspeichernankommen/<int:id>/"  ,ankommen_speichern, name='zeitspeichernankommen'),
    path('zeitspeichernverlassen/<int:id>/',verlassen_speichern, name='zeitspeichernverlassen'),
    path('zeitspeichernverlassen_alle/',alle_abmelden, name='zeitspeichernverlassen_alle'),
    path('exportexcel/',export_excel, name='export_excel'),
    path('importexcel/',import_excel, name='import_excel'),
    path("anwesenheiten/",anwesenheitsliste,name="anwesenheitsliste"),
    path("anwesenheiten_tag/",anwesenheitsliste_tag,name="anwesenheitsliste_tag"),
    path("anmeldung_korrigieren/",anmeldung_korrigieren,name="anmeldung_korrigieren"),
    path("anmeldung_entfernen/<int:id>/",anmeldung_entfernen,name="anmeldung_entfernen"),
    path("klassenauswahl/",klassenauswahl,name="klassenauswahl"),
    path("schueler_klassenauswahl/<str:alter>-<str:buchstabe>",schueler_klassenauswahl,name="schueler_klassenauswahl")


]