# Generated by Django 4.0.3 on 2022-04-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_schedule_shifts_schedule_shifts_schedulepk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='API.user'),
        ),
        migrations.CreateModel(
            name='REQUEST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('RequestedChange', models.CharField(blank=True, max_length=255, null=True)),
                ('EmpID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.employee')),
                ('ResolvingMgrID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.manager')),
                ('ScheduleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.schedule')),
            ],
        ),
        migrations.AddConstraint(
            model_name='request',
            constraint=models.UniqueConstraint(fields=('EmpID', 'Date', 'Time'), name='RequestPK'),
        ),
    ]
