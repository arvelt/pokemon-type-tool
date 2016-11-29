# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.generic import base

from front.models import Pokemon

class IndexView(base.View):
    def get(self, request, *args, **kwargs):
        pokemons = Pokemon.list()
        res = {
            'items': [e.to_dict() for e in pokemons]
        }
        return HttpResponse(json.dumps(res))
