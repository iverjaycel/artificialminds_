# Generated by Django 3.2.7 on 2022-03-23 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 23, 15, 39, 12, 749481)),
        ),
    ]
