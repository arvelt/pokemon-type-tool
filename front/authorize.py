
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from apiclient import discovery

from google.appengine.ext import ndb

def build_client():
    key = ndb.Key('SericeAccountToken', 'pkmn-tool-service-account')
    entity = key.get()
    if entity is None:
        return None
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(entity.credential, scope)
    http_auth = credentials.authorize(Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    return discovery.build('sheets', 'v4', http=http_auth, discoveryServiceUrl=discoveryUrl)
