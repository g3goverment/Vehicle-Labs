# Generated by Django 3.1 on 2020-09-08 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicedetails_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedetails',
            name='userID',
        ),
    ]