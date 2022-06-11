# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MataKuliah(models.Model):
    nama = models.CharField(max_length=255)
    dosen = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tugas(models.Model):
    nama = models.CharField(max_length=255)
    kumpul = models.DateField()
    status = models.BooleanField()
    matakuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
