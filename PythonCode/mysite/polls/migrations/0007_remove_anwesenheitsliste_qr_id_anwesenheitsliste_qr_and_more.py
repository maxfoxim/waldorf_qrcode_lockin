# Generated by Django 4.2.4 on 2023-10-14 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_anwesenheitsliste_delete_aufzeichnungen"),
    ]

    operations = [
        migrations.RemoveField(model_name="anwesenheitsliste", name="qr_id",),
        migrations.AddField(
            model_name="anwesenheitsliste",
            name="qr",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.person",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="person",
            name="ankunft",
            field=models.DateTimeField(default="2023-01-01 12:00:00.000000", verbose_name="Ankunft"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="person",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="person",
            name="klasse",
            field=models.CharField(max_length=3, verbose_name="Klasse"),
        ),
        migrations.DeleteModel(name="Choice",),
        migrations.DeleteModel(name="Question",),
    ]
