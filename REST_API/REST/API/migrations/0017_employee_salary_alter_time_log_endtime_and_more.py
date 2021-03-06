# Generated by Django 4.0.3 on 2022-04-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0016_alter_time_log_endtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Salary',
            field=models.FloatField(default=15.0),
        ),
        migrations.AlterField(
            model_name='time_log',
            name='EndTime',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.CheckConstraint(check=models.Q(('Salary__gte', 0.0), ('Salary__lte', 100000000.0)), name='my_float_constraint'),
        ),
    ]
