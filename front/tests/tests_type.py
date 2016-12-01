# -*- coding: utf-8 -*-
from front.models import Type


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

    def test_check_effect(self):
        assert Type.check_effect(Type.ELECTRIC, Type.WATER, Type.FLYING) == Type.DOUBLE_SUPER_EFFECT  # ギャラドスにかみなり
        assert Type.check_effect(Type.ICE, Type.DRAGON, Type.FLYING) == Type.DOUBLE_SUPER_EFFECT  # カイリューにこおり
        assert Type.check_effect(Type.GROUND, Type.GHOST, Type.POISON) == Type.SUPER_EFFECT  # ゲンガーにじめん
        assert Type.check_effect(Type.POISON, Type.GRASS, Type.POISON) == Type.NORMAL_EFFECT  # フシギバナにどく
        assert Type.check_effect(Type.ROCK, Type.STEEL, Type.FLYING) == Type.NORMAL_EFFECT  # エアームドにいわ
        assert Type.check_effect(Type.ELECTRIC, Type.ROCK, Type.GROUND) == Type.NOTHING_EFFECT  # サイドンにじめん
        assert Type.check_effect(Type.DRAGON, Type.WATER, Type.FAIRY) == Type.NOTHING_EFFECT  # マリルリにドラゴン

        # オニドリルに？
        assert Type.check_effect(Type.FIGHTING, Type.NORMAL, Type.FLYING) == Type.NORMAL_EFFECT
        assert Type.check_effect(Type.ELECTRIC, Type.NORMAL, Type.FLYING) == Type.SUPER_EFFECT
        assert Type.check_effect(Type.ICE, Type.NORMAL, Type.FLYING) == Type.SUPER_EFFECT
        assert Type.check_effect(Type.ROCK, Type.NORMAL, Type.FLYING) == Type.SUPER_EFFECT
        assert Type.check_effect(Type.GRASS, Type.NORMAL, Type.POISON) == Type.FEW_EFFECT

        # フシギバナに？
        assert Type.check_effect(Type.GROUND, Type.GRASS, Type.POISON) == Type.NORMAL_EFFECT

    def test_get_super_effective1(self):
        assert Type.get_super_effective(Type.NORMAL, 99) == [Type.FIGHTING]
        assert Type.get_super_effective(Type.FIRE, 99) == [Type.WATER, Type.GROUND, Type.ROCK]
        assert Type.get_super_effective(Type.WATER, 88) == [Type.ELECTRIC, Type.GRASS]
        assert Type.get_super_effective(Type.ELECTRIC, None) == [Type.GROUND]
        assert Type.get_super_effective(Type.GRASS, []) == [Type.FIRE, Type.ICE, Type.POISON, Type.FLYING, Type.BUG]
        assert Type.get_super_effective(Type.ICE, 99) == [Type.FIRE, Type.FIGHTING, Type.ROCK, Type.STEEL]
        assert Type.get_super_effective(Type.FIGHTING, 99) == [Type.FLYING, Type.PSYCHIC, Type.FAIRY]
        assert Type.get_super_effective(Type.POISON, 88) == [Type.GROUND, Type.PSYCHIC]
        assert Type.get_super_effective(Type.GROUND, None) == [Type.WATER, Type.GRASS, Type.ICE]
        assert Type.get_super_effective(Type.FLYING, 88) == [Type.ELECTRIC, Type.ICE, Type.ROCK]
        assert Type.get_super_effective(Type.PSYCHIC, 99) == [Type.BUG, Type.GHOST, Type.DARK]
        assert Type.get_super_effective(Type.BUG, None) == [Type.FIRE, Type.FLYING, Type.ROCK]
        assert Type.get_super_effective(Type.GHOST, None) == [Type.GHOST, Type.DARK]
        assert Type.get_super_effective(Type.DRAGON, 99) == [Type.ICE, Type.DRAGON, Type.FAIRY]
        assert Type.get_super_effective(Type.DARK, 99) == [Type.FIGHTING, Type.BUG, Type.FAIRY]
        assert Type.get_super_effective(Type.STEEL, 88) == [Type.FIRE, Type.FIGHTING, Type.GROUND]
        assert Type.get_super_effective(Type.FAIRY, 99) == [Type.POISON, Type.STEEL]

    def test_get_super_effective2(self):
        assert Type.get_super_effective(Type.NORMAL, Type.FLYING) == [Type.ELECTRIC, Type.ICE, Type.ROCK]  # オニドリル
        assert Type.get_super_effective(Type.GRASS, Type.POISON) == [Type.FIRE, Type.ICE, Type.FLYING, Type.PSYCHIC]  # フシギバナ
        assert Type.get_super_effective(Type.DRAGON, Type.FLYING) == [Type.ICE, Type.ROCK, Type.DRAGON, Type.FAIRY]  # カイリュー
        assert Type.get_super_effective(Type.GRASS, Type.BUG) == [Type.FIRE, Type.ICE, Type.POISON, Type.FLYING, Type.BUG, Type.ROCK]  # パラセクト
        assert Type.get_super_effective(Type.ROCK, Type.GROUND) == [Type.WATER, Type.GRASS, Type.ICE, Type.FIGHTING, Type.GROUND, Type.STEEL]  # イワーク
        assert Type.get_super_effective(Type.GHOST, Type.POISON) == [Type.GROUND, Type.PSYCHIC, Type.GHOST, Type.DARK]  # ゲンガー
