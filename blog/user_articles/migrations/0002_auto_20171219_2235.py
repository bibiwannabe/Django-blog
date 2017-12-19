# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20171219_0835'),
        ('user_articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='artical',
            old_name='gclick',
            new_name='click',
        ),
        migrations.AddField(
            model_name='comment',
            name='aid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_articles.Artical'),
        ),
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo'),
        ),
    ]