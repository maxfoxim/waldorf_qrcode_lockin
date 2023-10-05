from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable, AnwesenheitenTable
from django_tables2 import SingleTableView
#from .forms import PostForm
from django.shortcuts import render
from .forms import TableForm
from polls.models import Anwesenheitsliste, Person

from django.utils import timezone
import datetime
import pytz

import sqlite3
from sqlite3 import Error
def create_connection():
    db_file="db.sqlite3"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



def update_task(conn, task):
    sql = ''' UPDATE polls_person
                SET klasse = ? 
                   WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def insert_task(conn, task):
    sql = ''' CREATE INTO polls_anwesenheitsliste
              VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


class PersonTableView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'


class AnwesenheitslisteView(SingleTableView):
    model = Anwesenheitsliste
    table_class = AnwesenheitenTable
    template_name = 'anwesenheiten.html'

"""
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
"""


def ankommen_speichern(request, id):
    aktuelle_zeit=datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    current_day = timezone.now().day
    # nach ID und aktuellem Tag filtern --> gibt Liste zurück
    Bereits_Eingeloggt=Anwesenheitsliste.objects.filter(qr_id=id).filter(ankunft__day=current_day).values_list("ankunft")
    
    if len(Bereits_Eingeloggt)>0: # Bereits ein Eintrag vorhanden
        pass
    else:
        Datum=Anwesenheitsliste(qr_id=id,ankunft=aktuelle_zeit,verlassen=aktuelle_zeit,kommentar="Test")
        Datum.save()
    
    print("Zeitzone Jetzt",datetime.datetime.now(pytz.timezone('Europe/Berlin')))
 
    meetingData = Anwesenheitsliste.objects.all()
    return render(request, 'hello.html', {'data': meetingData })
  

def verlassen_speichern(request, id):
    aktuelle_zeit=datetime.datetime.now(pytz.timezone('Europe/Berlin'))
    current_day = timezone.now().day
    Ausloggwert=Anwesenheitsliste.objects.get(qr_id=id,ankunft__day=current_day)    
    Ausloggwert.verlassen=aktuelle_zeit
    Ausloggwert.save()
    print("Zeitzone Verlassen",Ausloggwert.verlassen)



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