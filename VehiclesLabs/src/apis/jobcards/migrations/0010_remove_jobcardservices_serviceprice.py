# Generated by Django 3.1 on 2020-09-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0009_jobcardservices_serviceprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcardservices',
            name='servicePrice',
        ),
    ]
