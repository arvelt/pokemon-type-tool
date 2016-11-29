# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from .views import IndexView

urlpatterns = [
    url(r'^v1/pokemons', IndexView.as_view()),
]
