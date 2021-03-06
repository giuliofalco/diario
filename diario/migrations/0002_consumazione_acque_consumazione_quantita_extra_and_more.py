# Generated by Django 4.0.2 on 2022-02-24 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumazione',
            name='acque',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='consumazione',
            name='quantita_extra',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='categoria',
            field=models.IntegerField(choices=[(0, 'Altro'), (1, 'Latticini'), (2, 'Cereali'), (3, 'Pane'), (4, 'Pasta'), (5, 'Carni'), (6, 'Legumi'), (7, 'Dolci'), (8, 'Patate'), (9, 'Bevande'), (10, 'Pesce')], default=0),
        ),
        migrations.AlterField(
            model_name='diario',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 24, 19, 43, 24, 499736, tzinfo=utc)),
        ),
    ]
