# Generated by Django 3.2 on 2021-05-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dispositivos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('mac', models.CharField(max_length=20)),
                ('vendor', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=100)),
                ('osfamily', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('nombre_dispositivo', models.CharField(max_length=40)),
                ('last_seen', models.CharField(max_length=40)),
                ('connected_to', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Dispositivo',
            },
        ),
    ]