# Generated by Django 3.1 on 2020-11-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0011_merge_20201112_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestedparts',
            name='partMedia',
            field=models.JSONField(null=True),
        ),
    ]
