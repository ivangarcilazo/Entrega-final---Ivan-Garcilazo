# Generated by Django 5.0.4 on 2024-06-05 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAccount', '0005_delete_userprofile'),
        ('AppKinda', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppAccount.carposts'),
        ),
    ]