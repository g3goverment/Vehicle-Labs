# Generated by Django 3.1 on 2020-10-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorcustomer', '0004_auto_20200923_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorcustomer',
            name='delivered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
