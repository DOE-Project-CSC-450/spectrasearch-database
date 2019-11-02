# Generated by Django 2.2.6 on 2019-11-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191102_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReflectionGeometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=5)),
                ('GeoKey', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Spectral_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Spectral_Distribution_Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpectralSearchID', models.IntegerField()),
                ('SpectralQuantity', models.CharField(max_length=13)),
                ('ReflectionGeometry', models.CharField(max_length=5)),
                ('TransmissionGeometry', models.CharField(max_length=5)),
                ('BandwidthFWHM', models.DecimalField(decimal_places=6, max_digits=6)),
                ('BandwidthCorrected', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SpectralQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=13)),
                ('SpectralQKey', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionGeometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=5)),
                ('TranKey', models.IntegerField()),
            ],
        ),
    ]
