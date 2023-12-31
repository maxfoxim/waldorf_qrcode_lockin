# Generated by Django 4.2.4 on 2023-10-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aufzeichnungen",
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
                ("ankunft", models.DateField(verbose_name="Ankunft")),
                ("verlassen", models.DateField(verbose_name="Verlassen")),
                ("kommentar", models.CharField(max_length=2, verbose_name="Kommentar")),
            ],
        ),
    ]
