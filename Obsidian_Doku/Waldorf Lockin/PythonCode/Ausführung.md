Code ausführen
```python
python manage.py runserver
```


Datenbanken aktualiseren
https://docs.djangoproject.com/en/4.2/intro/tutorial02/

```python
python manage.py makemigrations

python manage.py migrate
```



Terminal DB abfragen:

```python
Test=Anwesenheitsliste.objects.filter(qr_id=1).filter(ankunft__day=3).values_list("ankunft").all()
```
