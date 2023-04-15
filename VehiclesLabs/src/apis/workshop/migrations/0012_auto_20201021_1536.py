# Generated by Django 3.1 on 2020-10-21 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0011_workshopmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopmanager',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshopmanager',
            name='createdBy',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshopmanager',
            name='isDeleted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='workshopmanager',
            name='meta',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='workshopmanager',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workshopmanager',
            name='updatedBy',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshopmanager',
            name='usermanageID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workshopmanager',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
