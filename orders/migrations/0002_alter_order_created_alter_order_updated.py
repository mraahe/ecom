# Generated by Django 4.2.7 on 2023-12-25 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 1, 55, 36, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 29, 1, 55, 36, tzinfo=datetime.timezone.utc)),
        ),
    ]