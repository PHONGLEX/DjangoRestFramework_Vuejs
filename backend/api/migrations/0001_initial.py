# Generated by Django 3.2.6 on 2021-08-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Psi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=10)),
                ('o3_sub_index', models.FloatField(default=0)),
                ('pm10_twenty_four_hourly', models.FloatField(default=0)),
                ('pm10_sub_index', models.FloatField(default=0)),
                ('co_sub_index', models.FloatField(default=0)),
                ('pm25_twenty_four_hourly', models.FloatField(default=0)),
                ('so2_sub_index', models.FloatField(default=0)),
                ('updated_timestamp', models.DateTimeField()),
            ],
            options={
                'ordering': ('-updated_timestamp',),
            },
        ),
    ]
