from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable, AnwesenheitenTable
from django_tables2 import SingleTableView
#from .forms import PostForm
from django.shortcuts import render
from .forms import TableForm
from polls.models import Anwesenheitsliste, Person
import pandas as pd 
from django.contrib import messages
from django.utils import timezone
import datetime
import pytz
from datetime import datetime
import os
from pathlib import Path


class PersonTableView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'htmlseiten/people.html'

class AnwesenheitslisteView(SingleTableView):
    model = Anwesenheitsliste
    table_class = AnwesenheitenTable
    template_name = 'htmlseiten/anwesenheiten.html'

def hauptseite(request):
    return render(request, 'htmlseiten/hauptseite.html', {'data': []})
 

def ankommen_speichern(request, id):
    aktuelle_zeit=datetime.now(pytz.timezone('Europe/Berlin'))
    current_day = timezone.now().day
    current_month = timezone.now().month

    # nach ID und aktuellem Tag filtern --> gibt Liste zurück
    Bereits_Eingeloggt=Anwesenheitsliste.objects.filter(qr_id=id).filter(ankunft__day=current_day).filter(ankunft__month=current_month).values_list("ankunft")
    if len(Bereits_Eingeloggt)>0: # Bereits ein Eintrag vorhanden
        print("Eintrag bereits vorhanden.")
    else:
        Datum=Anwesenheitsliste(qr_id=id,ankunft=aktuelle_zeit,verlassen=None,kommentar=None,aufenthaltsdauer=0  )
        Datum.save()

        Person_Heutigeanmeldung=Person.objects.get(id=id)
        Person_Heutigeanmeldung.ankunft=aktuelle_zeit
        Person_Heutigeanmeldung.save()
    
    #meetingData = Anwesenheitsliste.objects.all()
    Personen=Person.objects.get(id=id)
    Name=    Personen.vorname
    Nachname=Personen.nachname
    print("ID ist",Name,Person)
    
    return render(request, 'htmlseiten/hello.html', {'data': [Name+" "+Nachname]})



def verlassen_speichern(request, id):
    aktuelle_zeit=datetime.now(pytz.timezone('Europe/Berlin'))
    current_day = timezone.now().day
    current_month = timezone.now().month
    Personen=Person.objects.get(id=id)
    Name=    Personen.vorname
    Nachname=Personen.nachname

    try:
        Auslogwert=Anwesenheitsliste.objects.get(qr_id=id,ankunft__day=current_day,ankunft__month=current_month)    
        
        delta=(aktuelle_zeit-Auslogwert.ankunft)
        Auslogwert.verlassen=aktuelle_zeit
        Auslogwert.aufenthaltsdauer=round(delta.seconds/60)

        Auslogwert.save()

        #messages.info(request, 'Erfolgreiche Nachricht')  ?
        #print("Zeitzone Verlassen",Auslogwert.verlassen)
        #render(request, 'hello.html', {'data': ["byebye"]})
        return render(request, 'htmlseiten/abschied.html', {'data': [Name+" "+Nachname]})
    except:
        return render(request, 'htmlseiten/keineAnmeldung.html', {'data': [Name+" "+Nachname]})


def alle_abmelden(request):
    """
    Alle Schüler die sich noch nicht abgemeldet haben, zusammen abmelden.
    """

    #my_scheduled_task.schedule(repeat=Task.DAILY, time=datetime.time(hour=8, minute=53))

    aktuelle_zeit=datetime.now(pytz.timezone('Europe/Berlin'))
    current_day =   timezone.now().day
    current_month = timezone.now().month

    #Auslogwert=Anwesenheitsliste.objects.get(ankunft__day=current_day ,ankunft__month=current_month)  
    Auslogwert=Anwesenheitsliste.objects.filter(ankunft__day=current_day).filter(ankunft__month=current_month)    

    #Auslogwert.verlassen=aktuelle_zeit
    print("ALLE ABMELDEN")
    for Zeile in Auslogwert:
        print(Zeile,Zeile.verlassen, Zeile.qr_id)
        if Zeile.verlassen==None:
            Zeile.verlassen=aktuelle_zeit
            delta=(aktuelle_zeit-Zeile.ankunft)
            Zeile.aufenthaltsdauer = round(delta.seconds/60)
            Zeile.save()
        else:
            print("Bereits einzeln ausgeloggt:",Zeile.verlassen)
    return render(request, 'htmlseiten/feierabend.html', {'data': None })


def klassenauswahl(request):
    alter=range(1,14)
    buchstaben = ["a","b"]
    return render(request, 'htmlseiten/klassenauswahl.html', { "alter":alter, "buchstaben":buchstaben })


def schueler_klassenauswahl(request,alter,buchstabe):
    print("Klasse:",alter,buchstabe,str(alter)+buchstabe)
    meetingData=Person.objects.filter(klasse=str(alter)+buchstabe)  
    return render(request, 'htmlseiten/schueler_klassenauswahl.html', {'data':meetingData})


