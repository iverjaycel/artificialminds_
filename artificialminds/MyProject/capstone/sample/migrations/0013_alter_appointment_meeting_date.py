# Generated by Django 4.0.1 on 2022-04-08 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0012_alter_appointment_meeting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='meeting_date',
            field=models.DateField(default=datetime.datetime(2022, 4, 8, 16, 53, 0, 714273)),
        ),
    ]
