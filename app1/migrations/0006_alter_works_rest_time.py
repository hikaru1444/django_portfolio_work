# Generated by Django 4.0.2 on 2022-05-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_works_other_alter_works_rest_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='rest_time',
            field=models.TimeField(default='00:00', verbose_name='休憩'),
        ),
    ]
