# Generated by Django 4.2.4 on 2023-10-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0005_alter_aufzeichnungen_kommentar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Anwesenheitsliste",
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
                ("qr_id", models.IntegerField(default=0)),
                ("ankunft", models.DateTimeField(verbose_name="Ankunft")),
                ("verlassen", models.DateTimeField(verbose_name="Verlassen")),
                (
                    "kommentar",
                    models.CharField(max_length=100, verbose_name="Kommentar"),
                ),
            ],
        ),
        migrations.DeleteModel(name="Aufzeichnungen",),
    ]
