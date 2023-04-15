# Generated by Django 3.1 on 2020-09-30 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
        ('parts', '0006_auto_20200923_1213'),
        ('workshop', '0005_auto_20200910_1646'),
        ('vendorinventory', '0005_vendorinventory_excel_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopInventory',
            fields=[
                ('workshopInventoryID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('workshopPartQty', models.IntegerField(blank=True, null=True)),
                ('min_qty', models.IntegerField(blank=True, default=5, null=True)),
                ('workshopPartPrice', models.FloatField(max_length=10, null=True)),
                ('meta', models.JSONField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False, null=True)),
                ('createdBy', models.CharField(max_length=120)),
                ('updatedBy', models.CharField(max_length=120)),
                ('partID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parts.partdetails')),
                ('vendorID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.vendordetail')),
                ('vendorInventoryID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendorinventory.vendorinventory')),
                ('workshopID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshop.workshopdetail')),
            ],
        ),
    ]
