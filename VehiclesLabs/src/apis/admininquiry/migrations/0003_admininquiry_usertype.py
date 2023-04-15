# Generated by Django 3.1 on 2020-11-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admininquiry', '0002_admininquiry_garagename'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininquiry',
            name='usertype',
            field=models.CharField(blank=True, choices=[('Vendor', 'vendor'), ('Workshop Owner', 'workshop_owner'), ('Other', 'other')], max_length=128, null=True),
        ),
    ]