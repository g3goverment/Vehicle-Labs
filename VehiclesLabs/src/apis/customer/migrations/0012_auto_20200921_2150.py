# Generated by Django 3.1 on 2020-09-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20200915_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='cusaddress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='cusemail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
