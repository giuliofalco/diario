# Generated by Django 4.0.2 on 2022-02-25 20:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0002_consumazione_acque_consumazione_quantita_extra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 20, 48, 27, 963326, tzinfo=utc), unique=True),
        ),
        migrations.AddConstraint(
            model_name='consumazione',
            constraint=models.UniqueConstraint(fields=('tipo_pasto', 'diario'), name='pasto_unico'),
        ),
    ]
