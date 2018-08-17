from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Siswa(models.Model):
    kelas_choices = (
        ('XII.RPL-1', 'XII.RPL-1'),
        ('XII.RPL-2', 'XII.RPL-2'),
        ('XII.RPL-3', 'XII.RPL-3'),
        ('XII.TKJ-1', 'XII.TKJ-1'),
        ('XII.TKJ-2', 'XII.TKJ-2'),
        ('XII.TKJ-3', 'XII.TKJ-3'),
        ('XII.TKJ-4', 'XII.TKJ-4'),
    )

    program_choices = (
        ('Teknik Komputer dan Jaringan', 'Teknik Komputer dan Jaringan'),
        ('Rekayasa Perangkat Lunak', 'Rekayasa Perangkat Lunak'),
    )

    NIS = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=15, choices=kelas_choices)
    program_ahli = models.CharField(max_length=30, choices=program_choices)
    pkl = models.BooleanField(default=False)
    status_judul = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nama

class Instansi(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __unicode__(self):
        return self.nama

class InstansiTKJ(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __unicode__(self):
        return self.nama

class Pembimbing(models.Model):
    jurusan_choices = (
        ('TKJ', 'TKJ'),
        ('RPL', 'RPL'),
    )

    nama = models.CharField(max_length=40)
    jurusan = models.CharField(max_length=3, choices=jurusan_choices)

    def __unicode__(self):
        return self.nama
