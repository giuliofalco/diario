# Generated by Django 3.2.11 on 2022-04-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OffPcto', '0005_auto_20220414_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aziende',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
