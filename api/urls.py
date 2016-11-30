# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from .views import ListView, GetView

urlpatterns = [
    url(r'^v1/pokemons/(?P<pokemon_id>[^/]+)$', GetView.as_view()),
    url(r'^v1/pokemons$', ListView.as_view()),
]
