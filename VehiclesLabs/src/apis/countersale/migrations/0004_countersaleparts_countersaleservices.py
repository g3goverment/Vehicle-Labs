# Generated by Django 3.1 on 2020-09-28 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20200910_1608'),
        ('workshopinventory', '__first__'),
        ('countersale', '0003_auto_20200928_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounterSaleServices',
            fields=[
                ('countersaleServicesID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('services', models.CharField(blank=True, max_length=120, null=True)),
                ('servicePrice', models.FloatField(blank=True, max_length=15, null=True)),
                ('servicePrices', models.CharField(blank=True, max_length=120, null=True)),
                ('meta', models.JSONField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False, null=True)),
                ('createdBy', models.CharField(max_length=120)),
                ('updatedBy', models.CharField(max_length=120)),
                ('countersaleID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countersale.countersale')),
                ('serviceID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.servicedetails')),
            ],
        ),
        migrations.CreateModel(
            name='CounterSaleParts',
            fields=[
                ('counterSalePartsID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('workshopInventoryIDs', models.CharField(blank=True, max_length=120, null=True)),
                ('partsPrice', models.FloatField(blank=True, max_length=15, null=True)),
                ('partsPrices', models.CharField(blank=True, max_length=120, null=True)),
                ('partQty', models.IntegerField(blank=True, null=True)),
                ('partQtys', models.CharField(blank=True, max_length=120, null=True)),
                ('meta', models.JSONField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False, null=True)),
                ('createdBy', models.CharField(max_length=120)),
                ('updatedBy', models.CharField(max_length=120)),
                ('jobID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='countersale.countersale')),
                ('workshopInventoryID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshopinventory.workshopinventory')),
            ],
        ),
    ]