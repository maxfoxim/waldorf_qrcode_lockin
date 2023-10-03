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
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE polls_person
                SET klasse = ? 
                   WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def insert_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
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
    Datum=Anwesenheitsliste(qr_id=id,ankunft=datetime.datetime.now(pytz.timezone('Europe/Berlin')),verlassen=timezone.now(),kommentar="Test")
    Datum.save()
    print("Zeitzone Jetzt",datetime.datetime.now(pytz.timezone('Europe/Berlin')))
    #conn=create_connection()
    #update_task(conn, ("10x",id))    

def verlassen_speichern(request, id):
    conn=create_connection()
    update_task(conn, ("10x",id))   

def html_button(request):
    if request.method == "POST":  
        form = TableForm(request.POST)  
        if form.is_valid():  
            num = form.cleaned_data['num']
            return render(request, 'people.html', {'Number':num, 'range': range(1,11)})
    else:  
        form = TableForm()  
    return render(request,'people.html',{'form':form})