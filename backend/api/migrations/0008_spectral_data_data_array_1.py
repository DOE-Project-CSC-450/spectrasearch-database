# Generated by Django 2.2.6 on 2019-11-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_spectral_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='spectral_data',
            name='data_array_1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
