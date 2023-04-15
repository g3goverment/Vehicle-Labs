# Generated by Django 3.1 on 2020-12-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorsalecard', '0005_auto_20201209_1106'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='vendorpartsale',
            index=models.Index(fields=['-createdAt'], name='vendorsalec_created_2015fd_idx'),
        ),
        migrations.AddIndex(
            model_name='vendorsalecard',
            index=models.Index(fields=['deliveredAt', '-createdAt'], name='vendorsalec_deliver_2f6e99_idx'),
        ),
    ]
