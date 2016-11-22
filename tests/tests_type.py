# -*- coding: utf-8 -*-
from src.main import Type

class TestType(object):
    def test_table_super_effective(self):
        assert Type.type_table[Type.WATER][Type.FIRE] == 1
        assert Type.type_table[Type.FIGHTING][Type.ICE] == 1
        assert Type.type_table[Type.GROUND][Type.POISON] == 1

    def test_table_few_effective(self):
        assert Type.type_table[Type.FIRE][Type.WATER] == 2
        assert Type.type_table[Type.GRASS][Type.FIRE] == 2

    def test_table_nothing_effective(self):
        assert Type.type_table[Type.NORMAL][Type.GHOST] == 9
        assert Type.type_table[Type.ELECTRIC][Type.GROUND] == 9
        assert Type.type_table[Type.FIGHTING][Type.GHOST] == 9
        assert Type.type_table[Type.POISON][Type.STEEL] == 9
        assert Type.type_table[Type.GROUND][Type.FLYING] == 9
        assert Type.type_table[Type.GHOST][Type.NORMAL] == 9
        assert Type.type_table[Type.DRAGON][Type.FAIRY] == 9

    def test_table_normal_effective(self):
        assert Type.type_table[Type.GROUND][Type.GHOST] == Type.NORMAL_EFFECT

    def test_check_effect1(self):
        assert Type.check_effect(Type.ELECTRIC, Type.WATER, Type.FLYING) == Type.DOUBLE_SUPER_EFFECT  # ギャラドスにかみなり
        assert Type.check_effect(Type.ICE, Type.DRAGON, Type.FLYING) == Type.DOUBLE_SUPER_EFFECT  # カイリューにこおり
        assert Type.check_effect(Type.GROUND, Type.GHOST, Type.POISON) == Type.SUPER_EFFECT  # ゲンガーにじめん
        assert Type.check_effect(Type.POISON, Type.GRASS, Type.POISON) == Type.NORMAL_EFFECT  # フシギバナにどく
        assert Type.check_effect(Type.ROCK, Type.STEEL, Type.FLYING) == Type.NORMAL_EFFECT  # エアームドにいわ
        assert Type.check_effect(Type.ELECTRIC, Type.ROCK, Type.GROUND) == Type.NOTHING_EFFECT  # サイドンにじめん
        assert Type.check_effect(Type.DRAGON, Type.WATER, Type.FAIRY) == Type.NOTHING_EFFECT  # マリルリにドラゴン

    def test_get_super_effective(self):
        pass
