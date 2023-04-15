# Generated by Django 3.1 on 2020-08-29 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0004_auto_20200827_1733'),
        ('fueltype', '0002_auto_20200827_1644'),
        ('vehicles', '0004_remove_vehiclesdetail_cusid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehiclebrands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCardDetail',
            fields=[
                ('jobID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('brandID', models.ForeignKey(default=150, on_delete=django.db.models.deletion.CASCADE, to='vehiclebrands.vehiclebrand')),
                ('cusID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customerdetail')),
                ('fueltypeID', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='fueltype.fueltype')),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicleID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehiclesdetail')),
            ],
        ),
    ]
