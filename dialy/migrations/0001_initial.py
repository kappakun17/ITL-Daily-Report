# Generated by Django 2.2.28 on 2022-07-04 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0006_auto_20220704_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfactionLevel', models.IntegerField(max_length=100)),
                ('comment', models.TextField(max_length=800)),
                ('is_public', models.BooleanField(default=False)),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Schedule')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]