# Generated by Django 3.1 on 2020-09-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_auto_20200918_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediadetails',
            name='mediaFor',
            field=models.CharField(blank=True, choices=[('User Profile', 'USER_PROFILE'), ('Workshop Profile', 'WORKSHOP_PROFILE')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='mediadetails',
            name='mediaType',
            field=models.CharField(blank=True, choices=[('Image', 'Image'), ('Video', 'Video')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='mediadetails',
            name='mediaURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
