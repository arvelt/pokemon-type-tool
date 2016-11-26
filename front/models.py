# -*- coding: utf-8 -*-
import logging

from google.appengine.ext import ndb

from .authorize import build_client

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
    (17, u'ようせい'),
)


class Type(object):

    """No Change!
    If change bellow, change cls.type_table value.
    """
    NORMAL_EFFECT = 0
    SUPER_EFFECT = 1
    FEW_EFFECT = 2
    """end
    """

    NOTHING_EFFECT = 9
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
    def get_super_effective(cls, *args):
        length = len(args)
        if length == 1:
            target_type1 = args[0]
            super_types = []
            for _type in xrange(18):
                if cls.check_effect( _type , target_type1) == cls.SUPER_EFFECT or cls.check_effect(_type , target_type1) == cls.DOUBLE_SUPER_EFFECT:
                    super_types.append(_type)
            return super_types
        if length == 2:
            target_type1 = args[0]
            target_type2 = args[1]
            super_types = []
            for _type in xrange(18):
                if cls.check_effect( _type , target_type1, target_type2) == cls.SUPER_EFFECT or cls.check_effect(_type , target_type1, target_type2) == cls.DOUBLE_SUPER_EFFECT:
                    super_types.append(_type)
            return super_types

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
        else:
            raise TypeError('check_effect() takes less than 4 arguments')


class Pokemon(ndb.Model):
    no = ndb.IntegerProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)
    type1 = ndb.StringProperty(indexed=True)
    type2 = ndb.StringProperty(indexed=True)
    hp = ndb.IntegerProperty()
    attack = ndb.IntegerProperty()
    defence = ndb.IntegerProperty()
    sp_attack = ndb.IntegerProperty()
    sp_defence = ndb.IntegerProperty()
    speed = ndb.IntegerProperty()
    sum = ndb.IntegerProperty()

    @classmethod
    def find_all(cls):
        client = build_client()
        result = client.spreadsheets().values().get(
            spreadsheetId='1o-EUyH_JOyn_obfq61MHGyjyQkvhHNCsdAt7P9okQDE',
            range='sheet1',

        ).execute()

        items = []
        for index, pkmn in enumerate(result.get('values', [])):
            if index == 0:
                continue
            no, name, type1, type2, hp, atk, df, spatk, spdf, spd, _sum = pkmn
            items.append(cls(
                no=int(no),
                name=name,
                type1=type1,
                type2=type2,
                attack=int(atk),
                defence=int(df),
                sp_attack=int(spatk),
                sp_defence=int(spdf),
                speed=int(spd),
                sum=int(_sum),
            ))
        return items

class SericeAccountToken(ndb.Model):
    credential = ndb.JsonProperty()
