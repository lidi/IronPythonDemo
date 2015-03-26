import os

import requests

API_TOKEN = "2e365d63958b1c9fb41b714f431bb3925e16c2b5"
API_URL = "https://api.github.com/user/repos"

url = "{}?access_token={}".format(API_URL, API_TOKEN)
req_json = requests.get(url).json()

for repo in req_json:
    print repo['git_url']