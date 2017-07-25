# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-25 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('friend_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='name',
        ),
        migrations.AddField(
            model_name='friends',
            name='friend_id',
            field=models.ManyToManyField(related_name='friendid', to='login_app.Users'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='user',
            field=models.ManyToManyField(related_name='friend', to='login_app.Users'),
        ),
    ]