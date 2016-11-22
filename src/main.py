# -*- coding: utf-8 -*-

u"""
こうかはばつぐんだ！：It's super effective!
こうかはいまひとつのようだ…：It's not very effective…
(ポケモン)には効果がないみたいだ…：It doesn't affect (ポケモン)!
"""

class Type(object):
    NORMAL_EFFECT = 0
    SUPER_EFFECT = 1
    FEW_EFFECT = 2
    DOUBLE_SUPER_EFFECT = 4
    NOTHING_EFFECT = 9

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
    def get_super_effective(cls, target_type1, target_type2):
        return 0

    u"""
    return True or False or None
    """
    @classmethod
    def check_effect(cls, _type, *args):
        length = len(args)
        if length == 1:
            target_type1 = args[0]
            return cls.type_table[_type][target_type1]
        elif length == 2:
            target_type1 = args[0]
            target_type2 = args[1]
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
            elif is_super(type1) and is_few(type2):
                # 打ち消し
                return cls.NORMAL
            elif is_super(type2) and is_few(type1):
                # 打ち消し
                return cls.NORMAL
            elif is_super(type1) or is_super(type2):
                # こうかはばつぐん
                return cls.SUPER_EFFECT
            elif is_few(type1) or is_few(type2):
                # こうかはいまひとつ
                return cls.SUPER_EFFECT
            else:
                return cls.NORMAL_EFFECT
        else:
            raise TypeError('check_effect() takes less than 4 arguments')
