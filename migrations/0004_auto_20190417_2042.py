# Generated by Django 2.0.5 on 2019-04-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billdotcom', '0003_billsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='billsession',
            name='device_id',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='billsession',
            name='mfa_id',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]