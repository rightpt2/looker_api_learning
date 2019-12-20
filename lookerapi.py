# -*- coding: UTF-8 -*-
import requests
from pprint import pprint as pp
import json
import re
import urllib.request

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class LookerApi(object):

    def __init__(self, token, secret, host):

        self.token = token
        self.secret = secret
        self.host = host

        self.session = requests.Session()
        self.session.verify = False
        self.session.trust_env = False

        self.auth()

    def auth(self):
        url = '{}{}'.format(self.host,'login')
        params = {'client_id':self.token,
                  'client_secret':self.secret}
        r = self.session.post(url,params=params)
        access_token = r.json().get('access_token')
        head = {'Authorization': 'token {}'.format(access_token)}
        self.head = head
        self.session.headers.update(head)
