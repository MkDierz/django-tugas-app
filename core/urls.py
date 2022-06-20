# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from baton.autodiscover import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("baton/", include("baton.urls")),
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls")),
]
