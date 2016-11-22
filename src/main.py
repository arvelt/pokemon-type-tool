# -*- coding: utf-8 -*-

u"""
こうかはばつぐんだ！：It's super effective!
こうかはいまひとつのようだ…：It's not very effective…
(ポケモン)には効果がないみたいだ…：It doesn't affect (ポケモン)!
"""
NORMAL_EFFECT = 0
SUPER_EFFECT = 1
FEW_EFFECT = 2
NOTHING_EFFECT = 9

NOMAL = 0
FIRE = 1
WATER = 2
GRASS = 3
ELECTRIC = 4
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

class Type(object):
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
    def check_effect(cls, type, target_type1, target_type2):
        return 0
