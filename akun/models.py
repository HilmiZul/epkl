from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Akun(models.Model):
    username = models.ForeignKey(User)
    nama_depan = models.CharField(max_length=10)
    nama_belakang = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nama_depan
