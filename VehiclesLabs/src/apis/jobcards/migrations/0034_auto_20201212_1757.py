# Generated by Django 3.1 on 2020-12-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0033_auto_20201024_1220'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='jobcarddetail',
            index=models.Index(fields=['jobID'], name='jobcards_jo_jobID_31338a_idx'),
        ),
        migrations.AddIndex(
            model_name='jobcarddetail',
            index=models.Index(fields=['jobID'], name='jobID_idx'),
        ),
    ]