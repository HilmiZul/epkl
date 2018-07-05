# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-20 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permohonan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perihal', models.CharField(default=None, max_length=20)),
                ('nama_instansi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Instansi')),
                ('nama_siswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Siswa')),
            ],
        ),
    ]
