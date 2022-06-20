# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Tugas, MataKuliah

# Register your models here.


class TugasInline(admin.TabularInline):
    model = Tugas
    extra = 0
    readonly_fields = ("nama", "kumpul", "desc")
    can_delete = False


@admin.register(Tugas)
class TugasAdmin(admin.ModelAdmin):
    list_display = [
        f.name
        for f in Tugas._meta.get_fields()
        if not f.is_relation and (f.name != "id")
    ]
    list_editable = ["status"]
    pass


@admin.register(MataKuliah)
class MatakuliahAdmin(admin.ModelAdmin):
    list_display = [
        f.name
        for f in MataKuliah._meta.get_fields(include_parents=True)
        if not f.is_relation and (f.name != "id")
    ]
    inlines = [TugasInline]
    pass
