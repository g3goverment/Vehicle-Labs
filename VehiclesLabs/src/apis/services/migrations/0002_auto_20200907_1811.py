# Generated by Django 3.1 on 2020-09-07 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedetails',
            old_name='serviceMRP',
            new_name='servicePrice',
        ),
    ]