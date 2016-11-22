# -*- coding: utf-8 -*-
from src.main import Type

class TestType(object):
    def test_get_super_effective(self):
        assert Type.get_super_effective(0, 1) == 0

    def test_get_super_effective(self):
        assert Type.get_super_effective(0, 1) == 0
