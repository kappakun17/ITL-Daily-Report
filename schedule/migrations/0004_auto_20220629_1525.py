# Generated by Django 2.2.28 on 2022-06-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20220629_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='memo',
            new_name='staff_memo',
        ),
        migrations.AddField(
            model_name='schedule',
            name='traineer_memo',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='memo'),
        ),
    ]
