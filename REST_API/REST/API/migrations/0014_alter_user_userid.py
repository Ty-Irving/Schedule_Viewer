# Generated by Django 4.0.3 on 2022-04-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0013_alter_user_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
