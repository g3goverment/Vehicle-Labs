# Generated by Django 3.1 on 2020-08-27 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopDetail',
            fields=[
                ('workshopID', models.AutoField(
                    primary_key=True, serialize=False, unique=True)),
                ('workshopname', models.CharField(max_length=12, unique=True)),
                ('workshopemail', models.EmailField(max_length=254)),
                ('workshopphone', models.CharField(max_length=10)),
                ('workshopaddress', models.CharField(max_length=200)),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('userID', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
