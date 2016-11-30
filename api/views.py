# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import base

from front.models import Pokemon, MAX_POKEMONS


def id_valid_id(_id):
    if 1 <= int(_id) and int(_id) <= MAX_POKEMONS:
        return True
    else:
        return False


class ListView(base.View):
    def get(self, request, *args, **kwargs):
        pokemons = Pokemon.list()
        res = {
            'items': [e.to_dict() for e in pokemons]
        }
        return HttpResponse(json.dumps(res))


class GetView(base.View):
    def get(self, request, pokemon_id, *args, **kwargs):
        if not id_valid_id(pokemon_id):
            return HttpResponseNotFound(json.dumps({
                'error': {
                    'errors': [{
                        'domain': 'global',
                        'reason': 'notFound',
                        'message': 'Not Found'
                       }],
                    'code': 404,
                    'message': 'Not Found'
                }}))
        entity = Pokemon.get_by_id(pokemon_id)
        res = entity.to_dict()
        return HttpResponse(json.dumps(res))
