# Generated by Django 2.2.28 on 2022-06-16 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'ITLユーザー', 'verbose_name_plural': 'ITLユーザー群'},
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date time'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='no-mail', max_length=250, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='no-firstname', max_length=100, verbose_name='first name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='no-lastname', max_length=100, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='user',
            table='user_model',
        ),
    ]
