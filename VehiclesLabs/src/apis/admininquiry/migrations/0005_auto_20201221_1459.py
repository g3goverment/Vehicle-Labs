# Generated by Django 3.1 on 2020-12-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admininquiry', '0004_admininquiry_workshopownership'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='admininquiry',
            index=models.Index(fields=['usertype', 'workshopOwnership', 'ownerPhone', 'ownerName', 'garageName', '-createdAt'], name='admininquir_usertyp_fc44c4_idx'),
        ),
    ]
