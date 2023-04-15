# Generated by Django 3.1 on 2020-09-15 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20200910_1608'),
        ('jobcards', '0019_auto_20200914_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcarddetail',
            name='totalPartsAmount',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='jobcarddetail',
            name='totalServiceAmount',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.CreateModel(
            name='JobcardParts',
            fields=[
                ('jobcardPartsID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('parts', models.CharField(blank=True, max_length=120, null=True)),
                ('partsPrice', models.FloatField(blank=True, max_length=15, null=True)),
                ('partsPrices', models.CharField(blank=True, max_length=120, null=True)),
                ('meta', models.JSONField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False, null=True)),
                ('createdBy', models.CharField(max_length=120)),
                ('updatedBy', models.CharField(max_length=120)),
                ('jobID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobcards.jobcarddetail')),
                ('partsID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.servicedetails')),
            ],
        ),
    ]
