# Generated by Django 3.2.11 on 2022-03-14 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0009_alter_diario_note'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diario',
            options={'ordering': ['data']},
        ),
        migrations.AlterField(
            model_name='diario',
            name='data',
            field=models.DateField(default=datetime.date(2022, 3, 14), unique=True),
        ),
    ]
