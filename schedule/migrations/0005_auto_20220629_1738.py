# Generated by Django 2.2.28 on 2022-06-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20220629_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateTimeField(verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
