# -*- coding: utf-8 -*-
import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.main import Type

class TestType(object):
    def test_get_super_effective(self):
        assert Type.get_super_effective(0, 1) == 0

    def test_get_super_effective(self):
        assert Type.get_super_effective(0, 1) == 0