def anwesenheitsliste(request):
    meetingData = Anwesenheitsliste.objects.all()
    #messages.info(request, 'Erfolgreiche Nachricht')  
    return render(request, 'htmlseiten/anwesenheiten.html', {'data': meetingData })



def anwesenheitsliste_tag(request):
    #meetingData = Anwesenheitsliste.objects.all()
    #messages.info(request, 'Erfolgreiche Nachricht')  
    #aktuelle_zeit=datetime.now(pytz.timezone('Europe/Berlin'))
    current_day = timezone.now().day
    current_month = timezone.now().month
    meetingData=Anwesenheitsliste.objects.filter(ankunft__day=current_day).filter(ankunft__month=current_month)    
    print(meetingData)
    return render(request, 'htmlseiten/anwesenheiten_tag.html', {'data': meetingData })

def anmeldung_korrigieren(request):
    #aktuelle_zeit=datetime.now(pytz.timezone('Europe/Berlin'))
    current_day = timezone.now().day
    current_month = timezone.now().month
    meetingData=Anwesenheitsliste.objects.filter(ankunft__day=current_day).filter(ankunft__month=current_month)    
    return render(request, 'htmlseiten/anmeldung_korrigieren.html', {'data': meetingData })

def anmeldung_entfernen(request,id):
    Auslogwert=Anwesenheitsliste.objects.get(id=id).delete()
    print(Auslogwert)
    #Auslogwert.delete()
    #Auslogwert.save()
    return render(request, 'htmlseiten/korrektur_confirm.html', {'data': []})

def export_excel(request):
    """
    Exportie die Anwesenheitsliste in eine Excel Datei
    """
    anwesenheits_eintraege = Anwesenheitsliste.objects.all()
    #personen = Person.objects.all()
    print("---------------")
    #print("Personen bei Export Excel",personen)
    vornamen=[]
    nachnamen=[]
    ankunft=[]
    verlassen=[]
    klasse=[]
    differenz=[]
    kommentar=[]
    for zeile in anwesenheits_eintraege:
        schueler=Person.objects.get(id=zeile.qr_id)
        nachnamen .append(schueler.nachname)
        vornamen  .append(schueler.vorname)
        klasse    .append(schueler.klasse)
        kommentar .append(zeile.kommentar)

        ankunft   .append(zeile.ankunft.  strftime("%d.%m.%Y %H:%M"))

        if zeile.verlassen == None: # Vergessene Abmeldungen auf 18:00 gleichen Tag festlegen
            verlassen .append(zeile.ankunft.strftime("%d.%m.%Y 18:00"))
            zeile.kommentar = "Abmeldung Automatisch"
            zeile.save()
        else:
            verlassen .append(zeile.verlassen.strftime("%d.%m.%Y %H:%M"))

        delta=(datetime.strptime(verlassen[-1],"%d.%m.%Y %H:%M")-datetime.strptime(ankunft[-1],"%d.%m.%Y %H:%M"))
        differenz .append(round((delta).total_seconds()/60))
    print(nachnamen)
    data={"Nachnamen":nachnamen,"Vornamen":vornamen,"Klasse":klasse,"Ankunft":ankunft,"Verlassen":verlassen,"DauerMinuten":differenz,"Kommentar":kommentar}
    df1 = pd.DataFrame(data,columns=['Vornamen','Nachnamen',"Klasse",'Ankunft','Verlassen','DauerMinuten','Kommentar'])
    two_up = Path(__file__).resolve().parents[1]
    print(two_up)
    df1.to_excel(str(two_up)+"/static/output.xlsx",index=False)  # download button
    data=[]
    return render(request, 'htmlseiten/excelexport.html', {'data': data })


def import_excel(request):
    """
    Importiere die Personenliste in die DB-Tabelle Personen
    """
    try:
        Personden_pd=pd.read_excel('Personen.xlsx') # Sollte absoluter Pfad sein
    except:
        Personden_pd=pd.read_excel('/home/admin/Desktop/Personen.xlsx') 


    for index, row in Personden_pd.iterrows():
        print("-------------")
        print("Row",row)
        print("vorname",row["Vorname"],"nachname",row["Nachname"],"klasse",row["Klasse"])
        Personen_Stand=Person(id=index,vorname=row["Vorname"],nachname=row["Nachname"],klasse=row["Klasse"],qr_id=index,ankunft=None)
    Personen_Stand.save()
    return render(request, 'htmlseiten/excelimport.html', {'data': Personen_Stand })


"""
def html_button(request):
    if request.method == "POST":  
        form = TableForm(request.POST)  
        if form.is_valid():  
            num = form.cleaned_data['num']
            return render(request, 'people.html', {'Number':num, 'range': range(1,11)})
    else:  
        form = TableForm()  
    return render(request,'people.html',{'form':form})
"""