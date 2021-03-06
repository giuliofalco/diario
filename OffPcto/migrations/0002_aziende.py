# Generated by Django 3.2.11 on 2022-04-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OffPcto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aziende',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partita_iva', models.CharField(max_length=200)),
                ('ragione_sociale', models.CharField(max_length=200)),
                ('tutor_referente_azienda', models.CharField(max_length=200)),
                ('sede_comune', models.CharField(max_length=200)),
                ('sede_provincia', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('settore', models.CharField(max_length=200)),
            ],
        ),
    ]
