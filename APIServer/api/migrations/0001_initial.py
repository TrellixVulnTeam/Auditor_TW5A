# Generated by Django 3.2 on 2021-05-24 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='access_point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essid', models.CharField(max_length=40)),
                ('bssid', models.CharField(max_length=40)),
                ('encriptacion', models.CharField(max_length=40)),
                ('spectrum', models.CharField(max_length=20)),
                ('rates', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=50)),
                ('channel_bandwidth', models.CharField(max_length=30)),
                ('cipher', models.CharField(max_length=30)),
                ('suite', models.CharField(max_length=30)),
                ('deauth_last_seen', models.CharField(max_length=50)),
                ('deauth_first_seen', models.CharField(max_length=50)),
                ('signal_quality', models.IntegerField()),
                ('central_channel', models.IntegerField()),
                ('fspl', models.IntegerField()),
                ('rssi', models.IntegerField()),
                ('canal', models.IntegerField()),
                ('frecuencia', models.IntegerField()),
                ('beacons', models.IntegerField()),
                ('deauth_frames', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Access Point',
            },
        ),
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
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connected_to', models.CharField(max_length=40)),
                ('mac_device', models.CharField(max_length=40)),
                ('manufacturer', models.CharField(max_length=50)),
                ('ap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.access_point')),
            ],
            options={
                'verbose_name': 'Device',
            },
        ),
    ]
