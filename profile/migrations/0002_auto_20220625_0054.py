# Generated by Django 2.2.28 on 2022-06-24 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]
