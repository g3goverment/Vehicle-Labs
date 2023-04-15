# Generated by Django 3.1 on 2020-10-14 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.apis.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_merge_20201014_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionRecord',
            fields=[
                ('subscriptionID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('timePeriod', models.IntegerField()),
                ('meta', models.JSONField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('expiredAt', models.DateTimeField(default=src.apis.accounts.models.get_expiredAt)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False, null=True)),
                ('isActivated', models.BooleanField(default=True, null=True)),
                ('createdBy', models.CharField(max_length=120)),
                ('updatedBy', models.CharField(max_length=120)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
