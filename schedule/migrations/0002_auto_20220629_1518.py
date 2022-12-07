# Generated by Django 2.2.28 on 2022-06-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountManagement', '0002_itlgroup_group'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='category',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='group',
        ),
        migrations.AddField(
            model_name='training',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.Category'),
        ),
        migrations.AddField(
            model_name='training',
            name='group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='accountManagement.ITLGroup'),
        ),
    ]
