# Generated by Django 3.1 on 2020-09-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0008_auto_20200908_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcardservices',
            name='servicePrice',
            field=models.FloatField(blank=True, max_length=15, null=True),
        ),
    ]
