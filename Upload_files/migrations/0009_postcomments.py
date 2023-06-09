# Generated by Django 3.2.16 on 2022-12-18 11:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Upload_files', '0008_auto_20221110_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateField(default=datetime.datetime(2022, 12, 18, 12, 5, 46, 342561))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Upload_files.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
