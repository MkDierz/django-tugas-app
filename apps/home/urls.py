# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('tugas', views.list_tugas, name='tugas_list'),
    path('tugas/create', views.create_tugas, name='tugas_create'),
    path('tugas/<tugas_id>', views.get_tugas, name='tugas_get'),
    path('tugas/<tugas_id>/delete', views.delete_tugas, name='tugas_delete'),
    path('tugas/<tugas_id>/update', views.edit_tugas, name='tugas_edit'),
    path('tugas/<tugas_id>/done', views.mark_as_done, name='tugas_done'),

    path('mk', views.list_mk, name='mk_list'),
    path('mk/create', views.create_mk, name='mk_create'),
    path('mk/<mk_id>', views.get_mk, name='mk_get'),
    path('mk/<mk_id>/delete', views.delete_mk, name='mk_delete'),
    path('mk/<mk_id>/update', views.edit_mk, name='mk_edit'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
