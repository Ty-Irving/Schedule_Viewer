# Generated by Django 4.0.3 on 2022-04-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0015_remove_schedule_shifts_time_schedule_shifts_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_log',
            name='EndTime',
            field=models.TimeField(default=None, null=True),
        ),
    ]
