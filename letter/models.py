from __future__ import unicode_literals
from django.db import models

from master.models import Siswa, Instansi, InstansiTKJ

# Create your models here.
class Permohonan(models.Model):
    perihal = models.CharField(max_length=200, default=None)
    nama_siswa = models.ForeignKey(Siswa)
    nama_instansi = models.ForeignKey(Instansi)

    def __unicode__(self):
        return self.perihal

class PermohonanTKJ(models.Model):
    perihal = models.CharField(max_length=200, default=None)
    nama_siswa = models.ForeignKey(Siswa)
    nama_instansi = models.ForeignKey(InstansiTKJ)

    def __unicode__(self):
        return self.perihal
