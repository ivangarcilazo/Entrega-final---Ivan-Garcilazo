# Generated by Django 5.0.4 on 2024-06-04 00:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAccount', '0002_rename_user_id_carposts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='carposts',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
