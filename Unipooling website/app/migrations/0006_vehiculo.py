# Generated by Django 3.2.8 on 2022-03-23 18:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_ruta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('color', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=200)),
            ],
        ),
    ]
