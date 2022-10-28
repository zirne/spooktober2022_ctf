import itertools
import string
import requests

USABLE_CHARS = string.ascii_uppercase
URI = 'http://spooktoberctf.se:22083/clients'


def string_maker(strlen=1):
    return list(set([''.join(x) for x in itertools.permutations([c for c in USABLE_CHARS], strlen)]))

res = []

#for c in string_maker():
#    r = requests.post(URI, {'name[length]': 5})
#    res.append(r)
#    if r.text != '[]':
#        print()

for i in range(1000):
    r = requests.post(URI, {'length': i})
    resp = r.text
    if resp != '[]':
        print()

print()