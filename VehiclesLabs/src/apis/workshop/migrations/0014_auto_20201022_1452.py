# Generated by Django 3.1 on 2020-10-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0013_auto_20201022_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopdetail',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workshopdetail',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
