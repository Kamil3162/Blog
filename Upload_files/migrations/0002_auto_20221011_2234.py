# Generated by Django 3.2.9 on 2022-10-11 20:34

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Upload_files', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('custom_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]
