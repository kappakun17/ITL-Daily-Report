# Generated by Django 2.2.28 on 2022-06-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itlgroup',
            name='group',
            field=models.PositiveSmallIntegerField(default=15, unique=True, verbose_name='th'),
            preserve_default=False,
        ),
    ]
