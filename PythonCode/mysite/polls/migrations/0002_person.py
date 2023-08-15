# Generated by Django 4.2.4 on 2023-08-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vorname", models.CharField(max_length=100, verbose_name="Vorname")),
                ("nachname", models.CharField(max_length=100, verbose_name="Nachname")),
                ("klasse", models.CharField(max_length=2, verbose_name="Klasse")),
                ("qr_id", models.IntegerField(default=0)),
            ],
        ),
    ]
