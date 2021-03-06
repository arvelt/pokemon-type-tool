# -*- coding: utf-8 -*-

u"""
こうかはばつぐんだ！：It's super effective!
こうかはいまひとつのようだ…：It's not very effective…
(ポケモン)には効果がないみたいだ…：It doesn't affect (ポケモン)!
"""

TYPES = (
    (99, u'なし'),
    (0, u'ノーマル'),
    (1, u'ほのお'),
    (2, u'みず'),
    (3, u'でんき'),
    (4, u'くさ'),
    (5, u'こおり'),
    (6, u'かくとう'),
    (7, u'どく'),
    (8, u'じめん'),
    (9, u'ひこう'),
    (10, u'エスパー'),
    (11, u'むし'),
    (12, u'いわ'),
    (13, u'ゴースト'),
    (14, u'ドラゴン'),
    (15, u'あく'),
    (16, u'はがね'),
    (17, u'フェアリー'),
)


def type_value_to_name(value):
    for v, n in TYPES:
        if v == value:
            return n
    return TYPES[0][1]


def type_name_to_value(name):
    for v, n in TYPES:
        if n == name:
            return v
    return TYPES[0][0]


def is_valid_range(_type):
    if (0 <= _type and _type <= 17):
        return True
    else:
        return False


class Type(object):

    """No Change!
    If change bellow, change cls.type_table value.
    """
    NORMAL_EFFECT = 0
    SUPER_EFFECT = 1
    FEW_EFFECT = 2
    NOTHING_EFFECT = 9
    """end
    """

    DOUBLE_SUPER_EFFECT = 4
    DOUBLE_FEW_EFFECT = 5

    NORMAL = 0
    FIRE = 1
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHTING = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17

    type_table = [
        [0,0,0,0,0,0,0,0,0,0,0,0,2,9,0,0,2,0],
        [0,2,2,0,1,1,0,0,0,0,0,1,2,0,2,0,1,0],
        [0,1,2,0,2,0,0,0,1,0,0,0,1,0,2,0,0,0],
        [0,0,1,2,2,0,0,0,9,1,0,0,0,0,2,0,0,0],
        [0,2,1,0,2,0,0,2,1,2,0,2,1,0,2,0,0,0],
        [0,2,2,0,1,2,0,0,1,1,0,0,0,0,1,0,0,0],
        [1,0,0,0,0,1,0,2,0,2,2,2,1,9,0,1,1,2],
        [0,0,0,0,1,0,0,2,2,0,0,0,2,2,0,0,9,1],
        [0,1,0,1,2,0,0,1,0,9,0,2,1,0,0,0,1,0],
        [0,0,0,2,1,0,1,0,0,0,0,1,2,0,0,0,2,0],
        [0,0,0,0,0,0,1,1,0,0,2,0,0,0,0,9,2,0],
        [0,2,0,0,1,0,2,2,0,2,1,0,0,2,0,1,2,2],
        [0,1,0,0,0,1,2,0,2,1,0,1,0,0,0,0,2,0],
        [9,0,0,0,0,0,0,0,0,0,1,0,0,1,0,2,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,9],
        [0,0,0,0,0,0,2,0,0,0,1,0,0,1,0,2,0,2],
        [0,2,2,2,0,1,0,0,0,0,0,0,1,0,0,0,2,1],
        [0,2,0,0,0,0,1,2,0,0,0,0,0,0,1,1,2,0],
    ]

    u"""
    return List of int
    """
    @classmethod
    def get_super_effective(cls, type1, type2):
        super_types = []
        for _type in xrange(18):
            if cls.check_effect( _type , type1, type2) == cls.SUPER_EFFECT or cls.check_effect(_type , type1, type2) == cls.DOUBLE_SUPER_EFFECT:
                super_types.append(_type)
        return super_types

    u"""
    return SUPER_EFFECT or NORMAL_EFFECT or FEW_EFFECT or NOTHING_EFFECT
    """
    @classmethod
    def check_effect(cls, _type, target_type1, target_type2):
        if is_valid_range(target_type2):
            return cls._check_effect2(_type, target_type1, target_type2)
        else:
            return cls._check_effect1(_type, target_type1)

    @classmethod
    def _check_effect1(cls, _type, target_type1):
        if (is_valid_range(_type) and is_valid_range(target_type1)):
            return cls.type_table[_type][target_type1]
        else:
            raise ValueError

    @classmethod
    def _check_effect2(cls, _type, target_type1, target_type2):
        if is_valid_range(_type) and is_valid_range(target_type1) and is_valid_range(target_type2):
            pass
        else:
            raise ValueError

        type1 = cls.type_table[_type][target_type1]
        type2 = cls.type_table[_type][target_type2]

        def is_nothing(_type):
            return _type == cls.NOTHING_EFFECT

        def is_super(_type):
            return _type == cls.SUPER_EFFECT

        def is_few(_type):
            return _type == cls.FEW_EFFECT

        if is_nothing(type1) or is_nothing(type2):
            # こうかはない
            return cls.NOTHING_EFFECT
        elif is_super(type1) and is_super(type2):
            # 4倍
            return cls.DOUBLE_SUPER_EFFECT
        elif is_few(type1) and is_few(type2):
            # 1/4倍
            return cls.DOUBLE_FEW_EFFECT
        elif is_super(type1) and is_few(type2):
            # 打ち消し
            return cls.NORMAL_EFFECT
        elif is_super(type2) and is_few(type1):
            # 打ち消し
            return cls.NORMAL_EFFECT
        elif is_super(type1) or is_super(type2):
            # こうかはばつぐん
            return cls.SUPER_EFFECT
        elif is_few(type1) or is_few(type2):
            # こうかはいまひとつ
            return cls.FEW_EFFECT
        else:
            return cls.NORMAL_EFFECT
