# Generated by Django 3.0.5 on 2021-05-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modo_monitor', '0004_auto_20210528_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
