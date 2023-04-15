# Generated by Django 3.1 on 2020-12-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20200910_1608'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='servicedetails',
            index=models.Index(fields=['serviceName', 'serviceType', '-createdAt'], name='services_se_service_c35f66_idx'),
        ),
    ]
