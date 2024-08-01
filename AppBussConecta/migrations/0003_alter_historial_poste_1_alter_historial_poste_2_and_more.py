# Generated by Django 5.0.7 on 2024-07-29 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "AppBussConecta",
            "0002_alter_historial_poste_1_alter_historial_poste_2_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historial",
            name="poste_1",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(1000000),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="historial",
            name="poste_2",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(1000000),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="historial",
            name="poste_3",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(1000000),
                ]
            ),
        ),
    ]