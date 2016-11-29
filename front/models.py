# -*- coding: utf-8 -*-
import logging

from google.appengine.ext import ndb

from .authorize import build_client

u"""
こうかはばつぐんだ！：It's super effective!
こうかはいまひとつのようだ…：It's not very effective…
(ポケモン)には効果がないみたいだ…：It doesn't affect (ポケモン)!
"""

MAX_POKEMONS = 931  # 総数。フォルム違い、メガシンカ、アローラのすがた
MAX_POKEMONS_NO = 802  # 全国図鑑

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
    super_types = ndb.StringProperty(repeated=True)

    @classmethod
    def key_from_id(cls, _id):
        return ndb.Key(cls, str(_id))

    @classmethod
    def list(cls):
        if cls.exists():
            return cls.list_from_datastore()
        else:
            return cls.list_from_spreadsheet()

    @classmethod
    def exists(cls):
        key = cls.key_from_id(1)
        if key.get():
            return True
        else:
            return False

    @classmethod
    def list_from_spreadsheet(cls):
        _list = cls._list_from_spreadsheet()

        items = []
        for index, pkmn in enumerate(_list):
            if index == 0:
                continue
            _id, no, name, type1, type2, hp, atk, df, spatk, spdf, spd, _sum = pkmn

            _type1 = type_name_to_value(type1)
            _type2 = type_name_to_value(type2)
            super_types = Type.get_super_effective(_type1, _type2)

            super_types_name = []
            for super_type in super_types:
                for v, n in TYPES:
                    if v == super_type:
                        super_types_name.append(n)
                        break

            entity = cls(
                id=_id,
                no=int(no),
                name=name,
                type1=type1,
                type2=type2,
                hp=int(hp),
                attack=int(atk),
                defence=int(df),
                sp_attack=int(spatk),
                sp_defence=int(spdf),
                speed=int(spd),
                sum=int(_sum),
                super_types=super_types_name
            )
            entity.put_async()
            items.append(entity)
        return items

    @classmethod
    def _list_from_spreadsheet(cls):
        logging.debug('call _list_from_spreadsheet')
        client = build_client()
        result = client.spreadsheets().values().get(
            spreadsheetId='1o-EUyH_JOyn_obfq61MHGyjyQkvhHNCsdAt7P9okQDE',
            range='sheet1',
        ).execute()
        return result.get('values', [])

    @classmethod
    def list_from_datastore(cls):
        logging.debug('call list_from_datastore')
        return cls._get_multi_async().get_result()

    @classmethod
    @ndb.tasklet
    def _get_multi_async(cls):
        keys = [cls.key_from_id(v + 1) for v in xrange(MAX_POKEMONS)]
        entityes = yield ndb.get_multi_async(keys)
        raise ndb.Return(entityes)
