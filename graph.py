"""Requests-OAuthlib sample for Microsoft Graph """
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.

import requests

import config

auth = config.auth

base_url = 'https://graph.microsoft.com/v1.0/'

url = "https://login.microsoftonline.com/{}/oauth2/v2.0/token".format(auth['tenant_id'])
data = {
    'client_id': auth['client_id'],
    'client_secret': auth['client_secret'],
    'scope': 'https://graph.microsoft.com/.default',
    'grant_type': 'client_credentials'
}

r = requests.post(url, data=data)

if r.status_code == 200:
    token = r.json()['access_token']
    headers = {
        "Authorization": "Bearer " + token}
else:
    raise requests.exceptions.BaseHTTPError("Bad response: " + str(r.status_code) + str(r.content))


# call = 'https://graph.microsoft.com/v1.0/groups/39daa82e-56b3-40c1-a37a-533b293962eb/members'

def get_group_id_list(group_names):
    groups = requests.get(base_url + 'groups', headers=headers).json()['value']
    return {g['displayName']: g['id'] for g in groups if g['displayName'] in group_names}


get_group_id_list(config.groups)
