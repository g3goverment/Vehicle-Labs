# Generated by Django 3.1 on 2020-09-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countersale', '0002_auto_20200928_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countersale',
            name='partID',
        ),
        migrations.RemoveField(
            model_name='countersale',
            name='seviceID',
        ),
    ]
