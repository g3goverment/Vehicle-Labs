# Generated by Django 3.1 on 2020-09-28 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0005_auto_20200910_1646'),
        ('countersale', '0006_remove_countersaleparts_partsprices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countersale',
            name='workshopinventoryID',
        ),
        migrations.AddField(
            model_name='countersale',
            name='workshopID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshop.workshopdetail'),
        ),
    ]
