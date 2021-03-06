# Generated by Django 4.0.3 on 2022-04-06 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_alter_user_dno_schedule_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='SCHEDULE_SHIFTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('ScheduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.schedule')),
            ],
        ),
        migrations.AddConstraint(
            model_name='schedule_shifts',
            constraint=models.UniqueConstraint(fields=('ScheduleID', 'Date'), name='SchedulePK'),
        ),
    ]
