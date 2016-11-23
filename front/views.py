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

from .form import TypesForm
from src.main import Type

class IndexView(TemplateView):
    template_name = "index.html"
    _types = [
        {'value': 0, 'name': u'ノーマル'},
        {'value': 1, 'name': u'ほのお'},
        {'value': 2, 'name': u'みず'},
        {'value': 3, 'name': u'でんき'},
        {'value': 4, 'name': u'くさ'},
        {'value': 5, 'name': u'こおり'},
        {'value': 6, 'name': u'かくとう'},
        {'value': 7, 'name': u'どく'},
        {'value': 8, 'name': u'じめん'},
        {'value': 9, 'name': u'ひこう'},
        {'value': 10, 'name': u'エスパー'},
        {'value': 11, 'name': u'むし'},
        {'value': 12, 'name': u'いわ'},
        {'value': 13, 'name': u'ゴースト'},
        {'value': 14, 'name': u'ドラゴン'},
        {'value': 15, 'name': u'あく'},
        {'value': 16, 'name': u'はがね'},
        {'value': 17, 'name': u'フェアリー'},
    ]

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'types': self._types,
            'super_types_names': [],
            'selected1': 0,
            'selected2': 19,
            })

    def post(self, request, *args, **kwargs):
        form = TypesForm(request.POST)
        super_types_names = []
        selected1 = 0
        selected2 = 19
        if form.is_valid():
            type1 = form.cleaned_data['type1']
            type2 = form.cleaned_data['type2']
            if type2 == 19:
                super_type = Type.get_super_effective(type1)
            else:
                super_type = Type.get_super_effective(type1, type2)
            for _type_value in super_type:
                _type = [n for n in self._types if n['value'] == _type_value][0]
                super_types_names.append(_type)
            selected1 = type1
            selected2 = type2
        return self.render_to_response({
            'types': self._types,
            'super_types_names': super_types_names,
            'selected1': selected1,
            'selected2': selected2,
            })
