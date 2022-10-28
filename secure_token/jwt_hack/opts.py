import requests
import jwt


BASE_URI = 'http://spooktoberctf.se:22081'

JWKS_PATH = f'{BASE_URI}/jwks'
TOKEN_PATH = f'{BASE_URI}/token'
LOGIN_PATH = f'{BASE_URI}/login'

r = []

for p in [JWKS_PATH, TOKEN_PATH, LOGIN_PATH]:
    r.append(requests.options(p))

res = [x.text for x in r]


print()