# Generated by Django 3.1 on 2020-09-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobcards', '0013_merge_20200910_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcardservices',
            name='isDeleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]