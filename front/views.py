# -*- coding: utf-8 -*-
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import TypesForm
from .authorize import build_client
from .models import Pokemon, Type, TYPES


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        form = TypesForm(initial={
            'type1': 0,
            'type2': 99,
        })
        client = build_client()
        result = client.spreadsheets().values().get(
            spreadsheetId='1o-EUyH_JOyn_obfq61MHGyjyQkvhHNCsdAt7P9okQDE',
            range='sheet1',

        ).execute()
        # pokemons = [
        #     Pokemon(
        #         hp=255,
        #         attack=100,
        #         defence=100,
        #         sp_attack=100,
        #         so_defence=100,
        #         speed=00,
        #     )
        # ]
        pokemons = result.values
        return self.render_to_response({
            'super_types_names': [],
            'form': form,
            'pokemons': pokemons,
            })

    def post(self, request, *args, **kwargs):
        form = TypesForm(request.POST)
        super_types_names = []
        if form.is_valid():
            type1 = form.cleaned_data['type1']
            type2 = form.cleaned_data['type2']
            if type2 == 99:
                super_type = Type.get_super_effective(type1)
            else:
                super_type = Type.get_super_effective(type1, type2)
            for _type_value in super_type:
                _type_name = [n for v, n in TYPES if v == _type_value][0]
                super_types_names.append(_type_name)
        return self.render_to_response({
            'super_types_names': super_types_names,
            'form': form,
            })
