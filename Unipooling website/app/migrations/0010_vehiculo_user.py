# Generated by Django 3.2.8 on 2022-05-04 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_user_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]