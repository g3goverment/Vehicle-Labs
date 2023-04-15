# Generated by Django 3.1 on 2020-12-04 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting_software', '0002_auto_20201203_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounting',
            name='workshopUserID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workshop_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accounting',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_user', to=settings.AUTH_USER_MODEL),
        ),
    ]