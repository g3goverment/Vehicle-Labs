# Generated by Django 3.1 on 2020-12-14 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0034_auto_20201212_1757'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='jobcarddetail',
            name='jobcards_jo_jobID_31338a_idx',
        ),
        migrations.RemoveIndex(
            model_name='jobcarddetail',
            name='jobID_idx',
        ),
    ]
