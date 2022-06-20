# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models


# Create your models here.
class MataKuliah(models.Model):
    nama = models.CharField(max_length=255)
    dosen = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mata Kuliah"
        verbose_name_plural = "Daftar mata Kuliah"

    def __str__(self):
        return self.nama


class Tugas(models.Model):
    nama = models.CharField(max_length=255)
    kumpul = models.DateField()
    status = models.BooleanField()
    matakuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tugas"
        verbose_name_plural = "Daftar Tugas"

    def __str__(self):
        return self.nama
