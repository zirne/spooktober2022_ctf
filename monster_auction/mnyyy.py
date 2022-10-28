import string
import itertools
import requests
import urllib.parse

CHARS = string.ascii_letters
NUMS = string.digits
SPECIALS = "_-%*\\/"

USABLE_CHARS = f'{CHARS}{NUMS}{SPECIALS}'

def urlencode(string):
    if isinstance(string, str):
        return urllib.parse.quote_plus(string)
    return string

def string_maker(strlen=1):
    return list(set([''.join(x) for x in itertools.permutations([c for c in USABLE_CHARS], strlen)]))


URI = 'http://spooktoberctf.se:22083/clients'


def fetch(inp={}):
    retval = requests.post(URI, data=inp, timeout=1)
    t = retval.text
    if inp.get('__proto__', None) is not None:
        print()
    if retval.status_code != 200:
        print()
    return t


#test = b'Jason' + b'\x00'
#test = b'Ja'
#test = 'Ja\"'
#test = 'Jason'

#test = 'Jason                                                                          asdf'
#datta = {'[name, location]': 'Dracula, Transylvania'}
#datta = {'[name]': 'Dracula', '[location]': 'Transylvania'}
#datta = {'.length': ';'}
#datta = {'[name]': 'Dracula'}



#datta = {'name': b'Dracula\x00', 'location': 'Transylvania'}


#r = requests.post(URI, data=datta, timeout=1)
# res = r.text

# rng = requests.request('OPTIONS',URI, params={'name': 'Dracula'*10000}) # Options berättar vilka metoder som finns att tillgå
# aaa = requests.patch(URI, json={'name': 'Dracula'}, timeout=1).text
aa = requests.delete(URI, json={'name': 'Dracula'}, timeout=1).text
a = fetch({'name': 'Dracula'})
b = fetch({'[name]': 'Dracula'})
c = fetch({'[name]': 'Dracula'})
d = fetch({'%name%': 'Dracula'})
e = requests.options('http://spooktoberctf.se:22083/*')
f = fetch({'length': ''})
counter = 0
#skipped = 0
for i in range(1, 4):
    test_strings = string_maker(i)
    str_count = len(test_strings)
    print(f'Testing {str_count} strings with character length {i}.')
    for s in test_strings:
        counter = counter + 1
        if counter % 100 == 0:
            print(f'Parsed: {counter}/{str_count}')
#        if s[0] not in string.ascii_uppercase:
#            skipped = skipped + 1
#            continue
        try:
            value_data = urlencode(f'Ja{s}')
            r = requests.post(URI, data={'location': value_data})
            if r.text != "[]":
                print()
        except Exception as e:
            pass



print()