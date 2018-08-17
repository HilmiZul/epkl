from __future__ import unicode_literals
from django.db import models

from master.models import Siswa, Pembimbing

# Create your models here.
class KaryaIlmiah(models.Model):
    nama = models.ForeignKey(Siswa)
    judul = models.TextField()
    tanggal_acc = models.DateField()
    pembimbing = models.ForeignKey(Pembimbing)

    def __unicode__(self):
        return self.judul
