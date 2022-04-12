# Generated by Django 4.0.3 on 2022-04-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0015_remove_schedule_shifts_time_schedule_shifts_endtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Salary',
            field=models.FloatField(default=15.0),
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.CheckConstraint(check=models.Q(('Salary__gte', 0.0), ('Salary__lte', 100000000.0)), name='my_float_constraint'),
        ),
    ]