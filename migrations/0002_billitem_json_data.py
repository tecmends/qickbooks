# Generated by Django 2.0.5 on 2019-04-08 14:09

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('billdotcom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billitem',
            name='json_data',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=False,
        ),
    ]