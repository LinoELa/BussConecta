# Generated by Django 5.0.7 on 2024-08-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppBussConecta", "0005_set_default_for_poste2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historial",
            name="tiempo_creado",
        ),
        migrations.AlterField(
            model_name="historial",
            name="poste_1",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="historial",
            name="poste_2",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="historial",
            name="poste_3",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
