# Generated by Django 4.0.3 on 2022-04-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FName', models.CharField(max_length=35)),
                ('LName', models.CharField(max_length=35)),
                ('Location', models.CharField(max_length=255)),
                ('DNo', models.IntegerField(null=True)),
                ('UserUsername', models.CharField(max_length=255)),
            ],
        ),
    ]
