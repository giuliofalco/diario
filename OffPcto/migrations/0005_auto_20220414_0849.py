# Generated by Django 3.2.11 on 2022-04-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OffPcto', '0004_alter_aziende_tutor_referente_azienda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aziende',
            name='partita_iva',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='aziende',
            name='sede_comune',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='aziende',
            name='sede_provincia',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='aziende',
            name='settore',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='aziende',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
