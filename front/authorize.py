# -*- coding: utf-8 -*-
import os

from httplib2 import Http
from apiclient import discovery

from google.appengine.ext import ndb


SCOPE = 'https://www.googleapis.com/auth/spreadsheets.readonly'


def get_credential():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
        from oauth2client.contrib.appengine import AppAssertionCredentials
        return AppAssertionCredentials(SCOPE)
    else:
        from oauth2client.service_account import ServiceAccountCredentials
        key = ndb.Key('SericeAccountToken', 'pkmn-tool-service-account')
        entity = key.get()
        if entity is None:
            return None
        return ServiceAccountCredentials.from_json_keyfile_dict(entity.credential, SCOPE)


def build_client():
    credentials = get_credential()
    http_auth = credentials.authorize(Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    return discovery.build('sheets', 'v4', http=http_auth, discoveryServiceUrl=discoveryUrl)
