# Generated by Django 3.1 on 2020-08-27 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopdetail',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workshopdetail',
            name='workshopname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='workshopdetail',
            name='workshopphone',
            field=models.CharField(max_length=10),
        ),
    ]
