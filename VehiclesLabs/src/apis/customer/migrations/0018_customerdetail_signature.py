# Generated by Django 3.1 on 2020-10-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20201007_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetail',
            name='signature',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]