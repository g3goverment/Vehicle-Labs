# Generated by Django 3.1 on 2020-09-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countersale', '0008_auto_20200929_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinorServices',
            fields=[
                ('mserviceID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('mserviceName', models.CharField(blank=True, max_length=200, null=True)),
                ('mservicePrice', models.FloatField(blank=True, default=0, null=True)),
                ('meta', models.JSONField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False, null=True)),
                ('createdBy', models.CharField(max_length=120)),
                ('updatedBy', models.CharField(max_length=120)),
            ],
        ),
    ]
