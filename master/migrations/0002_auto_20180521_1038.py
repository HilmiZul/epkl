# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-21 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='kelas',
            field=models.CharField(choices=[('XI RPL 1', 'XI RPL 1'), ('XI RPL 2', 'XI RPL 2'), ('XI RPL 3', 'XI RPL 3'), ('XI.TKJ-1', 'XI.TKJ-1'), ('XI.TKJ-2', 'XI.TKJ-2'), ('XI.TKJ-3', 'XI.TKJ-3'), ('XI.TKJ-4', 'XI.TKJ-4')], max_length=15),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='program_ahli',
            field=models.CharField(choices=[('Teknik Komputer dan Jaringan', 'Teknik Komputer dan Jaringan'), ('Rekayasa Perangkat Lunak', 'Rekayasa Perangkat Lunak')], max_length=30),
        ),
    ]
