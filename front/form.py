# -*- coding: utf-8 -*-

from django import forms
from src.main import TYPES

class TypesForm(forms.Form):
    type1=forms.TypedChoiceField(choices=TYPES, coerce=lambda v:int(v))
    type2=forms.TypedChoiceField(choices=TYPES, coerce=lambda v:int(v))
