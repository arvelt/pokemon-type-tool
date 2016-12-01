# -*- coding: utf-8 -*-
import logging

from google.appengine.ext import ndb

from .authorize import build_client

MAX_POKEMONS = 931  # 総数。フォルム違い、メガシンカ、アローラのすがた
MAX_POKEMONS_NO = 802  # 全国図鑑


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
    def get_by_id(cls, _id):
        key = cls.key_from_id(_id)
        return key.get()

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

    def to_dict(self):
        return {
            'id': int(self.key.id()),
            'no': self.no,
            'name': self.name,
            'type1': self.type1,
            'type2': self.type2,
            'hp': self.hp,
            'attack': self.attack,
            'defence': self.defence,
            'sp_attack': self.sp_attack,
            'sp_defence': self.sp_defence,
            'speed': self.speed,
            'sum': self.sum,
            'super_types': self.super_types,
            }
