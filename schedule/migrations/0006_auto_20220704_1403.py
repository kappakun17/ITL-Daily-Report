# Generated by Django 2.2.28 on 2022-07-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20220629_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='staff_memo',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='staff memo'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='traineer_memo',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='traineer memo'),
        ),
    ]