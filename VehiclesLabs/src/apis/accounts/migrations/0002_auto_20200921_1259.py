# Generated by Django 3.1 on 2020-09-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='utype',
            field=models.CharField(blank=True, choices=[('Admin', 'admin'), ('Workshop Owner', 'workshop_owner'), ('Vendor', 'vendor')], max_length=128, null=True),
        ),
    ]
