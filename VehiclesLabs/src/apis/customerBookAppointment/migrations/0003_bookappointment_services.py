# Generated by Django 3.1 on 2020-09-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerBookAppointment', '0002_appointservices_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='services',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
